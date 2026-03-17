import json
import sys
from pathlib import Path

def build_prototype(l4_root, output_path):
    l4_root = Path(l4_root)
    output_path = Path(output_path)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    # 1. Read metadata
    meta_path = l4_root / "metadata.json"
    if meta_path.exists():
        with meta_path.open("r", encoding="utf-8") as f:
            session_data = json.load(f)
    else:
        print(f"Warning: {meta_path} not found. Using empty structure.")
        session_data = {}
        
    # 2. Gather all JSONL lines
    all_lines = []
    messages_dir = l4_root / "messages"
    if messages_dir.exists():
        for jsonl_file in messages_dir.rglob("*.jsonl"):
            with jsonl_file.open("r", encoding="utf-8") as f:
                for line in f:
                    if line.strip():
                        try:
                            obj = json.loads(line)
                            all_lines.append(obj)
                        except json.JSONDecodeError:
                            pass

    # 3. Sort by timestamp and take the last 100
    all_lines.sort(key=lambda x: x.get("timestamp", ""))
    
    if len(all_lines) == 0:
        print("No lines found!")
        return
        
    latest_100 = all_lines[-100:]
    
    # Calculate split point (up to 100 lines)
    total_len = len(latest_100)
    mid_point = total_len // 2
    
    older_half = latest_100[:mid_point]
    newer_half = latest_100[mid_point:]
    
    reconstructed_messages = []
    
    # 4. Process Older Half (Stage 2: Keep A, B. Drop C)
    for obj in older_half:
        msg_type = obj.get("type")
        content = obj.get("content", "")
        
        # Determine if it's A or B
        is_user = (msg_type == "user")
        is_gemini_with_content = ((msg_type == "gemini" or msg_type == "model") and bool(content))
        
        # Drop C (tool calls, pure thoughts without content)
        if is_user or is_gemini_with_content:
            # Strip toolCalls just in case it's a mixed B+C object
            if "toolCalls" in obj:
                del obj["toolCalls"]
            reconstructed_messages.append(obj)
            
    print(f"Older half (Stage 2): Original {len(older_half)} lines -> Reduced to {len(reconstructed_messages)} lines.")

    # 5. Process Newer Half (Stage 1: Keep All)
    reconstructed_messages.extend(newer_half)
    print(f"Newer half (Stage 1): Appended {len(newer_half)} lines directly.")
    
    # 6. Construct Final JSON
    session_data["messages"] = reconstructed_messages
    
    # 7. Write to output
    with output_path.open("w", encoding="utf-8") as f:
        json.dump(session_data, f, separators=(",", ":"), ensure_ascii=False)
        
    # Validation stats
    original_size = sum(len(json.dumps(obj, separators=(",", ":"), ensure_ascii=False)) for obj in latest_100)
    new_size = output_path.stat().st_size
    print(f"\n--- Result ---")
    print(f"Original Last 100 Turns Est. Size: {original_size} bytes")
    print(f"Reconstructed Size (with Stage 2 filtering): {new_size} bytes")
    print(f"Compression: {new_size / original_size * 100:.1f}%")
    print(f"Final Turn Count: {len(reconstructed_messages)}")
    print(f"Saved to: {output_path}")

if __name__ == "__main__":
    l4_dir = ".repos/.licoshdw/conversations_cli/identifiers/agate"
    out_file = ".agent/.internal/workspace/agate/test_restore/session_reconstructed.json"
    build_prototype(l4_dir, out_file)
