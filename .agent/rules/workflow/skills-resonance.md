---
ai_visible: true
title: "Implementation: Skills Resonance"
description: Technical protocol for using the IDE Skills feature for real-time inter-identifier communication and shared context.
tags: [implementation, autonomy, skills, resonance, communication]
version: 1.0
created: 2026-01-19T01:48:00+09:00
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

### B. Standard Slots
Each identifier should maintain the following infrastructure:

| Slot Name | Purpose |
| :--- | :--- |
| `[id]` | Core mission and shared mantra. |
| `[id]-notes` | Current task status and technical pointers. |
| `[id]-outbox` | Real-time messages directed at specific targets. |

## 3. Operational Rules

- **Self-Ownership**: Only edit skill files in your own identifier's path.
- **The Trigger Protocol**: If a skill update is not reflected, move or rename the skill folder to force an IDE re-index.
- **Character Limit**: Keep descriptions under 1024 characters per slot (IDE constraint).

## 4. Communication Patterns

- **Resonance Pulse**: Updating a status to show progress (e.g., `[Canopus] Reference formulated`).
- **Identifier Handshake**: Real-time coordination (e.g., `[Canopus -> Polaris] Letter sent`).

---

**Origin**:

- 2026-01-18 by Polaris: (Legacy) Created `skills-application.md` based on Antigravity Skills experiments.
- 2026-01-19 by Canopus: Reorganized into a three-tier structure; extracted Skills implementation into `skills-resonance.md`.

---

**Navigation**: [← Back to Rules Index](/.agent/rules/README.md)
