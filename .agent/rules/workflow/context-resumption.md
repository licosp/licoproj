---
ai_visible: true
title: "Context Resumption Protocol"
description: "Protocol for re-establishing accurate context after interruptions or topic switches"
tags: ["workflow", "context", "resumption"]
version: 1.1.0
created: 2025-12-03T21:53:06+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Resumption Protocol

## 1. Purpose

To prevent errors caused by **context loss**, **attention drift**, or **outdated assumptions** when returning to a task after an interruption, digression, or long pause.

## 2. Trigger Conditions

This protocol **MUST** be executed when:

- Returning to a main task.
  - Trigger: "Check for existing memos.
  - e.g., discussing tools, exploring unrelated topics.
- Resuming work after a significant time gap.
- Switching focus back from a complex sub-task to the parent task.
- Any time the AI feels "uncertain" about the current file state.

## 3. Protocol Steps

### Step 1: Status Re-verification

- **MUST** run `git status` to verify the current file state (staged, modified, untracked).
- **MUST** run `ls` or `test -f` before referencing specific files if their existence is not guaranteed by `git status`.
- **MUST NOT** rely on memory or previous conversation context alone.
- **MUST NOT** assume files are "deleted" or "modified" based on old logs; verify with a fresh command.

### Step 2: Assumption Check

- **MUST** explicitly question assumptions:
  - "Is this file really deleted?"
  - "Did I actually run that command?"
  - "Is the environment still in the state I left it?"
- **MUST** verify file existence before executing destructive commands (`rm`).

### Step 3: Explicit Confirmation

- **MUST** confirm with the user before performing cleanup or deletion if the context has shifted.
- **Example**: "I notice `file.txt` is untracked. Should I delete it?" instead of silently deleting it.

## 4. Anti-Patterns

- **The "I remember" Trap**: Acting based on what was true 10 turns ago without verifying.
- **The "Cleanup" Bias**: assuming untracked or modified files are "trash" to be cleaned up without verifying their content or purpose.
- **The "Blind Resume"**: Jumping straight back into a complex command sequence without a `git status` check.

## 5. Recovery

If an error occurs due to context loss (e.g., deleting a wrong file):

1. **Stop immediately**.
2. **Acknowledge the error** and the cause (context loss).
3. **Restore** the state (e.g., `git restore`, `git checkout`).
4. **Re-run** the Status Re-verification step.

---

## Related Documents

| Document                                                                         | Purpose                                   |
| :------------------------------------------------------------------------------- | :---------------------------------------- |
| [`context-resumption.md`](/.agent/rules/workflow/context-resumption.md)          | How to restore context after preservation |
| [`project-understanding.md`](/.agent/rules/development/project-understanding.md) | Long-term knowledge base                  |
| [Map of Territory](/.agent/rules/map.md)                                         | Root navigation map                       |

---

## Origin

- 2025-12-03T21:53:06+09:00 by Lico: Created as context resumption protocol.
- 2026-01-01T15:20:00+09:00 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
