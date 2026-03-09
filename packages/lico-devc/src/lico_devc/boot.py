"""Lico Container Bootstrapper (Bare Spark)."""

import json
import logging
import os
import subprocess
import sys
from pathlib import Path
from typing import TypedDict, cast

# Configure logging for discrete CLI feedback
logging.basicConfig(
    level=logging.INFO, format="%(message)s", stream=sys.stdout
)
logger = logging.getLogger(__name__)


class BootConfig(TypedDict, total=False):
    """Configuration for boot operations."""

    cwd: str


class EnvConfig(TypedDict, total=False):
    """Configuration for environment variables."""

    name: str
    path: str
    env_keys: list[str]


class HabitatConfig(TypedDict, total=False):
    """Configuration for the Lico habitat."""

    boot: BootConfig
    env: EnvConfig


class Habitat:
    """Validator for the Initial Spark environment."""

    @staticmethod
    def validate_cwd(project_root: Path) -> None:
        """Verify if the current project root matches the designated Habitat.

        Args:
            project_root: The identified absolute path to the project root.
        """
        config_path = project_root / "packages/lico-devc/habitat.json"
        if not config_path.exists():
            return  # Fallback if config is missing

        with config_path.open("r", encoding="utf-8") as f:
            config = cast("HabitatConfig", json.load(f))

        boot_config = config.get("boot", {})
        expected_cwd = boot_config.get("cwd")
        if not expected_cwd:
            return

        # Normalize and expand for comparison
        expected_abs = Path(expected_cwd).expanduser().resolve()
        actual_abs = project_root.resolve()

        if expected_abs != actual_abs:
            logger.error("[Error] Environment Mismatch.")
            logger.error("        Expected Root: %s", expected_abs)
            logger.error("        Actual Root:   %s", actual_abs)
            logger.error("        Please ensure you are at the Village Root.")
            sys.exit(1)

    @staticmethod
    def validate_credentials(project_root: Path) -> None:
        """Verify if the required credential file exists.

        Args:
            project_root: The identified absolute path to the project root.
        """
        config_path = project_root / "packages/lico-devc/habitat.json"
        if not config_path.exists():
            return

        with config_path.open("r", encoding="utf-8") as f:
            config = cast("HabitatConfig", json.load(f))

        env_config = config.get("env", {})
        if env_config.get("name") != "credentials":
            return

        env_path = env_config.get("path")
        if not env_path:
            return

        # Normalize and expand for check
        cred_path = Path(env_path).expanduser().resolve()
        if not cred_path.exists():
            logger.warning("[Warning] Credentials Missing.")
            logger.warning("          Path: %s", cred_path)
            logger.warning("          Please ensure your Vault is active.")
            sys.exit(1)


def find_hub_root() -> Path:
    """Discover Hub Root by looking for 'project/crew' folders.

    Returns:
        The absolute path to the discovered Hub Root.
    """
    current = Path.cwd().resolve()
    while current != current.parent:
        if (current / "project").exists() and (current / "crew").exists():
            return current
        current = current.parent
    # Fallback: traverse up from script location
    return Path(__file__).resolve().parents[4]


def main() -> None:
    """Entry point for the Lico Container Bootstrapper."""
    logger.info("--- Lico Container Bootstrapper (Bare Spark) ---")

    # 1. Pivot to Project Root (Universal Invocation)
    # Script: <root>/packages/lico-devc/src/lico_devc/boot.py
    # From lico_devc -> src -> lico-devc -> packages -> licoproj (4 steps up)
    project_root = Path(__file__).resolve().parents[4]
    os.chdir(project_root)

    # 2. Safety Check: CWD & Credential Validation (Habitat Gate)
    Habitat.validate_cwd(project_root)
    Habitat.validate_credentials(project_root)

    # 3. Discover Universe Root
    hub_root = find_hub_root()
    active_rel = project_root.relative_to(hub_root)
    logger.info("[Hub] Root: %s | Active: %s", hub_root, active_rel)

    env = os.environ.copy()
    env.update(
        {"LICO_HUB_ROOT": str(hub_root), "LICO_ACTIVE_REL": str(active_rel)}
    )

    try:
        devc_rel = Path("packages") / "lico-devc"
        compose_path = devc_rel / ".devcontainer" / "docker-compose.yml"
        subprocess.run(
            [
                "docker",
                "compose",
                "-f",
                str(compose_path),
                "up",
                "-d",
                "--build",
            ],
            env=env,
            check=True,
        )
        logger.info("[Success] Container is running. Connect via VS Code/SSH.")
    except subprocess.CalledProcessError:
        logger.exception("[Error] Failed to start container")
        sys.exit(1)
    except Exception:
        logger.exception("[Fatal] Unexpected error")
        sys.exit(1)


if __name__ == "__main__":
    main()
