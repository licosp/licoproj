import argparse
import json
import sys
import uuid
from datetime import datetime, timezone
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Pack a filtered JSONL file and a metadata file into a final L3 JSON session file.")
    parser.add_argument("input_jsonl", type=str, help="Path to the filtered JSONL file (e.g., filtered_memory.jsonl)")
    parser.add_argument("metadata_json", type=str, help="Path to the original metadata.json file")
    parser.add_argument("output_dir", type=str, help="Path to the output directory (e.g., ~/.gemini/tmp/crew-agate/chats/)")
    
    parser.add_argument("--id", type=str, required=True, help="Identifier name (e.g., agate, alexandrite)")
    parser.add_argument("--s1", type=int, required=True, help="Number of Stage 1 turns included")
    parser.add_argument("--s2", type=int, required=True, help="Number of Stage 2 turns included")
    
    args = parser.parse_args()
    
    jsonl_path = Path(args.input_jsonl)
    meta_path = Path(args.metadata_json)
    output_dir = Path(args.output_dir).expanduser().resolve()
    
    if not jsonl_path.exists():
        print(f"Error: Input JSONL {jsonl_path} does not exist.", file=sys.stderr)
        sys.exit(1)
        
    # 1. Read metadata
    session_data = {}
    base_id = "unknown"
    if meta_path.exists():
        with meta_path.open("r", encoding="utf-8") as f:
            session_data = json.load(f)
            base_id = session_data.get("sessionId", "unknown")
    else:
        print(f"Warning: Metadata file {meta_path} not found. Creating a generic session structure.", file=sys.stderr)
        session_data = {}
        
    # 2. Generate New Identity and Timestamps
    new_uuid = str(uuid.uuid4())
    short_hash = new_uuid[:8]
    
    now_utc = datetime.now(timezone.utc)
    now_local = datetime.now() # Using system local time for filename as Gemini CLI does
    
    # Format: 2026-03-15T12-37
    filename_date = now_local.strftime("%Y-%m-%dT%H-%M")
    output_filename = f"session-{filename_date}-{short_hash}.json"
    output_path = output_dir / output_filename
    
    # Update Session Data
    session_data["sessionId"] = new_uuid
    # Format: 2026-03-15T12:37:00.000Z
    session_data["startTime"] = now_utc.strftime("%Y-%m-%dT%H:%M:%S.%f")[:-3] + "Z"
    session_data["lastUpdated"] = session_data["startTime"]
    
    # 3. Create JSON Summary
    summary_obj = {
        "id": args.id,
        "baseId": base_id,
        "lines": {
            "s1": args.s1,
            "s2": args.s2
        }
    }
    session_data["summary"] = json.dumps(summary_obj, separators=(",", ":"), ensure_ascii=False)
        
    # 4. Read messages from JSONL
    messages = []
    with jsonl_path.open("r", encoding="utf-8") as f:
        for line in f:
            if line.strip():
                try:
                    obj = json.loads(line)
                    messages.append(obj)
                except json.JSONDecodeError as e:
                    print(f"Warning: Failed to parse line in {jsonl_path}: {e}", file=sys.stderr)
                    
    # 5. Assemble
    session_data["messages"] = messages
    
    # 6. Write final JSON
    output_dir.mkdir(parents=True, exist_ok=True)
    
    # Check for accidental overwrite (highly unlikely with UUID, but defensive)
    if output_path.exists():
        output_path = output_dir / f"session-{filename_date}-{short_hash}-restored.json"
        
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(session_data, f, separators=(",", ":"), ensure_ascii=False)
        
    print(f"--- Packaging Summary ---")
    print(f"Messages packed: {len(messages)}")
    print(f"New Session ID: {new_uuid}")
    print(f"Base Session ID: {base_id}")
    print(f"Summary generated: {session_data['summary']}")
    print(f"Final JSON Size: {output_path.stat().st_size} bytes")
    print(f"Saved to: {output_path}")

if __name__ == "__main__":
    main()
