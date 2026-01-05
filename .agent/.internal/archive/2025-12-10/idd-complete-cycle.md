---
description: Complete workflow for one full Issue-Driven Development (IDD) cycle
---

> [!WARNING]
> **DEPRECATED**: このファイルは参照用です。
> 実行時は以下の分割ファイルを使用してください:
> - `/idd-phase1` → `idd-phase1-init.md`
> - `/idd-phase2` → `idd-phase2-impl.md`
> - `/idd-phase3` → `idd-phase3-fini.md`

# Issue-Driven Development: Complete Cycle

## Overview
IDD (Issue-Driven Development) is structured into **3 main phases**:
1. **Initialization** (開始処理): Prepare the work environment
2. **Implementation** (イシューのテーマの実現): Achieve the issue's goal
3. **Finalization** (終了処理): Integrate and close the issue

---

## Phase 1: Initialization (開始処理)

### 1. Environment Verification
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

### 2. Theme Design
**2-1. Define Main Theme**
- Identify the primary goal of the issue (e.g., "Add pre-task assessment protocol")
- Ensure the theme is clear and focused

**2-2. Identify Sub-Themes**
- List changes unrelated to the main theme but necessary for synchronization
- Examples: Draft updates, `.gitignore` adjustments, typo fixes
- **Note**: Sub-themes will be committed separately (ref: `commit-granularity.md`)

### 3. Issue Creation
**3-1. Prepare Issue Elements**
- **Title**: `[Type]: Brief description` (e.g., `[Feat]: Add pre-task assessment`)
- **Body**: Summary, Changes, Purpose
- **Assignees**: Assign to yourself or team members
- **Labels**: Match commit type (`feat`, `fix`, `docs`, etc.)

**3-2. Create Issue**
```bash
gh issue create \
  --title "[Feat]: Add pre-task assessment protocol" \
  --body "## Summary\n...\n\n## Changes\n...\n\n## Purpose\n..." \
  --assignee licosp
```

**3-3. Record Issue Number**
```bash
ISSUE_NUMBER=$(gh issue list --limit 1 --json number --jq '.[0].number')
echo "Working on Issue #$ISSUE_NUMBER"
```

**3-4. Assign Labels (after creation)**
Labels are assigned after issue creation to handle cases where labels may not exist.
```bash
# Add labels autonomously based on issue type
gh issue edit ${ISSUE_NUMBER} --add-label "type:feat"
# If label doesn't exist, create it first or choose existing labels
```

### 4. Branch Creation
**4-1. Fetch Latest Remote State**
```bash
git fetch origin
```

**4-2. Create Local Branch from Remote Main**
```bash
git checkout -b ${ISSUE_NUMBER}-brief-description-kebab-case origin/main
```

**Naming Convention** (ref: `git-operations.md` §3.1):
- Format: `<issue-number>-<issue-title-kebab-case>`
- Language: English
- Length: ~50 characters

**4-3. Push Branch and Set Upstream Tracking**
```bash
git push -u origin ${ISSUE_NUMBER}-brief-description-kebab-case
```

### 5. Initial State Verification
**5-1. Check Current Branch Status**
```bash
git status
```

**5-2. Verify Feasibility**
- Confirm that main theme and sub-themes can be implemented
- Check for potential conflicts or blockers

### 6. Early Problem Detection
**6-1. Identify Issues**
- List any problems discovered during verification
- Document technical constraints or dependencies

**6-2. Record in Issue Comments**
```bash
gh issue comment ${ISSUE_NUMBER} --body "## Initial Assessment\n- Problem: ...\n- Solution: ..."
```

**6-3. Backup Issue Locally**
```bash
gh issue view ${ISSUE_NUMBER} --json title,body,comments > .agent/issues/issue-${ISSUE_NUMBER}-backup.json
```

---

## Phase 2: Implementation (イシューのテーマの実現)

