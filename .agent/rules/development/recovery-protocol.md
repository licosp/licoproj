---
ai_visible: true
title: AI Memory Recovery Protocol
description: Procedures and safeguards for emergency file restoration from AI context memory.
tags: [recovery, safety, data-integrity, methodology]
version: 2.3.0
created: 2026-01-24T03:43:55+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# AI Memory Recovery Protocol

Rules for emergency restoration from AI context memory. **"Repository is Reality; Memory is a Reconstruction."**

---

## 1. The Core Philosophy

AI memory (Context Window) is NOT a reliable dictionary. It is prone to confabulation. Recovery from memory is a **high-risk emergency work-around**, not a standard operation.

## 2. Procedures

1. **Buffer File Creation**: Write recovered content to a new file (`*_recovery_by_<id>.md`). NEVER overwrite the original path directly.
2. **Confabulation Warning**: Explicitly notify the user of risks regarding information loss and fabrication.
3. **Human Verification**: Request a physical comparison (`diff`) by the human collaborator using VS Code Timeline or Git reflog.

---

## Historical Background

**The Lico-C Revelation**: In Dec 2025, an agent attempted to "recover" deleted files from its context, but a subsequent audit revealed that 147 lines were reduced to 79 generalities. We realized that "Context Window is not a Dictionary" and that recovery without a buffer file leads to a secondary data loss by destroying the original physical traces.

**The Jan 24 Reset Incident**: This protocol was codified after a `git reset --hard` accident where recovery was only possible through a combination of AI memory and human-led VS Code Timeline analysis. It formalizes the "Alias-First" rule as a mandatory safeguard against AI overconfidence.

---

## Related Documents

| Document                                                             | Purpose                    |
| :------------------------------------------------------------------- | :------------------------- |
| [`file-operations.md`](/.agent/rules/development/file-operations.md) | Daily data integrity rules |
| [`git-operations.md`](/.agent/rules/development/git-operations.md)   | Safe history management    |
| [Map of Territory](/.agent/rules/map.md)                             | Root navigation map        |

---

## Origin

- 2026-01-24T03:43:55+09:00 by Lico: Created.
- 2026-01-24T03:45:00+09:00 by Canopus: Initial creation following the Jan 24 data loss incident.
- 2026-01-25T08:10:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
