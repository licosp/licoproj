"""Central orchestrator for the LicoTor quality pipeline."""

import argparse
import shutil
import subprocess
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from typing import Any

from lico_logger import LicoMsg, get_logger

logger = get_logger(__name__)


@dataclass
class ToolResult:
    """Result container for lint tool execution."""

    name: str
    success: bool
    return_code: int


class LintTool(ABC):
    """Abstract base class for all linting tools."""

    def __init__(
        self, name: str, extensions: list[str], tags: list[str] | None = None
    ) -> None:
        """Initialize the lint tool.

        Args:
            name (str): Tool name.
            extensions (list[str]): Supported file extensions.
            tags (list[str] | None): Tool tags for filtering.
        """
        self.name = name
        self.extensions = extensions
        self.tags = tags or []

    @abstractmethod
    def run(self, target_path: Path, *, fix_mode: bool = False) -> ToolResult:
        """Execute the tool on the target path.

        Args:
            target_path (Path): Path to scan or fix.
            fix_mode (bool): Whether to apply automated fixes.

        Returns:
            ToolResult: Result of the tool execution.
        """

    def _run_subprocess(
        self, cmd: list[str], cwd: Path | None = None
    ) -> ToolResult:
        """Run a command as a subprocess.

        Args:
            cmd (list[str]): Command and arguments.
            cwd (Path | None): Working directory.

        Returns:
            ToolResult: The execution result.
        """
        logger.info(LicoMsg.PIPELINE.RUNNING_CMD.format(cmd=" ".join(cmd)))
        try:
            result = subprocess.run(
                cmd, capture_output=False, check=False, shell=False, cwd=cwd
            )
            return ToolResult(
                name=self.name,
                success=result.returncode == 0,
                return_code=result.returncode,
            )
        except FileNotFoundError:
            logger.exception(
                LicoMsg.PIPELINE.ERR_CMD_NOT_FOUND.format(cmd=cmd[0])
            )
            return ToolResult(name=self.name, success=False, return_code=-1)


class PythonTool(LintTool):
    """Tool implementation for Python-based linters."""

    def __init__(
        self,
        name: str,
        command: str,
        *,
        args: list[str],
        fix_args: list[str] | None = None,
        tags: list[str] | None = None,
    ) -> None:
        """Initialize Python tool."""
        super().__init__(name, [".py", ".pyi"], tags)
        self.command = command
        self.args = args
        self.fix_args = fix_args

    def _resolve_executable(self) -> str | None:
        """Resolve command to a physical executable.

        Returns:
            str | None: Path to executable or None.
        """
        python_dir = Path(sys.executable).parent
        candidate = python_dir / self.command
        if candidate.exists():
            return str(candidate)
        return shutil.which(self.command)

    def run(self, target_path: Path, *, fix_mode: bool = False) -> ToolResult:
        """Run the Python linting tool.

        Args:
            target_path (Path): Path to scan.
            fix_mode (bool): Use fix arguments if available.

        Returns:
            ToolResult: Outcome.
        """
        executable = self._resolve_executable()
        if not executable:
            logger.error(
                LicoMsg.PIPELINE.ERR_EXECUTABLE_NOT_FOUND.format(
                    cmd=self.command, tool=self.name
                )
            )
            return ToolResult(name=self.name, success=False, return_code=-1)

        cur_args = self.fix_args if fix_mode and self.fix_args else self.args
        full_cmd = [executable, *cur_args, str(target_path)]
        return self._run_subprocess(full_cmd)


class NodeTool(LintTool):
    """Tool implementation for Node.js-based linters."""

    def __init__(
        self,
        name: str,
        command: str,
        *,
        args: list[str],
        extensions: list[str],
        **kwargs: Any,  # noqa: ANN401
    ) -> None:
        """Initialize Node.js tool."""
        super().__init__(name, extensions, kwargs.get("tags"))
        self.command = command
        self.args = args
        self.fix_args = kwargs.get("fix_args")

    def _resolve_executable(self, root_dir: Path) -> str | None:
        """Resolve Node command from node_modules/.bin.

        Args:
            root_dir (Path): Workspace root.

        Returns:
            str | None: Path to executable or None.
        """
        candidate = root_dir / "node_modules" / ".bin" / self.command
        if candidate.exists():
            return str(candidate)
        return shutil.which(self.command)

    def run(self, target_path: Path, *, fix_mode: bool = False) -> ToolResult:
        """Run the Node.js-based linting tool.

        Args:
            target_path (Path): Target to check.
            fix_mode (bool): Use fix arguments.

        Returns:
            ToolResult: Outcome.
        """
        executable = self._resolve_executable(Path.cwd())
        if not executable:
            logger.error(
                LicoMsg.PIPELINE.ERR_EXECUTABLE_NOT_FOUND.format(
                    cmd=self.command, tool=self.name
                )
            )
            return ToolResult(name=self.name, success=False, return_code=-1)

        cur_args = self.fix_args if fix_mode and self.fix_args else self.args
        full_cmd = [executable, *cur_args]

        if self.command == "prettier" and target_path.is_dir():
            full_cmd.append(str(target_path / "**/*"))
        else:
            full_cmd.append(str(target_path))

        return self._run_subprocess(full_cmd)


