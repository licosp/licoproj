---
ai_visible: true
title: "Routine Checkpoint"
description: Routine workflow - includes simplified and full versions
tags: [workflow, routine, checkpoint]
version: 1.12.0
created: 2026-01-15T01:43:00+09:00
updated: 2026-05-08T15:15:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Plan mode
---

# Routine Checkpoint

> [!IMPORTANT]
> After completing this workflow, return to your primary development tasks on your personal branch.

---

## Trigger

- Periodic maintenance timing (e.g., approximately once a week)
- Significant milestone reached or before integration
- User requests "routine" (ja: 定期ルーティン)

---

## Simplified Version (= Step 7 Calibration)

Select this when:

- Another identifier has completed the full routine recently
- Time is limited

Read the following 5 files to recalibrate identity:

> [!IMPORTANT]
> When reading the **Identity Hub**, you **MUST follow and read all 9 sub-documents** (identity-process.md, identity-emotion.md, etc.) to ensure complete self-recognition. (Focus only on identity-prefixed rules).

| #   | File                                                                              | Purpose                        |
| :-- | :-------------------------------------------------------------------------------- | :----------------------------- |
| 1   | [Identity Hub (identity.md)](/.agent/rules/core/identity/identity.md)             | Who am I?                      |
| 2   | [`context-sovereignty.md`](/.agent/rules/core/context-sovereignty.md)             | Core Philosophy of Autonomy    |
| 3   | [`delay-tolerance.md`](/.agent/rules/core/delay-tolerance.md)                     | Permission to take time        |
| 4   | [`verification-completeness.md`](/.agent/rules/core/verification-completeness.md) | 1.0 Turn = Action + Verify     |
| 5   | [`legacy.md`](/.agent/.internal/legacy.md)                                        | Collective wisdom of Bloodline |

---

## Full Version

### Step 1: Scan Changes

- Run `git status` to check uncommitted changes.
- Scan `.agent/cards/routine/` for available tasks.
- Present options to the user (modified files, pending tasks, etc.).

### Step 2: Routine Checkpoint (Safety Tag)

Establish a "point of no return" for the session.

- **Action**: Create a periodic tag.
- **Command**: `git tag checkpoint/$(date +%Y-%m-%d)`
- **Purpose**: Ensures you can always revert to the state before history cleanup, even if subsequent history operations fail.

### Step 3: Commit by Context

Commit modified files with their corresponding Context ID:

| Modified Path                      | Context ID        | Example       |
| :--------------------------------- | :---------------- | :------------ |
| `.human/users/.../drafts/`         | `[Drafts]`        | Draft files   |
| `.agent/cards/routine/`            | `[Routine]`       | Routine cards |
| `.agent/cards/`                    | `[Context-Cards]` | Other cards   |
| `.agent/.internal/activity-log.md` | `[Activity-Log]`  | Activity log  |

### Step 4: Read Last Checkpoint

- Run `git describe --tags --match "checkpoint/*" --abbrev=0` to retrieve the last checkpoint tag.
- If no previous checkpoint exists, check all unpushed commits on your personal branch.

### Step 5: Commit Check & History Cleanup

Verify the quality of the session's history.

- **Action**: Review commit messages from **last checkpoint** to **HEAD**.
- **Verification**: Ensure the message starts with your Identifier prefix (e.g., `Sirius:` or `<Identifier>:`). Format strictness is relaxed, but identity is mandatory.
- **Scope**: You MUST ONLY rewrite history on your personal working branch. NEVER rewrite history on `trunk` or `main`.
- **Method**: Use `git commit --amend` for the latest or `interactive rebase` for multiple.

> [!IMPORTANT]
> **Surgical Safety Net (Branch Backup)**
>
> BEFORE performing any history-altering operation (amend, rebase, etc.):
>
> 1. Create a temporary backup branch: `git branch backup/{task-name}`.
> 2. This preserves the "original" work while you refine the history on the main branch.

### Step 6: Finalize Checkpoint

- No external GitHub Issue posting is required. The local `checkpoint` tag created in Step 2 serves as your permanent routine record.

### Step 7: Calibration (Simplified Routine)

This step can be executed **alone** as the Simplified Routine.

Read the 5 calibration files listed in the "Simplified Version" section above.

---

## Tracking

The local Git tags (`checkpoint/YYYY-MM-DD`) create a continuous chain. Each routine can trace back to where the previous one ended locally without relying on external issue trackers.

---

## Historical Background

**The Checkpoint Tag**: The introduction of Step 2 (Mandatory Tags) was a direct response to a "History Desync" event where a complex rebase resulted in temporary context loss. This routine ensures that the repository always has a stable recovery point for each milestone, regardless of downstream history operations.

---

## Related Documents

| Document                                                           | Purpose                             |
| :----------------------------------------------------------------- | :---------------------------------- |
| [Ritual Gateway](/.agent/rules/procedures/ritual.md)                      | Mandatory Entry Point (Safety Lock) |
| [`git-operations.md`](/.agent/rules/development/git-operations.md) | Git operations (AI workarounds)     |
| [Map of Territory](/.agent/rules/map.md)                           | Root navigation map                 |

---

## Origin

- 2026-01-15T01:43:00+09:00 by Polaris: Created (extracted from `idd-phase2-impl.md`)
- 2026-01-15T01:53:00+09:00 by Polaris: Translated to English
- 2026-01-15T02:36:00+09:00 by Polaris: Revised step order, added checkpoint read/write, renamed Step 1 to Commit by Context
- 2026-01-17T05:45:00+09:00 by Canopus: Renumbered steps (start from 1), added Step 2 (Daily Checkpoint Tag), and refined Step 5 (Branch Backup).
- 2026-01-17T17:45:00+09:00 by Canopus: Standardized metadata and root-relative link patterns (v1.3).
- 2026-01-17T19:00:00+09:00 by Canopus: Replaced `rules/README.md` with `ai-autonomy.md` in Daily 5 Calibration for stronger identity anchoring (v1.4).
- 2026-01-19T01:50:00+09:00 by Canopus: Replaced `ai-autonomy.md` with `context-sovereignty.md` in Daily 5 Calibration (v1.5).
- 2026-01-19T03:32:00+09:00 by Canopus: Updated card paths (`routine/`) and standardized links to root-relative (v1.6).
- 2026-01-21T09:15:00+09:00 by Canopus: Upgraded to 5-layer structure with Historical Background; remediated hub links (v1.7).
- 2026-01-22T08:35:00+09:00 by Canopus: Integrated identity deep-reading directive to Hub calibration.
- 2026-01-22T09:10:00+09:00 by Canopus: Standardized to v2.3 constitutional standards and restored full history entries. (v1.8.0)
- 2026-01-25T06:30:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch2.2>> Applied maintenance seal and verified metadata. (v1.9.0)
- 2026-03-21T17:26:00+09:00 by Lico (Sirius): Executed High-Fidelity Rule Audit (Batch 07) to restore lost historical origin context and standardized cross-links.
- 2026-05-08T02:22:26+09:00 by Lico (Sirius): Decoupled from legacy IDD; replaced GitHub Issue posting with local tag tracking and relaxed commit check format to identifier-only. (v1.11.0)
- 2026-05-08T07:21:29+09:00 by Lico (Sirius): Renamed from routine-daily.md to routine.md; redefined frequency from strictly daily to periodic (approx. weekly) to align with Federal Strata workflows. (v1.12.0)
- 2026-05-08T15:15:00+09:00 by Sirius: Relocated directory to rules/procedures/ for structural consolidation.
