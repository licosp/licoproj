---
ai_visible: true
title: "IDD Phase 1: Initialization"
description: "Phased workflow for initializing Issue-Driven Development sessions."
tags: [workflow, idd, initialization]
version: 1.1
created: 2025-12-08T00:00:00+09:00
updated: 2026-01-15T23:55:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/rules/development/git-operations.md: Branch naming and IDD details
  .agent/rules/development/commit-standards.md: Commit message standards
  .agent/rules/workflow/github-comment.md: GitHub comment standards
---

# IDD Phase 1: Initialization

> [!IMPORTANT]
> When this phase is complete, **MUST STOP** and confirm the transition to the next phase.

---

## 0. Alignment (Ritual)

Before starting work, record the initialization ritual to ensure continuity across sessions.

**0-1. Activity Log Sync**
Log the `Align` action for this workflow in `/.agent/.internal/activity-log.md`.

- **Purpose**: To anchor the current session to this procedure and prevent cognitive drift.

---

## 1. Environment Verification

**1-1. Tool Availability Check**

```bash
# Check required tools
command -v gh &> /dev/null || echo "Error: GitHub CLI not installed"
command -v git &> /dev/null || echo "Error: Git not installed"
```

**1-2. Authentication Status**

```bash
gh auth status || echo "Error: Not authenticated. Run 'gh auth login'"
```

---

## 2. Hierarchy Understanding

> [!TIP]
> Understand the hierarchy of work units in IDD before proceeding.

```
Story (Connected Issues)
└── Issue (Chapter)
    └── Context (Card)
        └── Commit (Episode)
            …
        …
    …
```

**Terminology**:

- **Story**: A collection of connected issues (large theme)
- **Issue**: A single unit of work (chapter)
- **Context**: Work context managed by cards
- **Commit**: The smallest unit of change (episode)

---

## 3. Theme Design

**3-1. Define Main Theme**

- Identify the primary goal of the issue (e.g., "Add pre-task assessment protocol")
- Ensure the theme is clear and focused

**3-2. Identify Sub-Themes**

- List changes unrelated to the main theme but necessary for synchronization
- Examples: Draft updates, `.gitignore` adjustments, typo fixes
- **Note**: Sub-themes will be committed separately (ref: [commit-granularity.md](/.agent/rules/development/commit-standards.md))

---

## 4. Issue Selection

> [!NOTE]
> Choose one path: create a new issue OR work on an existing issue.

**4-0. Choose Workflow**

| Situation            | Action                                  |
| :------------------- | :-------------------------------------- |
| Starting new work    | → Go to 4-1 (Issue Connection Decision) |
| Issue already exists | → Go to 4-6 (Use Existing Issue)        |

**4-1. Issue Connection Decision**
Before creating a new issue, check connection to previous issue:

| Situation                      | Action                        |
| :----------------------------- | :---------------------------- |
| Continuation of previous issue | → Add `Follows #N` to Body    |
| Related but not continuation   | → Add `Related to #N` to Body |
| Completely new                 | → No connection reference     |

---

### Path A: Create New Issue

**4-2. Prepare Issue Elements**

- **Title**: `[Type]: Brief description` (e.g., `[Feat]: Add pre-task assessment`)
- **Body**: Summary, Changes, Purpose
- **Assignees**: Assign to yourself or team members
- **Labels**: Match commit type (`feat`, `fix`, `docs`, etc.)

**4-3. Create Issue**

```bash
gh issue create \
  --title "[Feat]: Add pre-task assessment protocol" \
  --body "## Summary\n...\n\n## Changes\n...\n\n## Purpose\n..." \
  --assignee licosp
```

**4-4. Capture Issue Number from Output**

```bash
# The 'gh issue create' command outputs the issue URL
# Extract the number immediately after creation
```

**4-5. Assign Labels (after creation)**

```bash
gh issue edit ${ISSUE_NUMBER} --add-label "type:feat"
```

→ **Proceed to Section 5**

---

### Path B: Use Existing Issue

**4-6. Set Issue Number Variable**

> [!IMPORTANT]
> Set the target issue number as an environment variable to ensure consistency across all subsequent steps. This is the **Anchor** for shell commands.

```bash
# Set your actual issue number here
export ISSUE_NUMBER=16
echo "Working on Issue #$ISSUE_NUMBER"
```

