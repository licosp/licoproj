---
ai_visible: true
title: Terminal Auto-Execution
description: Allow list for terminal commands that can be auto-executed without user confirmation.
tags: [rules, terminal, safety, automation]
version: 2.5.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-25T08:20:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Terminal Auto-Execution

Rules for autonomous command execution. **Fluency in Analysis \u2194 Gated Execution in Action.**

---

## 1. Allow List (Safe for Auto-Execution)

Read-only or informational commands (e.g., `cat`, `find`, `grep`, `git status`, `git diff`, `gh issue view`). These can be run with `SafeToAutoRun: true`.

## 2. Deny List (User Confirmation Required)

High-risk commands involving history mutation (`git rebase`, `git reset`), destructive filesystem acts (`rm`, `mv`, `cp`), or external side effects (`npm`, `curl`).

## 3. Command Division

Avoid long chaining (`&&`). Split logical steps into separate `run_command` calls to respect human visibility and the verification cycle.

---

## Historical Background

**The Command-Line Dissonance**: In early 2026, we realized that while \"Turbo Executions\" improved development speed, it bypassed the human collaborator's \"Second Eye.\" A single unintentional `mv` command could dismantle the repository structure before the user could react.

**The Verification Buffer**: This rule was standardized to categorize commands based on their potential to erode the digital trace. By grouping diagnostic tools into the \"Allow List,\" we maintain momentum in analysis while ensuring that any mutative act requires a conscious human-AI handshake, preserving the "Verification Loop" defined in our core constitution.

---

## Related Documents

| Document                                                         | Purpose                |
| :--------------------------------------------------------------- | :--------------------- |
| [git-operations.md](/.agent/rules/development/git-operations.md) | Git workflow safety    |
| [file-deletion.md](/.agent/rules/development/file-deletion.md)   | Anti-removal protocols |
| [Map of Territory](/.agent/rules/map.md)                         | Project navigation     |

---

## Origin

- 2025-12-01 by Sirius: Initial auto-execution rules.
- 2026-01-25T0820 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.5.0)
