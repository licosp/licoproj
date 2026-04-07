"""L3 session packaging tool for Lico memory management."""

import argparse
import json
import sys
import uuid
from datetime import UTC, datetime
from pathlib import Path
from typing import Any

from lico_logger import LicoMsg, get_logger

logger = get_logger(__name__)


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


def main() -> None:
    """Entry point for session packaging."""
    parser = argparse.ArgumentParser(
        description="Pack filtered JSONL and metadata into L3 JSON."
    )
    parser.add_argument("input_jsonl", help="Path to filtered JSONL")
    parser.add_argument("metadata_json", help="Path to metadata.json")
    parser.add_argument("output_dir", help="Path to output directory")
    parser.add_argument("--id", required=True, help="Identifier name")
    parser.add_argument("--s1", type=int, required=True, help="S1 count")
    parser.add_argument("--s2", type=int, required=True, help="S2 count")

    args = parser.parse_args()
    jsonl_path, meta_path = Path(args.input_jsonl), Path(args.metadata_json)
    out_dir = Path(args.output_dir).expanduser().resolve()

    if not jsonl_path.exists():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=jsonl_path))
        sys.exit(1)

    session_data, new_uuid, base_id = _prepare_session_data(
        meta_path, args.id, args.s1, args.s2
    )

    filename_date = datetime.now(UTC).strftime("%Y-%m-%dT%H-%M")
    out_file = out_dir / f"session-{filename_date}-{new_uuid[:8]}.json"

    messages: list[dict[str, Any]] = []
    with jsonl_path.open("r", encoding="utf-8") as f:
        for line in f:
            if not (stripped := line.strip()):
                continue
            try:
                messages.append(json.loads(stripped))
            except json.JSONDecodeError as e:
                logger.warning(
                    LicoMsg.MEMORY.ERR_INVALID_JSON.format(
                        path=jsonl_path, error=e
                    )
                )

    session_data["messages"] = messages
    out_dir.mkdir(parents=True, exist_ok=True)

    if out_file.exists():
        out_file = out_dir / f"session-{filename_date}-{new_uuid[:8]}-r.json"

    with out_file.open("w", encoding="utf-8") as f:
        json.dump(session_data, f, separators=(",", ":"), ensure_ascii=False)

    logger.info(LicoMsg.MEMORY.PACK_SUMMARY_HEADER)
    logger.info(LicoMsg.MEMORY.PACK_COUNT.format(count=len(messages)))
    logger.info(LicoMsg.MEMORY.PACK_SESSION_ID.format(id=new_uuid))
    logger.info(LicoMsg.MEMORY.PACK_BASE_ID.format(id=base_id))
    logger.info(
        LicoMsg.MEMORY.PACK_SUMMARY_TEXT.format(text=session_data["summary"])
    )
    logger.info(LicoMsg.MEMORY.PACK_SIZE.format(size=out_file.stat().st_size))
    logger.info(LicoMsg.MEMORY.PACK_SAVED.format(path=out_file))


if __name__ == "__main__":
    main()
