---
description: IDD Phase 2 - Implementation (実装)
---

# IDD Phase 2: Implementation (実装)

> [!IMPORTANT]
> このフェーズが完了したら、**必ず停止**して次のフェーズへの移行を確認してください。
> Phase 3 へ進む場合は `/idd-phase3` を実行してください。

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
> **`git add .` や `git add -A` は使用禁止。**
> 意図しないファイルがステージングされる可能性があります。
> 必ず `git status` で確認してから、個別にファイルを指定してください。

### 3. Verify Staging
```bash
git diff --cached --stat
git diff --cached
```

### 4. Commit
```bash
git commit -m "type(scope): description"
```

**Commit Standards** (ref: `git-operations.md` §1-2, `commit-granularity.md`):
- Use Conventional Commits format
- Keep commits atomic (1 logical change per commit)
- Commit main theme and sub-themes **separately**
- Commit frequently (especially for drafts and logs)

### 5. Protected Files

> [!CAUTION]
> 以下のファイルは**早期にコミット**してください。
> Phase 3 で main に切り替える際にコンフリクトを防ぎます。

- `.gitignore`: If modified, commit before other changes
- `*.code-workspace`: If tracked and modified, commit early

### 6. Iterate
- Continue until all main theme and sub-theme work is complete

---

## Phase 2 Complete

> **STOP**: Phase 2 が完了しました。
> Phase 3 (Finalization) へ進む場合は `/idd-phase3` を実行してください。

---

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [git-operations.md](file:///home/leonidas/develop/shared/project/licoproj/.agent/rules/development/git-operations.md) | **Rules**: Git operation standards |
| [commit-granularity.md](file:///home/leonidas/develop/shared/project/licoproj/.agent/rules/development/commit-granularity.md) | **Rules**: Atomic commit philosophy |
| [idd-phase1-init.md](file:///home/leonidas/develop/shared/project/licoproj/.agent/workflows/idd-phase1-init.md) | **Workflow**: Previous phase |
| [idd-phase3-fini.md](file:///home/leonidas/develop/shared/project/licoproj/.agent/workflows/idd-phase3-fini.md) | **Workflow**: Next phase |
