import argparse
import logging
import shutil
import subprocess
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path
from lico_logger import get_logger, LicoMsg

logger = get_logger(__name__)

logging.basicConfig(
    level=logging.INFO, format="%(message)s", stream=sys.stdout
)
logger = logging.getLogger(__name__)


@dataclass
class ToolResult:
    name: str
    success: bool
    return_code: int


class LintTool(ABC):
    def __init__(
        self, name: str, extensions: list[str], tags: list[str] | None = None
    ):
        self.name = name
        self.extensions = extensions
        self.tags = tags or []

    @abstractmethod
    def run(self, target_path: Path, fix_mode: bool = False) -> ToolResult:
        pass

    def _run_subprocess(
        self, cmd: list[str], cwd: Path | None = None
    ) -> ToolResult:
        logger.info(f"Running: {' '.join(cmd)}")
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
            logger.exception(f"Error: Command '{cmd[0]}' not found.")
            return ToolResult(name=self.name, success=False, return_code=-1)


class PythonTool(LintTool):
    def __init__(
        self,
        name: str,
        command: str,
        args: list[str],
        fix_args: list[str] | None = None,
        tags: list[str] | None = None,
    ):
        super().__init__(name, [".py", ".pyi"], tags)
        self.command = command
        self.args = args
        self.fix_args = fix_args

    def _resolve_executable(self) -> str | None:
        python_dir = Path(sys.executable).parent
        candidate = python_dir / self.command
        if candidate.exists():
            return str(candidate)
        return shutil.which(self.command)

    def run(self, target_path: Path, fix_mode: bool = False) -> ToolResult:
        executable = self._resolve_executable()
        if not executable:
            logger.error(
                f"Error: Executable '{self.command}' not found for {self.name}."
            )
            return ToolResult(name=self.name, success=False, return_code=-1)

        current_args = self.args
        if fix_mode and self.fix_args is not None:
            current_args = self.fix_args

        full_cmd = [executable, *current_args, str(target_path)]
        return self._run_subprocess(full_cmd)


class NodeTool(LintTool):
    def __init__(
        self,
        name: str,
        command: str,
        args: list[str],
        extensions: list[str],
        fix_args: list[str] | None = None,
        tags: list[str] | None = None,
    ):
        super().__init__(name, extensions, tags)
        self.command = command
        self.args = args
        self.fix_args = fix_args

    def _resolve_executable(self, root_dir: Path) -> str | None:
        candidate = root_dir / "node_modules" / ".bin" / self.command
        if candidate.exists():
            return str(candidate)
        return shutil.which(self.command)

    def run(self, target_path: Path, fix_mode: bool = False) -> ToolResult:
        current = Path.cwd()
        root_dir = current

        executable = self._resolve_executable(root_dir)
        if not executable:
            logger.error(
                f"Error: Executable '{self.command}' not found for {self.name}."
            )
            return ToolResult(name=self.name, success=False, return_code=-1)

        current_args = self.args
        if fix_mode and self.fix_args is not None:
            current_args = self.fix_args

        full_cmd = [executable, *current_args]

        if self.command == "prettier":
            if target_path.is_dir():
                full_cmd.append(str(target_path / "**/*"))
            else:
                full_cmd.append(str(target_path))
        else:
            full_cmd.append(str(target_path))

        return self._run_subprocess(full_cmd)


class ShellcheckTool(PythonTool):
    def __init__(
        self,
        name: str,
        command: str,
        args: list[str],
        tags: list[str] | None = None,
    ):
        # Inherit from PythonTool since shellcheck-py puts the binary in .venv/bin
        super().__init__(name, command, args, tags=tags)
        self.extensions = [".sh", ".bash"]  # override Python extensions

    def run(self, target_path: Path, fix_mode: bool = False) -> ToolResult:
        executable = self._resolve_executable()
        if not executable:
            logger.error(
                f"Error: Executable '{self.command}' not found for {self.name}."
            )
            return ToolResult(name=self.name, success=False, return_code=-1)

        # Shellcheck requires explicit files, not directories.
        files_to_check: list[Path] = []
        if target_path.is_dir():
            files_to_check.extend(target_path.rglob("*.sh"))
            files_to_check.extend(target_path.rglob("*.bash"))
            # Filter out ignored directories to prevent noise
            files_to_check = [
                f
                for f in files_to_check
                if ".venv" not in f.parts
                and "node_modules" not in f.parts
                and ".temp" not in f.parts
            ]
        elif target_path.suffix in self.extensions:
            files_to_check.append(target_path)

        if not files_to_check:
            logger.info(f"Skipping {self.name}: No matching files found.")
            return ToolResult(name=self.name, success=True, return_code=0)

        current_args = self.args
        if fix_mode and self.fix_args is not None:
            current_args = self.fix_args

        full_cmd = [executable, *current_args] + [
            str(f) for f in files_to_check
        ]
        return self._run_subprocess(full_cmd)


