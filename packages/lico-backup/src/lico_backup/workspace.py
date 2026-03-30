import argparse
import subprocess
import sys
from pathlib import Path

from lico_logger import LicoMsg, get_logger

logger = get_logger(__name__)


def main():
    parser = argparse.ArgumentParser(
        description="Backup the entire shared crew workspace."
    )
    args = parser.parse_args()

    home = Path.home()
    src_dir = home / "develop" / "shared"
    dest_dir = home / "develop" / "shared-backup"

    if not src_dir.exists() or not src_dir.is_dir():
        logger.error(LicoMsg.BACKUP.ERR_SRC_NOT_FOUND.format(src=src_dir))
        sys.exit(1)

    logger.info(LicoMsg.BACKUP.START.format(src=src_dir, dest=dest_dir))
    dest_dir.mkdir(parents=True, exist_ok=True)

    cmd = [
        "rsync",
        "-av",
        "--exclude=.venv/",
        "--exclude=node_modules/",
        "--exclude=.temp/",
        "--exclude=.trash/",
        str(src_dir) + "/",
        str(dest_dir) + "/",
    ]

    try:
        subprocess.run(cmd, check=True)
        logger.info(LicoMsg.BACKUP.SUCCESS)
    except subprocess.CalledProcessError as e:
        logger.error(LicoMsg.BACKUP.ERR_FAILED.format(error=e))
        sys.exit(1)


if __name__ == "__main__":
    main()
