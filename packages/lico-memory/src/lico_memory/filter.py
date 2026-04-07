"""L4 log filtering and thought extraction tool."""

import argparse
import json
import sys
from pathlib import Path
from typing import Any

from lico_logger import LicoMsg, get_logger

logger = get_logger(__name__)


def _filter_log_files(
    jsonl_files: list[Path], l4_root: Path, stage1_quota: int, stage2_quota: int
) -> tuple[list[dict[str, Any]], list[dict[str, Any]], list[str]]:
    """Iterate over files and collect messages for Stage 1 & 2.

    Args:
        jsonl_files (list[Path]): List of JSONL files to process.
        l4_root (Path): Root directory for path relativization.
        stage1_quota (int): Quota for full retention turns.
        stage2_quota (int): Quota for condensed turns.

    Returns:
        tuple: (stage1_lines, stage2_lines, files_touched).
    """
    stage1_lines: list[dict[str, Any]] = []
    stage2_lines: list[dict[str, Any]] = []
    files_touched: list[str] = []

    for jsonl_file in jsonl_files:
        if (
            len(stage1_lines) >= stage1_quota
            and len(stage2_lines) >= stage2_quota
        ):
            break

        files_touched.append(str(jsonl_file.relative_to(l4_root)))

        try:
            with jsonl_file.open("r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
        except OSError as e:
            logger.warning(
                LicoMsg.MEMORY.FILTER_READ_ERR.format(file=jsonl_file, error=e)
            )
            continue

        lines.reverse()

        for line in lines:
            if len(stage1_lines) < stage1_quota:
                try:
                    stage1_lines.append(json.loads(line))
                except json.JSONDecodeError:
                    pass
            elif len(stage2_lines) < stage2_quota:
                try:
                    obj = json.loads(line)
                    msg_type = obj.get("type")
                    content = str(obj.get("content", ""))
                    is_model = msg_type in {"gemini", "model"}
                    is_gemini_with_content = is_model and bool(content)

                    if msg_type == "user" or is_gemini_with_content:
                        if "toolCalls" in obj:
                            del obj["toolCalls"]
                        stage2_lines.append(obj)
                except json.JSONDecodeError:
                    pass
            else:
                break

    return stage1_lines, stage2_lines, files_touched


def main() -> None:
    """Entry point for log filtering."""
    parser = argparse.ArgumentParser(
        description="Extract and filter L4 JSONL logs."
    )
    parser.add_argument("input_dir", help="Path to identifier's L4 directory")
    parser.add_argument("output_file", help="Path to output JSONL file")
    parser.add_argument("--stage1", type=int, default=500, help="Stage 1 quota")
    parser.add_argument("--stage2", type=int, default=500, help="Stage 2 quota")

    args = parser.parse_args()
    l4_root, output_path = Path(args.input_dir), Path(args.output_file)
    stage1_quota, stage2_quota = args.stage1, args.stage2

    if not l4_root.exists() or not l4_root.is_dir():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=l4_root))
        sys.exit(1)

    messages_dir = l4_root / "messages"
    if not messages_dir.exists():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=messages_dir))
        sys.exit(1)

    jsonl_files = sorted(messages_dir.rglob("*.jsonl"), reverse=True)
    stage1_lines, stage2_lines, files_touched = _filter_log_files(
        jsonl_files, l4_root, stage1_quota, stage2_quota
    )

    stage2_lines.reverse()
    stage1_lines.reverse()
    final_messages = stage2_lines + stage1_lines

    logger.info(LicoMsg.MEMORY.FILTER_SUMMARY_HEADER)
    logger.info(
        LicoMsg.MEMORY.FILTER_QUOTA.format(s1=stage1_quota, s2=stage2_quota)
    )
    logger.info(
        LicoMsg.MEMORY.FILTER_ACTUAL_COLLECTED.format(
            s1=len(stage1_lines), s2=len(stage2_lines)
        )
    )
    logger.info(LicoMsg.MEMORY.FILTER_FILES_ACCESSED)
    for f in files_touched:
        logger.info(LicoMsg.MEMORY.FILTER_FILE_ENTRY.format(file=f))

    if final_messages:
        logger.info(
            LicoMsg.MEMORY.FILTER_OLDEST_TIMESTAMP.format(
                ts=final_messages[0].get("timestamp")
            )
        )

    logger.info(
        LicoMsg.MEMORY.FILTER_TOTAL_TURNS.format(count=len(final_messages))
    )

    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        for msg in final_messages:
            line = json.dumps(msg, separators=(",", ":"), ensure_ascii=False)
            f.write(line + "\n")

    logger.info(LicoMsg.MEMORY.FILTER_SAVED.format(path=output_path))


if __name__ == "__main__":
    main()