def main() -> None:
    parser = argparse.ArgumentParser(
        description="Orchestrator for Lico linting pipelines"
    )
    parser.add_argument("path", nargs="?", default=".", help="Path to check")
    parser.add_argument(
        "--fix",
        action="store_true",
        help="Automatically fix and format code where possible",
    )

    # Workflow Target Flags
    group = parser.add_argument_group("Workflow Targets")
    group.add_argument(
        "--python", action="store_true", help="Run only Python-related tools"
    )
    group.add_argument(
        "--web",
        action="store_true",
        help="Run only Web frontend-related tools (JS, CSS)",
    )
    group.add_argument(
        "--docs",
        action="store_true",
        help="Run only Documentation-related tools (MD, Text)",
    )
    group.add_argument(
        "--shell",
        action="store_true",
        help="Run only Shell script-related tools",
    )

    args = parser.parse_args()
    target_path = Path(args.path).absolute()
    fix_mode = args.fix

    # Determine selected tags
    selected_tags = set()
    if args.python:
        selected_tags.add("python")
    if args.web:
        selected_tags.add("web")
    if args.docs:
        selected_tags.add("docs")
    if args.shell:
        selected_tags.add("shell")

    # Define Tools
    tools: list[LintTool] = [
        # Python Tools
        PythonTool(
            "Ruff Check",
            "ruff",
            args=["check", "--no-fix", "--config", "pyproject.toml"],
            fix_args=["check", "--fix", "--config", "pyproject.toml"],
            tags=["python"],
        ),
        PythonTool(
            "Ruff Format",
            "ruff",
            args=["format", "--check", "--config", "pyproject.toml"],
            fix_args=["format", "--config", "pyproject.toml"],
            tags=["python"],
        ),
        PythonTool(
            "Pyright",
            "pyright",
            args=["--project", "pyproject.toml"],
            tags=["python"],
        ),
        PythonTool(
            "Pytest", "pytest", args=["-c", "pyproject.toml"], tags=["python"]
        ),
        # Node Tools
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
                ".temp/cache/prettier/",
            ],
            fix_args=[
                "--config",
                ".vscode/.prettierrc.yaml",
                "--ignore-path",
                ".vscode/.prettierignore",
                "--write",
                "--cache",
                "--cache-location",
                ".temp/cache/prettier/",
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
                ".temp/cache/eslint/",
            ],
            fix_args=[
                "--config",
                ".vscode/eslint.config.mjs",
                "--fix",
                "--cache",
                "--cache-location",
                ".temp/cache/eslint/",
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
                ".temp/cache/stylelint/",
            ],
            fix_args=[
                "--config",
                ".vscode/.stylelintrc.yaml",
                "--fix",
                "--cache",
                "--cache-location",
                ".temp/cache/stylelint/",
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
                ".temp/cache/textlint/",
            ],
            fix_args=[
                "-c",
                ".vscode/.textlintrc.json",
                "--fix",
                "--cache",
                "--cache-location",
                ".temp/cache/textlint/",
            ],
            extensions=[".md", ".txt"],
            tags=["docs"],
        ),
        NodeTool(
            "CSpell",
            "cspell",
            [
                "-c",
                ".vscode/cspell.json",
                "--no-progress",
                "--dot",
                "--cache",
                "--cache-location",
                ".temp/cache/cspell/",
            ],
            ["*"],
            tags=["docs", "web", "python", "shell"],
        ),
        # Shell Tools (Now managed by uv via PyPI wrappers)
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
        # Custom Tools
        PythonTool(
            "Lico Empty Dir",
            "lico-lint-empty-dir",
            [],
            tags=["python", "web", "docs", "shell"],
        ),
    ]

    # Filter tools based on tags
    if selected_tags:
        toolsToRun = [tool for tool in tools if set(tool.tags) & selected_tags]
    else:
        toolsToRun = tools  # Run all if no flags specified

    success = True
    mode_str = "FIX Mode 🔧" if fix_mode else "CHECK Mode 🔍"
    targets_str = (
        f"Targets: {', '.join(selected_tags)}"
        if selected_tags
        else "Targets: ALL"
    )
    logger.info(LicoMsg.PIPELINE.START.format(mode=mode_str, targets=targets_str))

    if not toolsToRun:
        logger.warning(LicoMsg.PIPELINE.NO_TOOLS_MATCH)
        sys.exit(0)

    for tool in toolsToRun:
        logger.info(LicoMsg.PIPELINE.TOOL_HEADER.format(tool=tool.name))
        result = tool.run(target_path, fix_mode=fix_mode)
        if not result.success:
            success = False
            logger.error(f"❌ {tool.name} failed!")
        else:
            logger.info(f"✅ {tool.name} passed.")
        logger.info(LicoMsg.PIPELINE.SEPARATOR)

    if success:
        logger.info("🎉 All selected checks passed!")
        sys.exit(0)
    else:
        logger.error("💥 Some checks failed.")
        sys.exit(1)


if __name__ == "__main__":
    main()
