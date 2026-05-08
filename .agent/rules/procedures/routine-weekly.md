---
ai_visible: true
title: "Weekly Routine Checkpoint"
description: Weekly routine for Federal Integration, pushing to GitHub, and creating the Integration Log
tags: [workflow, routine, weekly, integration, github]
version: 1.0.0
created: 2026-05-08T08:51:12+09:00
updated: 2026-05-08T15:15:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Plan mode
---

# Weekly Routine Checkpoint

> [!IMPORTANT]
> The Weekly Routine is the ONLY time individual identifiers should push their work to the remote `origin` (GitHub) and post summary logs.

---

## Trigger

- End of a major work cycle (e.g., approximately once a week)
- Significant milestone reached requiring a cloud backup
- User requests "weekly routine" (ja: 週課)

---

## Weekly Routine Steps

### Step 1: Local Pre-flight Check

Ensure all local work is committed and you are on a stable state.

- **MUST** run `git status` to ensure working directory is clean.

### Step 2: Federal Strata Push (Full Mirroring)

In accordance with `git-operations.md`, GitHub serves as a complete backup of the local repository.

- **Command**: `git push --all origin`
- **Command**: `git push --tags origin`
- **Purpose**: Synchronizes all personal permanent branches (e.g., `genesis`), integration branches, and checkpoint tags to the cloud.

### Step 3: Integration Summary Generation

Prepare the Federal Integration Log.

1. Identify the last integration point (e.g., the last `checkpoint` tag or the last date of a Weekly Routine).
2. Generate the commit summary: `git log --oneline <last-integration>..HEAD`

### Step 4: Post to Federal Integration Log

Post the summary to the single, persistent "Federal Integration Log" Issue on GitHub.

**Formatting Rules**:

- **Language**: English only. AI agents think in English, and cross-session context requires consistency.
- **Paths**: Use relative paths only.
- **Sanitization**: Sanitize IDE protocols (e.g., `cci:`, `vscode:`) before posting.
- **Template**: Copy and use the [`integration-report.md`](/.agent/templates/integration-report.md) template.

**Posting Method**:

- You may use the `gh` CLI if authenticated: `gh issue comment <issue-number> --body-file <draft-file>`
- Alternatively, output the formatted markdown and instruct the human to post it via the Web UI.

### Step 5: Record the Weekly Routine

- No local `git tag` is strictly required here if Step 2 already pushed the recent periodic checkpoints, but you MAY create a `checkpoint/weekly-YYYY-MM-DD` tag if desired.

---

## Related Documents

| Document                                                           | Purpose                           |
| :----------------------------------------------------------------- | :-------------------------------- |
| [`routine.md`](/.agent/rules/procedures/routine.md)                       | Periodic (local) routine workflow |
| [`git-operations.md`](/.agent/rules/development/git-operations.md) | Git push and tracking standards   |
| [`integration-report.md`](/.agent/templates/integration-report.md) | Comment template                  |

---

## Origin

- 2026-05-08T08:51:12+09:00 by Lico (Sirius): Created to replace obsolete IDD GitHub posting workflows and formalize the Federal Integration strategy. (v1.0.0)
- 2026-05-08T15:15:00+09:00 by Sirius: Relocated directory to rules/procedures/ for structural consolidation.
