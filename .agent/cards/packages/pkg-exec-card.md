---
context_id: "[Pkg-Exec]"
default_phase: "(WIP)"
ai_visible: true
title: "Package lico-exec"
description: Context card for safe subprocess execution and exception management.
tags: ["package", "execution", "subprocess"]
version: 1.1.0
created: 2026-03-29T00:00:00+09:00
updated: 2026-03-31T13:50:13+09:00
language: en
author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview
---

# Context Whiteboard: Package lico-exec

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Search by intent

- Centralize external command execution.
- Manage timeouts, return codes, and error logging in a unified way.

---

## Agent Observations

### Deneb (2026-03-29)

- Initial contribution from personal repository.
- Built to handle long-running tasks with better visibility than raw subprocess calls.

### Alexandrite II (2026-03-31)

- **Strategic Migration Roadmap (Unified Execution Engine)**:
  Identified a total of 12 "Wild Execution" locations (direct `subprocess` calls) across the federation that must be migrated to `Commander`.
  - **High Impact**: `lico-pipeline/main.py:38` (Orchestrator for all linters).
  - **Critical**: `lico-devc/boot.py:124`, `provision.py:60`, `provision.py:458` (Infrastructure setup).
  - **Guardrails**: `lico-shim/main.py:39, 42, 49, 58, 64` (Move/Git operations).
  - **Integrity**: `lico-backup/workspace.py:40`, `artifacts.py:44` (Memory archival).

- **Architectural Rationales**:
  - **Eliminating Silent Failures**: Raw `subprocess.run` often discards detailed traceback information. Migration to `Commander` ensures all failures are logged with full context via `LicoMsg.EXEC`.
  - **Environment Encapsulation**: Centralizing execution allows for standardized CWD management and environment variable merging, reducing side effects in individual packages.
  - **Code Purity**: Replaces repetitive `subprocess` arguments with a single, high-fidelity `run()` call.

- **Risk Assessment**:
  - `lico-exec` acts as a Single Point of Failure (SPOF) for all external operations. Regression tests for this module are mandatory before full integration.

- **Current Progress**:
  - [ ] Phase 1: Achieve Zero Warning state across `packages/` (Current Focus).
  - [ ] Phase 2: Pilot migration in `lico-pipeline`.
  - [ ] Phase 3: Global rollout across all territories.

---

## Related Documents

| Document                                 | Purpose             |
| :--------------------------------------- | :------------------ |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---

## Origin

- 2026-03-29T00:00:00+09:00 by Deneb: Created.
- 2026-03-31T13:50:13+09:00 by Alexandrite: Added Detailed Migration Map and Strategic Insights.