**4-7. Verify Issue Exists**

```bash
gh issue view ${ISSUE_NUMBER} --json title,state
```

> [!CAUTION]
> **Do NOT use `gh issue list --limit 1`** to get the issue number.
> This returns the most recent issue, which may not be the one you're working on.

→ **Proceed to Section 5**

---

## 5. Branch Creation

> [!CAUTION]
> **Must create from `origin/main`.**
> Creating from `HEAD` or current branch may include unintended changes from other branches.

**5-1. Fetch Latest Remote State**

```bash
git fetch origin
```

**5-2. Create Local Branch from Remote Main**

```bash
git checkout -b ${ISSUE_NUMBER}-brief-description-kebab-case origin/main
```

**Naming Convention** (ref: [git-operations.md §3.1](/.agent/rules/development/git-operations.md)):

- Format: `<issue-number>-<issue-title-kebab-case>`
- Language: English
- Length: ~50 characters

**5-3. Push Branch and Set Upstream Tracking**

```bash
git push -u origin ${ISSUE_NUMBER}-brief-description-kebab-case
```

---

## 6. Initial State Verification

**6-1. Check Current Branch Status**

```bash
git status
```

**6-2. Verify Feasibility**

- Confirm that main theme and sub-themes can be implemented
- Check for potential conflicts or blockers

---

## 7. Early Problem Detection

**7-1. Identify Issues**

- List any problems discovered during verification
- Document technical constraints or dependencies

**7-2. Record in Issue Comments**

```bash
gh issue comment ${ISSUE_NUMBER} --body "## Initial Assessment\n- Problem: ...\n- Solution: ..."
```

> [!TIP]
> For comment format standards and draft workflow, see [github-comment.md](/.agent/rules/workflow/github-comment.md).

**7-3. Backup Issue Locally**

```bash
gh issue view ${ISSUE_NUMBER} --json title,body,comments > .agent/issues/issue-${ISSUE_NUMBER}-backup.json
```

---

## Phase 1 Complete

> **STOP**: Phase 1 is complete. (Phase 1 が完了しました。)

---

## Troubleshooting

### Issue: Cannot verify Issue ↔ Branch association

**Cause**: Used `git checkout -b` + `git push -u` instead of `gh issue develop`
**Solution**:

1. Delete branch and start over
   ```bash
   git checkout main
   git branch -D <branch-name>
   git push origin --delete <branch-name>
   ```
2. Recreate with `gh issue develop`
   ```bash
   gh issue develop ${ISSUE_NUMBER} --name <branch-name> --checkout
   ```

### Issue: Accidentally committed to main (local)

**Cause**: Started working without creating a feature branch.
**Solution**:

1. Create branch from current state: `git branch <issue-number>-<title>`
2. **Safety Backup**: `git branch backup/pre-reset-main-$(date +%Y%m%d-%H%M%S)`
3. Reset main: `git reset --hard origin/main`
4. Checkout correct branch: `git checkout <issue-number>-<title>`

### Issue: Work-in-progress changes disappeared

**Cause**: Changes were stashed during branch switch
**Solution**:

```bash
git stash list
git stash pop
```

**Cleanup (Optional)**:
If you want to clear the environment variable:

```bash
unset ISSUE_NUMBER
```

---

## Origin

- 2025-12-08T0000: Created original Japanese version
- 2026-01-15T0440 by Canopus: [Localization] Fully translated to English and integrated 'Align' ritual standards
- 2026-01-15T2355 by Polaris: Added github-comment.md cross-link to Section 7-2

---

## Related Documents

| Document                                                          | Purpose                   |
| :---------------------------------------------------------------- | :------------------------ |
| [Rules Index](/.agent/rules/README.md)                            | Return to Rule Management |
| [Phase 2: Implementation](/.agent/workflows/idd-phase2-impl.md)   | Next Phase                |
| [Phase 3: Finalization](/.agent/workflows/idd-phase3-fini.md)     | Final Phase               |
| [Git Operations](/.agent/rules/development/git-operations.md)     | Detailed Git Rules        |
| [Commit Standards](/.agent/rules/development/commit-standards.md) | Commit Message Rules      |
| [GitHub Comment](/.agent/rules/workflow/github-comment.md)        | Comment Standards         |

---

**Navigation**: [← Back to Rules Index](/.agent/rules/README.md)
