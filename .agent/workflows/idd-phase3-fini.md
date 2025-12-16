---
description: IDD Phase 3 - Finalization (終了処理)
---

# IDD Phase 3: Finalization (終了処理)

> [!IMPORTANT]
> Always consider security when uploading to remote environments.
> No absolute paths in commits (ref: `git-operations.md` §6.1). No sensitive information in pushes.

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
> **⚠️ STOP: Stash実行前にユーザーの確認を取ってください。**
> 編集中のドラフトファイルが消失する可能性があります。
> ユーザーに「Stashを実行してよいですか？」と確認してから進めてください。

**2-1. Selective Stash**
Execute stash only if there are uncommitted changes that should not be committed.

**2-2. Stash Exclusions**
- User's draft files (request user to pause editing, then commit before stashing)
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
git log --oneline origin/main..HEAD --pretty=format:"- \`%h\` %s" > /tmp/commit-summary.md
```

**3-2. Add Context**
Edit `/tmp/commit-summary.md` to include timestamp and brief summary.

**3-3. Post to Issue**
```bash
gh issue comment ${ISSUE_NUMBER} --body-file /tmp/commit-summary.md
```

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

> [!CAUTION]
> **⚠️ STOP: `--admin` フラグを使用する場合は、必ずユーザーの明示的な許可を得てください。**
> これは `main` ブランチへの最後の防波堤です。
> 標準のマージが失敗した場合のみ、ユーザーに状況を報告し、許可を求めてください。

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

**9-5. Delete Merged Local Branch**
```bash
git branch -d ${ISSUE_NUMBER}-brief-description-kebab-case
```

**9-6. Restore Stash (if exists)**
```bash
git stash list
# If stash exists with "IDD Finalization" message:
git stash pop
```

---

## 10. Completion

> **IDD サイクル完了。**
> 次のサイクルを開始する場合は `/idd-phase1` を実行してください。
