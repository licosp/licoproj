---
# Context Configuration
context_id: "[Pkg-Backup]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
title: "Package lico-backup"
description: "Context card for developing the lico-backup package"
tags: ["package", "backup", "sync"]
version: 1.0.0
created: 2026-03-19T21:01:42+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Package lico-backup

## Human Notes

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

- Manage robust backup scripts via Python subprocess (rsync).
- Backup IDE artifacts and the full workspace.

---

## Agent Observations

### Agate (2026-03-19)

- Initial creation. Replaced inline bash scripts in `sync-memory.md` with Python equivalents.

---

## Related Documents

| Document                                 | Purpose             |
| :--------------------------------------- | :------------------ |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---

## Origin

- 2026-03-19T21:01:42+09:00 by Agate: Created as instead of readme file.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
