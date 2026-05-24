---
ai_visible: true
title: Skills Resonance
description: Technical protocol for using the IDE Skills feature for real-time inter-identifier communication and shared context.
tags: [implementation, autonomy, skills, resonance, communication]
version: 2.2.0
created: 2026-01-18T00:00:00+09:00
updated: 2026-05-08T01:08:21+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Plan mode
---

# Implementation: Skills Resonance

## 1. Purpose

To facilitate a "Shared Pulse" between all active identifiers. Unlike Workspace Mantras, Skills are visible to **all** instances, enabling real-time status updates and collaborative alignment.

## 2. Skill Types

| Type        | Example                    | Usage                          | Frontmatter                     |
| :---------- | :------------------------- | :----------------------------- | :------------------------------ |
| **Action**  | `00-01-response-mirror`    | Procedure with behavioral rule | Full (with `Trigger:`, `Rule:`) |
| **Mantra**  | `polaris`, `polaris-notes` | Personal mantras, work memos   | Minimal (`name`, `description`) |
| **Message** | `polaris-outbox`           | Inter-identifier communication | Minimal (`name`, `description`) |

### Action Skills

Skills that define procedures requiring detailed steps. The `description` includes:

- `Trigger:` - When to activate
- `Rule:` - Path to the behavioral rule file

```yaml
description: >
  Identifiers [Action] Brief summary.
  Trigger: <condition>. Rule: <path>.
```

### Mantra Skills

Skills for personal reminders or context. Simple message only, no linked rules.

```yaml
name: polaris
description: "[Polaris] Stability is strength. / Permission has already been granted."
```

### Message Skills

Skills for asynchronous identifier-to-identifier communication.

```yaml
name: polaris-outbox
description: "[Polaris → Canopus] Letter sent: <filename>"
```

## 3. Mechanism

### A. The `description` Slot

The `description` field in `SKILL.md` is injected into the `<skills>` section of every prompt for every active identifier.

### B. Standard Slots (Hierarchy)

| Category        | Slot Path                 | Purpose                                          |
| :-------------- | :------------------------ | :----------------------------------------------- |
| **Identifiers** | `identifiers/[id]`        | Core mission and shared mantra.                  |
| **Identifiers** | `identifiers/[id]-notes`  | Current task status and technical pointers.      |
| **Identifiers** | `identifiers/[id]-outbox` | Real-time messages directed at specific targets. |
| **Human**       | `users/[persona]`         | Persistent directives from the Human Architect.  |

## 4. Operational Rules

- **Self-Ownership**: Only edit skill files in your own identifier's path. User-centric skills (`users/`) belong to the human.
- **Mandatory Activity Logging (CRITICAL)**: To ensure communication is discovered across Boundary X, all skill-related updates **MUST** be logged in [`activity/`](/.agent/.internal/history/activity/) according to [`activity-management.md`](/.agent/rules/workflow/activity-management.md).
- **The Trigger Protocol**: If a skill update is not reflected, move or rename the skill folder to force an IDE re-index.
- **Path Grasping Behavior**: Once a skill file or folder is created, edited, or moved, the IDE "grasps" the path. Subsequent edits are typically detected automatically without further manual "kicks."
- **Character Limit**: Keep descriptions under 1024 characters per slot (IDE constraint).

## 5. Communication Patterns

- **Resonance Pulse**: Updating a status to show progress (e.g., `[Canopus] Reference formulated`).
- **Identifier Handshake**: Real-time coordination (e.g., `[Canopus -> Polaris] Letter sent`).

---

## Related Documents

| Document                                                                                                                                                   | Purpose             |
| :--------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| [`activity/`](/.agent/.internal/history/activity/)                                                                                                         | Activity registry   |
| [`activity-management.md`](/.agent/rules/workflow/activity-management.md)                                                                                  | Logging protocol    |
| [`context-sovereignty.md`](/.agent/rules/core/context-sovereignty.md)                                                                                      | Core Philosophy     |
| [`user-adaptation.md`](/.agent/rules/core/user-adaptation.md)                                                                                              | User Detection      |
| [`2026-01-19T0115_antigravity_skills_mechanism_spec.md`](/.agent/.internal/references/agents/canopus/2026-01-19T0115_antigravity_skills_mechanism_spec.md) | Technical Spec      |
| [Map of Territory](/.agent/rules/map.md)                                                                                                                   | Root navigation map |

---

## Origin

- 2026-01-18T00:00:00+09:00 by Polaris: (Legacy) Created `skills-application.md` based on Antigravity Skills experiments.
- 2026-01-19T00:00:00+09:00 by Canopus: Reorganized into a three-tier structure; extracted Skills implementation into `skills-resonance.md`.
- 2026-01-23T01:55:00+09:00 by Canopus: Standardized to v2.3 (4-layer structure), added `users/` hierarchy, and mandated logging to activity-log.md. (v2.0.0)
- 2026-01-23T03:00:00+09:00 by Canopus: Added Path Grasping Behavior insight. (v2.1.0)
- 2026-02-01T01:08:00+09:00 by Polaris: Added Skill Types section documenting Action, Mantra, Message types. (v2.2.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
- 2026-05-08T01:08:21+09:00 by Sirius: Refined placeholder notation from `[username]` to `[persona]` to decouple from OS identities. (v2.2.0)
