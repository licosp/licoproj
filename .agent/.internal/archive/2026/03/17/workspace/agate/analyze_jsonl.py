import json
import sys
from pathlib import Path

def analyze_jsonl(filepath):
    path = Path(filepath)
    if not path.exists():
        print(f"File not found: {filepath}")
        return

    total_lines = 0
    categories = {
        "user_input": 0,
        "slash_command": 0,
        "model_final_response": 0,
        "model_thought_only": 0,
        "model_tool_call": 0,
        "tool_response": 0,
        "other": 0
    }
    
    total_chars = 0
    pure_conversation_chars = 0

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip():
                continue
            total_lines += 1
            total_chars += len(line)
            
            try:
                obj = json.loads(line)
                msg_type = obj.get("type")
                
                # 1. User Input
                if msg_type == "user":
                    content_val = obj.get("content", "")
                    if isinstance(content_val, list):
                        content = str(content_val).strip()
                    else:
                        content = str(content_val).strip()
                    if content.startswith("/"):
                        categories["slash_command"] += 1
                    else:
                        categories["user_input"] += 1
                        pure_conversation_chars += len(line)
                        
                # 2. Model Responses
                elif msg_type == "model":
                    has_content = bool(obj.get("content", "").strip())
                    has_thoughts = bool(obj.get("thoughts", ""))
                    has_tool_calls = bool(obj.get("toolCalls", []))
                    
                    if has_tool_calls:
                        categories["model_tool_call"] += 1
                    elif has_content and not has_tool_calls:
                        # Final response in a turn (might have thoughts attached, but has final content)
                        categories["model_final_response"] += 1
                        # Calculate size of a hypothetically stripped pure response
                        pure_obj = {"id": obj.get("id"), "type": "model", "content": obj.get("content"), "timestamp": obj.get("timestamp")}
                        pure_conversation_chars += len(json.dumps(pure_obj, separators=(",", ":"), ensure_ascii=False))
                    elif has_thoughts and not has_content and not has_tool_calls:
                        # Interim thought blocks (sometimes emitted by CLI)
                        categories["model_thought_only"] += 1
                    else:
                        categories["other"] += 1
                        
                # 3. Tool Responses
                elif msg_type == "tool":
                    categories["tool_response"] += 1
                else:
                    categories["other"] += 1
                    
            except json.JSONDecodeError:
                categories["other"] += 1

    print("--- JSONL Composition Analysis ---")
    print(f"Target: {filepath}")
    print(f"Total Lines (JSON Objects): {total_lines}")
    print("----------------------------------")
    for k, v in categories.items():
        print(f"{k}: {v} ({(v/total_lines)*100:.1f}%)")
    
    print("----------------------------------")
    print("--- Size / Compression Estimate ---")
    print(f"Total File Size (chars): {total_chars}")
    print(f"Estimated Pure Conv Size (chars): {pure_conversation_chars}")
    print(f"Potential Compression Ratio (Size): {(pure_conversation_chars/total_chars)*100:.1f}% of original")
    
    # Calculate Line Compression Ratio
    # Pure lines = User Input + Model Final Response
    pure_lines = categories["user_input"] + categories["model_final_response"]
    print(f"Potential Compression Ratio (Lines): {(pure_lines/total_lines)*100:.1f}% of original ({pure_lines}/{total_lines} lines)")

if __name__ == "__main__":
    analyze_jsonl(sys.argv[1])
