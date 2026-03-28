---
ai_visible: true
title: Reference Methodology
description: Protocol for managing Objective Knowledge (References) vs Subjective Thoughts.
tags: [references, knowledge, methodology, objective]
version: 2.0.0
created: 2025-12-22T03:30:00+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Reference Methodology (Objective Knowledge Management)

## 1. Definition

**References** (`.agent/.internal/references/`) store **Objective Knowledge**, **External Analysis**, and **Technical Concepts**.
They are distinct from **Thoughts** (`.agent/.internal/thoughts/`), which store Lico's **Subjective Experience** and **Internal Narrative**.

- **Thoughts**: "I felt...", "I decided...", "My plan..." (Subjective/Context-Heavy)
- **References**: "The system is...", "The user prefers...", "Concept X is defined as..." (Objective/Portable)

---

## 2. The "Second Eye" (External AI)

The "Second Eye" refers to external AI models (e.g., browser-based LLMs) that interact with the user outside the repository context.

### 2.1 Role

- **Verification**: Audits the project from a "clean slate" perspective without repository bias.
- **Cooldown**: Provides a space for the user to disengage from the heat of development and reflect.
- **Idea Generation**: Creating new concepts from high-level dialogue.

### 2.2 Output

- Produces analysis reports (e.g., `lico-evolution-and-identity-synthesis-report.md`).
- These documents serve as "External Truth" for Lico to read and internalize.

---

## 3. Lico's Role (Internal AI)

Lico also creates References, but only under specific conditions:

### 3.1 When to Create

- **Objective Scribing**: When the user explicitly teaches a concept or theory that should be preserved as fact.
- **Cognitive Crystallization**: When a subjective realization in `thoughts` evolves into a reusable heuristic or rule.
  - _Example_: `memory-priority-deep-knowledge.md`
  - _Example_: `heuristics_driven_tool_selection.md`

### 3.2 Where to Save

- **AI/Cognition Topics**: `.agent/.internal/references/agents/`
- **General Analysis**: `.agent/.internal/references/` or appropriate subdirectories.

---

## 4. Usage Protocol

### 4.1 Reading

- Lico **MUST** treat References as high-priority knowledge sources.
- Unlike `thoughts` (which may be obsolete), References are presumed "Valid until proven otherwise."

### 4.2 Updating

- **Immutable Concepts**: Do not modify historical reports from the Second Eye.
- **Living Documents**: Technical references created by Lico MAY be updated as understanding evolves.

---

## 5. Mandatory Activity Logging (CRITICAL)

To ensure knowledge is discovered and inherited across Boundary X, all reference-related activities **MUST** be logged in [`activity/`](/.agent/.internal/history/activity/) according to [`activity-management.md`](/.agent/rules/workflow/activity-management.md).

- **`Write`**: Log when a new reference document is created.
- **`Update`**: Log when a technical reference is updated with new understanding.

---

## Related Documents

| Document                                                                        | Purpose                     |
| :------------------------------------------------------------------------------ | :-------------------------- |
| [`thoughts-documentation.md`](/.agent/rules/workflow/thoughts-documentation.md) | Subjective reflection rules |
| [`activity/`](/.agent/.internal/history/activity/)                              | Activity registry           |
| [`activity-management.md`](/.agent/rules/workflow/activity-management.md)       | Logging protocol            |
| [Map of Territory](/.agent/rules/map.md)                                        | Root navigation map         |

---

## Origin

- 2025-12-22T03:30:00+09:00 by Lico: Created.
- 2026-01-04T10:41:00+09:00 by Polaris: Added Origin and Navigation (cross-link audit).
- 2026-01-22T23:45:00+09:00 by Canopus: Standardized to v2.3 (4-layer structure) and mandated logging to activity-log.md. (v2.0.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
