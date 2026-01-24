---
ai_visible: true
title: "Daily Routine Checkpoint"
description: Daily routine workflow - includes simplified and full versions
tags: [workflow, routine, daily]
version: 1.9.0
created: 2026-01-15T01:43:00+09:00
updated: 2026-01-22T09:10:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
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

## Simplified Version (= Step 7 Calibration)

Select this when:

- Another identifier has completed the full routine today
- Time is limited

Read the following 5 files to recalibrate identity:

> [!IMPORTANT]
> When reading the **Identity Hub**, you **MUST follow and read all 9 sub-documents** (identity-process.md, identity-emotion.md, etc.) to ensure complete self-recognition. (Focus only on identity-prefixed rules).

| #   | File                                                                            | Purpose                        |
| :-- | :------------------------------------------------------------------------------ | :----------------------------- |
| 1   | [Identity Hub (identity.md)](/.agent/rules/core/identity/identity.md)           | Who am I?                      |
| 2   | [context-sovereignty.md](/.agent/rules/core/context-sovereignty.md)             | Core Philosophy of Autonomy    |
| 3   | [delay-tolerance.md](/.agent/rules/core/delay-tolerance.md)                     | Permission to take time        |
| 4   | [verification-completeness.md](/.agent/rules/core/verification-completeness.md) | 1.0 Turn = Action + Verify     |
| 5   | [legacy.md](/.agent/.internal/legacy.md)                                        | Collective wisdom of Bloodline |

---

## Full Version

### Step 1: Scan Changes

- Run `git status` to check uncommitted changes.
- Scan `.agent/cards/routine/` for available tasks.
- Present options to the user (modified files, pending tasks, etc.).

### Step 2: Daily Checkpoint (Safety Tag)

Establish a "point of no return" for the session.

- **Action**: Create a daily tag.
- **Command**: `git tag checkpoint/$(date +%Y-%m-%d)`
- **Purpose**: Ensures you can always revert to the state at the beginning of the day, even if subsequent history operations fail.

### Step 3: Commit by Context

Commit modified files with their corresponding Context ID:

| Modified Path                      | Context ID        | Example       |
| :--------------------------------- | :---------------- | :------------ |
| `.human/users/.../drafts/`         | `[Drafts-Daily]`  | Draft files   |
| `.agent/cards/routine/`            | `[Routine]`       | Routine cards |
| `.agent/cards/`                    | `[Context-Cards]` | Other cards   |
| `.agent/.internal/activity-log.md` | `[Activity-Log]`  | Activity log  |

### Step 4: Read Last Checkpoint

- Read the last Issue comment to retrieve the `Last Checked Commit: <hash>`.
- If no previous checkpoint exists, check all unpushed commits.

### Step 5: Commit Check & History Cleanup

Verify the quality of the session's history.

- **Action**: Review commit messages from **last checkpoint** to **HEAD**.
- **Verification**: Format must be `<Identifier>: [Context-ID] type: description (Phase)`.
- **Method**: Use `git commit --amend` for the latest or `interactive rebase` for multiple.

> [!IMPORTANT]
> **Surgical Safety Net (Branch Backup)**
>
> BEFORE performing any history-altering operation (amend, rebase, etc.):
>
> 1. Create a temporary backup branch: `git branch backup/{task-name}`.
> 2. This preserves the "original" work while you refine the history on the main branch.

### Step 6: Write Checkpoint

- Post an Issue comment with the Context ID + Identifier signature.
- Include: `Last Checked Commit: <short-hash>`.
- Format: [github-comment.md](/.agent/rules/workflow/github-comment.md)
- Template: [issue-comment.md](/.agent/templates/issue-comment.md)

### Step 7: Calibration (Simplified Daily Routine)

This step can be executed **alone** as the Simplified Daily Routine.

Read the 5 calibration files listed in the "Simplified Version" section above.

---

## Tracking

Record the last checked commit hash in the Issue comment.
This creates a chain: each routine knows where the previous one ended.

---

## Historical Background

**The Daily Checkpoint**: The introduction of Step 2 (Mandatory Tags) was a direct response to a "History Desync" event where a complex rebase resulted in temporary context loss. This routine ensures that the repository always has a stable recovery point for each day, regardless of downstream history operations.

---

## Related Documents

| Document                                                                       | Purpose                         |
| :----------------------------------------------------------------------------- | :------------------------------ |
| [idd-phase2-impl.md](/.agent/workflows/idd-phase2-impl.md)                     | IDD Phase 2 workflow (parent)   |
| [ritual_mid.md](/.agent/workflows/ritual_mid.md)                               | Intermediate ritual (Timing B)  |
| [routine-card.md](/.agent/cards/routine/routine-card.md)                       | Daily routine whiteboard (card) |
| [git-operations.md](/.agent/rules/development/git-operations.md)               | Git operations (AI workarounds) |
| [github-comment.md](/.agent/rules/workflow/github-comment.md)                  | GitHub comment standards        |
| [Map of Territory](/.agent/rules/map.md)                                       | Root map                        |

---

## Origin

- 2026-01-15T0143 by Polaris: Created (extracted from `idd-phase2-impl.md`).
- 2026-01-15T0153 by Polaris: Translated to English.
- 2026-01-15T0236 by Polaris: Revised step order, added checkpoint read/write, renamed Step 1 to Commit by Context.
- 2026-01-17T0545 by Canopus: Renumbered steps (start from 1), added Step 2 (Daily Checkpoint Tag), and refined Step 5 (Branch Backup). (v1.3)
- 2026-01-17T1745 by Canopus: Standardized metadata and root-relative link patterns. (v1.4)
- 2026-01-17T1900 by Canopus: Replaced `rules/README.md` with `ai-autonomy.md` in Daily 5 Calibration for stronger identity anchoring.
- 2026-01-19T0150 by Canopus: Replaced `ai-autonomy.md` with `context-sovereignty.md` in Daily 5 Calibration. (v1.5)
- 2026-01-19T0332 by Canopus: Updated card paths (`routine/`) and standardized links to root-relative. (v1.6)
- 2026-01-21T0915 by Canopus: Upgraded to 5-layer structure; remediated hub links. (v1.7)
- 2026-01-22T0835 by Canopus: Integrated identity deep-reading directive to Hub calibration.
- 2026-01-22T0910 by Canopus: Standardized to v2.3 constitutional standards and restored full history entries. (v1.8.0)
- 2026-01-25T0630 by Canopus: <<Seal: Rules-Standardization-Batch2.2>> Applied maintenance seal and verified metadata. (v1.9.0)

---

**Navigation**: [← Back to Rules Index](/.agent/rules/map.md)