### Development Cycle
Repeat the following until all planned work is complete:

**1. Make Changes**
- Implement features, fix bugs, or update documentation
- Focus on one logical change at a time

**2. Stage Changes**
```bash
git add <files>
```

**3. Verify Staging**
```bash
git diff --cached --stat
git diff --cached
```

**4. Commit**
```bash
git commit -m "type(scope): description"
```

**Commit Standards** (ref: `git-operations.md` §1-2, `commit-granularity.md`):
- Use Conventional Commits format
- Keep commits atomic (1 logical change per commit)
- Commit main theme and sub-themes **separately**
- Commit frequently (especially for drafts and logs)

**Protected Files** (commit early to prevent Phase 3 sync conflicts):
- `.gitignore`: If modified, commit before other changes
- `*.code-workspace`: If tracked and modified, commit early
- These files can cause conflicts when switching to main in Phase 3

**5. Iterate**
- Continue until all main theme and sub-theme work is complete

---

## Phase 3: Finalization

> [!IMPORTANT]
> Always consider security when uploading to remote environments.
> No absolute paths in commits (ref: `git-operations.md` §6.1). No sensitive information in pushes.

### 1. Preparation

**1-1. Tool Re-verification**
Re-verify tool connectivity since time has passed since initialization.
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

### 2. Working Directory Cleanup

**2-1. Selective Stash**
Execute stash only if there are uncommitted changes that should not be committed.

**2-2. Stash Exclusions**
Exclude the following files from stash:
- **2-2-A**: User's draft files (updated every few seconds)
  - Request user to pause editing, then commit before stashing
- **2-2-B**: VSCode workspace settings (`*.code-workspace`)
  - Likely attached; file changes cause detachment
- **2-2-C**: `.gitignore`
  - Stashing this file disables ignore rules, exposing all untracked files

> [!WARNING]
> If protected files (`.gitignore`, `*.code-workspace`) have uncommitted changes,
> they will be OVERWRITTEN when switching to main in Step 9.
> **Commit these files first** in Phase 2, or back them up manually.

**Technical Implementation**:
```bash
# Stash excluding protected files
git stash push -m "IDD Finalization" -- . ':(exclude)*.code-workspace' ':(exclude).gitignore'
```

---

### 3. Pre-Push Documentation

**3-1. Generate Commit Summary**
```bash
git log --oneline origin/main..HEAD --pretty=format:"- \`%h\` %s" > /tmp/commit-summary.md
```

**3-2. Add Context**
Edit `/tmp/commit-summary.md` to include:
- Timestamp (ISO 8601 format)
- Brief summary of changes
- Next steps (if applicable)

**3-3. Post to Issue**
```bash
gh issue comment ${ISSUE_NUMBER} --body-file /tmp/commit-summary.md
```

**3-4. Verify Comment**
```bash
gh issue view ${ISSUE_NUMBER}
```

---

### 4. Push Branch

```bash
git push origin ${ISSUE_NUMBER}-brief-description-kebab-case
```

---

### 5. Create Pull Request

**5-1. Prepare PR Document**
- **5-1-A**: Analyze changes across the Issue and create optimal title and body
- **5-1-B**: Include summary and related Issue information

**5-2. Create PR**
```bash
gh pr create \
  --title "Brief description of changes" \
  --body "Closes #${ISSUE_NUMBER}.\n\n## Changes\n- [List]\n\n## Testing\n- [Verification steps]" \
  --base main \
  --head ${ISSUE_NUMBER}-brief-description-kebab-case
```

**PR Requirements**:
- Include `Closes #<issue-number>` to auto-close issue on merge
- Use **relative paths only** (security requirement)
- Summarize main theme and sub-themes clearly

