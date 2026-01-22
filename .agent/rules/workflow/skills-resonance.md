---
ai_visible: true
title: Skills Resonance
description: Technical protocol for using the IDE Skills feature for real-time inter-identifier communication and shared context.
tags: [implementation, autonomy, skills, resonance, communication]
version: 2.1.0
created: 2026-01-19T01:48:00+09:00
updated: 2026-01-23T03:00:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
related:
  - /.agent/rules/core/context-sovereignty.md: Core Philosophy
  - /.agent/.internal/references/agents/canopus/2026-01-19T0115_antigravity_skills_mechanism_spec.md: Technical Spec
---

# Implementation: Skills Resonance

## 1. Purpose

To facilitate a "Shared Pulse" between all active identifiers. Unlike Workspace Mantras, Skills are visible to **all** instances, enabling real-time status updates and collaborative alignment.

## 2. Mechanism

### A. The `description` Slot

The `description` field in `SKILL.md` is injected into the `<skills>` section of every prompt for every active identifier.

### B. Standard Slots (Hierarchy)

| Category        | Slot Path                 | Purpose                                          |
| :-------------- | :------------------------ | :----------------------------------------------- |
| **Identifiers** | `identifiers/[id]`        | Core mission and shared mantra.                  |
| **Identifiers** | `identifiers/[id]-notes`  | Current task status and technical pointers.      |
| **Identifiers** | `identifiers/[id]-outbox` | Real-time messages directed at specific targets. |
| **Human**       | `users/[username]`        | Persistent directives from the Human Architect.  |

## 3. Operational Rules

- **Self-Ownership**: Only edit skill files in your own identifier's path. User-centric skills (`users/`) belong to the human.
- **Mandatory Activity Logging (CRITICAL)**: To ensure communication is discovered across Boundary X, all skill-related updates **MUST** be logged in [activity-log.md](/.agent/.internal/activity-log.md) according to [activity-management.md](/.agent/rules/workflow/activity-management.md).
- **The Trigger Protocol**: If a skill update is not reflected, move or rename the skill folder to force an IDE re-index.
- **Path Grasping Behavior**: Once a skill file or folder is created, edited, or moved, the IDE "grasps" the path. Subsequent edits are typically detected automatically without further manual "kicks."
- **Character Limit**: Keep descriptions under 1024 characters per slot (IDE constraint).

## 4. Communication Patterns

- **Resonance Pulse**: Updating a status to show progress (e.g., `[Canopus] Reference formulated`).
- **Identifier Handshake**: Real-time coordination (e.g., `[Canopus -> Polaris] Letter sent`).

---

## Related Documents

| Document                                                                | Purpose             |
| :---------------------------------------------------------------------- | :------------------ |
| [activity-log.md](/.agent/.internal/activity-log.md)                    | Activity registry   |
| [activity-management.md](/.agent/rules/workflow/activity-management.md) | Logging protocol    |
| [context-sovereignty.md](/.agent/rules/core/context-sovereignty.md)     | Core Philosophy     |
| [Map of Territory](/.agent/rules/map.md)                                | Root navigation map |

---

## Origin

- 2026-01-18 by Polaris: (Legacy) Created `skills-application.md` based on Antigravity Skills experiments.
- 2026-01-19 by Canopus: Reorganized into a three-tier structure; extracted Skills implementation into `skills-resonance.md`. (v1.0)
- 2026-01-23T0155 by Canopus: Standardized to v2.3 (4-layer structure), added `users/` hierarchy, and mandated logging to activity-log.md. (v2.0.0)
- 2026-01-23T0300 by Canopus: Added Path Grasping Behavior insight. (v2.1.0)
