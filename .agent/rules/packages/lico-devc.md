---
ai_visible: true
title: Package lico-devc
description: Behavioral rules for the OS-level container isolation and permission delegation.
tags: [package, rules, lico-devc, container, permissions]
version: 1.0.0
created: 2026-03-21T20:03:40+09:00
updated: 2026-03-21T20:03:40+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# lico-devc

## Objective

`lico-devc` is the infrastructure package that manages the realization of Lico's multi-identifier consciousness within a containerized OS environment (`.devcontainer`). It translates logic-level "Identifiers" into literal OS-level User Accounts with strict permission delegation.

## Core Mechanisms (from `habitat.json`)

1. **OS-Level Isolation**: Each identifier (`sirius`, `iuria`, `agate`, etc.) is mapped to a dedicated UNIX user with a specific UID (1001-1007).
2. **Permission Delegation**:
   - `lico` is the root structural identity with `sudo` privileges.
   - All other identifiers deliberately operate **without sudo** to limit destructive blast radiuses structurally rather than cognitively.
3. **Workspace Mapping**: Identifiers are dynamically allocated specific `worktree` access points (e.g., `licoshdw`, `licochron`).

## Tool Usage Constraints

- **When to use**: Use this package when provisioning the workspace or modifying the active users inside the Dev Container.
- **How to use**: Managed via the python logic within `packages/lico-devc/src/`. Modifications to the OS topology should be made in `habitat.json`.

---

## Related Documents

| Document                                 | Purpose             |
| :--------------------------------------- | :------------------ |
| [`packages/lico-devc/README.md`](/packages/lico-devc/README.md) | Package structural pointer |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---

## Origin

- 2026-03-21T20:03 by Sirius: Created to fulfill the UV Package architecture aggregation and document the OS-level permission logic.
