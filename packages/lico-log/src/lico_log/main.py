"""Standard dual-stream log appender for LicoTor ecosystem."""

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


def append_to_log(file_path: Path, content: str) -> None:
    """Append content to a log file with timestamp and locking.

    Args:
        file_path (Path): Path to the log file.
        content (str): Text content to append.
    """
    now = datetime.now(UTC)
    timestamp = now.strftime("[%Y-%m-%dT%H:%M:%S.%f]")
    final_content = f"{timestamp} {content}"

    try:
        with file_path.open("a", encoding="utf-8") as f:
            # Simple advisory locking
            fcntl.flock(f, fcntl.LOCK_EX)
            f.write(final_content + "\n")
            fcntl.flock(f, fcntl.LOCK_UN)

    except OSError:
        logger.exception(LicoMsg.LOG_APPENDER.WRITE_FAILED)
        sys.exit(1)
    except Exception:
        logger.exception(LicoMsg.LOG_APPENDER.READ_FAILED)
        sys.exit(1)


REQUIRED_ARGS = 3


def main() -> None:
    """CLI Entry point."""
    if len(sys.argv) < REQUIRED_ARGS:
        logger.error(LicoMsg.LOG_APPENDER.USAGE)
        sys.exit(1)

    log_path = Path(sys.argv[1])
    log_content = sys.argv[2]

    append_to_log(log_path, log_content)


if __name__ == "__main__":
    main()
