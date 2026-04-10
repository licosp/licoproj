"""JSON to JSONL converter for Lico CLI logs."""

import argparse
import contextlib
import json
import sys
from datetime import datetime
from pathlib import Path
from typing import Any, cast

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


def _read_jsonl_file(file_path: Path) -> list[dict[str, Any]]:
    """Read a JSONL file and return a list of dictionaries.

    Args:
        file_path (Path): Path to the JSONL file.

    Returns:
        list[dict[str, Any]]: List of parsed JSON objects.
    """
    data: list[dict[str, Any]] = []
    if not file_path.exists():
        return data

    try:
        with file_path.open("r", encoding="utf-8") as f:
            for line in f:
                if not (stripped := line.strip()):
                    continue
                with contextlib.suppress(json.JSONDecodeError):
                    data.append(json.loads(stripped))
    except OSError as e:
        logger.warning(
            LicoMsg.MEMORY.BACKUP_READ_LOG_ERR.format(file=file_path, error=e)
        )
    return data


def get_existing_ids(file_path: Path) -> set[str]:
    """Read an existing JSONL file and return a set of all message IDs.

    Args:
        file_path (Path): Path to the JSONL file.

    Returns:
        set[str]: A set containing all unique message IDs found.
    """
    existing_ids: set[str] = set()
    for obj in _read_jsonl_file(file_path):
        if msg_id := _extract_message_id(obj):
            existing_ids.add(msg_id)
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


def _save_jsonl_file(file_path: Path, messages: list[dict[str, Any]]) -> None:
    """Sort messages by timestamp and save to a JSONL file.

    Args:
        file_path (Path): Target file path.
        messages (list[dict[str, Any]]): List of messages to save.
    """
    messages.sort(key=lambda x: str(x.get("timestamp", "")))

    with file_path.open("w", encoding="utf-8") as f:
        for msg in messages:
            line = json.dumps(
                msg,
                separators=(",", ":"),
                ensure_ascii=False,
                sort_keys=True,
            )
            f.write(line + "\n")


def _process_single_target_file(
    target_file: Path, new_msgs: list[dict[str, Any]]
) -> tuple[int, int]:
    """Merge and save a single storage file.

    Args:
        target_file (Path): The file to update.
        new_msgs (list[dict[str, Any]]): New messages to add.

    Returns:
        tuple[int, int]: (added, skipped) counts.
    """
    target_file.parent.mkdir(parents=True, exist_ok=True)
    count_added = 0
    count_skipped = 0

    known_ids = get_existing_ids(target_file)
    merged_msgs = _read_jsonl_file(target_file)

    for msg in new_msgs:
        msg_id = _extract_message_id(msg)
        if msg_id and msg_id in known_ids:
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

    _save_jsonl_file(target_file, merged_msgs)
    return count_added, count_skipped


def _update_storage_files(
    new_messages_by_file: dict[Path, list[dict[str, Any]]], output_root: Path
) -> tuple[int, int]:
    """Merge new messages with existing storage and save to JSONL files.

    Args:
        new_messages_by_file (dict[Path, list[dict[str, Any]]]): Grouped data.
        output_root (Path): Root directory for output logs.

    Returns:
        tuple[int, int]: A tuple of (total_added, total_skipped).
    """
    total_added = 0
    total_skipped = 0

    for target_file, new_msgs in new_messages_by_file.items():
        added, skipped = _process_single_target_file(target_file, new_msgs)
        total_added += added
        total_skipped += skipped

    logger.info(LicoMsg.MEMORY.PACK_SAVED.format(path=output_root))
    return total_added, total_skipped


def _normalize_input_data(
    data: Any,  # noqa: ANN401
) -> tuple[list[dict[str, Any]], dict[str, Any] | None, bool]:
    """Normalize input JSON into messages and metadata.

    Args:
        data (Any): Raw parsed JSON.

    Returns:
        tuple: (messages, metadata, has_metadata_flag).
    """
    if isinstance(data, list):
        return cast("list[dict[str, Any]]", data), None, False  # type: ignore[invalid-return-type]
    if isinstance(data, dict):
        # messages is expected to be a list in the dict
        messages = cast("list[dict[str, Any]]", data.pop("messages", []))
        return messages, data, True  # type: ignore[invalid-return-type]

    logger.error(LicoMsg.MEMORY.BACKUP_STRUCT_ERROR)
    sys.exit(1)


def _save_metadata(output_root: Path, metadata: dict[str, Any]) -> None:
    """Merge and save metadata to a JSON file.

    Args:
        output_root (Path): The root directory for output.
        metadata (dict[str, Any]): The metadata to save.
    """
    meta_path = output_root / "metadata.json"
    if meta_path.exists():
        with (
            contextlib.suppress(KeyError, AttributeError, TypeError),
            meta_path.open("r", encoding="utf-8") as mf,
        ):
            existing_meta = json.load(mf)
            existing_meta.update(metadata)
            metadata = existing_meta

    with meta_path.open("w", encoding="utf-8") as mf:
        json.dump(metadata, mf, indent=2, ensure_ascii=False)


def main() -> None:
    """Entry point for JSON to JSONL conversion."""
    parser = argparse.ArgumentParser(
        description="Convert Gemini CLI JSON to date-partitioned JSONL."
    )
    parser.add_argument("input_json", help="Path to the monolithic .json file")
    parser.add_argument(
        "output_root",
        help="Root directory for output",
    )

    args = parser.parse_args()
    input_path, output_root = Path(args.input_json), Path(args.output_root)

    if not input_path.exists():
        logger.error(LicoMsg.MEMORY.ERR_NOT_FOUND.format(path=input_path))
        sys.exit(1)

    try:
        with input_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError:
        logger.exception(LicoMsg.MEMORY.BACKUP_JSON_ERROR)
        sys.exit(1)

    messages, metadata, has_metadata = _normalize_input_data(data)
    output_root.mkdir(parents=True, exist_ok=True)

    if has_metadata and metadata:
        _save_metadata(output_root, metadata)

    if not messages:
        logger.error(LicoMsg.MEMORY.BACKUP_NO_MSG)
        sys.exit(0)

    logger.info(LicoMsg.MEMORY.BACKUP_START.format(path=input_path))
    messages_root = output_root / "messages" if has_metadata else output_root
    new_messages_by_file = _group_messages_by_date(messages, messages_root)
    _update_storage_files(new_messages_by_file, output_root)


if __name__ == "__main__":
    main()
