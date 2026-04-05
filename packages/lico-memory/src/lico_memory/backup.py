"""JSON to JSONL converter for Lico CLI logs."""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any

from lico_logger import LicoMsg, get_logger

logger = get_logger(__name__)


def parse_date(timestamp_str: str) -> str:
    """Extract YYYY/MM/DD from an ISO 8601 timestamp string.

    Args:
        timestamp_str (str): The raw ISO 8601 timestamp.

    Returns:
        str: The extracted date in YYYY/MM/DD format.
    """
    try:
        # e.g., "2026-02-07T11:00:15.692Z" -> "2026/02/07"
        dt = datetime.fromisoformat(timestamp_str)
        return dt.strftime("%Y/%m/%d")
    except ValueError:
        # Fallback if parsing fails
        return "unknown_date"


def _extract_message_id(msg: dict[str, Any]) -> str | None:
    """Generate a unique ID for a message from its fields.

    Args:
        msg (dict[str, Any]): The message dictionary.

    Returns:
        str | None: The extracted ID or None if not found.
    """
    msg_id = msg.get("id")
    if not msg_id:
        s_id = msg.get("sessionId")
        m_id = msg.get("messageId")
        if s_id is not None and m_id is not None:
            msg_id = f"{s_id}_{m_id}"
    return str(msg_id) if msg_id else None


def get_existing_ids(file_path: Path) -> set[str]:
    """Read an existing JSONL file and return a set of all message IDs.

    Args:
        file_path (Path): Path to the JSONL file.

    Returns:
        set[str]: A set containing all unique message IDs found.
    """
    existing_ids: set[str] = set()
    if not file_path.exists():
        return existing_ids

    try:
        with file_path.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    obj = json.loads(line)
                    msg_id = _extract_message_id(obj)
                    if msg_id:
                        existing_ids.add(msg_id)
                except json.JSONDecodeError:
                    pass
    except OSError as e:
        logger.warning(
            LicoMsg.MEMORY.BACKUP_READ_IDS_ERR.format(path=file_path, error=e)
        )

    return existing_ids


def _group_messages_by_date(
    messages: list[dict[str, Any]], messages_root: Path
) -> dict[Path, list[dict[str, Any]]]:
    """Group new messages by their target file path based on date.

    Args:
        messages (list[dict[str, Any]]): List of message dictionaries.
        messages_root (Path): Root directory for message storage.

    Returns:
        dict[Path, list[dict[str, Any]]]: Mapping of target paths to messages.
    """
    new_messages_by_file: dict[Path, list[dict[str, Any]]] = {}
    for msg in messages:
        msg_id = _extract_message_id(msg)
        timestamp = msg.get("timestamp")

        if not timestamp or not msg_id:
            continue

        date_path = parse_date(str(timestamp))
        target_dir = messages_root / date_path
        target_file = target_dir / "log.jsonl"

        if target_file not in new_messages_by_file:
            new_messages_by_file[target_file] = []

        new_messages_by_file[target_file].append(msg)

    return new_messages_by_file


def _update_storage_files(
    new_messages_by_file: dict[Path, list[dict[str, Any]]], output_root: Path
) -> tuple[int, int]:
    """Merge new messages with existing storage and save to JSONL files.

    Args:
        new_messages_by_file (dict[Path, list[dict[str, Any]]]): Grouped data.
        output_root (Path): Root directory for output logs.

    Returns:
        tuple[int, int]: A tuple of (count_added, count_skipped).
    """
    count_added = 0
    count_skipped = 0

    for target_file, new_msgs in new_messages_by_file.items():
        target_file.parent.mkdir(parents=True, exist_ok=True)

        merged_msgs: list[dict[str, Any]] = []
        known_ids: set[str] = set()

        if target_file.exists():
            known_ids = get_existing_ids(target_file)
            try:
                with target_file.open("r", encoding="utf-8") as f:
                    for line in f:
                        if not line.strip():
                            continue
                        try:
                            merged_msgs.append(json.loads(line))
                        except json.JSONDecodeError:
                            pass
            except OSError as e:
                logger.warning(
                    LicoMsg.MEMORY.BACKUP_READ_LOG_ERR.format(
                        file=target_file, error=e
                    )
                )

        for msg in new_msgs:
            msg_id = _extract_message_id(msg)
            if msg_id in known_ids:
                count_skipped += 1
                continue
            merged_msgs.append(msg)
            if msg_id:
                known_ids.add(msg_id)
            count_added += 1
            logger.info(
                LicoMsg.MEMORY.BACKUP_ENTRY.format(
                    id=msg_id, ts=msg.get("timestamp")
                )
            )

        merged_msgs.sort(key=lambda x: str(x.get("timestamp", "")))

        with target_file.open("w", encoding="utf-8") as f:
            for msg in merged_msgs:
                line = json.dumps(
                    msg,
                    separators=(",", ":"),
                    ensure_ascii=False,
                    sort_keys=True,
                )
                f.write(line + "\n")

    logger.info(LicoMsg.MEMORY.PACK_SAVED.format(path=output_root))
    return count_added, count_skipped


def main() -> None:
    """Entry point for JSON to JSONL conversion."""
    parser = argparse.ArgumentParser(
        description="Convert Gemini CLI JSON to date-partitioned JSONL."
    )
    parser.add_argument("input_json", help="Path to the monolithic .json file")
    parser.add_argument(
        "output_root",
        help=(
            "Root directory for output (e.g., "
            ".repos/.licoshdw/conversations_cli/identifiers/agate/)"
        ),
    )

    args = parser.parse_args()

    input_path = Path(args.input_json)
    output_root = Path(args.output_root)

    if not input_path.exists():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=input_path))
        sys.exit(1)

    try:
        with input_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        logger.exception(LicoMsg.MEMORY.BACKUP_JSON_ERROR)
        sys.exit(1)

    messages: list[dict[str, Any]] = []
    has_metadata = False

    if isinstance(data, list):
        messages = data
        data = None  # No metadata to save
    elif isinstance(data, dict):
        messages = data.pop("messages", [])
        has_metadata = True
    else:
        logger.error(LicoMsg.MEMORY.BACKUP_STRUCT_ERROR)
        sys.exit(1)

    output_root.mkdir(parents=True, exist_ok=True)

    # 1. Save Metadata if present
    if has_metadata and data:
        meta_path = output_root / "metadata.json"

        # Merge existing metadata if present
        if meta_path.exists():
            try:
                with meta_path.open("r", encoding="utf-8") as mf:
                    existing_meta = json.load(mf)
                    existing_meta.update(data)
                    data = existing_meta
            except (KeyError, AttributeError, TypeError):
                pass

        with meta_path.open("w", encoding="utf-8") as mf:
            json.dump(data, mf, indent=2, ensure_ascii=False)

    if not messages:
        logger.error(LicoMsg.MEMORY.BACKUP_NO_MSG)
        sys.exit(0)

    logger.info(LicoMsg.MEMORY.BACKUP_START.format(path=input_path))
    messages_root = output_root / "messages" if has_metadata else output_root

    new_messages_by_file = _group_messages_by_date(messages, messages_root)
    _update_storage_files(new_messages_by_file, output_root)


if __name__ == "__main__":
    main()
