"""Configuration management for LicoTor."""

import json
from pathlib import Path
from typing import Any

from lico_logger import LicoMsg, get_logger


class ConfigManager:
    """Manages project configuration and paths."""

    def __init__(self, config_path: Path | None = None) -> None:
        """Initialize the ConfigManager.

        Args:
            config_path (Path | None): Optional path to a project.json.
                If None, uses the default one in the package.
        """
        self.pkg_root: Path = Path(__file__).parent
        self.logger = get_logger(__name__)

        if config_path:
            self.config_path: Path = config_path
        else:
            self.config_path = self.pkg_root / "project.json"

        self._config: dict[str, Any] = self._load_config()
        self._validate_config()

        self.logger.info(
            LicoMsg.CONFIG.LOAD_SUCCESS.format(path=self.config_path)
        )

    def _load_config(self) -> dict[str, Any]:
        """Load the configuration from JSON.

        Returns:
            dict[str, Any]: The loaded configuration.

        Raises:
            FileNotFoundError: If the config file is not found.
        """
        if not self.config_path.exists():
            msg = LicoMsg.CONFIG.ERR_NOT_FOUND.format(path=self.config_path)
            raise FileNotFoundError(msg)
        with self.config_path.open("r", encoding="utf-8") as f:
            return json.load(f)

    def _validate_config(self) -> None:
        """Validate the configuration structure and values (Level 1 & 2)."""
        self._validate_app_section(self._config.get("app"))
        self._validate_sync_section(self._config.get("sync"))
        self._validate_windows_section(self._config.get("windows"))

    def _validate_paths(self, win_config: dict[str, Any]) -> None:
        """Recursively validate all values in the windows section.

        Ensures that all paths are absolute.

        Args:
            win_config (dict[str, Any]): The windows configuration subtree.

        Raises:
            TypeError: If a path is not absolute or type is invalid.
        """
        for key, value in win_config.items():
            if isinstance(value, dict):
                self._validate_paths(value)
                continue

            if not isinstance(value, str):
                msg = LicoMsg.CONFIG.ERR_INVALID_TYPE.format(key=key)
                raise TypeError(msg)

            if not self._is_absolute_path(value):
                msg = LicoMsg.CONFIG.ERR_PATH_ABSOLUTE.format(
                    key=key, path=value
                )
                raise TypeError(msg)

    @property
    def sleep_duration(self) -> int:
        """Get the generic sleep duration for app operations.

        Returns:
            int: Seconds.
        """
        return int(self._config["app"]["sleep"])

    @property
    def sleep_start(self) -> int:
        """Alias for sleep_duration (compatibility).

        Returns:
            int: Seconds.
        """
        return self.sleep_duration

    @property
    def sleep_end(self) -> int:
        """Alias for sleep_duration (compatibility).

        Returns:
            int: Seconds.
        """
        return self.sleep_duration

    @property
    def app_start_command(self) -> list[str]:
        """Get the command list to start the application.

        Returns:
            list[str]: Command and arguments.
        """
        return list(self._config["app"]["commands"])

    @property
    def window_title(self) -> str:
        """Get the game window title.

        Returns:
            str: Window title.
        """
        label = self._config["app"]["label"]
        return str(label).replace(".exe", "")

    @property
    def running_app_name(self) -> str:
        """Get the executable name for process detection.

        Returns:
            str: Filename.
        """
        return str(self._config["app"]["label"])

    @property
    def hub_branch(self) -> str:
        """Get the hub (trunk) branch name.

        Returns:
            str: Branch name.
        """
        return str(self._config["sync"]["branch"]["hub"])

    @property
    def dest_branch(self) -> str:
        """Get the destination (windows) branch name.

        Returns:
            str: Branch name.
        """
        return str(self._config["sync"]["branch"]["windows"])

    @property
    def sync_targets(self) -> list[str]:
        """Get the list of files/directories to sync.

        Returns:
            list[str]: Paths relative to workspace root.
        """
        return list(self._config["sync"]["target"])

    @property
    def project_root(self) -> Path:
        """Get the project root path.

        Returns:
            Path: Path.
        """
        # Derived from the capture script path
        return Path(self._config["windows"]["vision"]["capture"]).parents[4]

    @property
    def powershell_exe(self) -> str:
        """Get the shell executable name.

        Returns:
            str: Command name.
        """
        return Path(self._config["windows"]["system"]["powershell"]).name

    @property
    def shell_dir(self) -> Path:
        """Get the shell directory path.

        Returns:
            Path: Path.
        """
        return Path(self._config["windows"]["system"]["powershell"]).parent

    @property
    def capture_script_path(self) -> Path:
        """Get the capture script path.

        Returns:
            Path: Path.
        """
        return Path(self._config["windows"]["vision"]["capture"])

    @property
    def output_image_path(self) -> Path:
        """Get the output image path.

        Returns:
            Path: Path.
        """
        return Path(self._config["windows"]["vision"]["screen"])

    @property
    def uv_path(self) -> Path:
        """Get the uv executable path.

        Returns:
            Path: Path.
        """
        return Path(self._config["windows"]["tools"]["uv"])

    @property
    def git_exe(self) -> str:
        """Get the git executable path.

        Returns:
            str: Path.
        """
        return str(self._config["windows"]["tools"]["git"])

    @property
    def git_workspace_root(self) -> Path:
        """Get the git workspace root path.

        Returns:
            Path: Path.
        """
        return self.project_root

    @staticmethod
    def _is_absolute_path(val: str) -> bool:
        """Check if a string is a WSL absolute path (starts with /).

        Returns:
            bool: True if absolute.
        """
        return val.startswith("/")

    @staticmethod
    def _validate_app_section(app: object) -> None:
        """Validate the 'app' section of the configuration.

        Args:
            app (object): The app section data.

        Raises:
            TypeError: If the section or its fields are invalid.
        """
        if not isinstance(app, dict):
            raise TypeError(LicoMsg.CONFIG.ERR_APP_SECTION)
        if "sleep" not in app:
            raise TypeError(LicoMsg.CONFIG.ERR_APP_SLEEP)
        if not isinstance(app.get("commands"), list):
            raise TypeError(LicoMsg.CONFIG.ERR_APP_COMMANDS)

    @staticmethod
    def _validate_sync_section(sync: object) -> None:
        """Validate the 'sync' section of the configuration.

        Args:
            sync (object): The sync section data.

        Raises:
            TypeError: If the section or its fields are invalid.
        """
        if not isinstance(sync, dict):
            raise TypeError(LicoMsg.CONFIG.ERR_SYNC_SECTION)
        if not isinstance(sync.get("branch"), dict):
            raise TypeError(LicoMsg.CONFIG.ERR_SYNC_BRANCH)
        if not isinstance(sync.get("target"), list):
            raise TypeError(LicoMsg.CONFIG.ERR_SYNC_TARGET)

    def _validate_windows_section(self, win: object) -> None:
        """Validate the 'windows' section and its paths.

        Args:
            win (object): The windows section data.

        Raises:
            TypeError: If the section or paths are invalid.
        """
        if not isinstance(win, dict):
            raise TypeError(LicoMsg.CONFIG.ERR_WINDOWS_SECTION)

        # Level 2: Path formats for windows (Execution inside try block)
        try:
            self._validate_paths(win)
        except (KeyError, TypeError) as e:
            msg = LicoMsg.CONFIG.ERR_STRUCT.format(error=e)
            raise TypeError(msg) from e
