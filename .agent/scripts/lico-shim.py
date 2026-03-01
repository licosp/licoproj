#!/usr/bin/python3
"""lico-shim: Unified Python Command Shim Router.

This script acts as a fast, strict-mode interceptor for common shell commands.
Instead of being invoked as `lico-shim`, it expects to be invoked via a symlink
(e.g., .runtimes/bin/rm -> lico-shim.py). It reads `sys.argv[0]` to determine
its identity, parses `shim_config.yaml` for feature flags, and then either
executes safety logic or drops directly into the native system binary.

Managed by: .agent/rules/development/command-shims.md
"""

import argparse
import datetime
import os
import subprocess
import sys
import typing
from pathlib import Path


class _Logger:
    @staticmethod
    def info(msg: str, *args: object) -> None:
        if args:
            msg %= args
        os.write(1, (msg + "\n").encode("utf-8"))

    @staticmethod
    def error(msg: str, *args: object) -> None:
        if args:
            msg %= args
        os.write(2, (msg + "\n").encode("utf-8"))

    @staticmethod
    def exception(msg: str, *args: object) -> None:
        _, exc_val, _ = sys.exc_info()
        if exc_val:
            msg = f"{msg} Error: {exc_val}"
        _Logger.error(msg, *args)


logger = _Logger()

# Provide a fallback if PyYAML is not installed in the system python,
# though we strongly expect it to be since this is a heavy AI dev box.
try:
    import yaml
except ImportError:
    logger.exception("\U0001f6ab [Shim] FATAL: python3-yaml is missing.")
    logger.exception("   It is not installed on the base system.")
    logger.exception("   Run: sudo apt-get install python3-yaml")
    sys.exit(1)


SCRIPT_PATH = Path(__file__).resolve()
SCRIPT_DIR = SCRIPT_PATH.parent
REPO_ROOT = SCRIPT_DIR.parent.parent
CONFIG_FILE = SCRIPT_DIR / "shim_config.yaml"
IGNORE_FILE = SCRIPT_DIR / "shim_ignore_dirs"

# Native Binaries to pass through to
NATIVE_BINARIES = {
    "rm": "/bin/rm",
    "mv": "/bin/mv",
    "grep": "/usr/bin/grep",
    "git": "/usr/bin/git",
    # "python": None # handled specially
}


def _parse_config_data(default_cfg: dict[str, bool], parsed: object) -> None:
    """Parse the raw YAML data and update the configuration dictionary."""
    if isinstance(parsed, dict) and "shims" in parsed:
        shims = typing.cast(object, parsed["shims"])
        if isinstance(shims, dict):
            shims_dict = typing.cast("dict[str, object]", shims)
            for k, v in shims_dict.items():
                default_cfg[str(k)] = bool(v)


def load_config() -> dict[str, bool]:
    """Load the YAML configuration, defaulting to False for all flags.

    Returns:
        dict[str, bool]: The loaded configuration mapping shim names to states.
    """
    default_cfg = {
        "git": False,
        "grep": False,
        "mv": False,
        "rm": False,
        "python": False,
    }
    if not CONFIG_FILE.exists():
        return default_cfg
    try:
        with CONFIG_FILE.open() as f:
            parsed = yaml.safe_load(f)
            _parse_config_data(default_cfg, parsed)
    except yaml.YAMLError:
        logger.exception(
            "\U0001f6ab [Shim] WARNING: Failed to parse %s.",
            CONFIG_FILE,
        )
        logger.exception("   Defaulting to OFF for all shims.")

    return default_cfg


def save_config(config: dict[str, bool]) -> None:
    """Save the updated configuration back to YAML."""
    data = {"shims": config}
    with CONFIG_FILE.open("w") as f:
        yaml.safe_dump(data, f, default_flow_style=False)


