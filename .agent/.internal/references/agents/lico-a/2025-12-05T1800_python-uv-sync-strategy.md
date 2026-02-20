---
ai_visible: true
title: Python Environment Switching with uv sync
description: Idea for future Python workflow using uv sync group switching
tags: [python, uv, workflow, future-planning]
version: 1.0
created: 2025-12-05T18:00:00+09:00
updated: 2025-12-29T05:47:00+09:00
language: en
author: Lico (Lico-A)
ai_model: Gemini 3 Pro (High) Planning mode
status: draft
---

# Idea: Python Environment Switching with `uv sync`

## Context

The user utilizes `uv sync --group <group-name>` to dynamically swap library sets within a single `.venv`, matching the current task context (e.g., image processing vs. web dev).

## Proposal

If Lico or the project expands Python usage in the future (sub-projects, scripts), we should adopt this pattern.

### Potential Use Cases

1.  **Context-Specific Environments**:
    Instead of monolithic environments, switch dependency groups based on the active sub-project.

    ```bash
    uv sync --group pyspartaimg --group dev
    ```

2.  **Lico's Code Quality (Future)**:
    If Lico starts writing complex Python scripts, we should enforce linting (Ruff) and type checking (Mypy) _before_ execution.
    - Currently not needed (scripts are simple), but a valid future direction.
    - Could integrate into a `pre-execution` workflow.

## Status

- Currently just an idea/reference.
- Captured to ensure Lico remembers this advanced usage of `uv` when the need arises.

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
