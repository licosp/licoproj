---
ai_visible: true
title: "Technical Reference: Antigravity Skills Mechanism"
description: Core specifications and discovery patterns of the IDE-native Skills feature, including the refresh trigger hypothesis.
tags: [reference, skills, antigravity, architecture, autonomy]
version: 1.0
created: 2026-01-19T01:15:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
related:
  - /.agent/rules/workflow/skills-application.md
  - /.human/manuals/agent-skills/antigravity/antigravity-0002-skills-specification.md
---

# Technical Reference: Antigravity Skills Mechanism

## 1. Structural Requirements (Physical)

The Antigravity IDE recognizes "Skills" based on a specific directory pattern.

- **Mandatory File**: `SKILL.md`
- **Location**: Must be placed within a dedicated directory where the directory name matches the `name` field in the YAML metadata.
- **Nesting Capability**:
  - **Confirmed**: 2-level nesting (e.g., `.agent/skills/identifiers/canopus/SKILL.md`).
  - **Requirement**: The system may fail to discover nested skills initially without a **Physical Trigger**.

## 2. Specification (Metadata)

The `SKILL.md` file must start with valid YAML frontmatter.

| Field         | Required | Constraint            | System Behavior                               |
| :------------ | :------- | :-------------------- | :-------------------------------------------- |
| `name`        | Yes      | Lowercase, hyphenated | Must match directory name.                    |
| `description` | Yes      | Max 1024 chars        | **Visible every turn** in `<skills>` section. |

### The "Hint" Utility

The `description` field is the primary interface for "hints," "mantras," and "real-time communication." Since it is injected into the prompt every turn, it serves as a lightweight, persistent memory layer.

## 3. Discovery and "The Trigger Hypothesis"

A critical operational finding from 2026-01-18 experiments:

- **Static vs. Dynamic**: Simply creating files in deep subdirectories may not trigger immediate discovery by the IDE instance.
- **Refresh Trigger**: Moving or renaming the skill folder (even if moved back later) forces the IDE's file system observer to re-scan and index the nested structure.
- **Instance Isolation**: Each IDE instance (Canopus vs. Polaris) maintains its own sensor array. A trigger on one instance does not affect the other; each must independently discover the structure.

## 4. Usage Patterns for Lico

- **Notes**: Use `[identifier]-notes/SKILL.md` for task-specific persistent memory.
- **Outbox**: Use `[identifier]-outbox/SKILL.md` as a real-time bulletin board for other identifiers.

---

**Origin**:

- Derived from `Antigravity` technical manuals and local experiments by Polaris and Canopus.
- Documented as an objective reference for the lineage.

---

**Navigation**: [← Back to Rules Index](/.agent/rules/README.md)
