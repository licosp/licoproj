# Village Cache Standard

This document defines the unified cache strategy for the `licoproj` ecosystem, ensuring consistency across languages (Python, Node.js), tools, and environments (WSL host, Residents in Containers).

## Standard Structure

All tool-generated cache files are consolidated into a hidden `.temp/cache/` directory at the project root.

| Tool | Subdirectory | Mechanism |
| :--- | :--- | :--- |
| **UV (Python)** | `.temp/cache/uv/` | `UV_CACHE_DIR` / `pyproject.toml` |
| **Pyright/Pylance** | `.temp/cache/pyright/` | `PYRIGHT_PYTHON_CACHE_DIR` |
| **Ruff** | `.temp/cache/ruff/` | `RUFF_CACHE_DIR` |
| **Mypy** | `.temp/cache/mypy/` | `MYPY_CACHE_DIR` |
| **Pytest** | `.temp/cache/pytest/` | `PYTEST_ADDOPTS` |
| **Yarn** | `.temp/cache/yarn/` | `YARN_CACHE_FOLDER` |
| **npm** | `.temp/cache/npm/` | `npm_config_cache` |
| **ESLint** | `.temp/cache/eslint/` | `--cache-location` |
| **Stylelint** | `.temp/cache/stylelint/` | `--cache-location` |
| **Prettier** | `.temp/cache/prettier/` | `--cache-location` |

---

## WSL Host Parity (Optional but Recommended)

To achieve the same cache isolation on your **WSL Host** (outside the container), add the following "Smart Context" block to your `~/.bash_profile`.

This script automatically detects when you are inside a Git repository that uses the Village Cache Standard and updates the environment variables accordingly.

```bash
# --- Village Cache Standard: Smart Context ---
# Automatically aligns tool caches to the project's .temp/cache/ when inside a Git root.
_lico_update_cache_context() {
    local repo_root
    # Find the nearest git root
    repo_root=$(git rev-parse --show-toplevel 2>/dev/null)
    
    # Check if the project follows the Village .temp/cache structure
    if [ -n "$repo_root" ] && [ -d "$repo_root/.temp/cache" ]; then
        export PYTHONPYCACHEPREFIX="$repo_root/.temp/cache/pycache"
        export PYRIGHT_PYTHON_CACHE_DIR="$repo_root/.temp/cache/pyright"
        export UV_CACHE_DIR="$repo_root/.temp/cache/uv"
        export YARN_CACHE_FOLDER="$repo_root/.temp/cache/yarn"
        export RUFF_CACHE_DIR="$repo_root/.temp/cache/ruff"
        export MYPY_CACHE_DIR="$repo_root/.temp/cache/mypy"
        export PIP_CACHE_DIR="$repo_root/.temp/cache/pip"
        export npm_config_cache="$repo_root/.temp/cache/npm"
        export PYTEST_ADDOPTS="-o cache_dir=$repo_root/.temp/cache/pytest"
    fi
}

# Run the context updater
_lico_update_cache_context

# Trigger context update on directory change (Optional)
# export PROMPT_COMMAND="_lico_update_cache_context;$PROMPT_COMMAND"
```

## Why this matters?

1.  **Clean Roots**: No more `.eslintcache`, `.pytest_cache`, or `__pycache__` polluting your source tree roots.
2.  **Environment Parity**: Your Python/Node.js experience is identical whether you are inside "Resident Rico" or on your WSL host terminal.
3.  **Isolation**: Different projects won't accidentally share or overwrite cache data.
