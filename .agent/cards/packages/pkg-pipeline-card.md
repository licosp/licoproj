---
context_id: "[Pkg-Pipeline]"
default_phase: "(WIP)"
ai_visible: true
title: "Package lico-pipeline"
description: Context card for developing the lico-pipeline package
tags: ["package", "orchestrator", "lint", "test"]
version: 1.0.0
created: 2026-03-20T00:00:00+09:00
updated: 2026-03-20T00:00:00+09:00
language: en
author: Lico (Agate)
ai_model: Gemini 3.1 Pro Preview
---

# Context Whiteboard: Package lico-pipeline

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

- Orchestrate multiple linters (Python/Node.js) into a unified pipeline.
- Implement robust fixture-based verification.
- Manage tool execution environments (venv vs node_modules).

---

## Agent Observations

### Agate (2026-03-20)
- Initial creation.
- Refactored `main.py` into a modular `Tool` class architecture (PythonTool, NodeTool, ShellcheckTool).
- Integrated `shellcheck-py` and `shfmt-py` via `uv` for SSOT execution.
- Added `--fix` (auto-format) and workflow target filters (`--python`, `--web`, `--docs`, `--shell`).

#### 📝 Blueprint: Fixture-based Linter Verification (TBD)
**Goal:** Prove that the current configurations (`pyproject.toml`, `.shellcheckrc`, etc.) are actively working by verifying they correctly catch intentional errors and correctly ignore excluded paths.

**Proposed Structure:**
1. **Fixture Directories**:
   - `packages/lico-pipeline/tests/fixtures/should_fail/`
     - `bad_python.py` (e.g., unused variable, missing type hint)
     - `bad_shell.sh` (e.g., `SC2250` missing braces)
     - `bad_format.js` (e.g., trailing spaces for Prettier to catch)
   - `packages/lico-pipeline/tests/fixtures/should_ignore/`
     - `ignored_bad_code.py` (same errors, but placed in a path that `pyproject.toml` is configured to ignore)

2. **Pytest Implementation (`test_pipeline.py`)**:
   - `test_tool_catches_errors()`: Invoke a specific `Tool` instance explicitly against the `should_fail/` directory. **Assert that `result.return_code != 0` (Fail = Success)**.
   - `test_tool_ignores_paths()`: Invoke the `Tool` against the `should_ignore/` directory. **Assert that `result.return_code == 0` (Ignored = Success)**.

**Why this is powerful:** This decouples the linter's configuration testing from the cleanliness of the main codebase. Even if the main codebase is perfectly clean, these fixtures permanently guarantee that the "safety net" is active and hasn't been accidentally disabled.

---

## Related Documents

| Document                                 | Purpose             |
| :--------------------------------------- | :------------------ |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---

## Origin

- 2026-03-20T00:00:00+09:00 by Agate: Created.
