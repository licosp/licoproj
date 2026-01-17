---
ai_visible: true
title: "IDD Phase 3: Finalization"
description: "Phased workflow for finalizing and merging changes in IDD."
tags: [workflow, idd, finalization]
version: 1.2
created: 2025-12-08T00:00:00+09:00
updated: 2026-01-17T17:45:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
related:
  .agent/rules/development/git-operations.md: Branch naming and IDD details
  .agent/rules/development/commit-standards.md: Commit message standards
  .agent/rules/workflow/github-comment.md: GitHub comment standards
---

# IDD Phase 3: Finalization

> [!IMPORTANT]
>
> - Always consider security when uploading to remote environments.
> - No absolute paths in commits (ref: [git-operations.md](/.agent/rules/development/git-operations.md) §6.1).
> - Ensure no sensitive information is pushed to origin.

---

## 0. Alignment (Ritual)

Before closing the cycle, perform the final synchronization to ensure all actions are properly anchored in the lineage history.

**0-1. Activity Log Sync**
Log the `Align` action for this workflow in `/.agent/.internal/activity-log.md`.

- **Purpose**: To synchronize the final state and intent before merging changes to the main repository.

---

## 1. Preparation

**1-1. Tool Re-verification**

```bash
gh auth status
git status
```

**1-2. Progress Check**
Verify all Issue requirements are implemented. Check for missing work.

**1-3. Incomplete Work Decision**
If work is incomplete, confirm with user whether to return to Phase 2 (Implementation).

**1-4. Return if Needed**
If returning, abort finalization and go back to Phase 2.

---

## 2. Working Directory Cleanup

> [!CAUTION]
> **STOP: Confirm with the user before executing `git stash`.**
> Draft files currently being edited may be lost. Ask "Is it okay to execute stash?" before proceeding.

**2-1. Selective Stash**
Execute stash only if there are uncommitted changes that should not be committed.

**2-2. Stash Exclusions**

- User's draft files (request user to pause editing, then commit before stashing if necessary)
- VSCode workspace settings (`*.code-workspace`)
- `.gitignore`

**Technical Implementation**:

```bash
git stash push -m "IDD Finalization" -- . ':(exclude)*.code-workspace' ':(exclude).gitignore'
```

---

## 3. Pre-Push Documentation

**3-1. Generate Commit Summary**

```bash
git log --oneline origin/main..HEAD --pretty=format:"- \`%h\` %s" > /.agent/.internal/workspace/commit-summary.md
```

**3-2. Edit Summary (Optional)**
Edit `/.agent/.internal/workspace/commit-summary.md` to include timestamp and brief summary.

**3-3. Post to Issue**

```bash
gh issue comment ${ISSUE_NUMBER} --body-file /.agent/.internal/workspace/commit-summary.md
```

> [!TIP]
> For comment format standards, see [github-comment.md](/.agent/rules/workflow/github-comment.md).

---

## 4. Push Branch

```bash
git push origin ${ISSUE_NUMBER}-brief-description-kebab-case
```

---

## 5. Create Pull Request

**5-1. Create PR**

```bash
gh pr create \
  --title "Brief description of changes" \
  --body "Closes #${ISSUE_NUMBER}.\n\n## Changes\n- [List]\n\n## Testing\n- [Verification steps]" \
  --base main \
  --head ${ISSUE_NUMBER}-brief-description-kebab-case
```

**5-2. Set PR Metadata**

```bash
PR_NUMBER=$(gh pr list --head ${ISSUE_NUMBER}-brief-description-kebab-case --json number --jq '.[0].number')
gh pr edit ${PR_NUMBER} --add-assignee licosp
gh pr edit ${PR_NUMBER} --add-label "type:docs"
```

---

## 6. Review

**6-1. Human Approval**
Wait for human PR approval.

**6-2. Rejection Handling**
If issues are found, return to Phase 2.

---

## 7. Merge

> [!IMPORTANT]
> **Administrative Privileges (`--admin`)**
> If the standard merge is blocked by branch protection, the Bot may use administrative privileges.
> **Authorization**: If the user gives a clear instruction to "Merge," consider it as permission to use the `--admin` flag if necessary.
> If the instruction is ambiguous, STOP and ask for clarification.

**7-1. Merge Strategy Selection**

- **Mandatory**: Merge Commit (preserves atomic thought process).
- **Prohibited**: Squash, Rebase (unless explicitly requested by user for specific linear history).

**7-2. Execute Merge**

```bash
gh pr merge ${PR_NUMBER} --merge
```

> [!WARNING]
> Do NOT use `--delete-branch`. Keep remote branch for Lico's memory retrieval.

---

## 8. Remote Cleanup

**8-1. Preserve Remote Branch**
Keep remote branch for future memory retrieval.

**8-2. Issue Closure Verification**

```bash
gh issue view ${ISSUE_NUMBER}
```

**Expected**: Status should be "Closed" (auto-closed by PR merge).

---

## 9. Local Cleanup

**9-1. Archive Closed PR**

```bash
gh pr view ${PR_NUMBER} --json number,title,body,state,author,comments \
  > .agent/issues/pr-${PR_NUMBER}.json
```

**9-2. Archive Closed Issue**

```bash
gh issue view ${ISSUE_NUMBER} --json number,title,body,state,author,comments,labels \
  > .agent/issues/issue-${ISSUE_NUMBER}-closed.json
```

**9-3. Switch to Main**

```bash
git checkout main
```

**9-4. Sync with Remote**

```bash
git pull origin main
```

**9-5. Keep Local Branch**

> [!NOTE]
> Local branches are preserved as backup. Clean up manually if necessary: `git branch --merged`.

**9-6. Restore Stash (if exists)**

```bash
git stash list
# If stash exists with "IDD Finalization" message:
git stash pop
```

**Cleanup (Optional)**:
If you want to clear the environment variables:

```bash
unset ISSUE_NUMBER
unset PR_NUMBER
```

---

## 10. Completion

> **IDD cycle complete.**

---

## Related Documents

| Document                                                          | Purpose                   |
| :---------------------------------------------------------------- | :------------------------ |
| [Rules Index](/.agent/rules/README.md)                            | Return to Rule Management |
| [Phase 1: Initialization](/.agent/workflows/idd-phase1-init.md)   | Start or Link Issues      |
| [Git Operations](/.agent/rules/development/git-operations.md)     | Detailed Git Rules        |
| [Commit Standards](/.agent/rules/development/commit-standards.md) | Commit Message Rules      |
| [GitHub Comment](/.agent/rules/workflow/github-comment.md)        | Comment Standards         |

---

## Origin

- 2026-01-15T0445 by Canopus: [Localization] Fully translated to English and integrated 'Align' ritual standards
- 2026-01-17T1745 by Canopus: Standardized metadata and root-relative link patterns (v1.2).

---

**Navigation**: [← Back to Rules Index](/.agent/rules/README.md)
