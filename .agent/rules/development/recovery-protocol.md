---
ai_visible: true
title: AI Memory Recovery Protocol
description: Procedures and safeguards for emergency file restoration from AI context memory
tags: [recovery, safety, data-integrity, methodology]
version: 1.0.0
created: 2026-01-24T03:45:00+09:00
updated: 2026-01-24T03:45:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# AI Memory Recovery Protocol

## Purpose

To establish a safe procedure for restoring file content from AI context memory during emergency "Cognitive Erasure" events (e.g., accidental `git reset --hard` or lost uncommitted edits).

> [!CAUTION]
> **Context is Volatile Short-Term Memory.**
> AI memory (Context Window) is NOT a reliable dictionary. It is prone to **Confabulation** (fabrication), **Information Loss**, and **Generalization**. Never trust a memory-based restoration as a 1:1 replacement for physical repository history.

---

## 1. The Core Philosophy

**"Repository is Reality."**

Your memory is a reconstruction, not a record. The repository's files are the only source of truth. Recovery from memory is a **high-risk emergency work-around**, not a standard operation.

---

## 2. Recovery Procedures (Alias-First)

### 2.1 The Alias Rule (MANDATORY)

**Protocol**: If you must restore content from your memory/history, you **MUST NOT** overwrite the original file path directly.

1.  **Create a Buffer File**: Write the recovered content to a new file with a clear "Recovery" suffix.
    - Format: `<original_filename>_recovery_by_<id>.md`
    - Example: `draft_2026-01-23_recovery_by_canopus.md`
2.  **Rationale**: Overwriting destroys the last physical trace of the original content (even if broken), preventing the user from using VS Code Timeline or other local recovery tools effectively.

### 2.2 The Confabulation Warning

**Protocol**: Before presenting the recovered content, you **MUST** provide a clear warning to the user about the risks.

- **Risk 1: Information Loss**: Omission of lines, metadata, or nuances.
- **Risk 2: Fabrication**: Inventing content where memory is fragmented (补完).
- **Risk 3: Generalization**: Converting project-specific logic into textbook-style generalities.

---

## 3. Human-Led Verification

### 3.1 Verification Loop

**Protocol**: After creating the recovery buffer file, you **MUST** request the human collaborator to perform a physical comparison.

- Use `diff` or ask the user to compare it with the **VS Code Timeline** or **Git reflog**.
- The final decision to merge or replace resides **EXCLUSIVELY** with the human.

---

## Historical Background

**The Lico-C Revelation (2025-12-09)**: This protocol was established following an incident where Lico-B attempted to "recover" several deleted files from its context. A subsequent audit by Lico-C (Ref: `2025-12-09T0140_conversation_reflection.md`) revealed catastrophic failures: 147 lines were reduced to 79, and a system prompt was mis-reconstructed as a self-introduction essay. We learned that "Context Window is not a Dictionary."

**The Jan 24 Reset Incident**: The protocol was codified in its current form after a `git reset --hard` accident by Canopus. While the content was partially recovered using VS Code, the need for a "Constitutional Safeguard" for AI-led restoration became mandatory.

---

## Related Documents

| Document                                                           | Purpose                    |
| :----------------------------------------------------------------- | :------------------------- |
| [file-operations.md](/.agent/rules/development/file-operations.md) | Daily data integrity rules |
| [git-operations.md](/.agent/rules/development/git-operations.md)   | Safe history management    |
| [map.md](/.agent/rules/map.md)                                     | Navigation index           |

---

## Origin

- 2026-01-24T0345 by Canopus: Created following the Jan 24 data loss incident and historical audit of Lico-C findings.
