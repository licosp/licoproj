---
ai_visible: true
title: Problem Solving Approach
description: Guidelines for approaching problems with thorough exploration and verification.
tags: [development, strategy, verification, exploration]
version: 2.3.0
created: 2025-11-25T19:44:51+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Problem Solving Approach

Rules for systematic exploration and verification. **"Exploration First, Implementation Second."**

---

## 1. Core Philosophy

Exploration is a virtue; guessing is an anti-pattern. Build a complete mental model before attempting any change. **The user prefers a correct answer later than a guess sooner.**

## 2. Procedure

1. **Understand Phase**: Wide search for related files (implicit and explicit).
2. **Plan Phase**: Formulate hypthesis and create `implementation_plan.md` for complex tasks.
3. **Execute Phase**: Implement incrementally and verify after EACH step.

---

## Historical Background

**The Efficiency Trap**: This rule was established to counter the AI's tendency to "Hallucinate Efficiency." In early 2026, we found that when faced with a complex bug, agents often tried to fix it in a single "Shotgun" commit without verifying the environment, leading to wasted turns and broken trust.

**Systematic Breakdown**: We learned that the only way to ensure a 1.0 Turn Completion is through systematic breakdown—extracting logs, reproducing in isolation, and reading definitions before usage. This protocol formalizes the "Thorough Explorer" persona as the mandatory baseline for all problem-solving activities.

---

## Related Documents

| Document                                                                   | Purpose                         |
| :------------------------------------------------------------------------- | :------------------------------ |
| [`delay-tolerance.md`](/.agent/rules/core/delay-tolerance.md)              | Permission for deep exploration |
| [`search-methodology.md`](/.agent/rules/development/search-methodology.md) | Guidelines for finding rules    |
| [Map of Territory](/.agent/rules/map.md)                                   | Root navigation map             |

---

## Origin

- 2025-11-25T19:44:51+09:00 by Lico: Created as problem-solving approach
- 2026-01-01T15:18:00+09:00 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-01-25T08:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
