"""JSON to JSONL converter for Lico CLI logs."""

import argparse
import json
import sys
from datetime import datetime
from pathlib import Path


def parse_date(timestamp_str: str) -> str:
    """Extract YYYY/MM/DD from an ISO 8601 timestamp string."""
    try:
        # e.g., "2026-02-07T11:00:15.692Z" -> "2026/02/07"
        dt = datetime.fromisoformat(timestamp_str.replace("Z", "+00:00"))
        return dt.strftime("%Y/%m/%d")
    except ValueError:
        # Fallback if parsing fails
        return "unknown_date"


def get_existing_ids(file_path: Path) -> set[str]:
    """Read an existing JSONL file and return a set of all message IDs."""
    existing_ids = set()
    if not file_path.exists():
        return existing_ids

    try:
        with file_path.open("r", encoding="utf-8") as f:
            for line in f:
                if not line.strip():
                    continue
                try:
                    obj = json.loads(line)
                    # Try to find a unique identifier
                    msg_id = obj.get("id")
                    if not msg_id:
                        s_id = obj.get("sessionId")
                        m_id = obj.get("messageId")
                        if s_id is not None and m_id is not None:
                            msg_id = f"{s_id}_{m_id}"
                    
                    if msg_id:
                        existing_ids.add(msg_id)
                except json.JSONDecodeError:
                    pass
    except Exception as e:
        print(
            f"Warning: Failed to read existing IDs from {file_path}: {e}",
            file=sys.stderr,
        )

    return existing_ids


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Convert Gemini CLI JSON to date-partitioned JSONL."
    )
    parser.add_argument("input_json", help="Path to the monolithic .json file")
    parser.add_argument(
        "output_root",
        help="Root directory for output (e.g., .repos/.licoshdw/conversations_cli/identifiers/agate/)",
    )

    args = parser.parse_args()

    input_path = Path(args.input_json)
    output_root = Path(args.output_root)

    if not input_path.exists():
        print(f"Error: Input file '{input_path}' not found.", file=sys.stderr)
        sys.exit(1)

    try:
        with input_path.open("r", encoding="utf-8") as f:
            data = json.load(f)
    except json.JSONDecodeError as e:
        print(f"Error: Failed to parse JSON: {e}", file=sys.stderr)
        sys.exit(1)

    messages = []
    has_metadata = False

    if isinstance(data, list):
        messages = data
        data = None # No metadata to save
    elif isinstance(data, dict):
        messages = data.pop("messages", [])
        has_metadata = True
    else:
        print("Error: Unknown JSON root structure.", file=sys.stderr)
        sys.exit(1)
        
    output_root.mkdir(parents=True, exist_ok=True)
    
    # 1. Save Metadata if present
    if has_metadata and data:
        meta_path = output_root / "metadata.json"
        
        # Merge existing metadata if present (to preserve overarching info if updating)
        if meta_path.exists():
            try:
                with meta_path.open("r", encoding="utf-8") as mf:
                    existing_meta = json.load(mf)
                    existing_meta.update(data)
                    data = existing_meta
            except Exception:
                pass
                
        with meta_path.open("w", encoding="utf-8") as mf:
            json.dump(data, mf, indent=2, ensure_ascii=False)

    if not messages:
        print("No messages found in JSON.", file=sys.stderr)
        sys.exit(0)

    # 2. Setup output subdirectory logic
    # If it's a dict (agent log), we use 'messages/'. If list (user log), just put directly.
    messages_root = output_root / "messages" if has_metadata else output_root

    # Cache existing IDs per date to minimize file reads
    known_ids_cache: dict[Path, set[str]] = {}

    count_added = 0
    count_skipped = 0

    for msg in messages:
        # Require a timestamp to partition
        timestamp = msg.get("timestamp")
        
        # Determine ID for deduplication
        msg_id = msg.get("id")
        if not msg_id:
            s_id = msg.get("sessionId")
            m_id = msg.get("messageId")
            if s_id is not None and m_id is not None:
                msg_id = f"{s_id}_{m_id}"

        if not timestamp or not msg_id:
            continue

        date_path = parse_date(timestamp)
        target_dir = messages_root / date_path
        target_dir.mkdir(parents=True, exist_ok=True)

        target_file = target_dir / "log.jsonl"

        # Load existing IDs for this file if not already cached
        if target_file not in known_ids_cache:
            known_ids_cache[target_file] = get_existing_ids(target_file)

        if msg_id in known_ids_cache[target_file]:
            count_skipped += 1
            continue

        # Minify: remove spaces
        minified_json = json.dumps(
            msg, separators=(",", ":"), ensure_ascii=False
        )

        with target_file.open("a", encoding="utf-8") as out_f:
            out_f.write(minified_json + "\n")

        # Update cache so we don't duplicate within the same run
        known_ids_cache[target_file].add(msg_id)
        count_added += 1

    print(
        f"Done. Metadata saved. Added: {count_added}, Skipped (already existed): {count_skipped}. Output root: {output_root}"
    )


if __name__ == "__main__":
    main()
