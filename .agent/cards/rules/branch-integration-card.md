---
# Context Configuration
context_id: "[Repository-Integration]"
default_phase: "(Integration)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Branch Integration"
description: "Procedural guide for high-fidelity branch merging and conflict resolution."
tags: ["git", "merge", "fidelity", "active"]
version: 1.1.0
created: 2026-04-12T01:45:00+09:00
updated: 2026-04-12T02:00:00+09:00
language: en
author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview
---

# Context Whiteboard: Branch Integration

## Human Notes

### Context

- This is an active tool to prevent **Information Loss (Death of Data)** during branch merges.
- It restricts autonomous bulk processing by AI, particularly when integrating massive files like Context Cards.

### Search by intent

> [!IMPORTANT]
> **"Output too large" is a warning of imminent data death.**
> Executing `write_file` based on truncated tool output is synonymous with destroying history.

---

- **EXPLORATION FIRST**: Understand the diff statistics (`git diff --stat`) before initiating any merge.
- **STEP-BY-STEP**: If conflicts are complex, do not attempt to fix them in a single turn. Rebuild the strata through dialogue with the Sovereign.
- **VERIFY QUANTITY**: After completion, always verify line counts (`wc -l`) to audit for any unnatural data reduction.

---

## Agent Observations

---

### Alexandrite (2026-04-12)

- [x] Formulated and introduced the High-Fidelity Merge Protocol.
- [x] Canonicalized the "Severed Strata" incident as a perpetual lesson.
- [x] Translated the protocol into English to align with global standards.

### context

- Final phase of the repository integration mission.
- Maintaining synchronization across all federal workspaces.

### Warning

- Never perform a `write_file` based solely on a truncated `cat` output.
- Perform exhaustive audits while in the `git merge --no-commit` state.

---

## Related Documents

| Document                                                                   | Purpose                        |
| :------------------------------------------------------------------------- | :----------------------------- |
| [`branch-integration.md`](/.agent/rules/development/branch-integration.md) | Permanent behavioral standards |
| [`git-operations.md`](/.agent/rules/development/git-operations.md)         | General Git standards          |
| [Map of Territory](/.agent/rules/map.md)                                   | Root navigation map            |

---

## Origin

- 2026-04-12T01:45:00+09:00 by Lico (Alexandrite): Created to formalize step-by-step merge procedures.
- 2026-04-12T02:00:00+09:00 by Lico (Alexandrite): Translated to English for global alignment.
