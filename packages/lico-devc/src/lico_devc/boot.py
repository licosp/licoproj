"""Lico Container Bootstrapper (Bare Spark)."""

from lico_logger import LicoMsg, get_logger
import os
import subprocess
import sys
from pathlib import Path

from .manifest import load_habitat_config

# Configure logging for discrete CLI feedback
logging.basicConfig(
    level=logging.INFO, format="%(message)s", stream=sys.stdout
)
logger = get_logger(__name__)


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

        config = load_habitat_config(config_path)

        boot_config = config.get("boot", {})
        expected_cwd = boot_config.get("cwd")
        if not expected_cwd:
            return

        # Normalize and expand for comparison
        expected_abs = Path(expected_cwd).expanduser().resolve()
        actual_abs = project_root.resolve()

        if expected_abs != actual_abs:
            logger.error(LicoMsg.DEVC.ERR_ENV_MISMATCH.format(expected=expected_abs, actual=actual_abs))
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

        config = load_habitat_config(config_path)

        env_config = config.get("env", {})
        if env_config.get("name") != "credentials":
            return

        env_path = env_config.get("path")
        if not env_path:
            return

        # Normalize and expand for check
        cred_path = Path(env_path).expanduser().resolve()
        if not cred_path.exists():
            logger.warning(LicoMsg.DEVC.WARN_CRED_MISSING.format(path=cred_path))
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
    logger.info(LicoMsg.DEVC.BOOT_START)

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
    logger.info(LicoMsg.DEVC.HUB_INFO.format(root=hub_root, active=active_rel))

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
        logger.info(LicoMsg.DEVC.SUCCESS_RUNNING)
    except subprocess.CalledProcessError:
        logger.exception(LicoMsg.DEVC.ERR_START_FAILED)
        sys.exit(1)
    except Exception:
        logger.exception(LicoMsg.DEVC.ERR_BOOT_FATAL)
        sys.exit(1)


if __name__ == "__main__":
    main()
