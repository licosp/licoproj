"""Append content to a log file with timestamp and locking."""

import datetime
import fcntl
import os
import signal
import sys
from pathlib import Path

from lico_logger import LicoMsg, get_logger

logger = get_logger(__name__)


def append_log(log_path: str, content_file: str) -> None:
    """Read content and append to log with lock and timestamp."""
    try:
        content_path = Path(content_file)
        if not content_path.exists():
            logger.error(
                LicoMsg.LOG_APPENDER.CONTENT_NOT_FOUND.format(
                    file=content_file
                )
            )
            sys.exit(1)

        content = content_path.read_text(encoding="utf-8")

        # Replace {{TIMESTAMP}} with current ISO 8601 JST
        now_jst = datetime.datetime.now(
            datetime.timezone(datetime.timedelta(hours=9))
        )
        timestamp = now_jst.strftime("%Y-%m-%dT%H:%M:%S+09:00")
        final_content = content.replace("{{TIMESTAMP}}", timestamp)

        # Append with exclusive lock
        with Path(log_path).open("a", encoding="utf-8") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            f.write(final_content + "\n")
            fcntl.flock(f, fcntl.LOCK_UN)

    except (OSError, IOError) as e:
        logger.error(LicoMsg.LOG_APPENDER.WRITE_FAILED.format(error=e))
        sys.exit(1)
    except Exception as e:
        logger.error(LicoMsg.LOG_APPENDER.READ_FAILED.format(error=e))
        sys.exit(1)


def handle_signal(signum, frame):
    """Handle termination signals."""
    logger.error(LicoMsg.LOG_APPENDER.SIGNAL_EXIT.format(sig=signum))
    sys.exit(1)


def main() -> None:
    """CLI Entry point."""
    if len(sys.argv) < 3:
        logger.error(LicoMsg.LOG_APPENDER.USAGE)
        sys.exit(1)

    signal.signal(signal.SIGINT, handle_signal)
    signal.signal(signal.SIGTERM, handle_signal)

    log_path: str = sys.argv[1]
    content_file: str = sys.argv[2]

    signal.alarm(300)  # Extended to 5 minutes based on Leonidas instruction.

    append_log(log_path, content_file)


if __name__ == "__main__":
    main()
