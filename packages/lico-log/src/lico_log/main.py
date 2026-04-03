"""Log appender for LicoTor (v3.2.0).

Guardian of historical integrity and template rules.
"""

from __future__ import annotations

import fcntl
import signal
import sys
from datetime import UTC, datetime
from pathlib import Path
from typing import TYPE_CHECKING

from lico_logger import LicoMsg, get_logger

if TYPE_CHECKING:
    from types import FrameType

logger = get_logger(__name__)


def handle_signal(signum: int, _frame: FrameType | None) -> None:
    """Handle termination signals.

    Args:
        signum (int): Signal number.
        _frame (FrameType | None): Current stack frame (unused).
    """
    logger.error(LicoMsg.LOG_APPENDER.SIGNAL_EXIT.format(sig=signum))
    sys.exit(1)


# Setup signal handlers
signal.signal(signal.SIGINT, handle_signal)
signal.signal(signal.SIGTERM, handle_signal)


def validate_content(content: str) -> bool:
    """Validate that the content is a legitimate logging block.

    Args:
        content (str): The content to validate.

    Returns:
        bool: True if valid, False otherwise.
    """
    # 1. Reject empty or whitespace-only content
    stripped = content.strip()
    if not stripped:
        return False

    # 2. Reject accidental debug logs mixed in
    forbidden_keywords = {
        "LOGGING SUCCESS",
        "Exit Code:",
        "Process Group PGID:",
        "Successfully modified file:",
    }
    if any(kw in content for kw in forbidden_keywords):
        return False

    # 3. Ensure it starts with a valid header or section
    valid_starts = (
        "### Conversation:",
        "#### Response (Report):",
        "#### Response (Plan):",
    )
    return stripped.startswith(valid_starts)


def append_to_log(file_path: Path, content: str) -> None:
    """Append content to a log file with strict validation and locking.

    Args:
        file_path (Path): Path to the log file.
        content (str): Text content to append.
    """
    if not validate_content(content):
        logger.error("Refusing to append invalid or contaminated content.")
        sys.exit(1)

    try:
        with file_path.open("a", encoding="utf-8") as f:
            # Simple advisory locking
            fcntl.flock(f, fcntl.LOCK_EX)
            # Ensure proper spacing between blocks
            f.write("\n" + content.strip() + "\n")
            fcntl.flock(f, fcntl.LOCK_UN)

    except OSError:
        logger.exception(LicoMsg.LOG_APPENDER.WRITE_FAILED)
        sys.exit(1)


REQUIRED_ARGS = 3


def main() -> None:
    """CLI Entry point for lico-log."""
    if len(sys.argv) < REQUIRED_ARGS:
        logger.error(LicoMsg.LOG_APPENDER.USAGE)
        sys.exit(1)

    log_path = Path(sys.argv[1])
    input_buffer_path = Path(sys.argv[2])

    if not input_buffer_path.exists():
        logger.error("Input buffer not found: %s", input_buffer_path)
        sys.exit(1)

    try:
        content = input_buffer_path.read_text(encoding="utf-8")
        # Pre-process content: Expand {{TIMESTAMP}} to standard format
        # Format: YYYY-MM-DDTHH:MM:SS+09:00
        now_ts = datetime.now(UTC).astimezone().isoformat(timespec="seconds")
        content = content.replace("{{TIMESTAMP}}", now_ts)

        append_to_log(log_path, content)
    except OSError:
        logger.exception("Failed to read input buffer.")
        sys.exit(1)


if __name__ == "__main__":
    main()
