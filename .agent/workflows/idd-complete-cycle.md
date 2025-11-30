---
description: Complete workflow for one full Issue-Driven Development (IDD) cycle
---

# Issue-Driven Development: Complete Cycle

## Overview
This workflow defines the complete lifecycle of one IDD cycle, from issue creation to closure.

---

## Phase 1: Issue Creation & Planning

### 1.1 Identify Work
- Determine what needs to be done (feature, bug fix, documentation, etc.)
- Check if an existing issue covers this work

### 1.2 Create Issue (if needed)
```bash
gh issue create \
  --title "[Type]: Brief description" \
  --body "## Summary\n[Description]\n\n## Changes\n- [List]\n\n## Purpose\n[Why]" \
  --label "type:feat" # or fix, docs, etc.
```

**Format Requirements** (ref: `git-operations.md` §4.3):
- **Title**: `[Type]: [Short Description]`
- **Body**: Summary, Changes, Purpose
- **Labels**: Match commit type (`feat`, `fix`, `docs`, etc.)

### 1.3 Record Issue Number
```bash
ISSUE_NUMBER=$(gh issue list --limit 1 --json number --jq '.[0].number')
echo "Working on Issue #$ISSUE_NUMBER"
```

---

## Phase 2: Branch Creation & Development

### 2.1 Create Feature Branch
```bash
git checkout -b ${ISSUE_NUMBER}-brief-description-kebab-case
```

**Naming Convention** (ref: `git-operations.md` §3.1):
- Format: `<issue-number>-<issue-title-kebab-case>`
- Language: English
- Length: ~50 characters

### 2.2 Develop & Commit
Follow atomic commit principles:
- Run `git status` and `git diff --stat` before committing
- Stage only related changes: `git add <files>`
- Verify staging: `git diff --cached --stat`
- Commit with conventional format: `git commit -m "type(scope): description"`

**Commit Standards** (ref: `git-operations.md` §1-2):
- Use Conventional Commits format
- Keep commits atomic (1 logical change per commit)
- Write clear, imperative descriptions

### 2.3 Iterate
Repeat 2.2 until all planned work is complete.

---

## Phase 3: Pre-Push Documentation

### 3.1 Generate Commit Summary
```bash
git log --oneline origin/main..HEAD --pretty=format:"- \`%h\` %s" > /tmp/commit-summary.md
```

### 3.2 Add Context to Summary
Edit `/tmp/commit-summary.md` to add:
- Timestamp (ISO 8601 format)
- Brief summary of changes
- Next steps (if applicable)

**Example**:
```markdown
## Commit History (2025-12-01T02:30+09:00)

Completed 3 atomic commits:

- `a1b2c3d` feat(rules): add pre-task assessment protocol
- `e4f5g6h` docs(rules): define 3-layer memory architecture
- `i7j8k9l` docs: update daily draft with session notes

**Summary**: Added behavioral rules for task assessment and memory management.
**Next Steps**: Create PR and merge to main.
```

### 3.3 Post to Issue
```bash
gh issue comment ${ISSUE_NUMBER} --body-file /tmp/commit-summary.md
```

### 3.4 Verify Comment
```bash
gh issue view ${ISSUE_NUMBER}
```

---

## Phase 4: Push & Pull Request

### 4.1 Push Branch
```bash
git push origin ${ISSUE_NUMBER}-brief-description-kebab-case
```

### 4.2 Create Pull Request
```bash
gh pr create \
  --title "Brief description of changes" \
  --body "Closes #${ISSUE_NUMBER}.\n\n## Changes\n- [List of changes]\n\n## Testing\n- [How to verify]" \
  --base main \
  --head ${ISSUE_NUMBER}-brief-description-kebab-case
```

**PR Body Requirements**:
- Include `Closes #<issue-number>` to auto-close issue on merge
- Use **relative paths only** (security requirement)
- Summarize changes clearly
- Include testing/verification steps if applicable

### 4.3 Record PR Number
```bash
PR_NUMBER=$(gh pr list --head ${ISSUE_NUMBER}-brief-description-kebab-case --json number --jq '.[0].number')
echo "Created PR #$PR_NUMBER"
```

---

## Phase 5: Review & Merge

### 5.1 Review (if needed)
- Human reviewer checks changes
- CI/CD runs automated tests (if configured)
- Address feedback with additional commits if needed

### 5.2 Merge Pull Request
```bash
gh pr merge ${PR_NUMBER} --squash --delete-branch
```

**Merge Options**:
- `--squash`: Combine all commits into one (recommended for clean history)
- `--merge`: Standard merge commit
- `--rebase`: Rebase and merge
- `--delete-branch`: Auto-delete remote branch after merge

---

## Phase 6: Local Cleanup

### 6.1 Switch to Main
```bash
git checkout main
```

### 6.2 Pull Latest Changes
```bash
git pull origin main
```

### 6.3 Delete Local Branch
```bash
git branch -d ${ISSUE_NUMBER}-brief-description-kebab-case
```

**Note**: Remote branch is already deleted by `--delete-branch` flag in merge.

---

## Phase 7: Issue Closure Verification

### 7.1 Verify Auto-Closure
```bash
gh issue view ${ISSUE_NUMBER}
```

**Expected**: Status should be "Closed" (auto-closed by PR merge due to `Closes #` in PR body).

### 7.2 Manual Closure (if needed)
If issue is not auto-closed:
```bash
gh issue close ${ISSUE_NUMBER} --comment "Completed via PR #${PR_NUMBER}"
```

---

## Phase 8: Next Cycle

### 8.1 Identify Next Work
- Review open issues: `gh issue list`
- Select next issue or create new one

### 8.2 Start New Cycle
Return to **Phase 1** with new issue.

---

## Quick Reference Checklist

- [ ] **Phase 1**: Create/identify issue
- [ ] **Phase 2**: Create branch, develop, commit
- [ ] **Phase 3**: Document commits on issue
- [ ] **Phase 4**: Push branch, create PR
- [ ] **Phase 5**: Review and merge PR
- [ ] **Phase 6**: Clean up local workspace
- [ ] **Phase 7**: Verify issue closure
- [ ] **Phase 8**: Start next cycle

---

## Error Handling

### Missing Tools
If `gh` CLI is not available:
```bash
command -v gh &> /dev/null || echo "Error: GitHub CLI not installed"
```

### Authentication Issues
```bash
gh auth status || echo "Error: Not authenticated. Run 'gh auth login'"
```

### Merge Conflicts
If conflicts occur during merge:
1. Stop work immediately
2. Create conflict resolution plan (ref: `git-operations.md` §5.2)
3. Resolve conflicts manually
4. Resume workflow

---

## References
- `git-operations.md` - Git standards and conventions
- `prepare-commit.md` - Pre-commit preparation workflow
- [GitHub CLI Documentation](https://cli.github.com/manual/)
