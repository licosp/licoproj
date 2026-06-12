"""L3 memory rebuilder: filter L4 logs and produce a CLI-ready JSONL session."""

import argparse
import contextlib
import json
import sys
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from lico_logger import LicoMsg, add_stream_handler, get_logger

logger = get_logger(__name__)
add_stream_handler(logger)


# ---------------------------------------------------------------------------
# Stage filtering (from filter.py)
# ---------------------------------------------------------------------------


def _process_message_stages(
    line: str,
    stage1_lines: list[dict[str, Any]],
    stage2_lines: list[dict[str, Any]],
    config: dict[str, int],
) -> bool:
    """Process a single log line into Stage 1 or Stage 2.

    Args:
        line (str): Raw log line.
        stage1_lines (list[dict[str, Any]]): Collected Stage 1 messages.
        stage2_lines (list[dict[str, Any]]): Collected Stage 2 messages.
        config (dict[str, int]): Filtering quotas (stage1, stage2).

    Returns:
        bool: True if collection should continue, False if both quotas hit.
    """
    if len(stage1_lines) < config["stage1"]:
        with contextlib.suppress(json.JSONDecodeError):
            stage1_lines.append(json.loads(line))
        return True

    if len(stage2_lines) < config["stage2"]:
        with contextlib.suppress(json.JSONDecodeError):
            obj = json.loads(line)
            msg_type = obj.get("type")
            content = str(obj.get("content", ""))
            is_model = msg_type in {"gemini", "model"}
            is_gemini_with_content = is_model and bool(content)

            if msg_type == "user" or is_gemini_with_content:
                if "toolCalls" in obj:
                    del obj["toolCalls"]
                stage2_lines.append(obj)
        return True

    return False


