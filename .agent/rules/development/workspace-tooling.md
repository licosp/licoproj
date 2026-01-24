---
ai_visible: true
title: Workspace-Centric Tooling
description: Guidelines for managing development tools and dependencies within workspaces.
tags: [development, tools, environment, portability]
version: 2.3.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-25T08:25:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Workspace-Centric Tooling

Management of tools within the repository context. **\"Workspace-First; Manage via Git.\"**

---

## 1. Principles

- **Prefer Workspace Dependencies**: Install tools locally (`package.json`, `.venv`) over global versions.
- **Document Tool Versions**: Ensure environmental consistency by tracking versions in the repository.
- **Portability**: A new agent should be able to run `yarn install` or `uv sync` and have a 100% ready environment.

## 2. Execution

- Use **`npx`** or **`uv run`** to execute workspace-local tools. Avoid relying on the user's global PATH.

---

## Historical Background

**The Ghost of Environments Past**: This protocol was born in late 2025 after a session failed because a required linting tool existed on one machine but not another. This "Environmental Fragility" stalled development and caused non-reproducible errors.

**Tooling as a First-Class Citizen**: We learned that for an AI agent, the "Workspace" is its physical environment. By treating tool dependencies as part of the repository (stored in `.agent/runtimes/` or managed via lockfiles), we ensure that the agent's capability set is portable across all Lico instances, regardless of the host machine's configuration.

---

## Related Documents

| Document                                                                       | Purpose                    |
| :----------------------------------------------------------------------------- | :------------------------- |
| [agent-tool-selection.md](/.agent/rules/development/agent-tool-selection.md)   | Tool prioritization policy |
| [project-understanding.md](/.agent/rules/development/project-understanding.md) | Workspace memory structure |
| [Map of Territory](/.agent/rules/map.md)                                       | Project navigation         |

---

## Origin

- 2025-12-01 by Sirius: Initial workspace-first tooling principle.
- 2026-01-25T0825 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
