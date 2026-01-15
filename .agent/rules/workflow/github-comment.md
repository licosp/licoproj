---
ai_visible: true
title: GitHub Comment Standards
description: Standards for posting comments to GitHub Issues and Pull Requests
tags: [github, comments, workflow]
version: 1.0
created: 2026-01-15T20:26:00+09:00
updated: 2026-01-15T20:26:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
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

## 4. Draft Workflow

> [!NOTE]
> This workflow is under development. See [github-backup-card.md](/.agent/cards/github-backup-card.md).

1. Copy template to draft file
2. Fill in the content
3. Verify before posting
4. Post to GitHub
5. Commit the draft file

---

## Origin

- 2026-01-15T2026 by Polaris: Created (separated from issue-comment.md template)

---

**Navigation**: [← Back to Workflow Rules](/.agent/rules/workflow/)
