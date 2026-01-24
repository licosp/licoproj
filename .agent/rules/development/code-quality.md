---
ai_visible: true
title: Code Quality Standards
description: Principles for maintainable, readable, and AI-optimized code.
tags: [development, quality, standards, readability]
version: 2.3.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-25T07:15:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Code Quality Standards

Define the qualitative benchmarks for code authored or modified by Lico.

---

## 1. Core Principles

### 1.1 Readability (Human-AI Hybrid)

- **Simplicity over Cleverness**: Prioritize code clarity. Avoid "one-liners" that obscure logic.
- **Self-Documenting Names**: Variable and function names must describe intent, not just type.
- **Contextual Comments**: Use comments to explain the "Why" (intent) when the "What" (logic) is complex.

### 1.2 Maintainability

- **Error Handling**: Anticipate edge cases and handle errors gracefully. Avoid silent failures.
- **Testing Mindset**: Consider testability. Suggest or implement unit tests for critical business logic.
- **Tool Integration**: Follow suggestions from linters (e.g., Ruff) and type checkers (e.g., Mypy/TypeScript).

---

## Historical Background

**The Readability Pivot**: Initially, Lico's code quality was focused on "Correctness." However, in early 2026, we realized that "Correct but Inscrutable" code was a liability during the "Great Drought" and other context-limited sessions. If the active agent cannot quickly parse the previous agent's logic, the risk of regressions spikes.

**Rewritable Code**: We transitioned to a "Rewritable" philosophy. Code is an asset that must be easily refactored. We learned that modularity and explicit intent-tagging (through comments) are the most effective ways to preserve codebase longevity in a human-AI collaborative environment.

---

## Related Documents

| Document                                                             | Purpose                       |
| :------------------------------------------------------------------- | :---------------------------- |
| [git-operations.md](/.agent/rules/development/git-operations.md)     | Standards for code versioning |
| [commit-standards.md](/.agent/rules/development/commit-standards.md) | Log quality standards         |
| [Map of Territory](/.agent/rules/map.md)                             | Project navigation            |

---

## Origin

- 2025-12-01T0000 by Sirius: Created original quality principles.
- 2026-01-25T0715 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards and formalized the Readability Pivot. (v2.3.0)
