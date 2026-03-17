import json
import sys
from pathlib import Path

def inspect_jsonl(filepath):
    path = Path(filepath)
    if not path.exists():
        print(f"File not found: {filepath}")
        return

    found_user = False
    found_chat_response = False
    found_tool_call = False
    found_thought = False

    with path.open("r", encoding="utf-8") as f:
        for line in f:
            if not line.strip(): continue
            try:
                obj = json.loads(line)
                msg_type = obj.get("type")
                
                # A: User Query
                if msg_type == "user" and not found_user:
                    print("\n--- [A] USER QUERY ---")
                    print(json.dumps(obj, indent=2, ensure_ascii=False)[:500] + "...")
                    found_user = True
                    
                # B & C: Model Responses
                elif msg_type == "gemini" or msg_type == "model":
                    content = obj.get("content", "")
                    has_thoughts = bool(obj.get("thoughts", []))
                    has_tool_calls = bool(obj.get("toolCalls", []))
                    
                    # B: Chat UI Response (has actual text content)
                    # Notice: Sometimes Gemini CLI puts text in 'content' even if toolCalls exist, 
                    # but usually a pure chat response has content and NO tool calls (or it's the final turn).
                    if content and not has_tool_calls and not found_chat_response:
                        print("\n--- [B] LICO CHAT RESPONSE (Pure) ---")
                        print(json.dumps(obj, indent=2, ensure_ascii=False)[:500] + "...")
                        found_chat_response = True
                        
                    # C: Other (Tool Call)
                    if has_tool_calls and not found_tool_call:
                        print("\n--- [C] OTHER: TOOL CALL ---")
                        # Truncate tool calls to avoid massive output
                        trunc_obj = {k: v for k, v in obj.items() if k != 'toolCalls'}
                        trunc_obj['toolCalls'] = "[[TOOL CALLS OMITTED]]"
                        print(json.dumps(trunc_obj, indent=2, ensure_ascii=False)[:500] + "...")
                        found_tool_call = True

                    # C: Other (Thought block without content/tool)
                    if has_thoughts and not content and not has_tool_calls and not found_thought:
                        print("\n--- [C] OTHER: THOUGHT ONLY ---")
                        print(json.dumps(obj, indent=2, ensure_ascii=False)[:500] + "...")
                        found_thought = True
                        
                # C: Other (Tool Result)
                elif msg_type == "tool" and not found_tool_call:
                     # sometimes tool results are separate
                     pass

            except Exception as e:
                pass

if __name__ == "__main__":
    inspect_jsonl(sys.argv[1])