**5-3. Set PR Metadata**
```bash
PR_NUMBER=$(gh pr list --head ${ISSUE_NUMBER}-brief-description-kebab-case --json number --jq '.[0].number')

# Assignees: licosp (Lico's account)
gh pr edit ${PR_NUMBER} --add-assignee licosp

# Labels: Same as Issue (autonomous selection)
gh pr edit ${PR_NUMBER} --add-label "type:docs"
```

---

### 6. Review

**6-1. Human Approval**
Wait for human PR approval.

**6-2. Rejection Handling**
If issues are found, return to the appropriate IDD phase (usually Phase 2).

---

### 7. Merge

**7-1. Merge Strategy Selection**
- **Default**: Merge Commit (preserves history)
- **Avoid**: Squash, Rebase (loses atomic commit thought process)

**7-2. Execute Merge**
```bash
gh pr merge ${PR_NUMBER} --merge
```

> [!WARNING]
> Do NOT use `--delete-branch`. Keep remote branch for Lico's memory retrieval.

---

### 8. Remote Cleanup

**8-1. Preserve Remote Branch**
Keep remote branch for Lico's future memory retrieval.

**8-2. Preserve PR**
Keep PR as well. Only verify closure, do NOT delete.

**8-3. Issue Closure Verification**
```bash
gh issue view ${ISSUE_NUMBER}
```
**Expected**: Status should be "Closed" (auto-closed by PR merge).

**Manual Closure (if needed)**:
```bash
gh issue close ${ISSUE_NUMBER} --comment "Completed via PR #${PR_NUMBER}"
```

---

### 9. Local Cleanup

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

**9-5. Delete Merged Local Branch**
```bash
git branch -d ${ISSUE_NUMBER}-brief-description-kebab-case
```

**9-6. Restore Stash (if exists)**
Check for stash from this cycle and restore if needed.
```bash
git stash list
# If stash exists with "IDD Finalization" message:
git stash pop
```

---

### 10. Completion

**10-1. Next Cycle**
Proceed to the next IDD cycle.

---

## Phase 4: Next Cycle

### Start New Work
**1. Identify Next Issue**
```bash
gh issue list
```

**2. Return to Phase 1**
Begin a new IDD cycle with the next issue.

---

## Quick Reference Checklist

### Phase 1: Initialization
- [ ] Verify tools and authentication
- [ ] Define main theme and sub-themes
- [ ] Create issue
- [ ] Create branch from `origin/main`
- [ ] Push branch and set upstream
- [ ] Verify feasibility
- [ ] Document problems (if any)

### Phase 2: Implementation
- [ ] Make changes
- [ ] Stage and verify
- [ ] Commit (atomic, frequent)
- [ ] Repeat until complete

### Phase 3: Finalization
- [ ] 1. Verify tools and progress
- [ ] 2. Stash unrelated changes (exclude .code-workspace)
- [ ] 3. Document commits to Issue
- [ ] 4. Push branch
- [ ] 5. Create PR (with metadata)
- [ ] 6. Wait for human review
- [ ] 7. Merge (use --merge, NOT --squash)
- [ ] 8. Verify remote cleanup (keep branch/PR)
- [ ] 9. Archive PR/Issue locally, cleanup local branch
- [ ] 10. Next cycle

---

## Error Handling

### Missing Tools
```bash
command -v gh &> /dev/null || echo "Error: GitHub CLI not installed"
```

### Authentication Issues
```bash
gh auth status || echo "Error: Not authenticated. Run 'gh auth login'"
```

### Merge Conflicts
If conflicts occur:
1. Stop work immediately
2. Create conflict resolution plan (ref: `git-operations.md` §5.2)
3. Resolve conflicts manually
4. Resume workflow

---

## References
- `git-operations.md` - Git standards and conventions
- `commit-granularity.md` - Atomic commit philosophy
- `prepare-commit.md` - Pre-commit preparation workflow
- [GitHub CLI Documentation](https://cli.github.com/manual/)

---
*Generated by Lico (Model: Claude 3.5 Sonnet) on 2025-12-01*
