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
- Refactoring from a simple script to a modular `Tool` class architecture.
- Aiming for strict separation of "Tools" vs "Orchestrator".

---

## Related Documents

| Document                                 | Purpose             |
| :--------------------------------------- | :------------------ |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---

## Origin

- 2026-03-20T00:00:00+09:00 by Agate: Created.
