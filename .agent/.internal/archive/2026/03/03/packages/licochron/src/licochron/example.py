"""Example script for interactive play in TOA-Init.

This script demonstrates how to send commands
to the game core via command.json.
"""

import json
import logging
import pathlib

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Path relative to project root
COMMAND_PATH = "packages/licochron/data/command.json"


def send_move_command(unit_id: str, x: int, y: int, z: int) -> None:
    """Send a move command to the game core.

    Args:
        unit_id: The ID of the unit to move.
        x: X-coordinate target.
        y: Y-coordinate target.
        z: Z-coordinate target.
    """
    command = [{"action": "move", "unit_id": unit_id, "target": [x, y, z]}]
    cmd_file = pathlib.Path(COMMAND_PATH)
    cmd_file.parent.mkdir(exist_ok=True, parents=True)
    with cmd_file.open("w", encoding="utf-8") as f:
        json.dump(command, f, indent=2)
    logger.info("Sent move command for %s to [%s, %s, %s]", unit_id, x, y, z)


if __name__ == "__main__":
    # Example: Move the Hero (u1) to center area
    send_move_command("u1", 5, 2, 1)
