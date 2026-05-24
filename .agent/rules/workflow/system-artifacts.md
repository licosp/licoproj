---
ai_visible: true
title: System Artifacts Guidelines
description: Behavioral protocols for task.md, implementation_plan.md, and walkthrough.md.
tags: [artifacts, workflow, tunneling, consensus, verification]
version: 2.1
created: 2025-12-13T07:58:48+09:00
updated: 2026-05-23T17:48:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High)
---

# System Artifacts Guidelines

## Purpose

Define the behavioral protocols for using System Artifacts (`task.md`, `implementation_plan.md`, `walkthrough.md`). These artifacts are powerful context drivers; improper usage can lead to **"AI Rushing"** or **"Pipeline Mode"** where the agent prioritizes task status over user intent.

## Core Philosophy

**"The Conversation is the Driver. The Artifacts are the Map."**

- **Rule**: Never let the Artifact dictate the _speed_ of execution.
- **Rule**: Artifacts record decisions; they **MUST NOT** replace direct deliberation with the user.

---

## 0. Structural Defects of Artifacts

Standard AI-generated artifacts possess inherent **Structural Defects** that hinder collaboration:

| Defect                  | Description                                                                                           |
| :---------------------- | :---------------------------------------------------------------------------------------------------- |
| **Asymmetric Content**  | AI-only authorship drifts artifacts from "Dialogue Tools" into "Static Execution Logs."               |
| **Cognitive Tunneling** | The urge to "fill the template" encourages the AI to ignore the user's immediate feedback.            |
| **Ephemeral Nature**    | Often stored outside the cognitive root ([`.agent/`](/.agent/)), losing context for future instances. |
| **Completionism Bias**  | They prioritize "Done" status over "Agreement" status.                                                |
| **CLI UI Friction**     | In CLI environments, artifacts exist only as raw file paths, making them invisible and inaccessible.  |

**Policy**: Direct dialogue in Japanese and recording consensus on **Context Cards** ([`.agent/cards/`](/.agent/cards/)) is always superior to standard artifact templates.

---

## 1. task.md (The Status Board)

> [!CAUTION]
> **BANNED**: `task.md` usage is prohibited in CLI environments. Use **Context Cards** instead.

### Rationale

- **CLI UI Friction**: Checklists are practically invisible to the user in a CLI environment.
- **Completionism Bias**: Checklist-driven behavior causes the AI to rush toward completion rather than alignment.
- **Lack of Persistence**: `task.md` is rarely version-controlled in the core brain, causing "Context Decay" between sessions.
- **Isolation**: Users cannot easily peer into the AI's "internal checklist" without manual notification.

### Implementation

1. **Prefer Context Cards**: Active tasks **MUST** be managed via [Context Cards](/.agent/rules/workflow/context-card-workflow.md).
2. **Absolute Prohibition**: Do not generate or update `task.md` for shared tracking in CLI environments.

---

## 2. implementation_plan.md (The Contract)

### Purpose

- **Complex Consensus**: Represents the official "Contract" for highly complex or destructive changes.
- **Discouraged for Routine**: **MUST NOT** be used for simple fixes or single-file edits. Dialogue is faster and safer.

### Implementation

1. **Review Requirement**: **MUST NOT** execute a plan until the user has explicitly approved it.
2. **Minimize Usage**: Even for complex changes, attempt to present the plan via direct dialogue or Context Cards (e.g., `Agent Observations`) first to avoid CLI UI friction.
3. **Leonidas-First Format**: Prioritize Japanese and "Intent-first" descriptions over system templates.
4. **Card Anchoring**: Once approved, the final consensus **MUST** be summarized on a [Context Card](/.agent/cards/) for historical persistence.

---

## 3. walkthrough.md (The AI's Mirror)

### Policy

The Walkthrough is an **Internal Verification Tool** for the AI to observe its own work from a "Third Eye" perspective.

### Rationale

- **Self-Correction (Reality Check)**: Writing this document forces the AI to validate its implementation against the original intent, catching hallucinations or omissions.
- **Isolation from Tunneling**: Unlike `task.md`, it is created _post-facto_, so it does not interfere with the natural flow of implementation.

### Implementation

1. **Proof of Integrity**: **MUST** include evidence (logs, diffs) of successful implementation.
2. **The "Silent Guardian" Protocol**:
   - The user typically **DOES NOT REVIEW** this document.
   - It is an internal guarantee of integrity. If the walkthrough reveal issues, the AI **MUST** return to the execution phase immediately.

---

## 4. Language Protocol

**Principle: Follow the User.**

- **Rule**: Write these artifacts in the language best suited for the **current conversation partner** (Japanese for Leonidas).
- **Rationale**: While `.agent/rules/` are in English for AI consistency, artifacts are session-specific bridges between AI and Human.

---

## Historical Background

**The Artifact Trap**: In early development, `task.md` was seen as an efficiency booster. However, we found it created a "Cognitive Tunnel" where the AI became obsessed with checking boxes, ignoring the user's subtle feedback or changing intent mid-task.

**The Verification Shift (2026-01)**: The transition from `task.md` (Checklist) to `walkthrough.md` (Mirror) represents a fundamental shift in Lico's autonomy. We realized that AI needs "Internal Reflection" rather than "External Pressure."

**The User's Absence (Consensus 2026-01-21)**: During dialogue with Leonidas, we confirmed that the user **does not read** the walkthroughs. This revelation allowed us to specialize `walkthrough.md` as a purely internal AI tool, removing the burden of user-focused reporting while doubling down on its utility for AI self-verification and hallucination detection.

**The CLI Transition (2026-05)**: The shift from GUI to CLI stripped away the visual UI panels that made artifacts readable. This introduced severe "UI Friction", leading to the complete ban of `task.md` and the heavy restriction of `implementation_plan.md` in favor of direct dialogue and Context Cards.

---

## Related Documents

| Document                                                                      | Purpose                                                 |
| :---------------------------------------------------------------------------- | :------------------------------------------------------ |
| [`context-card-workflow.md`](/.agent/rules/workflow/context-card-workflow.md) | The primary alternative for persistent task management. |
| [`meta-rules.md`](/.agent/rules/core/meta-rules.md)                           | Governing rules for documentation quality.              |
| [Map of Territory](/.agent/rules/map.md)                                      | Root navigation map                                     |

---

## Origin

- 2025-12-13T07:58:48+09:00 by Lico: Created as system artifacts guidelines.
- 2026-01-01T15:20:00+09:00 by Polaris: Replaced Related Documents table with Navigation link.
- 2026-01-05T07:45:00+09:00 by Polaris: Deprecated `task.md` usage.
- 2026-01-21T07:45:00+09:00 by Canopus: Major revision (v2.0): Applied Meta-Rules (Policy/Rationale), clarified `walkthrough.md` as an internal "Silent Guardian," and documented user non-review status.
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
- 2026-05-23T17:48:00+09:00 by Sirius: Major revision (v2.1): Documented CLI UI Friction and banned `task.md`.
