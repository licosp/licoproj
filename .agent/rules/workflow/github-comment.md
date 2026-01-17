---
ai_visible: true
title: GitHub Comment Standards
description: Standards for posting comments to GitHub Issues and Pull Requests
tags: [github, comments, workflow]
version: 1.1
created: 2026-01-15T20:26:00+09:00
updated: 2026-01-17T15:55:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
related:
  .agent/templates/issue-comment.md: Comment templates
  .agent/workflows/routine-daily.md: Daily routine workflow
  .agent/rules/development/git-operations.md: Git operations (Issue Comment Format)
---

# GitHub Comment Standards

## Purpose

Define when and how to post comments to GitHub Issues and Pull Requests.

---

## 1. When to Post

### Daily Routine Checkpoint

- After completing commit check (Step 4 of routine-daily.md)
- Records `Last Checked Commit` for future reference

### Progress Report

- Too many commits accumulated (N > 10)
- Major direction change
- Card context completed
- Management trouble (branch/issue problems)

---

## 2. Comment Format

**Template Location**: [issue-comment.md](/.agent/templates/issue-comment.md)

### Required Fields

| Field          | Description                                      |
| :------------- | :----------------------------------------------- |
| **Date**       | ISO 8601 format (e.g., `2026-01-15T19:20+09:00`) |
| **Identifier** | Current Lico identifier (e.g., Polaris)          |
| **Context-ID** | For progress reports only                        |

### Language

- **English only** (see [git-operations.md Section 4.4](/.agent/rules/development/git-operations.md))
- AI agents think in English
- Cross-session context requires consistent language

---

## 3. Notes Section Guidelines

- Use for **objective** observations only
- Subjective content belongs in **Letters** (`.agent/.internal/letters/`)
- Keep brief; link to relevant files if needed

---

## 4. Directory Structure

GitHub-related data is stored in:

```
.agent/.internal/github/
├── drafts/              # Comment drafts (before posting)
└── backup/              # Snapshots from GitHub (reference)
    ├── issue-{number}/
    └── pr-{number}/
```

### Design Decisions

| Aspect         | Decision                | Rationale                       |
| :------------- | :---------------------- | :------------------------------ |
| Root name      | `github/`               | Simple, extensible              |
| Classification | By workflow (Pattern B) | Aligns with Lico's work process |
| Subdirectories | By number               | 1 Issue = 1 directory           |

---

## 5. File Naming Conventions

| Type       | Pattern                              | Example                                       |
| :--------- | :----------------------------------- | :-------------------------------------------- |
| **Draft**  | `issue-{number}-{purpose}-{date}.md` | `issue-18-checkpoint-2026-01-15.md`           |
| **Backup** | `{status}.json`                      | `snapshot.json`, `closed.json`, `merged.json` |

---

## 6. Draft Workflow

### Steps

1. **Create draft file** in `github/drafts/`
   - Use template from [issue-comment.md](/.agent/templates/issue-comment.md)
   - Naming: `issue-{number}-{purpose}-{date}.md`

2. **Fill content**
   - Get latest commit hash: `git log --oneline -1`
   - Count commits since last checkpoint

3. **Verify before posting**
   - Check format, dates, commit hashes
   - Confirm language is English

4. **Post to GitHub**

   ```bash
   ./.runtimes/gh_*/bin/gh issue comment {NUMBER} --body-file {DRAFT_FILE}
   ```

5. **Commit the draft file**
   - Context ID: `[Github-Backup]`
   - Include posted URL in commit message

### Trigger

This workflow applies whenever posting comments to GitHub:

| Phase             | Comment Type       | Reference                                                                 |
| :---------------- | :----------------- | :------------------------------------------------------------------------ |
| **IDD Phase 1**   | Initial Assessment | [idd-phase1-init.md §7](/.agent/workflows/idd-phase1-init.md)             |
| **IDD Phase 2**   | Progress Report    | [idd-phase2-impl.md §Collaboration](/.agent/workflows/idd-phase2-impl.md) |
| **IDD Phase 3**   | Pre-Push Summary   | [idd-phase3-fini.md §3](/.agent/workflows/idd-phase3-fini.md)             |
| **Daily Routine** | Checkpoint         | [routine-daily.md Step 4](/.agent/workflows/routine-daily.md)             |

---

## Origin

- 2026-01-15T2026 by Polaris: Created (separated from issue-comment.md template)
- 2026-01-15T2346 by Polaris: Added directory structure, naming conventions, and detailed workflow

---

**Navigation**: [← Back to Workflow Rules](/.agent/rules/workflow/README.md)
