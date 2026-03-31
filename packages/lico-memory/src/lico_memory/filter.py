import argparse
import json
import sys
from pathlib import Path

from lico_logger import LicoMsg, get_logger

logger = get_logger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description=(
            "Extract and filter L4 JSONL logs into a single condensed "
            "JSONL file."
        )
    )
    parser.add_argument(
        "input_dir",
        type=str,
        help=(
            "Path to the identifier's L4 directory (e.g., "
            ".repos/.licoshdw/conversations_cli/identifiers/agate)"
        ),
    )
    parser.add_argument(
        "output_file",
        type=str,
        help=(
            "Path to the output filtered JSONL file (e.g., "
            "filtered_memory.jsonl)"
        ),
    )
    parser.add_argument(
        "--stage1",
        type=int,
        default=500,
        help=(
            "Quota for Stage 1 (Full retention of recent turns). "
            "Default: 500"
        ),
    )
    parser.add_argument(
        "--stage2",
        type=int,
        default=500,
        help=(
            "Quota for Stage 2 (Filter out tool calls, keep "
            "conversation/thoughts). Default: 500"
        ),
    )

    args = parser.parse_args()

    l4_root = Path(args.input_dir)
    output_path = Path(args.output_file)
    stage1_quota = args.stage1
    stage2_quota = args.stage2

    if not l4_root.exists() or not l4_root.is_dir():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=l4_root))
        sys.exit(1)

    messages_dir = l4_root / "messages"

    if not messages_dir.exists():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=messages_dir))
        sys.exit(1)

    # Gather and sort JSONL files (newest first)
    jsonl_files = sorted(list(messages_dir.rglob("*.jsonl")), reverse=True)

    stage1_lines = []
    stage2_lines = []
    files_touched = []

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
        except Exception as e:
            logger.warning(
                LicoMsg.MEMORY.FILTER_READ_ERR.format(file=jsonl_file, error=e)
            )
            continue

        lines.reverse()

        for line in lines:
            if len(stage1_lines) < stage1_quota:
                try:
                    obj = json.loads(line)
                    stage1_lines.append(obj)
                except json.JSONDecodeError:
                    pass
            elif len(stage2_lines) < stage2_quota:
                try:
                    obj = json.loads(line)
                    msg_type = obj.get("type")
                    content = obj.get("content", "")
                    has_content = bool(content)
                    is_gemini_with_content = (
                        msg_type in ("gemini", "model")
                    ) and has_content

                    if msg_type == "user" or is_gemini_with_content:
                        if "toolCalls" in obj:
                            del obj["toolCalls"]
                        stage2_lines.append(obj)
                except json.JSONDecodeError:
                    pass
            else:
                break

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
        oldest = final_messages[0]
        logger.info(
            LicoMsg.MEMORY.FILTER_OLDEST_TIMESTAMP.format(
                ts=oldest.get("timestamp")
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