def is_in_git_repo() -> bool:
    """Check if the current working directory is inside a Git repository.

    Returns:
        bool: True if inside a Git work tree, False otherwise.
    """
    result = subprocess.run(
        ["/usr/bin/git", "rev-parse", "--is-inside-work-tree"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=False,
    )
    return result.returncode == 0


# -----------------------------------------------------------------------------
# Command-Specific Handlers
# -----------------------------------------------------------------------------


def handle_rm(args: list[str]) -> None:
    """Safety shim for rm: Move to trash instead of deleting."""
    timestamp = datetime.datetime.now(tz=datetime.UTC).strftime(
        "%Y-%m-%dT%H%M%S",
    )
    trash_dir = REPO_ROOT / ".trash" / timestamp

    files = [a for a in args if not a.startswith("-")]

    if not files:
        os.execvp(NATIVE_BINARIES["rm"], ["rm", *args])

    trash_dir.mkdir(parents=True, exist_ok=True)

    subprocess.run(
        [NATIVE_BINARIES["mv"], *files, str(trash_dir)],
        check=False,
    )

    if is_in_git_repo():
        for f in files:
            subprocess.run(
                [NATIVE_BINARIES["git"], "add", "-u", f],
                stderr=subprocess.DEVNULL,
                check=False,
            )


def handle_mv(args: list[str]) -> None:
    """Safety shim for mv: Try git mv first, fallback to native mv."""
    if is_in_git_repo():
        result = subprocess.run(
            [NATIVE_BINARIES["git"], "mv", *args],
            check=False,
        )
        if result.returncode == 0:
            return
    os.execvp(NATIVE_BINARIES["mv"], ["mv", *args])


def handle_grep(args: list[str]) -> None:
    """Safety shim for grep: Use git grep in repo, or exclude configs."""
    if is_in_git_repo():
        os.execvp(NATIVE_BINARIES["git"], ["git", "grep", "-I", *args])
    else:
        exclude_dirs = "{.git,.venv,node_modules,.shadow}"
        if IGNORE_FILE.exists():
            with IGNORE_FILE.open() as f:
                lines = [
                    line.strip()
                    for line in f
                    if line.strip() and not line.startswith("#")
                ]
                if lines:
                    exclude_dirs = "{" + ",".join(lines) + "}"

        os.execvp(
            NATIVE_BINARIES["grep"],
            ["grep", f"--exclude-dir={exclude_dirs}", *args],
        )


# Block definitions for git safety shim
BLOCKED_CMD_MESSAGES: dict[str, tuple[str, ...]] = {
    "shadow": (
        "Shadow Repository Detected.",
        "You are trying to operate on a file inside '.shadow/' from the root.",
        "Please 'cd' into the directory first context.",
    ),
    "restore": (
        "'git restore' is restricted.",
        "This command silently discards uncommitted changes.",
        "Use 'git checkout <file>' or overwrite explicitly.",
    ),
    "clean": (
        "'git clean' is restricted.",
        "This command deletes untracked files with no safety.",
        "Use 'rm <file>' (which is safe-shimmed) instead.",
    ),
    "reset_hard": (
        "'git reset --hard' is dangerous.",
        "This command destroys uncommitted changes and history.\n",
        "Alternatives:",
        "1. Soft Reset:  git reset --soft <commit>",
        "2. Bypass:      /usr/bin/git reset --hard <commit>",
    ),
}


def _block_action(reason_key: str) -> None:
    """Log an error block using defined messages and exit."""
    msgs = BLOCKED_CMD_MESSAGES[reason_key]
    logger.error("\U0001f6ab [Shim] BLOCKED: %s", msgs[0])
    for msg in msgs[1:]:
        logger.error("   %s", msg)
    logger.error("")
    sys.exit(1)


def _check_git_arg_shadow(arg: str) -> None:
    """Block git operations on the shadow repository from root."""
    if ".shadow/" in arg:
        _block_action("shadow")


def _check_git_arg_restore_clean(arg: str) -> None:
    """Block dangerous uncommitted data discard commands."""
    if arg == "restore":
        _block_action("restore")

    if arg == "clean":
        _block_action("clean")


def _check_git_reset_hard(args: list[str]) -> None:
    """Block hard resets without explicit bypass."""
    if "reset" in args and "--hard" in args:
        _block_action("reset_hard")


def handle_git(args: list[str]) -> None:
    """Safety shim for git: Prevent dangerous operations like hard reset."""
    for arg in args:
        _check_git_arg_shadow(arg)
        _check_git_arg_restore_clean(arg)

    _check_git_reset_hard(args)

    os.execvp(NATIVE_BINARIES["git"], ["git", *args])


# -----------------------------------------------------------------------------
# Main Router
# -----------------------------------------------------------------------------


def _dispatch_native(inv_name: str, cmd_args: list[str]) -> None:
    """Dispatch to a native binary or default python."""
    if inv_name in NATIVE_BINARIES:
        os.execvp(NATIVE_BINARIES[inv_name], [inv_name, *cmd_args])
    elif inv_name == "python":
        os.execvp(sys.executable, ["python", *cmd_args])
    else:
        logger.error(
            "\U0001f6ab [Shim] ERROR: Unknown link '%s'.",
            inv_name,
        )
        sys.exit(1)


def _dispatch_shim(inv_name: str, cmd_args: list[str]) -> None:
    """Dispatch to a safety shim implementation."""
    if inv_name == "python":
        os.execvp("uv", ["uv", "run", "python", *cmd_args])

    handlers = {
        "rm": handle_rm,
        "mv": handle_mv,
        "grep": handle_grep,
        "git": handle_git,
    }
    handler = handlers.get(inv_name)
    if handler:
        handler(cmd_args)


def main() -> None:
    """Entry point for the Unified Command Router."""
    inv_name = Path(sys.argv[0]).name
    cmd_args = sys.argv[1:]

    if inv_name in {"lico-shim", "lico-shim.py"}:
        handle_cli(cmd_args)
        return

    config = load_config()

    if inv_name not in config or not config.get(inv_name):
        _dispatch_native(inv_name, cmd_args)
    else:
        _dispatch_shim(inv_name, cmd_args)


def _print_status(config: dict[str, bool]) -> None:
    """Print the status of all shims."""
    logger.info("Command Shim Status:")
    for cmd, state in config.items():
        status_txt = "\033[32mON\033[0m" if state else "\033[31mOFF\033[0m"
        logger.info("  %s: %s", cmd.ljust(10), status_txt)


def _set_shim_state(
    config: dict[str, bool],
    command: str,
    *,
    state: bool,
) -> None:
    """Enable or disable a shim and save config."""
    if command == "all":
        for k in config:
            config[k] = state
        state_str = "enabled" if state else "disabled"
        logger.info("All shims %s.", state_str)
    else:
        config[command] = state
        state_str = "enabled" if state else "disabled"
        logger.info("Shim '%s' %s.", command, state_str)
    save_config(config)


def handle_cli(args: list[str]) -> None:
    """Manage the shim_config.yaml file."""
    parser = argparse.ArgumentParser(description="Manage Lico Command Shims")
    subparsers = parser.add_subparsers(dest="action", required=True)

    subparsers.add_parser("status", help="Show current shim status")

    on_parser = subparsers.add_parser("on", help="Enable a shim")
    on_parser.add_argument(
        "command",
        choices=["git", "grep", "mv", "rm", "python", "all"],
    )

    off_parser = subparsers.add_parser("off", help="Disable a shim")
    off_parser.add_argument(
        "command",
        choices=["git", "grep", "mv", "rm", "python", "all"],
    )

    parsed = parser.parse_args(args)

    config = load_config()

    if parsed.action == "status":
        _print_status(config)
    elif parsed.action == "on":
        _set_shim_state(config, parsed.command, state=True)
    elif parsed.action == "off":
        _set_shim_state(config, parsed.command, state=False)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        sys.exit(130)
