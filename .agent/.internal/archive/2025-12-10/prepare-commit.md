---
description: Prepare repository for commits following Issue-Driven Development
---

# Pre-Commit Preparation Workflow

This workflow aims to ensure the establishment of the following four relationships:

```
Issue ↔ Branch (Remote) ↔ Branch (Local) ↔ HEAD (Local)
```

## Prerequisites

- GitHub CLI is authenticated (`gh auth status`)
- Inside a Git repository
- Uncommitted changes exist locally

---

## Steps

### 1. Environment Check

```bash
# Verify GitHub CLI authentication
gh auth status

# Verify repository context
git rev-parse --is-inside-work-tree
```

**Expected Result**:
- `gh auth status`: Displays `✓ Logged in to github.com`
- `git rev-parse`: Returns `true`

---

### 2. Investigate Changes

```bash
# Check status of changes
git status

# Check summary of changes
git diff --stat
```

**Expected Result**:
- `git status`: Shows modified or untracked files
- Abort if no changes exist

---

### 3. Create GitHub Issue

**Relationship Established**: `Issue` creation

```bash
# Create issue
gh issue create --title "[Type]: [Short Description]" --body "[Detailed description]"
```

**Parameters**:
- `--title`: `[Type]: [Description]` format (e.g., `refactor: Consolidate Git Rules`)
- `--body`: Detailed explanation of changes
- Type: `feat`, `fix`, `docs`, `refactor`, `chore`, etc. (Conventional Commits compliant)

**Verification**:
```bash
# View created issue
gh issue view <issue-number>
```

**Expected Result**:
- Issue #N is created on GitHub
- Note the issue number (e.g., `#3`)

---

### 4. Create and Checkout Issue-Linked Branch

**Relationship Established**: `Issue ↔ Branch (Remote) ↔ Branch (Local) ↔ HEAD`

```bash
# Create and checkout branch using gh issue develop command
gh issue develop <issue-number> --name <issue-number>-<issue-title-kebab-case> --checkout
```

**Example Parameters**:
```bash
gh issue develop 3 --name 3-refactor-agent-rules-and-git-operations --checkout
```

**Important**: 
- **Always use `gh issue develop`**
- `git checkout -b` + `git push -u origin` **does NOT establish Issue ↔ Branch (Remote) association**
- Branch name format: `<issue-number>-<title-in-kebab-case>`

**Expected Result**:
```
github.com/<owner>/<repo>/tree/<branch-name>
From https://github.com/<owner>/<repo>
 * [new branch]      <branch-name> -> origin/<branch-name>
```

---

### 5. Verify Relationships

#### 5.1 Verify Branch (Local) ↔ HEAD

```bash
git branch
```

**Expected Result**:
```
* 3-refactor-agent-rules-and-git-operations
  main
```

The branch with `*` is the current HEAD.

---

#### 5.2 Verify Branch (Remote) ↔ Branch (Local)

```bash
git branch -vv
```

**Expected Result**:
```
* 3-refactor-agent-rules-and-git-operations a1b2c3d [origin/3-refactor-agent-rules-and-git-operations] Commit message
```

If `[origin/...]` is displayed, remote tracking (upstream) is configured.

---

#### 5.3 Verify Issue ↔ Branch (Remote)

##### Method 1: GitHub CLI

```bash
gh issue view <issue-number> --web
```

Open the Issue page in browser and verify the branch name appears in the "Development" section.

##### Method 2: GitHub API (via CLI)

```bash
gh api repos/:owner/:repo/issues/<issue-number>/timeline | jq '.[] | select(.event=="connected") | .source.issue.pull_request.html_url // .source'
```

**Note**: Visual confirmation via GitHub UI's "Development" section is most reliable for Issue-Branch association.

---

### 6. Analyze and Document Changes

**Purpose**: Create a comprehensive summary of all repository changes for the Issue comment and future commit reference.

#### 6.1 Investigate All Changes

```bash
# View short status
git status --short

# View detailed statistics
git diff --stat
```

#### 6.2 Categorize and Document

Create a changes summary file in `.agent/.internal/issue-<N>-changes-summary.md`:

**Required Structure**:
1. **Overview**: Total files changed, lines added/deleted
2. **Changes by Component**: Group files by logical component (e.g., rules, workflows, config)
3. **Attribute Assignment**: Tag each group with Added/Modified/Deleted
4. **Key Changes**: Highlight major changes and rationale

**Template**:
```markdown
# Repository Changes Summary

## Overview
- **Total Files**: X changed
- **Lines Added**: +Y
- **Lines Deleted**: -Z

## Changes by Component

### 1. Component Name

#### Added
- file1.md - Description

#### Modified
- file2.md - Description

#### Deleted
- file3.md - Rationale

## Summary by Attribute
| Attribute | Count | Description |
|-----------|-------|-------------|
| Added     | X     | ...         |
| Modified  | Y     | ...         |
| Deleted   | Z     | ...         |

## Key Changes
1. Major change description
```

#### 6.3 Post Summary to Issue

```bash
# Post the summary as a comment
gh issue comment <issue-number> --body-file .agent/.internal/issue-<N>-changes-summary.md
```

**Purpose**: 
- Documents work scope on GitHub
- Provides reference for commit planning
- Creates audit trail of changes

---

## Completion Checklist

Verify that **all** of the following are satisfied:

- [ ] **Issue**: GitHub Issue #N exists (`gh issue view N`)
- [ ] **Issue ↔ Branch (Remote)**: Branch name appears in GitHub UI's "Development" section
- [ ] **Branch (Remote)**: `origin/N-issue-title` exists (`git branch -r | grep N-issue-title`)
- [ ] **Branch (Remote) ↔ Branch (Local)**: Tracking is established (`git branch -vv` shows `[origin/...]`)
- [ ] **Branch (Local) ↔ HEAD**: Target branch is checked out (`git branch` shows `*`)
- [ ] **Changes Documented**: Summary file created and posted to Issue (`gh issue view N` shows comment)

---

## Troubleshooting

### Issue: Cannot verify Issue ↔ Branch (Remote) association

**Cause**: Used `git checkout -b` + `git push -u`

**Solution**:
1. Delete branch and start over
   ```bash
   git checkout main
   git branch -D <branch-name>
   git push origin --delete <branch-name>
   ```

2. Recreate with `gh issue develop`
   ```bash
   gh issue develop <issue-number> --name <branch-name> --checkout
   ```

### Issue: Work-in-progress changes disappeared

**Cause**: Changes were stashed during branch switch

**Solution**:
```bash
git stash list
git stash pop
```

---

## Next Steps

Once this preparation is complete, execute the commit workflow.。
