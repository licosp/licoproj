---
ai_visible: true
title: Search Methodology
description: Protocols for searching, filtering, and retrieving information in an infinite-scale repository.
tags: [development, search, retrieval, methodology, overflow]
version: 2.3.0
created: 2025-12-18T02:00:00+09:00
updated: 2026-01-25T08:15:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Search Methodology

Protocols for effective retrieval. **\"The result of a search is NEVER a File; it is ALWAYS a Candidate List.\"**

---

## 1. Core Philosophy

Treat search output as a list of candidates. Avoid \"Scalar Thinking\" (assuming the first or only result is the final answer). Always check for truncation or overflow.

## 2. The Universal Search Loop

1.  **Discovery**: Run tools; check for **Overflow**. If truncated, query is unreliable.
2.  **Filter**: Assess Signal-to-Noise. If too noisy, proced to Strategic Retreat.
3.  **Refine (Strategic Retreat)**: Abandon broad queries; use precise keyword or narrow scope.
4.  **Help Seeking**: If the loop repeats 3 times without SUCCESS, notify the user.

---

## Historical Background

**The Truncation Blindness**: This protocol was established to solve the "Overflow Trap" of early 2026. During the initial rule audits, agents frequently missed critical files because the `find` or `grep` result hit the tool limit (50 matches).

**Strategic Silence**: We learned that a partial search is often more dangerous than no search at all, as it invites false confidence. By mandating the "Strategic Retreat" and "Help Seeking" patterns, we ensure that Lico acknowledges the limits of its current visibility instead of making decisions based on fragmented data.

---

## Related Documents

| Document                                                                    | Purpose                             |
| :-------------------------------------------------------------------------- | :---------------------------------- |
| [problem-solving.md](/.agent/rules/development/problem-solving.md)          | \"Exploration First\" guidelines    |
| [hallucination-awareness.md](/.agent/rules/core/hallucination-awareness.md) | Risk of assumption-based navigation |
| [Map of Territory](/.agent/rules/map.md)                                    | Project navigation                  |

---

## Origin

- 2025-12-18 by Polaris: Initial search methodology creation.
- 2026-01-25T0815 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
