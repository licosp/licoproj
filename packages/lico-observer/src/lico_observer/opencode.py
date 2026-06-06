import argparse
import sys
from datetime import UTC, datetime
from pathlib import Path


def _get_timestamp() -> str:
    return datetime.now(tz=UTC).astimezone().isoformat(
        timespec="seconds"
    )

def init_environment(workspace_path: str) -> None:
    workspace = Path(workspace_path)
    opencode_temp_dir = workspace / ".temp" / "opencode"
    events_dir = opencode_temp_dir / "events"
    log_file = opencode_temp_dir / "plugin-debug.log"

    import shutil

    if events_dir.exists():
        shutil.rmtree(events_dir)
    events_dir.mkdir(parents=True, exist_ok=True)

    boot_time = _get_timestamp()
    log_file.write_text(f"--- Plugin Loaded at {boot_time} ---\n", encoding="utf-8")

def main() -> None:
    parser = argparse.ArgumentParser(description="Lico Observer OpenCode hook")
    parser.add_argument("--init", help="Initialize the opencode temp directory in the given workspace", type=str)
    parser.add_argument("payload", help="The event payload file", nargs="?", type=str)

    args = parser.parse_args()

    if args.init:
        init_environment(args.init)
        return

    if not args.payload:
        print("Error: No payload provided and --init not specified.")
        sys.exit(1)

    print(f"Received event payload: {args.payload}")
    print("timestamp:", _get_timestamp())


if __name__ == "__main__":
    main()
