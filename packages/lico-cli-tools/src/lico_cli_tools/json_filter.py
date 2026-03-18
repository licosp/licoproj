import argparse
import json
import sys
from pathlib import Path

def main():
    parser = argparse.ArgumentParser(description="Extract and filter L4 JSONL logs into a single condensed JSONL file.")
    parser.add_argument("input_dir", type=str, help="Path to the identifier's L4 directory (e.g., .repos/.licoshdw/conversations_cli/identifiers/agate)")
    parser.add_argument("output_file", type=str, help="Path to the output filtered JSONL file (e.g., filtered_memory.jsonl)")
    parser.add_argument("--stage1", type=int, default=500, help="Quota for Stage 1 (Full retention of recent turns). Default: 500")
    parser.add_argument("--stage2", type=int, default=500, help="Quota for Stage 2 (Filter out tool calls, keep conversation/thoughts). Default: 500")
    
    args = parser.parse_args()
    
    l4_root = Path(args.input_dir)
    output_path = Path(args.output_file)
    stage1_quota = args.stage1
    stage2_quota = args.stage2
    
    if not l4_root.exists() or not l4_root.is_dir():
        print(f"Error: Input directory {l4_root} does not exist or is not a directory.", file=sys.stderr)
        sys.exit(1)
        
    messages_dir = l4_root / "messages"
    
    if not messages_dir.exists():
        print(f"Error: Messages directory {messages_dir} not found.", file=sys.stderr)
        sys.exit(1)
        
    # Gather and sort JSONL files (newest first)
    jsonl_files = sorted(list(messages_dir.rglob("*.jsonl")), reverse=True)
    
    stage1_lines = []
    stage2_lines = []
    files_touched = []
    
    for jsonl_file in jsonl_files:
        if len(stage1_lines) >= stage1_quota and len(stage2_lines) >= stage2_quota:
            break
            
        files_touched.append(str(jsonl_file.relative_to(l4_root)))
        
        # Read all lines in file and reverse them to process newest first
        try:
            with jsonl_file.open("r", encoding="utf-8") as f:
                lines = [line.strip() for line in f if line.strip()]
        except Exception as e:
            print(f"Warning: Failed to read {jsonl_file}: {e}", file=sys.stderr)
            continue
            
        lines.reverse()
        
        for line in lines:
            if len(stage1_lines) < stage1_quota:
                # Stage 1: Keep everything
                try:
                    obj = json.loads(line)
                    stage1_lines.append(obj)
                except:
                    pass
            elif len(stage2_lines) < stage2_quota:
                # Stage 2: Filter A (User) and B (Gemini with content)
                try:
                    obj = json.loads(line)
                    msg_type = obj.get("type")
                    content = obj.get("content", "")

                    is_user = (msg_type == "user")
                    # Check if content is truthy (non-empty string or non-empty list)
                    has_content = bool(content)
                    is_gemini_with_content = ((msg_type == "gemini" or msg_type == "model") and has_content)

                    if is_user or is_gemini_with_content:
                        if "toolCalls" in obj:
                            del obj["toolCalls"]
                        stage2_lines.append(obj)
                except:
                    pass
            else:
                break # Both quotas met

    # Reverse the collected lists so they are chronological (oldest to newest)
    stage2_lines.reverse()
    stage1_lines.reverse()
    
    final_messages = stage2_lines + stage1_lines
    
    print(f"--- Extraction Summary ---")
    print(f"Target Quota: Stage1={stage1_quota}, Stage2={stage2_quota}")
    print(f"Actually Collected: Stage1={len(stage1_lines)}, Stage2={len(stage2_lines)}")
    print(f"Files accessed (newest to oldest):")
    for f in files_touched:
        print(f"  - {f}")
        
    if final_messages:
        oldest = final_messages[0]
        print(f"\nOldest extracted line timestamp: {oldest.get('timestamp')}")
        
    print(f"Total extracted turns: {len(final_messages)}")
    
    # Write to output JSONL
    output_path.parent.mkdir(parents=True, exist_ok=True)
    with output_path.open("w", encoding="utf-8") as f:
        for msg in final_messages:
            line = json.dumps(msg, separators=(",", ":"), ensure_ascii=False)
            f.write(line + "\n")
            
    print(f"Saved filtered JSONL to: {output_path}")

if __name__ == "__main__":
    main()
