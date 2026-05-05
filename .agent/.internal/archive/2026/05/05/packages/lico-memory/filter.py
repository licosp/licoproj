"""L4 log filtering and thought extraction tool."""

import argparse
import contextlib
import json
import sys
from pathlib import Path
from typing import Any

from lico_logger import LicoMsg, get_logger

logger = get_logger(__name__)


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


def _write_filtered_logs(
    s1: list[dict[str, Any]],
    s2: list[dict[str, Any]],
    touched: list[str],
    output_path: Path,
    config: dict[str, int],
) -> None:
    """Consolidate messages, print summary, and save to JSONL.

    Args:
        s1 (list[dict[str, Any]]): Recent turns.
        s2 (list[dict[str, Any]]): Condensed history.
        touched (list[str]): List of files accessed.
        output_path (Path): Path to save the result.
        config (dict[str, int]): Original quotas for summary.
    """
    s2.reverse()
    s1.reverse()
    final = s2 + s1

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

    if final:
        logger.info(LicoMsg.MEMORY.FILTER_OLDEST_TIMESTAMP.format(
            ts=final[0].get("timestamp")
        ))

    logger.info(LicoMsg.MEMORY.FILTER_TOTAL_TURNS.format(count=len(final)))

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        for msg in final:
            line = json.dumps(msg, separators=(",", ":"), ensure_ascii=False)
            f.write(line + "\n")

    logger.info(LicoMsg.MEMORY.FILTER_SAVED.format(path=output_path))


def main() -> None:
    """Entry point for log filtering."""
    parser = argparse.ArgumentParser(
        description="Extract and filter L4 JSONL logs."
    )
    parser.add_argument("input_dir", help="Path to identifier's L4 directory")
    parser.add_argument("output_file", help="Path to output JSONL file")
    parser.add_argument("--stage1", type=int, default=500, help="S1 quota")
    parser.add_argument("--stage2", type=int, default=500, help="S2 quota")

    args = parser.parse_args()
    l4_root, out_path = Path(args.input_dir), Path(args.output_file)
    config = {"stage1": args.stage1, "stage2": args.stage2}

    if not l4_root.exists() or not l4_root.is_dir():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=l4_root))
        sys.exit(1)

    msg_dir = l4_root / "messages"
    if not msg_dir.exists():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=msg_dir))
        sys.exit(1)

    files = sorted(msg_dir.rglob("*.jsonl"), reverse=True)
    s1: list[dict[str, Any]]
    s2: list[dict[str, Any]]
    s1, s2, touched = _filter_log_files(files, l4_root, config)

    _write_filtered_logs(s1, s2, touched, out_path, config)


if __name__ == "__main__":
    main()
