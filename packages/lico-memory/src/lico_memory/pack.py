"""L3 session packaging tool for Lico memory management."""

import argparse
import json
import sys
import uuid
from datetime import UTC, datetime
from pathlib import Path

from lico_logger import LicoMsg, get_logger

logger = get_logger(__name__)


def main():
    """Entry point for session packaging."""
    parser = argparse.ArgumentParser(
        description=(
            "Pack a filtered JSONL file and a metadata file into a final "
            "L3 JSON session file."
        )
    )
    parser.add_argument(
        "input_jsonl",
        type=str,
        help="Path to the filtered JSONL file (e.g., filtered_memory.jsonl)",
    )
    parser.add_argument(
        "metadata_json",
        type=str,
        help="Path to the original metadata.json file",
    )
    parser.add_argument(
        "output_dir",
        type=str,
        help=(
            "Path to the output directory (e.g., "
            "~/.gemini/tmp/crew-agate/chats/)"
        ),
    )

    parser.add_argument(
        "--id",
        type=str,
        required=True,
        help="Identifier name (e.g., agate, alexandrite)",
    )
    parser.add_argument(
        "--s1",
        type=int,
        required=True,
        help="Number of Stage 1 turns included",
    )
    parser.add_argument(
        "--s2",
        type=int,
        required=True,
        help="Number of Stage 2 turns included",
    )

    args = parser.parse_args()

    jsonl_path = Path(args.input_jsonl)
    meta_path = Path(args.metadata_json)
    output_dir = Path(args.output_dir).expanduser().resolve()

    if not jsonl_path.exists():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=jsonl_path))
        sys.exit(1)

    session_data = {}
    base_id = "unknown"
    if meta_path.exists():
        with meta_path.open("r", encoding="utf-8") as f:
            session_data = json.load(f)
            base_id = session_data.get("sessionId", "unknown")
    else:
        logger.warning(
            LicoMsg.MEMORY.PACK_META_NOT_FOUND.format(path=meta_path)
        )
        session_data = {}

    new_uuid = str(uuid.uuid4())
    short_hash = new_uuid[:8]
    now_utc = datetime.now(UTC)
    now_local = datetime.now()

    filename_date = now_local.strftime("%Y-%m-%dT%H-%M")
    output_filename = f"session-{filename_date}-{short_hash}.json"
    output_path = output_dir / output_filename

    session_data["sessionId"] = new_uuid
    session_data["startTime"] = (
        now_utc.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    )
    session_data["lastUpdated"] = session_data["startTime"]

    summary_obj = {
        "id": args.id,
        "baseId": base_id,
        "lines": {"s1": args.s1, "s2": args.s2},
    }
    session_data["summary"] = json.dumps(
        summary_obj, separators=(",", ":"), ensure_ascii=False
    )

    messages = []
    with jsonl_path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    obj = json.loads(line)
                    messages.append(obj)
                except json.JSONDecodeError as e:
                    logger.warning(
                        LicoMsg.MEMORY.ERR_INVALID_JSON.format(
                            path=jsonl_path, error=e
                        )
                    )

    session_data["messages"] = messages
    output_dir.mkdir(parents=True, exist_ok=True)

    if output_path.exists():
        output_path = (
            output_dir / f"session-{filename_date}-{short_hash}-restored.json"
        )

    with output_path.open("w", encoding="utf-8") as f:
        json.dump(session_data, f, separators=(",", ":"), ensure_ascii=False)

    logger.info(LicoMsg.MEMORY.PACK_SUMMARY_HEADER)
    logger.info(LicoMsg.MEMORY.PACK_COUNT.format(count=len(messages)))
    logger.info(LicoMsg.MEMORY.PACK_SESSION_ID.format(id=new_uuid))
    logger.info(LicoMsg.MEMORY.PACK_BASE_ID.format(id=base_id))
    logger.info(
        LicoMsg.MEMORY.PACK_SUMMARY_TEXT.format(text=session_data["summary"])
    )
    logger.info(
        LicoMsg.MEMORY.PACK_SIZE.format(size=output_path.stat().st_size)
    )
    logger.info(LicoMsg.MEMORY.PACK_SAVED.format(path=output_path))


if __name__ == "__main__":
    main()
