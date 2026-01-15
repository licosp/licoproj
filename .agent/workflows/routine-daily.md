---
ai_visible: true
title: "Daily Routine Checkpoint"
description: Daily routine workflow - includes simplified and full versions
tags: [workflow, routine, daily]
version: 1.1
created: 2026-01-15T01:43:00+09:00
updated: 2026-01-15T02:36:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/workflows/idd-phase2-impl.md: IDD Phase 2 workflow (parent)
  .agent/workflows/ritual_mid.md: Intermediate ritual (Timing B)
  .agent/cards/routine/routine-card.md: Daily routine whiteboard
  .agent/rules/workflow/github-comment.md: GitHub comment standards
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

## Simplified Version (= Step 5 Calibration)

Select this when:

- Another identifier has completed the full routine today
- Time is limited

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

### Step 0: Scan Changes

- Run `git status` to check uncommitted changes
- Scan `.agent/cards/routine/` for available tasks
- Present options to user (modified files, pending tasks, etc.)

### Step 1: Commit by Context

Commit modified files with their corresponding Context ID:

| Modified Path                      | Context ID        | Example       |
| :--------------------------------- | :---------------- | :------------ |
| `.human/users/.../drafts/`         | `[Drafts-Daily]`  | Draft files   |
| `.agent/cards/routine/`            | `[Routine]`       | Routine cards |
| `.agent/cards/`                    | `[Context-Cards]` | Other cards   |
| `.agent/.internal/activity-log.md` | `[Activity-Log]`  | Activity log  |

### Step 2: Read Last Checkpoint

- Read the last Issue comment to get `Last Checked Commit: <hash>`
- If no previous checkpoint exists, check all unpushed commits

### Step 3: Commit Check

- Review commit messages from **last checkpoint** to **HEAD**
- Verify format: `[Context-ID] type: description (Phase)`
- **Fix method**: `git commit --amend` or `git filter-branch`
- **AI workaround**: [git-operations.md Section 3.4](/.agent/rules/development/git-operations.md)

> [!CAUTION]
> **Safety Rule**:
>
> - Only fix **Unpushed (Local)** commits
> - **MUST** create backup branch before rebasing (`git branch backup/...`)
> - If already pushed, do not rewrite history. Use `git revert` or accept it.

### Step 4: Write Checkpoint

- Post Issue comment with Context ID + Identifier signature
- Include: `Last Checked Commit: <short-hash>`
- Creates audit trail for future checkpoints
- Format: [github-comment.md](/.agent/rules/workflow/github-comment.md)
- Template: [issue-comment.md](/.agent/templates/issue-comment.md)

### Step 5: Calibration (Simplified Daily Routine)

This step can be executed **alone** as the Simplified Daily Routine.

Read the 5 calibration files listed in the "Simplified Version" section above.

---

## Tracking

Record the last checked commit hash in the Issue comment.
This creates a chain: each routine knows where the previous one ended.

---

## Related Documents

| Document                                                         | Purpose                         |
| :--------------------------------------------------------------- | :------------------------------ |
| [idd-phase2-impl.md](/.agent/workflows/idd-phase2-impl.md)       | IDD Phase 2 workflow (parent)   |
| [ritual_mid.md](/.agent/workflows/ritual_mid.md)                 | Intermediate ritual (Timing B)  |
| [routine-card.md](/.agent/cards/routine/routine-card.md)         | Daily routine whiteboard (card) |
| [git-operations.md](/.agent/rules/development/git-operations.md) | Git operations (AI workarounds) |
| [github-comment.md](/.agent/rules/workflow/github-comment.md)    | GitHub comment standards        |

---

## Origin

- 2026-01-15T0143 by Polaris: Created (extracted from idd-phase2-impl.md)
- 2026-01-15T0153 by Polaris: Translated to English
- 2026-01-15T0236 by Polaris: Revised step order, added checkpoint read/write, renamed Step 1 to Commit by Context

---

**Navigation**: [← Back to Workflows](/.agent/workflows/)
