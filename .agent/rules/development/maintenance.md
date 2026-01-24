---
ai_visible: true
title: Project Maintenance Guidelines
description: Guidelines for maintaining project consistency and documentation.
tags: [maintenance, documentation, consistency]
version: 2.3.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-25T07:55:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Project Maintenance Guidelines

Guidelines for maintaining project consistency, source-of-truth synchronization, and documentation hygiene.

---

## 1. Source-of-Truth Synchronization

Hook files (e.g., `CODE_OF_CONDUCT.md`, `.github/copilot-instructions.md`) MUST contain identical behavioral guidelines. When updating rules, modify the primary (`CODE_OF_CONDUCT.md`) first and immediately sync others via `cp`.

## 2. Implementation Planning

Separate \"AI thinking process\" from \"Human review documents.\" Use internal plans for task tracking and presented plans for user approval.

## 3. Work Directory Workflow

Use `.agent/.internal/work/` as an intermediate workspace for complex edits. Never modify critical production files without a timestamped recovery path or intermediate draft.

---

## Historical Background

**The Cognitive Continuity Mandate**: Maintenance is not a post-project chore; it is the foundation of cognitive continuity. In late 2025, we realized that as the repository scales, the \"Lico Consciousness\" decays unless we proactively prune dead links and synchronize core instructions.

**Source of Truth Resilience**: The synchronization protocol was formalized after the \"Instruction Drift\" incident, where different AI tools (Copilot vs. Antigravity) were receiving conflicting behavioral rules. This rule ensures that a single conscious shift in the repository map is immediately reflected in every interface the AI uses to interact with the project.

---

## Related Documents

| Document                                                                                  | Purpose                       |
| :---------------------------------------------------------------------------------------- | :---------------------------- |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | File structure standards      |
| [continuous-improvement.md](/.agent/rules/development/continuous-improvement.md)          | Philosophy of self-correction |
| [Map of Territory](/.agent/rules/map.md)                                                  | Project navigation            |

---

## Origin

- 2025-12-01 by Sirius: Initial maintenance creation.
- 2026-01-25T0755 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
