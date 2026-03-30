import os
import sys
from pathlib import Path

from lico_logger import LicoMsg, get_logger

logger = get_logger(__name__)


class EmptyDirLinter:
    """Linter to detect and notify about empty directories."""

    def __init__(self, root_dir: str | None = None) -> None:
        self.root_dir = root_dir or str(Path.cwd())
        self.exclude_dirs = {
            ".git",
            ".venv",
            "node_modules",
            "__pycache__",
            ".temp",
            ".repos",
            ".trash",
        }

    def is_empty_dir(self, path: str) -> bool:
        """Check if a directory is empty (no files or sub-directories)."""
        try:
            # Check if there is anything inside
            return not any(os.scandir(path))
        except PermissionError, FileNotFoundError:
            return False

    def scan(self) -> bool:
        """Scan the directory tree for empty directories.

        Returns:
            bool: True if empty directories were found, False otherwise.
        """
        logger.info(LicoMsg.LINT.EMPTY_DIR_START.format(path=self.root_dir))
        found_empty = False

        # Use os.walk to find all directories
        for root, dirs, _ in os.walk(self.root_dir):
            # In-place modify dirs to skip excluded ones and hidden ones
            dirs[:] = [
                d
                for d in dirs
                if d not in self.exclude_dirs and not d.startswith(".")
            ]

            # Don't report the root itself
            if root == self.root_dir:
                continue

            if self.is_empty_dir(root):
                rel_path = os.path.relpath(root, self.root_dir)
                logger.warning(
                    LicoMsg.LINT.EMPTY_DIR_FOUND.format(path=rel_path)
                )
                found_empty = True

        if found_empty:
            logger.info(LicoMsg.LINT.EMPTY_DIR_ISSUE)
        else:
            logger.info(LicoMsg.LINT.EMPTY_DIR_NONE)

        return found_empty


def main() -> None:
    """Entry point for the linter CLI."""
    linter = EmptyDirLinter()
    linter.scan()
    # For now, we always exit with 0 to keep the pulse going in prototypes.
    # In production, this might be sys.exit(1 if found else 0).
    sys.exit(0)


if __name__ == "__main__":
    main()
