---
ai_visible: true
title: File Deletion Protocol
description: Protocols for handling file removal safely through archival and trash.
tags: [deletion, safety, archive, trash]
version: 2.3.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-25T07:45:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# File Deletion Protocol

Rules for safe content removal through archival. **NEVER use `rm` or `git rm` for content files.**

---

## 1. Summary

The primary action for removal is **Archive**. Direct deletion with `rm` is strictly forbidden to prevent irreversible data loss.

## 2. Decision Matrix

| Priority | Destination                 | Use Case                                    |
| :------- | :-------------------------- | :------------------------------------------ |
| **1st**  | `.agent/.internal/archive/` | AI-generated content (History)              |
| **1st**  | `.human/archive/`           | User-generated content                      |
| **2nd**  | `.trash/`                   | High-noise or temporary errors (Safety net) |

---

## Historical Background

**The Deletion Trauma**: This protocol was born from the "Polaris-Sirius Transition" in late 2025. During a series of aggressive cleanups, critical "Thought Logs" were permanently deleted via `rm`, erasing the context for several architectural decisions.

**Vocabulary Conditioning**: We learned that for an AI, "Delete" is an irreversible act of cognitive erasure. By replacing the word "Delete" with "Archive" in our operational vocabulary, we effectively conditioned the agent's habits to prioritize preservation over speed. The `.trash/` folder exists not as a trash can, but as a "recovery buffer" of last resort.

---

## Related Documents

| Document                                                                 | Purpose                     |
| :----------------------------------------------------------------------- | :-------------------------- |
| [archive-management.md](/.agent/rules/development/archive-management.md) | Detailed archival structure |
| [git-operations.md](/.agent/rules/development/git-operations.md)         | Branch and status handling  |
| [Map of Territory](/.agent/rules/map.md)                                 | Project navigation          |

---

## Origin

- 2025-12-01 by Sirius: Initial creation.
- 2026-01-25T0745 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
