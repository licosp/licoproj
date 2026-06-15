"""Security and consistency shim for Git and FS operations."""

import datetime
import os
import subprocess
import sys
from pathlib import Path

from lico_logger import LicoMsg, add_stream_handler, get_logger

logger = get_logger(__name__)
add_stream_handler(logger)

"""Unified Command Shim for Lico.

Provides safety nets for destructive commands and environment routing.
"""


def find_workspace_root() -> Path:
    """Find the root of the project.

    Returns:
        Path: The absolute path to the workspace root.
    """
    current = Path.cwd()
    for parent in [current, *current.parents]:
        if (parent / ".git").exists() or (parent / "pyproject.toml").exists():
            return parent
    return current


def handle_rm(args: list[str]) -> None:
    """Move files to .trash instead of deleting."""
    root = find_workspace_root()
    timestamp = datetime.datetime.now(tz=datetime.UTC).strftime(
        "%Y-%m-%dT%H%M%S"
    )
    trash_path = root / ".trash" / timestamp

    files = [a for a in args if not a.startswith("-")]
    if not files:
        os.execvp("/bin/rm", ["rm", *args])

    trash_path.mkdir(parents=True, exist_ok=True)
    subprocess.run(["/bin/mv", *files, str(trash_path)], check=False)

    # Try git rm just in case it was tracked
    result = subprocess.run(
        ["/usr/bin/git", "rev-parse", "--is-inside-work-tree"],
        capture_output=True,
        check=False,
    )
    if result.returncode == 0:
        for f in files:
            subprocess.run(
                ["/usr/bin/git", "add", "-u", f],
                capture_output=True,
                check=False,
            )


def handle_mv(args: list[str]) -> None:
    """Try git mv first, fallback to native mv."""
    result = subprocess.run(
        ["/usr/bin/git", "rev-parse", "--is-inside-work-tree"],
        capture_output=True,
        check=False,
    )
    if result.returncode == 0:
        git_mv = subprocess.run(["/usr/bin/git", "mv", *args], check=False)
        if git_mv.returncode == 0:
            return
    os.execvp("/bin/mv", ["mv", *args])


def handle_git(args: list[str]) -> None:
    """Block dangerous git commands."""
    for arg in args:
        if ".shadow/" in arg:
            logger.error(LicoMsg.SHIM.BLOCKED_SHADOW)
            sys.exit(1)
        if arg in {"restore", "clean"}:
            logger.error(LicoMsg.SHIM.BLOCKED_RESTRICTED.format(arg=arg))
            sys.exit(1)

    if "reset" in args and "--hard" in args:
        logger.error(LicoMsg.SHIM.BLOCKED_RESET_HARD)
        sys.exit(1)

    os.execvp("/usr/bin/git", ["git", *args])


def handle_python(args: list[str]) -> None:
    """Route python to uv run python."""
    os.execvp("uv", ["uv", "run", "python", *args])


def main() -> None:
    """Entry point for lico-shim."""
    min_args = 2
    if len(sys.argv) < min_args:
        logger.error(LicoMsg.SHIM.USAGE)
        sys.exit(1)

    command = sys.argv[1]
    args = sys.argv[2:]

    handlers = {
        "rm": handle_rm,
        "mv": handle_mv,
        "git": handle_git,
        "python": handle_python,
        "python3": handle_python,
    }

    handler = handlers.get(command)
    if handler:
        handler(args)
    else:
        # Fallback if command is not shimmed but somehow passed here
        logger.error(LicoMsg.SHIM.ERR_UNKNOWN.format(command=command))
        sys.exit(1)


if __name__ == "__main__":
    main()
