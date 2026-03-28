"""Unified Command Shim for Lico.

Provides safety nets for destructive commands and environment routing.
"""

import datetime
import os
import subprocess
import sys
from pathlib import Path


def find_workspace_root() -> Path:
    """Find the root of the project."""
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
            print(
                "❌ [Shim] BLOCKED: Operating on .shadow/ from root is forbidden. cd first.",
                file=sys.stderr,
            )
            sys.exit(1)
        if arg in ("restore", "clean"):
            print(
                f"❌ [Shim] BLOCKED: 'git {arg}' is restricted to prevent data loss.",
                file=sys.stderr,
            )
            sys.exit(1)

    if "reset" in args and "--hard" in args:
        print(
            "❌ [Shim] BLOCKED: 'git reset --hard' destroys history. Use --soft or bypass.",
            file=sys.stderr,
        )
        sys.exit(1)

    os.execvp("/usr/bin/git", ["git", *args])


def handle_python(args: list[str]) -> None:
    """Route python to uv run python."""
    os.execvp("uv", ["uv", "run", "python", *args])


def main() -> None:
    """Entry point for lico-shim."""
    if len(sys.argv) < 2:
        print("Usage: lico-shim <command> [args...]", file=sys.stderr)
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
        # Fallback to normal execution if command is not shimmed but somehow passed here
        print(
            f"❌ [Shim] ERROR: Unknown shim command '{command}'.",
            file=sys.stderr,
        )
        sys.exit(1)


if __name__ == "__main__":
    main()
