"""Append content to a log file with timestamp and locking."""

import datetime
import fcntl
import os
import signal
import sys
from pathlib import Path

# Strict Type Enforcement
# This script is designed to be checked with mypy


def handle_signal(signum: int, _frame: object | None) -> None:
    """Handle termination signals to ensure cleanup."""
    # Print to stderr to capture in logs if possible
    sys.stderr.write(f"Error: Received signal {signum}. Exiting...\n")
    sys.exit(128 + signum)


def append_log(log_path: str, content_file: str) -> None:
    """Append content from content_file to log_path with a header.

    Uses file locking to prevent race conditions.
    """
    if not Path(content_file).exists():
        sys.stderr.write(f"Error: Content file '{content_file}' not found.\n")
        sys.exit(1)

    try:
        content = Path(content_file).read_text(encoding="utf-8")
    except (OSError, ValueError) as e:
        sys.stderr.write(f"Error: Failed to read content file: {e}\n")
        sys.exit(1)

    # Generate Timestamp
    # Generate Timestamp (ISO 8601 with JST and seconds)
    jst = datetime.timezone(datetime.timedelta(hours=9))
    timestamp: str = datetime.datetime.now(jst).isoformat(timespec="seconds")

    # Replace placeholder
    # If the content doesn't have the placeholder, we might want to prepend a
    # header, but the current protocol assumes the AI generates the header
    # with the placeholder.
    final_content: str = content.replace("{{TIMESTAMP}}", timestamp)

    # Atomic Append with Locking
    try:
        # Open in Append mode
        # mode 'a' is atomic on POSIX for small writes generally,
        # but we use flock for safety across processes.
        with Path(log_path).open("a", encoding="utf-8") as f_dest:
            # Blocking Exclusive Lock
            # This ensures that if multiple appenders run, they wait for
            # each other (serialized) instead of crashing or interleaving.
            fcntl.flock(f_dest, fcntl.LOCK_EX)
            try:
                f_dest.write(final_content)
                f_dest.write("\n")  # Ensure newline at end
                f_dest.flush()
                # fsync to force write to disk? Maybe overkill but safe.
                os.fsync(f_dest.fileno())
            finally:
                fcntl.flock(f_dest, fcntl.LOCK_UN)

    except (OSError, ValueError) as e:
        sys.stderr.write(f"Error: Failed to write to log file: {e}\n")
        sys.exit(1)


def main() -> None:
    """Execute the log appender logic."""
    # Register Signal Handlers
    signal.signal(signal.SIGTERM, handle_signal)
    signal.signal(signal.SIGINT, handle_signal)

    # Singleton Enforcement (Replace safe_append.sh logic)
    # Lock this script file itself to ensure only one instance runs at a time.
    # If locked, wait or fail? For logging, we should probably wait
    # (blocking lock) to ensure the log is eventually written, or fail fast
    # if it takes too long.
    # Given the blocking lock in append_log, we might not need a separate
    # singleton lock IF the append_log lock covers the whole critical section.
    # However, to be safe against zombie interpreters, we can use a PID file
    # or flock on the script.

    # We will rely on the flock in append_log for serialization.
    # To prevent "zombies", we rely on the signal handlers and standard
    # timeouts (if invoked via extensive wrapper).
    # But since we deleted the wrapper, we should implement a self-timeout?
    # For now, we trust strict signal handling.

    arg_count_min = 3
    if len(sys.argv) < arg_count_min:
        sys.stderr.write(
            "Usage: python3 log_appender.py <log_path> <content_file>\n",
        )
        sys.exit(1)

    log_path: str = sys.argv[1]
    content_file: str = sys.argv[2]

    # Self-timeout watchdog (optional but good for robustness against hangs)
    signal.alarm(10)  # Kill self after 10 seconds if not done

    append_log(log_path, content_file)


if __name__ == "__main__":
    main()