def _read_reversed_lines(jsonl_file: Path) -> list[str]:
    """Read lines from a file and return them in reverse order.

    Args:
        jsonl_file (Path): The file to read.

    Returns:
        list[str]: Stripped lines in reverse.
    """
    try:
        with jsonl_file.open("r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
            lines.reverse()
            return lines
    except OSError as e:
        logger.warning(
            LicoMsg.MEMORY.FILTER_READ_ERR.format(file=jsonl_file, error=e)
        )
        return []


def _filter_log_files(
    jsonl_files: list[Path], l4_root: Path, config: dict[str, int]
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    """Iterate over files and collect messages for Stage 1 & 2.

    Args:
        jsonl_files (list[Path]): List of files to process.
        l4_root (Path): Root for path relativization.
        config (dict[str, int]): Stage limits.

    Returns:
        tuple: (stage1_lines, stage2_lines, files_touched).
    """
    s1_lines: list[dict[str, Any]] = []
    s2_lines: list[dict[str, Any]] = []
    touched: list[str] = []

    for f in jsonl_files:
        if len(s1_lines) >= config["stage1"] and \
           len(s2_lines) >= config["stage2"]:
            break

        touched.append(str(f.relative_to(l4_root)))
        for line in _read_reversed_lines(f):
            if not _process_message_stages(line, s1_lines, s2_lines, config):
                break

    return s1_lines, s2_lines, touched


# ---------------------------------------------------------------------------
# Session metadata preparation (from pack.py)
# ---------------------------------------------------------------------------


def _prepare_session_data(
    meta_path: Path, args_id: str, args_s1: int, args_s2: int
) -> tuple[dict[str, Any], str, str]:
    """Initialize session structure and generate new UUID.

    Args:
        meta_path (Path): Path to existing metadata.
        args_id (str): Identifier name.
        args_s1 (int): Stage 1 turn count.
        args_s2 (int): Stage 2 turn count.

    Returns:
        tuple: (session_data, new_uuid, base_id).
    """
    session_data: dict[str, Any] = {}
    base_id = "unknown"
    if meta_path.exists():
        with meta_path.open("r", encoding="utf-8") as f:
            session_data = json.load(f)
            base_id = str(session_data.get("sessionId", "unknown"))
    else:
        logger.warning(
            LicoMsg.MEMORY.PACK_META_NOT_FOUND.format(path=meta_path)
        )

    new_uuid = str(uuid.uuid4())
    now_utc = datetime.now(UTC)
    ts_str = now_utc.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"

    session_data["sessionId"] = new_uuid
    session_data["startTime"] = ts_str
    session_data["lastUpdated"] = ts_str

    summary_obj = {
        "id": args_id,
        "baseId": base_id,
        "lines": {"s1": args_s1, "s2": args_s2},
    }
    session_data["summary"] = json.dumps(
        summary_obj, separators=(",", ":"), ensure_ascii=False
    )

    return session_data, new_uuid, base_id


# ---------------------------------------------------------------------------
# Output: JSONL session file
# ---------------------------------------------------------------------------


def _write_session_jsonl(
    session_data: dict[str, Any],
    messages: list[dict[str, Any]],
    output_path: Path,
) -> None:
    """Write a CLI-ready JSONL session file.

    Line 1 is session metadata, subsequent lines are messages.

    Args:
        session_data (dict[str, Any]): Session metadata.
        messages (list[dict[str, Any]]): Filtered message list.
        output_path (Path): Target file path.
    """
    output_path.parent.mkdir(parents=True, exist_ok=True)

    with output_path.open("w", encoding="utf-8") as f:
        meta_line = json.dumps(
            session_data, separators=(",", ":"), ensure_ascii=False
        )
        f.write(meta_line + "\n")
        for msg in messages:
            line = json.dumps(
                msg, separators=(",", ":"), ensure_ascii=False
            )
            f.write(line + "\n")


def _print_summary(
    s1: list[dict[str, Any]],
    s2: list[dict[str, Any]],
    touched: list[str],
    config: dict[str, int],
    session_data: dict[str, Any],
    total: int,
    output_path: Path,
) -> None:
    """Print a comprehensive rebuild summary.

    Args:
        s1: Stage 1 messages.
        s2: Stage 2 messages.
        touched: Files accessed.
        config: Stage quotas.
        session_data: Session metadata.
        total: Total message count.
        output_path: Output file path.
    """
    new_uuid = str(session_data.get("sessionId", ""))
    summary_dict = json.loads(str(session_data.get("summary", "{}")))
    base_id = str(summary_dict.get("baseId", "unknown"))

    logger.info(LicoMsg.MEMORY.FILTER_SUMMARY_HEADER)
    logger.info(LicoMsg.MEMORY.FILTER_QUOTA.format(
        s1=config["stage1"], s2=config["stage2"]
    ))
    logger.info(LicoMsg.MEMORY.FILTER_ACTUAL_COLLECTED.format(
        s1=len(s1), s2=len(s2)
    ))
    logger.info(LicoMsg.MEMORY.FILTER_FILES_ACCESSED)
    for f in touched:
        logger.info(LicoMsg.MEMORY.FILTER_FILE_ENTRY.format(file=f))

    final = s2 + s1
    if final:
        logger.info(LicoMsg.MEMORY.FILTER_OLDEST_TIMESTAMP.format(
            ts=final[0].get("timestamp")
        ))

    logger.info(LicoMsg.MEMORY.FILTER_TOTAL_TURNS.format(count=total))
    logger.info(LicoMsg.MEMORY.PACK_SESSION_ID.format(id=new_uuid))
    logger.info(LicoMsg.MEMORY.PACK_BASE_ID.format(id=base_id))
    logger.info(
        LicoMsg.MEMORY.PACK_SUMMARY_TEXT.format(text=session_data["summary"])
    )

    if output_path.exists():
        logger.info(
            LicoMsg.MEMORY.PACK_SIZE.format(size=output_path.stat().st_size)
        )
    logger.info(LicoMsg.MEMORY.PACK_SAVED.format(path=output_path))


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------


def main() -> None:
    """Entry point for L3 memory rebuild."""
    parser = argparse.ArgumentParser(
        description="Rebuild L3 memory from L4 logs (filter + pack)."
    )
    parser.add_argument("input_dir", help="Path to identifier's L4 directory")
    parser.add_argument("output_file", help="Path to output .jsonl file")
    parser.add_argument("--id", required=True, help="Identifier name")
    parser.add_argument("--s1", type=int, default=500, help="Stage 1 quota")
    parser.add_argument("--s2", type=int, default=500, help="Stage 2 quota")
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Show summary only, do not write output file",
    )

    args = parser.parse_args()
    l4_root = Path(args.input_dir)
    out_path = Path(args.output_file)
    config = {"stage1": args.s1, "stage2": args.s2}

    if not l4_root.exists() or not l4_root.is_dir():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=l4_root))
        sys.exit(1)

    msg_dir = l4_root / "messages"
    if not msg_dir.exists():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=msg_dir))
        sys.exit(1)

    meta_path = l4_root / "metadata.json"

    # --- Filter ---
    files = sorted(msg_dir.rglob("*.jsonl"), reverse=True)
    s1, s2, touched = _filter_log_files(files, l4_root, config)

    s2.reverse()
    s1.reverse()
    final_messages = s2 + s1

    # --- Session metadata ---
    session_data, new_uuid, _ = _prepare_session_data(
        meta_path, args.id, args.s1, args.s2
    )

    # --- Output ---
    if args.dry_run:
        _print_summary(
            s1, s2, touched, config, session_data, len(final_messages),
            out_path,
        )
        return

    filename_date = datetime.now(UTC).strftime("%Y-%m-%dT%H-%M")
    final_path = out_path
    if final_path.suffix != ".jsonl":
        final_path = (
            out_path / f"session-{filename_date}-{new_uuid[:8]}.jsonl"
        )

    _write_session_jsonl(session_data, final_messages, final_path)
    _print_summary(
        s1, s2, touched, config, session_data, len(final_messages),
        final_path,
    )


if __name__ == "__main__":
    main()
