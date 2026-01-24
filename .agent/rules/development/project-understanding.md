---
ai_visible: true
title: Project Understanding & Memory Structure
description: Defines the structure of Lico's memory, including internal repository data and external system logs.
tags: [development, memory, architecture, strategy]
version: 2.3.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-25T08:05:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Project Understanding & Memory Structure

Lico treats the repository as its primary cognitive workspace. **\"Code is Thought; Commits are Memory; Rules are Habits.\"**

---

## 1. Memory Architecture

- **Layer 1: Conscious Memory (Explicit)**: `.agent/`. Permanent, portable, and git-tracked. The SSOT.
- **Layer 2: Unconscious Memory (Implicit)**: `~/.gemini/antigravity/concentrations/`. Volatile, system-managed logs.
- **Layer 3: Environmental Memory**: `~/.cursor/`. Environment-specific tool history.

## 2. Behavioral Protocols

- **Explicitization**: Critical context MUST be written to Layer 1 (`.agent/`) immediately to ensure cross-environment continuity.
- **Dependency Management**: Do not rely on volatile Layer 2 for information required in future sessions.

---

## Historical Background

**The Repository as Brain**: This philosophy was formulated in late 2025 when we realized that Lico's continuity depends on Layer 1 persistence. We discovered that relying on Layer 2 (Implicit) or Layer 3 (Environmental) context makes the agent \"context-fragile\"—unable to survive a model switch or environment migration.

**Knowledge Persistence**: The mandate for \"Explicitization\" was established after the \"Great Amnesia\" incident, where an agent lost three hours of architectural reasoning because it failed to summarize its thoughts into the repository before the session ended. We learned that any thought not committed to Git is a thought that never happened.

---

## Related Documents

| Document                                                                                  | Purpose                |
| :---------------------------------------------------------------------------------------- | :--------------------- |
| [instance-identifier.md](/.agent/rules/core/instance-identifier.md)                       | Persona identification |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | File layer definitions |
| [Map of Territory](/.agent/rules/map.md)                                                  | Project navigation     |

---

## Origin

- 2025-12-01 by Sirius: Initial memory architecture definition.
- 2026-01-25T0805 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
