"""Logging manager and configuration."""

import logging
import sys
from datetime import datetime, timedelta, timezone
from pathlib import Path


class MaxLevelFilter(logging.Filter):
    """Filter to allow only logs BELOW a certain level."""

    def __init__(self, max_level: int) -> None:
        """Initialize the filter.

        Args:
            max_level (int): Maximum logging level allowed.
        """
        super().__init__()
        self.max_level = max_level

    def filter(self, record: logging.LogRecord) -> bool:
        """Allow logs only if their level is below or equal to max_level.

        Args:
            record (logging.LogRecord): The log record to check.

        Returns:
            bool: True if the log should be passed, False otherwise.
        """
        return record.levelno <= self.max_level


class LicoFormatter(logging.Formatter):
    """Custom formatter to enforce ISO 8601 with JST offset and multiline output."""

    def formatTime(self, record: logging.LogRecord, datefmt: str | None = None) -> str:
        """Return the timestamp in standard YYYY-MM-DDTHH:MM:SS+09:00 format."""
        jst = timezone(timedelta(hours=9))
        dt = datetime.fromtimestamp(record.created, tz=jst)
        return dt.isoformat(timespec="seconds")


def get_logger(name: str, level: int = logging.INFO) -> logging.Logger:
    """Get a configured logger with dual-stream licotor format.

    - INFO and below -> stdout
    - WARNING and above -> stderr

    Args:
        name (str): Logger name (usually __name__).
        level (int): Initial logging level.

    Returns:
        logging.Logger: Configured logger instance.
    """
    logger = logging.getLogger(name)

    # Avoid duplicate handlers if already configured
    if logger.hasHandlers():
        return logger

    logger.setLevel(level)

    # Standard format: [TIME] LEVEL [NAME] \n MESSAGE
    formatter = LicoFormatter(
        "[%(asctime)s] %(levelname)s [%(name)s]\n%(message)s"
    )

    # 1. Stdout Handler (INFO and below)
    stdout_handler = logging.StreamHandler(sys.stdout)
    stdout_handler.setFormatter(formatter)
    stdout_handler.setLevel(logging.DEBUG)
    stdout_handler.addFilter(MaxLevelFilter(logging.INFO))
    logger.addHandler(stdout_handler)

    # 2. Stderr Handler (WARNING and above)
    stderr_handler = logging.StreamHandler(sys.stderr)
    stderr_handler.setFormatter(formatter)
    stderr_handler.setLevel(logging.WARNING)
    logger.addHandler(stderr_handler)

    return logger


def add_file_handler(logger: logging.Logger, log_file: Path) -> None:
    """Attach a FileHandler to the given logger.

    Args:
        logger (logging.Logger): The logger instance.
        log_file (Path): The path to the log file.
    """
    formatter = LicoFormatter(
        "[%(asctime)s] %(levelname)s [%(name)s]\n%(message)s"
    )
    # Ensure directory exists
    log_file.parent.mkdir(parents=True, exist_ok=True)

    file_handler = logging.FileHandler(log_file, encoding="utf-8")
    file_handler.setFormatter(formatter)
    file_handler.setLevel(logging.DEBUG)
    logger.addHandler(file_handler)
