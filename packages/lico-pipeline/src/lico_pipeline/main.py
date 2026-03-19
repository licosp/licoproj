import argparse
import logging
import shutil
import subprocess
import sys
from pathlib import Path

logging.basicConfig(
    level=logging.INFO, format="%(message)s", stream=sys.stdout
)
logger = logging.getLogger(__name__)

def _get_executable(name: str) -> str | None:
    """Resolve the executable path, prioritizing the active venv."""
    executable = shutil.which(name)
    if not executable:
        python_dir = Path(sys.executable).parent
        candidate = python_dir / f"{name}.exe"
        if not candidate.exists():
            candidate = python_dir / name

        if candidate.exists():
            executable = str(candidate)
    return executable

def run_command(command: list[str], path: Path | None = None) -> bool:
    """Run a shell command and return success."""
    executable = _get_executable(command[0])
    if not executable:
        logger.error(f"Error: Command '{command[0]}' not found.")
        return False

    full_cmd = [executable, *command[1:]]
    if path:
        full_cmd.append(str(path))
        
    logger.info(f"Running: {' '.join(full_cmd)}")
    try:
        result = subprocess.run(
            full_cmd, capture_output=False, check=False, shell=False
        )
    except FileNotFoundError:
        logger.exception(f"Error: Command '{executable}' not found.")
        return False
    else:
        return result.returncode == 0

def _parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Orchestrator for Lico linting pipelines")
    parser.add_argument("path", nargs="?", default=".", help="Path to check")
    return parser.parse_args()

def main() -> None:
    """Entry point for the unified pipeline orchestrator."""
    args = _parse_args()
    target_path = Path(args.path).absolute()
    
    # Define the pipeline steps. 
    # Notice we use 'uv run' for python tools to ensure environment correctness,
    # and 'yarn run' for node tools.
    commands = [
        (["ruff", "check", "--no-fix"], "Ruff Check", target_path),
        (["ruff", "format", "--check"], "Ruff Format", target_path),
        (["pyright"], "Pyright", target_path),
        (["yarn", "run", "lint"], "Yarn Lint (Prettier/ESLint/etc)", None), # yarn lint usually handles its own paths
        (["lico-lint-empty-dir"], "Lico Custom: Empty Directory Check", target_path),
    ]

    success = True
    for cmd, name, path_arg in commands:
        logger.info(f"\n--- {name} ---")
        if not run_command(cmd, path_arg):
            success = False
            logger.error(f"{name} failed!")

    if success:
        logger.info("\n✅ All pipeline checks passed successfully!")
        sys.exit(0)
    else:
        logger.error("\n❌ Some pipeline checks failed. Please review the errors above.")
        sys.exit(1)

if __name__ == "__main__":
    main()
