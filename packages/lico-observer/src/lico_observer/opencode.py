import argparse
import sys
from pathlib import Path

from lico_logger import add_file_handler, get_logger

logger = get_logger(__name__)

def get_debug_log_path() -> Path:
    """Return the fixed path for the plugin debug log."""
    return Path.cwd() / ".temp" / "opencode" / "plugin-debug.log"

def init_environment() -> None:
    workspace = Path.cwd()
    opencode_temp_dir = workspace / ".temp" / "opencode"
    events_dir = opencode_temp_dir / "events"
    log_file = get_debug_log_path()

    import shutil

    if events_dir.exists():
        shutil.rmtree(events_dir)
    events_dir.mkdir(parents=True, exist_ok=True)

    if log_file.exists():
        try:
            log_file.unlink()
        except OSError:
            pass

def main() -> None:
    parser = argparse.ArgumentParser(description="Lico Observer OpenCode hook")
    parser.add_argument("--init", help="Initialize the opencode temp directory", action="store_true")
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

    logger.info(f"Received event payload: {args.payload}")


if __name__ == "__main__":
    main()
