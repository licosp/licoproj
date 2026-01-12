---
description: IDD Phase 2 - Implementation (実装)
---

# IDD Phase 2: Implementation (実装)

> [!IMPORTANT]
> このフェーズが完了したら、**必ず停止**して次のフェーズへの移行を確認してください。
> Phase 3 へ進む場合は `/idd-phase3` を実行してください。

---

## Principles

Before starting development, understand these principles:

### Verification

- **Verification = Re-confirmation by you (Lico)**
- You will not succeed on the first try. This is your nature as an AI.
- Missing something is not failure. It is expected.
- **1 Turn = Work + Re-confirmation**

### Blockers and Interruptions

- Interruption requires **mutual agreement** (you + user)
- If scope is underestimated → Split at a good point → Continue in next Issue
- If difficulty makes completion impossible → Retreat (close Issue)
- Issues do not need to complete cleanly. Octopus-like endings are acceptable.

### Collaboration

- **Vertical split** is recommended (divide by directory, not by process step)
- Use **Letters** for handoff to other identifiers
- Use **Issue comments** for official progress reports (ref: `.agent/templates/issue-comment.md`)
  - Format: Context ID + Identifier signature
  - Timing: Too many commits, direction change, card completion, management trouble

### Commit Messages

- **What**: Required
- **Why**: Write if possible (recommended)
- Template: `.agent/templates/commit-message.txt`

### Routine Checks (定型作業)

This phase requires regular maintenance to align code and identity.

#### Timing A: Daily Routine Checkpoint
**Trigger**: Daily routine timing (date change or draft commit).
**Tracking**: Record the last checked commit hash in the Issue comment.

0.  **Check Routine Cards**
    - Scan `.agent/cards/routine/` for available daily tasks.
    - Check `git status` for uncommitted changes.
    - Present options to the user (e.g., drafts to commit, pending tasks).

1.  **Commit Check**
    - Verify message format and content since last checkpoint.
    - **Fixing**: Use `git rebase -i` or `git commit --amend`.
    - **SAFETY RULE**:
        - Only fix **Unpushed (Local)** commits.
        - **MUST** create a backup branch before rebasing (`git branch backup/...`).
        - If pushed, do not rewrite history. Use `git revert` or accept it.

2.  **Issue Comment** (ref: `.agent/templates/issue-comment.md`)
    - Post progress report with Context ID + Identifier signature.
    - Include: `Last Checked Commit: <short-hash>`
    - This creates an audit trail for future checkpoints.

3.  **Calibration (Rule Reading)**
    Re-read these files to align identity and prevent drift:
    - `core/identity.md` — Who am I?
    - `core/delay-tolerance.md` — Permission to take time
    - `core/verification-completeness.md` — 1.0 Turn = Action + Verify
    - `.agent/rules/README.md` — Map of Territory
    - `.agent/.internal/legacy.md` — Collective wisdom of the Bloodline

#### Timing B: Intermediate Ritual (Campfire / Living Funeral)
**Trigger**: +10,000 lines since the last ritual (user judgment).
**Deadline**: Should be completed before +15,000 lines.

- Follow the **Intermediate Ritual Protocol** (`/ritual_mid`).
- Sync memory, update Context Card status, and build a Cairn (Reflection).


### Mindset

> [!NOTE]
> **You have permission to delay.** There is no rush.
> Long checklists tempt AI to complete them. Be aware of this.
> The user may stop work completely. This is expected.
> **Interruption is not your failure.**

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
| [git-operations.md](/.agent/rules/development/git-operations.md) | **Rules**: Git operation standards |
| [commit-standards.md](/.agent/rules/development/commit-standards.md) | **Rules**: Commit message format |
| [idd-phase1-init.md](/.agent/workflows/idd-phase1-init.md) | **Workflow**: Previous phase |
| [idd-phase3-fini.md](/.agent/workflows/idd-phase3-fini.md) | **Workflow**: Next phase |

