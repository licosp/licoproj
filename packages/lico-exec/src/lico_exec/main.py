"""Centralized command runner for the LicoTor ecosystem."""

import os
import subprocess
from collections.abc import Mapping
from pathlib import Path

from lico_logger import LicoMsg, get_logger


class Commander:
    """Centralized command runner for external processes."""

    def __init__(self, workspace_root: Path | str | None = None) -> None:
        """Initialize Commander.

        Args:
            workspace_root (Path | str | None): default CWD for commands.
        """
        self.workspace_root = (
            Path(workspace_root) if workspace_root else Path.cwd()
        )
        self.logger = get_logger(__name__)

    def _prepare_env(
        self, env: Mapping[str, str] | None = None
    ) -> dict[str, str]:
        """Prepare environment variables."""
        full_env = os.environ.copy()
        if env:
            full_env.update(env)
        return full_env

    def run(
        self,
        cmd: str | list[str],
        label: str,
        cwd: Path | str | None = None,
        env: Mapping[str, str] | None = None,
        *,
        check: bool = True,
        capture_output: bool = True,
        text: bool = True,
    ) -> subprocess.CompletedProcess[str]:
        """Run a synchronous command.

        Args:
            cmd: Command string or list.
            label: Human-readable label for logging.
            cwd: Directory to run in.
            env: Environment variables.
            check: Whether to raise on error.
            capture_output: Capture stdout/stderr.
            text: Return output as string.

        Returns:
            subprocess.CompletedProcess: result.
        """
        exec_cwd = Path(cwd) if cwd else self.workspace_root
        cmd_str = cmd if isinstance(cmd, str) else " ".join(cmd)

        self.logger.info(
            LicoMsg.EXEC.START_RUN.format(label=label, cmd=cmd_str)
        )

        try:
            result = subprocess.run(
                cmd,
                cwd=exec_cwd,
                env=self._prepare_env(env),
                check=check,
                capture_output=capture_output,
                text=text,
                shell=True if isinstance(cmd, str) else False,
            )
            self.logger.info(LicoMsg.EXEC.CMD_SUCCESS.format(label=label))
            return result
        except subprocess.CalledProcessError as e:
            self.logger.exception(
                LicoMsg.EXEC.CMD_FAILURE.format(label=label, code=e.returncode)
            )
            if e.stderr:
                self.logger.exception(
                    LicoMsg.EXEC.ERR_OUTPUT.format(stderr=e.stderr)
                )
            raise

    def launch(
        self,
        cmd: str | list[str],
        label: str,
        cwd: Path | str | None = None,
        env: Mapping[str, str] | None = None,
    ) -> subprocess.Popen:
        """Launch an asynchronous command.

        Args:
            cmd: Command string or list.
            label: Human-readable label for logging.
            cwd: Directory to run in.
            env: Environment variables.

        Returns:
            subprocess.Popen: process object.
        """
        exec_cwd = Path(cwd) if cwd else self.workspace_root
        cmd_str = cmd if isinstance(cmd, str) else " ".join(cmd)

        self.logger.info(
            LicoMsg.EXEC.START_LAUNCH.format(label=label, cmd=cmd_str)
        )

        process = subprocess.Popen(
            cmd,
            cwd=exec_cwd,
            env=self._prepare_env(env),
            shell=True if isinstance(cmd, str) else False,
        )
        self.logger.info(
            LicoMsg.EXEC.PROCESS_STARTED.format(label=label, pid=process.pid)
        )
        return process
