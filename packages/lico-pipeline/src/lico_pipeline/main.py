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
    def run(self, target_path: Path) -> ToolResult:
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
    def __init__(self, name: str, command: str, args: list[str]):
        super().__init__(name, [".py", ".pyi"])
        self.command = command
        self.args = args

    def _resolve_executable(self) -> str | None:
        # Priority 1: Sibling of current python executable (venv)
        python_dir = Path(sys.executable).parent
        candidate = python_dir / self.command
        if candidate.exists():
            return str(candidate)
        
        # Priority 2: PATH
        return shutil.which(self.command)

    def run(self, target_path: Path) -> ToolResult:
        executable = self._resolve_executable()
        if not executable:
            logger.error(f"Error: Executable '{self.command}' not found for {self.name}.")
            return ToolResult(name=self.name, success=False, return_code=-1)

        full_cmd = [executable, *self.args, str(target_path)]
        return self._run_subprocess(full_cmd)


class NodeTool(LintTool):
    def __init__(self, name: str, command: str, args: list[str], extensions: list[str]):
        super().__init__(name, extensions)
        self.command = command
        self.args = args

    def _resolve_executable(self, root_dir: Path) -> str | None:
        # Priority 1: node_modules/.bin in the project root
        candidate = root_dir / "node_modules" / ".bin" / self.command
        if candidate.exists():
            return str(candidate)
        
        # Priority 2: PATH (global install - discouraged but possible)
        return shutil.which(self.command)

    def run(self, target_path: Path) -> ToolResult:
        # Node tools need to find the project root to locate node_modules.
        # Heuristic: look for package.json in CWD or parents.
        # For now, we assume CWD is the root (standard for our workflow).
        current = Path.cwd()
        root_dir = current 
        
        executable = self._resolve_executable(root_dir)
        if not executable:
            logger.error(f"Error: Executable '{self.command}' not found for {self.name}.")
            return ToolResult(name=self.name, success=False, return_code=-1)

        full_cmd = [executable, *self.args]
        
        # Prettier handling: if target is a dir, it needs a glob. 
        # But if it's a file, it just takes the file.
        if self.command == "prettier":
             if target_path.is_dir():
                 # Append glob to check all files in the directory
                 full_cmd.append(str(target_path / "**/*")) 
             else:
                 full_cmd.append(str(target_path))
        else:
             full_cmd.append(str(target_path))

        return self._run_subprocess(full_cmd)


def main() -> None:
    parser = argparse.ArgumentParser(description="Orchestrator for Lico linting pipelines")
    parser.add_argument("path", nargs="?", default=".", help="Path to check")
    args = parser.parse_args()
    target_path = Path(args.path).absolute()

    # Define Tools
    # Note: We explicitly pass config paths where applicable to ensure parity with IDE settings.
    tools: list[LintTool] = [
        # Python Tools
        PythonTool("Ruff Check", "ruff", ["check", "--no-fix", "--config", "pyproject.toml"]),
        PythonTool("Ruff Format", "ruff", ["format", "--check", "--config", "pyproject.toml"]),
        PythonTool("Pyright", "pyright", ["--project", "pyproject.toml"]),
        PythonTool("Pytest", "pytest", ["-c", "pyproject.toml"]),
        
        # Node Tools (Explicitly defined args mirroring package.json)
        NodeTool("Prettier", "prettier", ["--config", ".vscode/.prettierrc.yaml", "--ignore-path", ".vscode/.prettierignore", "--check", "--cache", "--cache-location", ".temp/cache/prettier/"], [".js", ".ts", ".md", ".json", ".yaml"]),
        NodeTool("ESLint", "eslint", ["--config", ".vscode/eslint.config.mjs", "--cache", "--cache-location", ".temp/cache/eslint/"], [".js", ".ts"]),
        NodeTool("Stylelint", "stylelint", ["--config", ".vscode/.stylelintrc.yaml", "--cache", "--cache-location", ".temp/cache/stylelint/"], [".css"]),
        NodeTool("Markdownlint", "markdownlint-cli2", ["--config", ".vscode/.markdownlint.yaml"], [".md"]),
        NodeTool("Textlint", "textlint", ["-c", ".vscode/.textlintrc.json", "--cache", "--cache-location", ".temp/cache/textlint/"], [".md", ".txt"]),
        NodeTool("CSpell", "cspell", ["-c", ".vscode/cspell.json", "--no-progress", "--dot", "--cache", "--cache-location", ".temp/cache/cspell/"], ["*"]),
        
        # Custom Tools
        PythonTool("Lico Empty Dir", "lico-lint-empty-dir", []),
    ]

    success = True
    print("\n🚀 Starting Lico Pipeline...\n")
    
    for tool in tools:
        print(f"--- {tool.name} ---")
        result = tool.run(target_path)
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