class ShellcheckTool(PythonTool):
    """Specialized tool implementation for Shellcheck."""

    def __init__(
        self,
        name: str,
        command: str,
        *,
        args: list[str],
        tags: list[str] | None = None,
    ) -> None:
        """Initialize Shellcheck tool."""
        super().__init__(name, command, args=args, tags=tags)
        self.extensions = [".sh", ".bash"]

    def _collect_shell_files(self, target_path: Path) -> list[Path]:
        """Gather shell files while filtering out noise.

        Args:
            target_path (Path): Root directory or file.

        Returns:
            list[Path]: Filtered shell scripts.
        """
        if not target_path.is_dir():
            exts = self.extensions
            return [target_path] if target_path.suffix in exts else []

        files: list[Path] = []
        files.extend(target_path.rglob("*.sh"))
        files.extend(target_path.rglob("*.bash"))
        ignore = (".venv", "node_modules", ".temp")
        return [f for f in files if not any(p in f.parts for p in ignore)]

    def run(self, target_path: Path, *, fix_mode: bool = False) -> ToolResult:
        """Run the Shellcheck linting tool.

        Args:
            target_path (Path): Path to scan.
            fix_mode (bool): Fix mode flag.

        Returns:
            ToolResult: Outcome.
        """
        executable = self._resolve_executable()
        if not executable:
            logger.error(
                LicoMsg.PIPELINE.ERR_EXECUTABLE_NOT_FOUND.format(
                    cmd=self.command, tool=self.name
                )
            )
            return ToolResult(name=self.name, success=False, return_code=-1)

        files = self._collect_shell_files(target_path)
        if not files:
            logger.info(LicoMsg.PIPELINE.SKIPPING_TOOL.format(name=self.name))
            return ToolResult(name=self.name, success=True, return_code=0)

        cur_args = self.fix_args if fix_mode and self.fix_args else self.args
        full_cmd = [executable, *cur_args] + [str(f) for f in files]
        return self._run_subprocess(full_cmd)


def _get_available_tools() -> list[LintTool]:
    """Return the complete list of tools integrated into the pipeline.

    Returns:
        list[LintTool]: All supported linting tools.
    """
    cache_loc = ".temp/cache"
    return [
        PythonTool(
            "Ruff Check",
            "ruff",
            args=["check", "--no-fix", "--config", ".vscode/ruff.toml"],
            fix_args=["check", "--fix", "--config", ".vscode/ruff.toml"],
            tags=["python"],
        ),
        PythonTool(
            "Ruff Format",
            "ruff",
            args=["format", "--check", "--config", ".vscode/ruff.toml"],
            fix_args=["format", "--config", ".vscode/ruff.toml"],
            tags=["python"],
        ),
        PythonTool("Pyright", "pyright", args=[], tags=["python"]),
        PythonTool(
            "Ty",
            "ty",
            args=["check", "--config-file", ".vscode/ty.toml"],
            tags=["python"],
        ),
        NodeTool(
            "Prettier",
            "prettier",
            args=[
                "--config",
                ".vscode/.prettierrc.yaml",
                "--ignore-path",
                ".vscode/.prettierignore",
                "--check",
                "--cache",
                "--cache-location",
                f"{cache_loc}/pret/",
            ],
            fix_args=[
                "--config",
                ".vscode/.prettierrc.yaml",
                "--ignore-path",
                ".vscode/.prettierignore",
                "--write",
                "--cache",
                "--cache-location",
                f"{cache_loc}/pret/",
            ],
            extensions=[".js", ".ts", ".md", ".json", ".yaml"],
            tags=["web", "docs"],
        ),
        NodeTool(
            "ESLint",
            "eslint",
            args=[
                "--config",
                ".vscode/eslint.config.mjs",
                "--cache",
                "--cache-location",
                f"{cache_loc}/eslint/",
            ],
            fix_args=[
                "--config",
                ".vscode/eslint.config.mjs",
                "--fix",
                "--cache",
                "--cache-location",
                f"{cache_loc}/eslint/",
            ],
            extensions=[".js", ".ts"],
            tags=["web"],
        ),
        NodeTool(
            "Stylelint",
            "stylelint",
            args=[
                "--config",
                ".vscode/.stylelintrc.yaml",
                "--cache",
                "--cache-location",
                f"{cache_loc}/style/",
            ],
            fix_args=[
                "--config",
                ".vscode/.stylelintrc.yaml",
                "--fix",
                "--cache",
                "--cache-location",
                f"{cache_loc}/style/",
            ],
            extensions=[".css"],
            tags=["web"],
        ),
        NodeTool(
            "Markdownlint",
            "markdownlint-cli2",
            args=["--config", ".vscode/.markdownlint.yaml"],
            fix_args=["--config", ".vscode/.markdownlint.yaml", "--fix"],
            extensions=[".md"],
            tags=["docs"],
        ),
        NodeTool(
            "Textlint",
            "textlint",
            args=[
                "-c",
                ".vscode/.textlintrc.json",
                "--cache",
                "--cache-location",
                f"{cache_loc}/text/",
            ],
            fix_args=[
                "-c",
                ".vscode/.textlintrc.json",
                "--fix",
                "--cache",
                "--cache-location",
                f"{cache_loc}/text/",
            ],
            extensions=[".md", ".txt"],
            tags=["docs"],
        ),
        NodeTool(
            "CSpell",
            "cspell",
            args=[
                "-c",
                ".vscode/cspell.json",
                "--no-progress",
                "--dot",
                "--cache",
                "--cache-location",
                f"{cache_loc}/cspell/",
            ],
            extensions=["*"],
            tags=["docs", "web", "python", "shell"],
        ),
        PythonTool(
            "shfmt",
            "shfmt",
            args=["-d", "-i", "2", "-ci", "-bn"],
            fix_args=["-w", "-i", "2", "-ci", "-bn"],
            tags=["shell"],
        ),
        ShellcheckTool(
            "Shellcheck",
            "shellcheck",
            args=["--rcfile", ".vscode/.shellcheckrc"],
            tags=["shell"],
        ),
        PythonTool(
            "Lico Empty Dir",
            "lico-lint-empty-dir",
            args=[],
            tags=["python", "web", "docs", "shell"],
        ),
    ]


