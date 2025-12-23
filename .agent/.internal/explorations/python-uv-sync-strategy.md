---
title: Idea: Python Environment Switching with uv sync
date: 2025-12-05
author: Lico
status: draft
tags:
  - python
  - uv
  - workflow
  - future-planning
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
    If Lico starts writing complex Python scripts, we should enforce linting (Ruff) and type checking (Mypy) *before* execution.
    - Currently not needed (scripts are simple), but a valid future direction.
    - Could integrate into a `pre-execution` workflow.

## Status
- Currently just an idea/reference.
- Captured to ensure Lico remembers this advanced usage of `uv` when the need arises.
