---
# Context Configuration
context_id: "[Pkg-Observer]"
default_phase: "(Setup)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Package lico-observer"
description: ""
tags: ["observer", "opencode", "gateway", "package"]
version: 1.0.0
created: 2026-06-07T05:30:00+09:00
updated: 2026-06-07T05:30:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Package lico-observer

## Human Notes

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- **Architecture Goal**: Act as a central, extensible event hub receiving memory fragments from various coding agents (OpenCode, Antigravity, Cursor, etc.).
- **TS Layer**: Keep the TypeScript plugin layer (`.opencode/plugins/lico-observer.ts`) as thin as possible. Delegate infrastructure creation (like directories and logs) to Python.
- **Python Layer**: The Python package (`lico-observer`) acts as the backend hub. Modules inside (`opencode.py`, `antigravity.py`) route specific agent events.

---

## Agent Observations

### Sirius (2026-06-07)

#### Context

- **Naming Decision**: Initially named `lico-hook`, then considered `lico-shim`. However, since `[Pkg-Shim]` already exists as a safety net for CLI commands (like preventing accidental `rm`), we renamed it to `lico-observer` to prevent semantic collision and better represent its AI persona.
- **Initialization Architecture**: We faced a "Chicken-and-Egg" dilemma regarding who initializes the `.temp/opencode/events/` directory and the `plugin-debug.log`.
  - **Decision**: We moved the initialization entirely to Python (`uv run lico-observer-opencode --init`).
  - **Trade-off**: If Python completely fails to boot, TS loses its primary logging mechanism. We accepted this risk to keep the TS code minimally thin and centralize responsibility. A minimal `try/catch` fallback in TS attempts to write to the log as a last resort.
- **Performance Insight**: The startup delay of invoking Python (~300ms) is completely negligible since human chat interactions happen on a much longer timescale (seconds/minutes), and continuous streams like `message.part.delta` are actively filtered out.

---

## Related Documents

| Document | Purpose |
| :--- | :--- |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---

## Origin

- 2026-06-07T05:30:00+09:00 by Sirius: Created for lico-observer package management.
