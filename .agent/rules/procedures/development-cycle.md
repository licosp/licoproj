---
ai_visible: true
title: "Development Cycle & Principles"
description: Core philosophy, mindset, and routine checks for continuous development
tags: [workflow, development, coding, philosophy, cycle]
version: 3.0.0
created: 2025-12-08T21:38:15+09:00
updated: 2026-05-08T15:15:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Development Cycle & Principles

> [!IMPORTANT]
> This document outlines the continuous development cycle under the Federal Strata architecture. There are no strict "phases". Development is continuous.

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
- Use the **Federal Integration Log** via `routine-weekly.md` for official progress reports

### Commit Messages

- **What**: Required
- **Why**: Write if possible (recommended)
- Template: `.agent/templates/commit-message.txt`

### Routine Checks

This phase requires regular maintenance to align code and identity.

#### Timing A: Periodic Routine Checkpoint

**Trigger**: Whenever a local checkpoint or identity alignment is needed.

Follow the [Periodic Routine Protocol](/.agent/rules/procedures/routine.md).

**Summary**:

- Simplified version: Read calibration files (identity, delay-tolerance, etc.)
- Full version: Drafts, Commit Check, Calibration

#### Timing B: Intermediate Ritual (Campfire / Living Funeral)

**Trigger**: +10,000 lines since the last ritual (user judgment).
**Deadline**: Should be completed before +15,000 lines.

- Follow the [Ritual Gateway (Safety Lock)](/.agent/rules/procedures/ritual.md).
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
git commit -m "<Identifier>: [Context-ID] type(scope): description (Phase)"
```

**Commit Standards** (ref: [`git-operations.md`](/.agent/rules/development/git-operations.md) §1-2, [`commit-standards.md`](/.agent/rules/development/commit-standards.md)):

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

## Cycle Completion

> **STOP**: A major development block is complete.
> To create a cloud backup and report progress, execute the Weekly Routine: see [`routine-weekly.md`](/.agent/rules/procedures/routine-weekly.md).

---

## Related Documents

| Document                                                               | Purpose                                        |
| :--------------------------------------------------------------------- | :--------------------------------------------- |
| [`git-operations.md`](/.agent/rules/development/git-operations.md)     | **Rules**: Git operation standards             |
| [`commit-standards.md`](/.agent/rules/development/commit-standards.md) | **Rules**: Commit message format               |
| [`routine.md`](/.agent/rules/procedures/routine.md)                           | **Workflow**: Periodic routine (Timing A)      |
| [`routine-weekly.md`](/.agent/rules/procedures/routine-weekly.md)             | **Workflow**: Weekly routine (Federal Log)     |
| [Ritual Gateway](/.agent/rules/procedures/ritual.md)                          | **Workflow**: Mandatory Entry Point (Timing B) |
| [Map of Territory](/.agent/rules/map.md)                               | Root navigation map                            |

---

## Origin

- 2025-12-08T21:38:15+09:00 by Lico: Created as implementation workflow.
- 2026-01-15T19:35:00+09:00 by Polaris: Divided based on IDD phases (ref: #27)
- 2026-01-17T17:45:00+09:00 by Canopus: Standardized metadata and root-relative link patterns (v1.2).
- 2026-01-23T10:50:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch2.1>> Standardized to v2.3 constitutional standards (4-layer structure, Historical Background integration).
- 2026-03-21T17:26:00+09:00 by Lico (Sirius): Executed High-Fidelity Rule Audit (Batch 07) to restore lost historical origin context and standardized cross-links.
- 2026-05-08T15:15:00+09:00 by Sirius: Relocated directory to rules/procedures/ for structural consolidation.
