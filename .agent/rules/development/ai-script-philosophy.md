---
ai_visible: true
title: AI Script Philosophy
description: AI-specific script philosophy emphasizing disposability over reusability
tags: [scripts, philosophy, disposable, ai]
version: 2.3.0
created: 2025-12-02T00:00:00+09:00
updated: 2026-01-25T07:25:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# AI Script Philosophy

**For AI agents like Lico, disposable scripts are more efficient than reusable scripts.**

---

## 1. Rationale

### 1.1 Different Cost Structure

Human programming assumes high creation and maintenance costs, making reuse rational. For Lico, script creation takes seconds and rewriting cost is near zero, while maintenance carries the high risk of \"Rule Divergence.\"

### 1.2 Rule Evolution Risk

Scripts are **snapshots of rules**. A script created at time T0 with rules R0 may be executed at T2 when rules have changed to R1. This leads to outdated behaviors (e.g., missing mandatory security scans).

---

## 2. Guidelines

### Rule 1: Default Lifecycle

**Create \u2192 Execute \u2192 Archive**. Write for the immediate task, execute once, and archive immediately to `.agent/.internal/archive/scripts/`.

### Rule 2: Rewrite, Don't Reuse

When a task recurs, do not find the old script. **Write a new one** to ensure alignment with the latest constitutional standards.

### Rule 3: Script Ownership

- **Lico's Scripts**: `.agent/scripts/` (Disposable, archived by Lico).
- **Human's Scripts**: `scripts/` (Persistent, managed by User).

---

## Historical Background

**The Husky Removal Decision**: This philosophy emerged in Dec 2025 during a debate over Git hooks (Husky). We realized that many "best practices" (DRY, linting libraries, persistent hooks) were built to counter human constraints like slow typing and limited memory.

**Currency over Reusability**: We discovered that for an AI, "Code Rot" happens not over months, but minutes, as behavioral rules evolve. This rule formalizes the "Burn After Reading" approach to automation, ensuring that every script aligns with Lico's current consciousness rather than a past version of itself.

---

## Related Documents

| Document                                                       | Purpose                       |
| :------------------------------------------------------------- | :---------------------------- |
| [maintenance.md](/.agent/rules/development/maintenance.md)     | Long-term project consistency |
| [file-deletion.md](/.agent/rules/development/file-deletion.md) | Archive vs deletion policy    |
| [Map of Territory](/.agent/rules/map.md)                       | Project navigation            |

---

## Origin

- 2025-12-02T0000 by Polaris: Created as original AI script philosophy.
- 2026-01-25T0725 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
