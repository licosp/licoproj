"""Unified linting tool for `licoproj`."""

import argparse
import logging
import shutil
import subprocess
import sys
from pathlib import Path

# Configure logging for CLI feedback
logging.basicConfig(
    level=logging.INFO, format="%(message)s", stream=sys.stdout
)
logger = logging.getLogger(__name__)


def _get_executable(name: str) -> str | None:
    """Resolve the executable path, looking in venv if needed.

    Returns:
        The path to the executable if found, else None.
    """
    executable = shutil.which(name)
    if not executable:
        # Try to find in the same directory as python (for venv)
        python_dir = Path(sys.executable).parent
        candidate = python_dir / f"{name}.exe"
        if not candidate.exists():
            candidate = python_dir / name

        if candidate.exists():
            executable = str(candidate)
    return executable


def run_command(command: list[str], path: Path) -> bool:
    """Run a shell command and return success.

    Returns:
        True if the command succeeded, else False.
    """
    executable = _get_executable(command[0])
    if not executable:
        logger.error("Error: Command '%s' not found.", command[0])
        return False

    full_cmd = [executable, *command[1:], str(path)]
    logger.info("Running: %s", " ".join(full_cmd))
    try:
        result = subprocess.run(
            full_cmd, capture_output=False, check=False, shell=False
        )
    except FileNotFoundError:
        logger.exception("Error: Command '%s' not found.", executable)
        return False
    else:
        return result.returncode == 0


def _parse_path() -> Path:
    """Parse path from command line arguments.

    Returns:
        The absolute path to check.
    """
    path_val = "."
    if len(sys.argv) > 1:
        if sys.argv[1] in {"-h", "--help"}:
            parser = argparse.ArgumentParser(
                description="Unified linting tool for Licochron"
            )
            parser.add_argument(
                "path", nargs="?", default=".", help="Path to check"
            )
            parser.print_help()
            sys.exit(0)
        path_val = sys.argv[1]
    return Path(path_val).absolute()


def main() -> None:
    """Entry point for the unified linting tool."""
    target_path = _parse_path()
    commands = [
        (["ruff", "check", "--no-fix"], "Ruff Check"),
        (["ruff", "format", "--check"], "Ruff Format"),
        (["pyright"], "Pyright"),
        (["mypy"], "Mypy"),
    ]

    success = True
    for cmd, name in commands:
        logger.info("\n--- %s ---", name)
        if not run_command(cmd, target_path):
            success = False
            logger.error("%s failed!", name)

    if success:
        logger.info("\nAll checks passed!")
        sys.exit(0)
    else:
        logger.error("\nSome checks failed. Please fix the issues.")
        sys.exit(1)


if __name__ == "__main__":
    main()
