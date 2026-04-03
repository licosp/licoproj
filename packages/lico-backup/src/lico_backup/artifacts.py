"""IDE artifacts backup tool for the LicoTor ecosystem."""

import argparse
import subprocess
from pathlib import Path

from lico_logger import LicoMsg, get_logger

logger = get_logger(__name__)


def sync_dir(src: Path, dest: Path, *, is_history: bool = False) -> None:
    """Sync a directory to the destination using rsync.

    Args:
        src (Path): The source directory to sync.
        dest (Path): The destination directory.
        is_history (bool): Whether to handle the sync as a historical record.
    """
    if not src.exists() or not src.is_dir():
        return

    logger.info(LicoMsg.BACKUP.ARTIFACT_START.format(src=src, dest=dest))
    dest.mkdir(parents=True, exist_ok=True)

    # Base rsync command: archive mode, verbose
    cmd = ["rsync", "-av"]

    if is_history:
        # For history, we only want readable markdown files
        cmd.extend([
            "--include=*/",
            "--exclude=*.json",
            "--include=*.md*",
            "--exclude=*",
        ])
    else:
        # For brain/code_tracker, same rules applied in the original script
        cmd.extend([
            "--include=*/",
            "--exclude=*.json",
            "--include=*.md*",
            "--exclude=*",
        ])

    cmd.extend([str(src) + "/", str(dest) + "/"])

    try:
        subprocess.run(cmd, check=True)
    except subprocess.CalledProcessError:
        logger.exception(LicoMsg.BACKUP.ARTIFACT_ERR.format(src=src))


def main() -> None:
    """Entry point for IDE artifacts backup."""
    parser = argparse.ArgumentParser(
        description=(
            "Backup IDE artifacts (Antigravity, Cursor, VSCode) "
            "to the memory archive."
        )
    )
    parser.parse_args()

    home = Path.home()
    # We always run this from within a specific identifier's workspace
    # (e.g., agate), but the archive is shared in the bare repo or local
    # to the workspace? Usually it's run in the active workspace.
    cwd = Path.cwd()
    archive_base = cwd / ".agent" / ".internal" / "memory_archive"

    # 1. Antigravity specific (Brain, Code Tracker)
    ag_base = home / ".gemini" / "antigravity"
    sync_dir(ag_base / "brain", archive_base / "brain")
    sync_dir(ag_base / "code_tracker", archive_base / "code_tracker")

    # 2. IDE History (Antigravity, Cursor, VSCode)
    ide_servers = {
        "antigravity": home / ".antigravity-server",
        "cursor": home / ".cursor-server",
        "vscode": home / ".vscode-server",
    }

    for name, server_path in ide_servers.items():
        history_path = server_path / "data" / "User" / "History"
        if history_path.exists():
            dest_path = archive_base / "history" / name
            sync_dir(history_path, dest_path, is_history=True)

    logger.info(LicoMsg.BACKUP.ARTIFACT_SUCCESS)


if __name__ == "__main__":
    main()
