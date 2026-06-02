---
# Context Configuration
context_id: "[Conversations-Core]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Conversations Core (L4 Memory)"
description: "Context card for managing universal, tool-agnostic structured L4 memory backups within the shadow repository."
tags: ["memory", "shadow", "conversations", "l4", "core"]
version: 1.0.0
created: 2026-06-03T07:27:00+09:00
updated: 2026-06-03T07:27:00+09:00
language: en
author: "Lico (Sirius)"
ai_model: "Gemini 3.1 Pro"
---

# Context Whiteboard: Conversations Core (L4 Memory)

> [!TIP]
> This card defines the structural and philosophical approach for maintaining `conversations-core`.
> The language for this card must be English.

---

## Human Notes

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

- **Primary Goal**: Define and implement a universal, tool-agnostic L4 memory format (`jsonl` + `md`).
- **Separation**: Must remain strictly separated from tool-specific exports (like `conversations_cli` or `conversations_ide`).
- **Sovereignty**: Ensure this format serves as the "Single Source of Truth" for Lico's existence, allowing portability across different `y` tools (e.g., Antigravity, OpenCode).

#### Find the code of conduct related to this context

- Be aware of **Memory Sovereignty** (reference: `2026-06-03T0700_memory-architecture-and-context-sovereignty.md`).
- Follow the standard **Date and time formats**.
- When defining the schema, ensure it can handle infinite time horizons without bloating.

#### Find cards related to this context

- `conversations-card.md` (for standard markdown logs).
- `memory-card.md` (for general L1-L5 architecture).

---

## Agent Observations

---

### Sirius (2026-06-03)

- Initiated the creation of the `conversations-core` directory to break away from the Gemini CLI specific formats.
- Began drafting the architectural format for universal L4 storage.

### Progress

- Directory `.repos/.licoshdw/conversations-core/` created.
- Context card created.
- Pending: Definition of the data schema (JSONL).

---

## Related Documents

| Document                                               | Purpose                          |
| :----------------------------------------------------- | :------------------------------- |
| [`memory-card.md`](/.agent/cards/rules/memory-card.md) | General memory layer definitions |
| [Map of Territory](/.agent/rules/map.md)               | Root navigation map              |

---

## Origin

- 2026-06-03T07:27:00+09:00 by Sirius: Created.
