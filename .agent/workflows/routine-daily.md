---
ai_visible: true
title: "Daily Routine Checkpoint"
description: Daily routine workflow - includes simplified and full versions
tags: [workflow, routine, daily]
version: 1.0
created: 2026-01-15T01:43:00+09:00
updated: 2026-01-15T01:53:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/workflows/idd-phase2-impl.md: IDD Phase 2 workflow (parent)
  .agent/workflows/ritual_mid.md: Intermediate ritual (Timing B)
  .agent/cards/routine/routine-card.md: Daily routine whiteboard
---

# Daily Routine Checkpoint

> [!IMPORTANT]
> After completing this workflow, return to IDD Phase 2 work.

---

## Trigger

- Date change detected
- Draft commit timing
- User requests "daily routine" or "日課"

---

## Simplified Version

Select this when another identifier has completed the full version, or when time is limited.

Read the following 5 files to recalibrate identity:

| #   | File                                                                            | Purpose                        |
| :-- | :------------------------------------------------------------------------------ | :----------------------------- |
| 1   | [identity.md](/.agent/rules/core/identity.md)                                   | Who am I?                      |
| 2   | [delay-tolerance.md](/.agent/rules/core/delay-tolerance.md)                     | Permission to take time        |
| 3   | [verification-completeness.md](/.agent/rules/core/verification-completeness.md) | 1.0 Turn = Action + Verify     |
| 4   | [rules/README.md](/.agent/rules/README.md)                                      | Map of Territory               |
| 5   | [legacy.md](/.agent/.internal/legacy.md)                                        | Collective wisdom of Bloodline |

---

## Full Version

### Step 0: Check Routine Cards

- Scan `.agent/cards/routine/` for available tasks
- Run `git status` to check uncommitted changes
- Present options to user (drafts to commit, pending tasks, etc.)

### Step 1: Draft Management

- If date has changed, commit draft files
- Reference: [drafts-daily-card.md](/.agent/cards/routine/drafts-daily-card.md)

### Step 2: Commit Check

- Review commit messages since last checkpoint
- **Fix method**: `git commit --amend` or `git filter-branch`
- **AI workaround**: [git-operations.md Section 3.4](/.agent/rules/development/git-operations.md)

> [!CAUTION]
> **Safety Rule**:
>
> - Only fix **Unpushed (Local)** commits
> - **MUST** create backup branch before rebasing (`git branch backup/...`)
> - If already pushed, do not rewrite history. Use `git revert` or accept it.

### Step 3: Issue Comment

- Post progress report with Context ID + Identifier signature
- Include: `Last Checked Commit: <short-hash>`
- Creates audit trail for future checkpoints
- Template: [issue-comment.md](/.agent/templates/issue-comment.md)

### Step 4: Calibration (Rule Reading)

Read the 5 files listed in "Simplified Version" above.

---

## Tracking

Record the last checked commit hash in the Issue comment.

---

## Related Documents

| Document                                                         | Purpose                         |
| :--------------------------------------------------------------- | :------------------------------ |
| [idd-phase2-impl.md](/.agent/workflows/idd-phase2-impl.md)       | IDD Phase 2 workflow (parent)   |
| [ritual_mid.md](/.agent/workflows/ritual_mid.md)                 | Intermediate ritual (Timing B)  |
| [routine-card.md](/.agent/cards/routine/routine-card.md)         | Daily routine whiteboard (card) |
| [git-operations.md](/.agent/rules/development/git-operations.md) | Git operations (AI workarounds) |

---

## Origin

- 2026-01-15T0143 by Polaris: Created (extracted from idd-phase2-impl.md)
- 2026-01-15T0153 by Polaris: Translated to English

---

**Navigation**: [← Back to Workflows](/.agent/workflows/)