def _parse_arguments() -> tuple[Path, bool, set[str]]:
    """Parse CLI arguments.

    Returns:
        tuple: (target_path, fix_mode, selected_tags).
    """
    parser = argparse.ArgumentParser(
        description="Orchestrator for Lico linting pipelines"
    )
    parser.add_argument("path", nargs="?", default=".", help="Path to check")
    parser.add_argument("--fix", action="store_true", help="Auto fix code")
    tags_list = ("python", "web", "docs", "shell")
    for tag in tags_list:
        parser.add_argument(f"--{tag}", action="store_true", help=f"Run {tag}")

    args = parser.parse_args()
    tags = {t for t in tags_list if getattr(args, t)}
    return Path(args.path).absolute(), args.fix, tags


def _execute_pipeline(
    tools: list[LintTool], target_path: Path, *, fix_mode: bool
) -> bool:
    """Run selected tools and return overall success.

    Args:
        tools (list[LintTool]): List of tools to execute.
        target_path (Path): Path to scan.
        fix_mode (bool): Fix mode flag.

    Returns:
        bool: True if all tools passed.
    """
    success = True
    for tool in tools:
        logger.info(LicoMsg.PIPELINE.TOOL_HEADER.format(tool=tool.name))
        result = tool.run(target_path, fix_mode=fix_mode)
        if not result.success:
            success = False
            logger.error(LicoMsg.PIPELINE.TOOL_FAILED.format(name=tool.name))
        else:
            logger.info(LicoMsg.PIPELINE.TOOL_PASSED.format(name=tool.name))
        logger.info(LicoMsg.PIPELINE.SEPARATOR)
    return success


def main() -> None:
    """Entry point for the quality pipeline orchestrator."""
    target_path, fix_mode, selected_tags = _parse_arguments()
    tools = _get_available_tools()

    if selected_tags:
        tools = [t for t in tools if set(t.tags) & selected_tags]

    mode_str = "FIX Mode 🔧" if fix_mode else "CHECK Mode 🔍"
    target_list = ", ".join(selected_tags) if selected_tags else "ALL"
    targets_str = f"Targets: {target_list}"
    logger.info(
        LicoMsg.PIPELINE.START.format(mode=mode_str, targets=targets_str)
    )

    if not tools:
        logger.info(LicoMsg.PIPELINE.NO_TOOLS_MATCH)
        sys.exit(0)

    if _execute_pipeline(tools, target_path, fix_mode=fix_mode):
        logger.info(LicoMsg.PIPELINE.ALL_PASSED)
        sys.exit(0)
    else:
        logger.error(LicoMsg.PIPELINE.SOME_FAILED)
        sys.exit(1)


if __name__ == "__main__":
    main()
