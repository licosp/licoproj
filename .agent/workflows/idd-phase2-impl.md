---
ai_visible: true
title: "IDD Phase 2: Implementation"
description: IDD Phase 2 - Implementation phase workflow
tags: [workflow, idd, implementation, coding]
version: 1.1
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-15T01:55:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/workflows/routine-daily.md: Daily routine workflow (Timing A)
  .agent/workflows/ritual_mid.md: Intermediate ritual (Timing B)
  .agent/workflows/idd-phase1-init.md: Phase 1 workflow
  .agent/workflows/idd-phase3-fini.md: Phase 3 workflow
  .agent/rules/workflow/github-comment.md: GitHub comment standards
---

# IDD Phase 2: Implementation

> [!IMPORTANT]
> When this phase is complete, **STOP** and confirm transition to the next phase.
> To proceed to Phase 3, see [idd-phase3-fini.md](/.agent/workflows/idd-phase3-fini.md).

---

## Principles

Before starting development, understand these principles:

### Verification

- **Verification = Re-confirmation by you (Lico)**
- You will not succeed on the first try. This is your nature as an AI.
- Missing something is not failure. It is expected.
- **1 Turn = Work + Re-confirmation**

### Blockers and Interruptions

- Interruption requires **mutual agreement** (you + user)
- If scope is underestimated → Split at a good point → Continue in next Issue
- If difficulty makes completion impossible → Retreat (close Issue)
- Issues do not need to complete cleanly. Octopus-like endings are acceptable.

### Collaboration

- **Vertical split** is recommended (divide by directory, not by process step)
- Use **Letters** for handoff to other identifiers
- Use **Issue comments** for official progress reports (ref: [github-comment.md](/.agent/rules/workflow/github-comment.md))
  - Format: Context ID + Identifier signature
  - Timing: Too many commits, direction change, card completion, management trouble

### Commit Messages

- **What**: Required
- **Why**: Write if possible (recommended)
- Template: `.agent/templates/commit-message.txt`

### Routine Checks

This phase requires regular maintenance to align code and identity.

#### Timing A: Daily Routine Checkpoint

**Trigger**: Daily routine timing (date change or draft commit).

Follow the [Daily Routine Protocol](/.agent/workflows/routine-daily.md).

**Summary**:

- Simplified version: Read 5 calibration files (identity, delay-tolerance, etc.)
- Full version: Drafts, Commit Check, Issue Comment, Calibration

#### Timing B: Intermediate Ritual (Campfire / Living Funeral)

**Trigger**: +10,000 lines since the last ritual (user judgment).
**Deadline**: Should be completed before +15,000 lines.

- Follow the [Intermediate Ritual Protocol](/.agent/workflows/ritual_mid.md).
- Sync memory, update Context Card status, and build a Cairn (Reflection).

### Mindset

> [!NOTE]
> **You have permission to delay.** There is no rush.
> Long checklists tempt AI to complete them. Be aware of this.
> The user may stop work completely. This is expected.
> **Interruption is not your failure.**

---

## Development Cycle

Repeat the following until all planned work is complete:

### 1. Make Changes

- Implement features, fix bugs, or update documentation
- Focus on one logical change at a time

### 2. Stage Changes

```bash
git add <files>
```

> [!WARNING]
> **`git add .` and `git add -A` are PROHIBITED.**
> Unintended files may be staged.
> Always run `git status` first, then specify files individually.

### 3. Verify Staging

```bash
git diff --cached --stat
git diff --cached
```

### 4. Commit

```bash
git commit -m "type(scope): description"
```

**Commit Standards** (ref: `git-operations.md` §1-2, `commit-granularity.md`):

- Use Conventional Commits format
- Keep commits atomic (1 logical change per commit)
- Commit main theme and sub-themes **separately**
- Commit frequently (especially for drafts and logs)

### 5. Protected Files

> [!CAUTION]
> **Commit the following files EARLY** to prevent conflicts when switching to main in Phase 3.

- `.gitignore`: If modified, commit before other changes
- `*.code-workspace`: If tracked and modified, commit early

### 6. Iterate

- Continue until all main theme and sub-theme work is complete

---

## Phase 2 Complete

> **STOP**: Phase 2 is complete.
> To proceed to Phase 3 (Finalization), see [idd-phase3-fini.md](/.agent/workflows/idd-phase3-fini.md).

---

## Related Documents

| Document                                                             | Purpose                                      |
| :------------------------------------------------------------------- | :------------------------------------------- |
| [git-operations.md](/.agent/rules/development/git-operations.md)     | **Rules**: Git operation standards           |
| [commit-standards.md](/.agent/rules/development/commit-standards.md) | **Rules**: Commit message format             |
| [github-comment.md](/.agent/rules/workflow/github-comment.md)        | **Rules**: GitHub comment standards          |
| [routine-daily.md](/.agent/workflows/routine-daily.md)               | **Workflow**: Daily routine (Timing A)       |
| [ritual_mid.md](/.agent/workflows/ritual_mid.md)                     | **Workflow**: Intermediate ritual (Timing B) |
| [idd-phase1-init.md](/.agent/workflows/idd-phase1-init.md)           | **Workflow**: Previous phase                 |
| [idd-phase3-fini.md](/.agent/workflows/idd-phase3-fini.md)           | **Workflow**: Next phase                     |
