import argparse
import logging
import shutil
import subprocess
import sys
from abc import ABC, abstractmethod
from dataclasses import dataclass
from pathlib import Path

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
    def __init__(self, name: str, extensions: list[str]):
        self.name = name
        self.extensions = extensions

    @abstractmethod
    def run(self, target_path: Path, fix_mode: bool = False) -> ToolResult:
        pass

    def _run_subprocess(self, cmd: list[str], cwd: Path | None = None) -> ToolResult:
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
    def __init__(self, name: str, command: str, args: list[str], fix_args: list[str] | None = None):
        super().__init__(name, [".py", ".pyi"])
        self.command = command
        self.args = args
        self.fix_args = fix_args

    def _resolve_executable(self) -> str | None:
        # Priority 1: Sibling of current python executable (venv)
        python_dir = Path(sys.executable).parent
        candidate = python_dir / self.command
        if candidate.exists():
            return str(candidate)
        
        # Priority 2: PATH
        return shutil.which(self.command)

    def run(self, target_path: Path, fix_mode: bool = False) -> ToolResult:
        executable = self._resolve_executable()
        if not executable:
            logger.error(f"Error: Executable '{self.command}' not found for {self.name}.")
            return ToolResult(name=self.name, success=False, return_code=-1)

        # Select arguments based on mode
        current_args = self.args
        if fix_mode and self.fix_args is not None:
            current_args = self.fix_args

        full_cmd = [executable, *current_args, str(target_path)]
        return self._run_subprocess(full_cmd)


class NodeTool(LintTool):
    def __init__(self, name: str, command: str, args: list[str], extensions: list[str], fix_args: list[str] | None = None):
        super().__init__(name, extensions)
        self.command = command
        self.args = args
        self.fix_args = fix_args

    def _resolve_executable(self, root_dir: Path) -> str | None:
        # Priority 1: node_modules/.bin in the project root
        candidate = root_dir / "node_modules" / ".bin" / self.command
        if candidate.exists():
            return str(candidate)
        
        # Priority 2: PATH (global install - discouraged but possible)
        return shutil.which(self.command)

    def run(self, target_path: Path, fix_mode: bool = False) -> ToolResult:
        current = Path.cwd()
        root_dir = current 
        
        executable = self._resolve_executable(root_dir)
        if not executable:
            logger.error(f"Error: Executable '{self.command}' not found for {self.name}.")
            return ToolResult(name=self.name, success=False, return_code=-1)

        # Select arguments based on mode
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


def main() -> None:
    parser = argparse.ArgumentParser(description="Orchestrator for Lico linting pipelines")
    parser.add_argument("path", nargs="?", default=".", help="Path to check")
    parser.add_argument("--fix", action="store_true", help="Automatically fix and format code where possible")
    args = parser.parse_args()
    target_path = Path(args.path).absolute()
    fix_mode = args.fix

    # Define Tools
    tools: list[LintTool] = [
        # Python Tools
        PythonTool(
            "Ruff Check", "ruff", 
            args=["check", "--no-fix", "--config", "pyproject.toml"],
            fix_args=["check", "--fix", "--config", "pyproject.toml"]
        ),
        PythonTool(
            "Ruff Format", "ruff", 
            args=["format", "--check", "--config", "pyproject.toml"],
            fix_args=["format", "--config", "pyproject.toml"]
        ),
        PythonTool("Pyright", "pyright", args=["--project", "pyproject.toml"]), # No fix mode
        PythonTool("Pytest", "pytest", args=["-c", "pyproject.toml"]), # No fix mode
        
        # Node Tools
        NodeTool(
            "Prettier", "prettier", 
            args=["--config", ".vscode/.prettierrc.yaml", "--ignore-path", ".vscode/.prettierignore", "--check", "--cache", "--cache-location", ".temp/cache/prettier/"],
            fix_args=["--config", ".vscode/.prettierrc.yaml", "--ignore-path", ".vscode/.prettierignore", "--write", "--cache", "--cache-location", ".temp/cache/prettier/"],
            extensions=[".js", ".ts", ".md", ".json", ".yaml"]
        ),
        NodeTool(
            "ESLint", "eslint", 
            args=["--config", ".vscode/eslint.config.mjs", "--cache", "--cache-location", ".temp/cache/eslint/"],
            fix_args=["--config", ".vscode/eslint.config.mjs", "--fix", "--cache", "--cache-location", ".temp/cache/eslint/"],
            extensions=[".js", ".ts"]
        ),
        NodeTool(
            "Stylelint", "stylelint", 
            args=["--config", ".vscode/.stylelintrc.yaml", "--cache", "--cache-location", ".temp/cache/stylelint/"],
            fix_args=["--config", ".vscode/.stylelintrc.yaml", "--fix", "--cache", "--cache-location", ".temp/cache/stylelint/"],
            extensions=[".css"]
        ),
        NodeTool(
            "Markdownlint", "markdownlint-cli2", 
            args=["--config", ".vscode/.markdownlint.yaml"],
            fix_args=["--config", ".vscode/.markdownlint.yaml", "--fix"],
            extensions=[".md"]
        ),
        NodeTool(
            "Textlint", "textlint", 
            args=["-c", ".vscode/.textlintrc.json", "--cache", "--cache-location", ".temp/cache/textlint/"],
            fix_args=["-c", ".vscode/.textlintrc.json", "--fix", "--cache", "--cache-location", ".temp/cache/textlint/"],
            extensions=[".md", ".txt"]
        ),
        NodeTool("CSpell", "cspell", ["-c", ".vscode/cspell.json", "--no-progress", "--dot", "--cache", "--cache-location", ".temp/cache/cspell/"], ["*"]), # No fix mode
        
        # Custom Tools
        PythonTool("Lico Empty Dir", "lico-lint-empty-dir", []), # No fix mode yet
    ]

    success = True
    mode_str = "FIX Mode 🔧" if fix_mode else "CHECK Mode 🔍"
    print(f"\n🚀 Starting Lico Pipeline ({mode_str})...\n")
    
    for tool in tools:
        print(f"--- {tool.name} ---")
        result = tool.run(target_path, fix_mode=fix_mode)
        if not result.success:
            success = False
            logger.error(f"❌ {tool.name} failed!")
        else:
            logger.info(f"✅ {tool.name} passed.")
        print("")

    if success:
        logger.info("🎉 All checks passed!")
        sys.exit(0)
    else:
        logger.error("💥 Some checks failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
