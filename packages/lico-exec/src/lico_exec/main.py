"""Centralized command runner for the LicoTor ecosystem."""

import subprocess
from pathlib import Path
from typing import TYPE_CHECKING

from lico_logger import add_file_handler, add_stream_handler, get_logger, LicoMsg

if TYPE_CHECKING:
    from collections.abc import Mapping

class Commander:
    """Centralized command runner for external processes."""

    def __init__(
        self,
        workspace_root: Path | str | None = None,
        env: "Mapping[str, str] | None" = None,
        debug_log_path: Path| None = None,
    ) -> None:
        """Initialize Commander.

        Args:
            workspace_root (Path | str | None): default CWD for commands.
            env (Mapping[str, str] | None): Base environment variables.
        """
        self.workspace_root = (
            Path(workspace_root) if workspace_root else Path.cwd()
        )
        self.env: Mapping[str, str] | None = env
        self.logger = get_logger(__name__)

        if debug_log_path is None:
            add_stream_handler(self.logger)
        else:
            add_file_handler(self.logger, log_file=debug_log_path)


    def _prepare_env(self) -> dict[str, str]:
        """Prepare environment variables.

        Returns:
            dict[str, str]: The merged environment dictionary.
        """
        import os
        full_env = os.environ.copy()
        if self.env:
            full_env.update(self.env)
        return full_env

    def run(
        self,
        cmd: str | list[str],
        label: str,
        *,
        check: bool = True,
        capture_output: bool = True,
        text: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        """Run a synchronous command.

        Args:
            cmd: Command string or list.
            label: Human-readable label for logging.
            check: Whether to raise on error.
            capture_output: Capture stdout/stderr.
            text: Return output as string.

        Returns:
            subprocess.CompletedProcess: Result of execution.
        """
        self.logger.info(LicoMsg.EXEC.RUNNING_CMD.format(label=label))
        try:
            result = subprocess.run(
                cmd,
                cwd=self.workspace_root,
                env=self._prepare_env(),
                check=check,
                capture_output=capture_output,
                text=text,
                shell=bool(isinstance(cmd, str)),
            )
            self.logger.info(LicoMsg.EXEC.CMD_SUCCESS.format(label=label))
        except subprocess.CalledProcessError as e:
            self.logger.exception(
                LicoMsg.EXEC.CMD_FAILURE.format(label=label, code=e.returncode)
            )
            if e.stderr:
                self.logger.error(
                    LicoMsg.EXEC.ERR_OUTPUT.format(stderr=e.stderr)
                )
            raise
        else:
            return result

    def launch(
        self,
        cmd: str | list[str],
        label: str,
    ) -> subprocess.Popen:
        """Launch a background process.

        Args:
            cmd: Command string or list.
            label: Descriptive label.

        Returns:
            subprocess.Popen: Process handle.
        """
        self.logger.info(LicoMsg.EXEC.RUNNING_CMD.format(label=label))
        return subprocess.Popen(
            cmd,
            cwd=self.workspace_root,
            env=self._prepare_env(),
            shell=bool(isinstance(cmd, str)),
        )
