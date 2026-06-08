import argparse
import sys
from pathlib import Path

from lico_logger import add_file_handler, get_logger

logger = get_logger(__name__)


def get_debug_log_path() -> Path:
    """Return the fixed path for the plugin debug log."""
    return Path.cwd() / ".temp" / "opencode" / "plugin-debug.log"

def get_events_log_path() -> Path:
    """Return the path for the JSONL events dump."""
    return Path.cwd() / ".temp" / "opencode" / "events.jsonl"

def get_user_input_log_path() -> Path:
    """Return the path for the filtered user input JSONL dump."""
    return Path.cwd() / ".temp" / "opencode" / "events-user-input.jsonl"

def get_agent_response_log_path() -> Path:
    """Return the path for the filtered agent response JSONL dump."""
    return Path.cwd() / ".temp" / "opencode" / "events-agent-response.jsonl"

def get_state_path() -> Path:
    """Return the path for the stateless role mapping file."""
    return Path.cwd() / ".temp" / "opencode" / "state.json"

def init_environment() -> None:
    workspace = Path.cwd()
    opencode_temp_dir = workspace / ".temp" / "opencode"
    events_dir = opencode_temp_dir / "events"
    log_file = get_debug_log_path()
    events_log = get_events_log_path()
    user_log = get_user_input_log_path()
    agent_log = get_agent_response_log_path()
    state_file = get_state_path()

    import shutil

    if events_dir.exists():
        shutil.rmtree(events_dir)
    events_dir.mkdir(parents=True, exist_ok=True)

    for f in [log_file, events_log, user_log, agent_log, state_file]:
        if f.exists():
            try:
                f.unlink()
            except OSError:
                pass

def main() -> None:
    parser = argparse.ArgumentParser(description="Lico Observer OpenCode hook")
    parser.add_argument(
        "--init", help="Initialize the opencode temp directory", action="store_true"
    )
    parser.add_argument("payload", help="The event payload file", nargs="?", type=str)

    args = parser.parse_args()

    if args.init:
        init_environment()

    # Configure file logging
    add_file_handler(logger, get_debug_log_path())

    if args.init:
        logger.info("--- Plugin Loaded ---")
        return

    if not args.payload:
        logger.error("No payload provided and --init not specified.")
        sys.exit(1)

    import json

    payload_path = Path(args.payload)
    if not payload_path.exists():
        logger.error(f"Payload file not found: {args.payload}")
        sys.exit(1)

    try:
        data = json.loads(payload_path.read_text(encoding="utf-8"))
        event_type = data.get("type", "UNKNOWN")
        logger.info(f"Received event: {event_type}")

        events_log = get_events_log_path()
        with open(events_log, "a", encoding="utf-8") as f:
            f.write(json.dumps(data, ensure_ascii=False) + "\n")

        # --- User Input Extraction Logic ---
        state_path = get_state_path()
        loaded_state = {}
        if state_path.exists():
            try:
                loaded_state = json.loads(state_path.read_text(encoding="utf-8"))
            except Exception:
                pass

        state = {"roles": {}, "buffered_parts": {}}
        if "roles" in loaded_state:
            state = loaded_state
        elif loaded_state:
            state["roles"] = loaded_state

        state_changed = False
        prop = data.get("properties", {})

        if event_type == "message.updated":
            info = prop.get("info", {})
            if isinstance(info, dict):
                msg_id = info.get("id")
                role = info.get("role")
                if msg_id and role and state["roles"].get(msg_id) != role:
                    state["roles"][msg_id] = role
                    state_changed = True
                    # Flush buffered parts if this is a user or assistant
                    if msg_id in state["buffered_parts"]:
                        if role == "user":
                            user_log = get_user_input_log_path()
                            with open(user_log, "a", encoding="utf-8") as f:
                                for buffered_event in state["buffered_parts"][msg_id]:
                                    f.write(json.dumps(buffered_event, ensure_ascii=False) + "\n")
                                    logger.info(f"Asynchronous buffering: {role, buffered_event.get('type')}, {buffered_event.get('id')}")
                        elif role == "assistant":
                            agent_log = get_agent_response_log_path()
                            with open(agent_log, "a", encoding="utf-8") as f:
                                for buffered_event in state["buffered_parts"][msg_id]:
                                    f.write(json.dumps(buffered_event, ensure_ascii=False) + "\n")
                                    logger.info(f"Asynchronous buffering: {role, buffered_event.get('type')}, {buffered_event.get('id')}")
                        # Clear buffer once role is known
                        del state["buffered_parts"][msg_id]

        elif event_type == "message.part.updated":
            part = prop.get("part", {})
            if isinstance(part, dict) and "text" in part:
                msg_id = part.get("messageID")
                if msg_id:
                    role = state["roles"].get(msg_id)
                    if role == "user":
                        # We know it's a user, append directly
                        user_log = get_user_input_log_path()
                        with open(user_log, "a", encoding="utf-8") as f:
                            f.write(json.dumps(data, ensure_ascii=False) + "\n")
                    elif role == "assistant":
                        # We know it's an assistant, append directly
                        agent_log = get_agent_response_log_path()
                        with open(agent_log, "a", encoding="utf-8") as f:
                            f.write(json.dumps(data, ensure_ascii=False) + "\n")
                    elif role is None:
                        # We don't know the role yet, buffer it
                        if msg_id not in state["buffered_parts"]:
                            state["buffered_parts"][msg_id] = []
                        state["buffered_parts"][msg_id].append(data)
                        state_changed = True

        if state_changed:
            state_path.write_text(json.dumps(state, ensure_ascii=False), encoding="utf-8")

    except Exception as e:
        logger.error(f"Failed to parse payload: {e}")


if __name__ == "__main__":
    main()
