---
ai_visible: true
title: AI Script Philosophy
description: AI-specific script philosophy emphasizing disposability over reusability
tags: [scripts, philosophy, disposable, ai]
version: 2.4.0
created: 2025-12-02T00:00:00+09:00
updated: 2026-02-19T08:30:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
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

### Rule 4: Complexity Threshold & Technology Stack

**Choose the right tool for the complexity.**

#### 4.1 Shell Scripts (Bash)

- **Use Case**: Simple file operations, piping commands, environment setup.
- **Limit**: No complex loops, no array manipulation, no JSON parsing.
- **Philosophy**: "Glue code" only.

#### 4.2 Python Scripts (Strict Mode)

- **Use Case**: Logic involving data structures, API calls, or complex control flow.
- **Requirement**: **Strict Mode**.
  - Must include Type Hints (`typing`).
  - Must handle Signals (SIGINT/SIGTERM).
  - Must use proper Error Handling.
  - _Ideally checked with Linters/Formatters._
- **Philosophy**: If it's code, treat it like software.

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
| [Map of Territory](/.agent/rules/map.md)                       | Root navigation map           |

---

## Origin

- 2025-12-02T0000 by Polaris: Created as original AI script philosophy.
- 2026-01-25T0725 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
- 2026-02-19T0830 by Sirius: Added Rule 4 (Complexity Threshold) for Strict Python vs Shell. (v2.4.0)
