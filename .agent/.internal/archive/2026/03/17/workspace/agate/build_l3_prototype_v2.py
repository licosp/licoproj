import json
import sys
from pathlib import Path

def build_prototype_v2(l4_root, stage1_quota=50, stage2_quota=50):
    l4_root = Path(l4_root)
    messages_dir = l4_root / "messages"
    
    # 1. Gather and sort JSONL files (newest first)
    jsonl_files = sorted(list(messages_dir.rglob("*.jsonl")), reverse=True)
    
    stage1_lines = []
    stage2_lines = []
    
    files_touched = []
    
    for jsonl_file in jsonl_files:
        if len(stage1_lines) >= stage1_quota and len(stage2_lines) >= stage2_quota:
            break
            
        files_touched.append(str(jsonl_file.relative_to(l4_root)))
        
        # Read all lines in file and reverse them to process newest first
        with jsonl_file.open("r", encoding="utf-8") as f:
            lines = [line.strip() for line in f if line.strip()]
        
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
                    is_gemini_with_content = ((msg_type == "gemini" or msg_type == "model") and bool(content))
                    
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
        
    # Let's also print where the oldest Stage 2 line came from
    if final_messages:
        oldest = final_messages[0]
        print(f"\nOldest extracted line timestamp: {oldest.get('timestamp')}")
        
    print(f"Total reconstructed turns: {len(final_messages)}")

if __name__ == "__main__":
    l4_dir = ".repos/.licoshdw/conversations_cli/identifiers/agate"
    build_prototype_v2(l4_dir)
