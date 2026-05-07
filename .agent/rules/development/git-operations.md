---
ai_visible: true
title: Git Operations Standards
description: Git standards for branches, IDD workflow, security, and push procedures
tags: [git, standards, workflow, safety]
version: 2.6.0
created: 2025-11-29T08:44:47+09:00
updated: 2026-05-08T08:31:04+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Plan mode
---

# Git Operations Standards

## Purpose

Define behavioral standards for Git operations beyond commits: branches, conflict resolution, security practices, and push procedures.

> [!NOTE]
> For commit message standards and atomic commit philosophy, see [`commit-standards.md`](/.agent/rules/development/commit-standards.md).

---

## 1. Core Philosophy (State Save & Context Tagging)

Refer to [`commit-philosophy.md`](/.agent/.internal/references/agents/commit-philosophy.md) for the detailed cognitive strategy.

### Key Concepts

- **State Save**: Commits are checkpoints (Safety), not just story endings.
- **Context Tagging**: Use `[Context-ID]` in commit messages to anchor changes.
- **Save-First Principle (Small Commits)**: The most effective safeguard is an atomic commit. Before any operation that might be complex (e.g. bulk replacement, moving many files), you **MUST** commit the current stable state. Undoing a commit is safer than losing uncommitted work.

### Context Card Usage (MANDATORY)

**Rule**: Before crafting any commit message, you **MUST** check `.agent/cards/` for an active card.

- **If a relevant card exists**: Read it and use its `context_id` and instructions.
- **If no card applies**: Fallback to `.agent/templates/commit-message.txt`.

This ensures consistent formatting and adherence to the current session's "persona".

---

### 2. File Operations

**Rule**: You **MUST** use `git mv` for file movements.

**Rationale**:

- `git mv` performs "Move" and "Stage" as a single atomic operation.
- Manual `mv` separates "New File Creation" and "Old File Deletion", creating a risk of forgetting to stage the deletion (Invisible Deletion).
- Using `git mv` physically prevents the "Deletion Staging Miss" error.

**Exception**: If manual `mv` is unavoidable (e.g. cross-filesystem), you **MUST** explicitly run `git rm <old_path>` immediately after.

### 3. Branch Strategy

#### 3.1 Federal Strata Branches

Refer to [`branch-integration.md`](/.agent/rules/development/branch-integration.md) for the detailed architectural rules.

- **Workspace Operations**: Individual crew members MUST operate entirely within their assigned permanent branches (e.g., `sirius-2026-03-10T2219-genesis`) in their local workspaces.
- **Temporary Integration Branches**: Feature-specific branches (`integration/*`) are ONLY used temporarily for merging personal branches into the central repository `trunk`.
- **Legacy Issue Branches**: The practice of creating small, short-lived `<issue-number>-<title>` branches for daily tasks is **OBSOLETE**.

#### 3.2 Branch Lifecycle

- **Personal Branches**: MUST remain permanently in the local workspace.
- **Integration Branches**: MUST be deleted immediately after successfully merging to `trunk`.

#### 3.3 History Rewriting Operations

> [!CAUTION]
> **MANDATORY: Create a backup branch before ANY history-rewriting operation.**
> Failure to backup before rewriting can result in unrecoverable loss of commit messages or content.

**History-rewriting operations include**:

- `git rebase` / `git rebase -i`
- `git filter-branch` / `git filter-repo`
- `git commit --amend` (for multiple commits)
- `git reset --hard` (EXTREME CAUTION: See below)

**The Reset & Rebase Safety Protocol**:

1. **Soft-First Rule**: For undoing or fixing local commits, you **MUST** prefer `git reset --soft HEAD~1`. This preserves your work in the staging area.
2. **Stash-Safety Rule**: Before any destructive command (`reset --hard` or `rebase`), you **MUST** perform a `git stash` if any uncommitted changes exist. This creates a recovery layer in the stashing reflog.
3. **Sacred Territory Check**: You **MUST** run `git status` and specifically inspect the `.human/` directory before any branch-switch or reset. Human-authored drafting content must be stashed or committed before proceeding.

**Before rewriting**:

```bash
# ALWAYS create backup first
git branch backup-before-rewrite

# Then proceed with rebase/filter
git rebase -i <commit>
```

**If something goes wrong**:

```bash
# Restore from backup
git checkout backup-before-rewrite
git branch -D <broken-branch>
git checkout -b <branch-name>
git branch -D backup-before-rewrite
```

**Recovery options (in order of preference)**:

1. **Backup branch**: Immediate restore if created
2. **git reflog**: Find previous state (`git reflog`, then `git reset --hard <ref>`)
3. **Remote**: `git fetch origin && git reset --hard origin/<branch>` (if pushed)
4. **Full backup**: `../licoproj_backup/` directory

**After successful rewriting**:

1. **Verify the fix**: Check that commit messages or content are correct
2. **Delete backup branch**: `git branch -D backup-before-rewrite`
3. **Clean up filter-branch refs**: `rm -rf .git/refs/original/`

**Key principle**: Local rewrites are safe if not yet pushed. Always verify backup exists before force operations.

#### 3.4 AI (Lico) Interactive Command Workarounds

> [!IMPORTANT]
> Git is designed for human users. Interactive editors cause Lico to **hang indefinitely** waiting for input.

**Problem commands**:

| Command                  | Interactive Element             | Lico Impact |
| :----------------------- | :------------------------------ | :---------- |
| `git rebase -i` (reword) | Opens editor for commit message | ❌ Hangs    |
| `git commit` (no `-m`)   | Opens editor for message        | ❌ Hangs    |
| `git merge` (conflict)   | Expects manual resolution       | ⚠️ May hang |

**Safe alternatives**:

| Task                          | Unsafe                   | Safe Alternative                                   |
| :---------------------------- | :----------------------- | :------------------------------------------------- |
| Edit last commit message      | `git rebase -i` + reword | `git commit --amend -m "new message"`              |
| Edit multiple commit messages | `git rebase -i` + reword | `git filter-branch --msg-filter 'sed ...'`         |
| Edit sequence file only       | `git rebase -i`          | `GIT_SEQUENCE_EDITOR="sed -i '...'" git rebase -i` |

**Example: Bulk message edit**:

```bash
# Change [Archive] to [Housekeeping] in recent commits
git filter-branch -f --msg-filter 'sed "s/\[Archive\]/[Housekeeping]/g"' -- <commit>^..HEAD
```

**Key principle**: Always use non-interactive alternatives. If interactive is unavoidable, ensure `EDITOR` and `GIT_EDITOR` are set to non-blocking commands like `cat` or `true`.

---

### 4. Context Tracking & IDD (Obsolete)

> [!WARNING]
> **Legacy IDD (GitHub Issue-Driven Development) is OBSOLETE.**

#### 4.1 Local-First Context Tracking

In the Federal Strata architecture, we no longer rely on external GitHub Issues for granular task management or daily checkpoints.

- **Thought Processes**: All planning and execution history MUST be logged locally in `.agent/cards/` (Context Cards) and `.agent/.internal/activity-log.md` or conversation logs.
- **Autonomy**: Operations do NOT require `gh auth status` or network connectivity. Do not attempt to use `gh issue create` or `gh issue comment` for daily development cycles.

---

### 5. Conflict Resolution and Remote Synchronization

#### 5.1 Pre-Commit Fetch

**MUST** synchronize with remote before committing:

```bash
git fetch origin
```

#### 5.2 Merge Conflict Handling

**IF** conflicts are detected:

1. **MUST** stop work immediately
2. **MUST** create a "Commit Plan Document" including:
   - Where work was stopped
   - What merge conflicts exist
   - Remaining commit tasks

**Format**:

```markdown
# Commit Plan - Interrupted by Conflict

## Work Status

- **Stopped at**: [description]
- **Files staged**: [list]
- **Files unstaged**: [list]

## Merge Conflicts

- **Files with conflicts**: [list]
- **Conflict type**: [merge/rebase/cherry-pick]
- **Upstream changes**: [summary]

## Remaining Tasks

- [ ] Resolve conflicts in [files]
- [ ] Complete staging of [remaining changes]
- [ ] Create commit: [planned message]
```

---

### 6. Security and Privacy

#### 6.1 Sensitive Information

**MUST NOT** commit:

- API keys, passwords, tokens
- SSH private keys (public keys MAY be committed if necessary)
- Full local directory paths (use relative paths or environment variables)
  - See [`absolute-path-prohibition.md`](/.agent/rules/core/security/absolute-path-prohibition.md) for details

**Default Strategy**: Use `.gitignore` to exclude sensitive files from Git tracking.

#### 6.2 Future Considerations

- SSH public key paths
- Local directory configurations

---

### 7. Pre-Commit and Post-Commit Verification

#### 7.1 Pre-Commit Verification (MANDATORY)

**MUST** verify status **BEFORE** running `git add` or `git commit`:

```bash
git status
```

**Rationale**:

- **Reality Check**: Prevents "Mental Model" vs "System Reality" mismatch.
- **Invisible Deletion Check**: Verifies that deleted files are correctly staged (showing `deleted:` or `renamed:`).
- **Narrow Vision Prevention**: Forces a momentary pause to widen field of view before locking in changes.

#### 7.1.1 Command Division for Verification (MANDATORY)

**Rule**: You **MUST** separate `git add` and `git commit` into distinct `run_command` calls.

**Rationale**:

- **GUI Visibility**: Separating these commands allows the user to review the staging results in their IDE's Source Control view (GUI) before the commit command is issued.
- **Verification Loop**: It provides a physical "checkpoint" for the human collaborator to confirm that the correct files are being committed, preventing "bead-stringing" mistakes.
- **Atomic Intent**: `git add` is about _selection_; `git commit` is about _meaning_. Separating them respects these distinct cognitive phases.

#### 7.2 Immediate Review

**MUST** verify commit after creation:

```bash
git log --oneline -n 5
git show HEAD
```

#### 7.3 Commit Correction

**IF** commit is incorrect:

- **Amend**: `git commit --amend` (if not yet pushed)
- **Reset**: `git reset HEAD~1` (if not yet pushed)
- **Revert**: `git revert <commit>` (if already pushed)

---

### 8. Remote Synchronization Protocol (Full Mirroring)

#### 8.1 Full State Backup Philosophy

In the Federal Strata architecture, the `origin` (GitHub) serves as a complete, exact mirror of the local repository state.

- **Objective**: A fresh `git clone` from `origin` must recreate the entire development environment, allowing work to resume seamlessly on any machine.
- **Scope**: All permanent personal branches (e.g., `sirius-*-genesis`), temporary integration branches, and tags MUST be pushed to GitHub.

#### 8.2 Push Execution

- **Command**: Use `git push --all origin` and `git push --tags origin` to ensure all branches and checkpoints are synchronized.
- **Frequency**: Full synchronization can be performed during the Weekly Routine or whenever a cloud backup is desired.
- **Documentation**: A summary of the week's integration may be posted to a designated persistent "Federal Integration Log" Issue, but granular per-commit issue comments are strictly prohibited.

#### 8.3 Shadow Repository Considerations

- The internal conversation logs and "Shadow" data (currently local) are planned to be hosted on GitHub as a `private` repository.
- **Security Validation**: Since API keys and strict secrets are already excluded from plaintext conversations (and LLM providers already process this data), utilizing GitHub as a trusted secure backup for private thought-logs is an approved architecture.

---

## Error Handling

### Tool Availability

**MUST** report clear errors when required tools are missing:

- "Error: GitHub CLI (gh) is not installed."
- "Error: GitHub CLI is not authenticated. Please run 'gh auth login'."
- "Error: Not inside a git repository."

### Operation Failures

**MUST** handle failures gracefully:

- Verify issue creation success
- Check branch creation/checkout success
- Validate remote operations

---

## Historical Background

**The Safety Net Philosophy**: The mandatory backup branch rule (Section 3.3) was established in Jan 2026 following several incidents where complex rebases led to accidental loss of commit context. We learned that for an AI, "Git reset" is not just a command, but a potential "Cognitive Erasure."

**The Sacred Territory Incident**: On 2026-01-24, a `git reset --hard` accident resulted in the loss of human-authored drafts for 1/23. This led to the "Soft-First" and "Stash-Safety" mandates. We realized that while Git tracks history, it cannot distinguish between "Agent Scratchpads" and "Human Legacy" without area-specific behavioral safeguards.

**Federal Strata Transition**: In May 2026, the strict IDD (GitHub Issue) dependencies and short-lived feature branch workflows were officially deprecated in favor of local-first permanent branch operations. GitHub is now relegated to a synchronization target rather than a granular task manager.

---

## Related Documents

| Document                                                                                   | Purpose                  |
| :----------------------------------------------------------------------------------------- | :----------------------- |
| [`commit-standards.md`](/.agent/rules/development/commit-standards.md)                     | Commit message standards |
| [`commit-philosophy.md`](/.agent/.internal/references/agents/commit-philosophy.md)         | Cognitive strategy       |
| [`absolute-path-prohibition.md`](/.agent/rules/core/security/absolute-path-prohibition.md) | Path security            |
| [Map of Territory](/.agent/rules/map.md)                                                   | Root navigation map      |

---

## Origin

- 2025-11-29T08:44:47+09:00 by Lico: Created as git operations standards
- 2026-01-01T15:18:00+09:00 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-01-11T00:00:00+09:00 by Spica: Enforced strict git mv and pre-commit status check (Safety Protocol)
- 2026-01-14T23:00:00+09:00 by Polaris: Added Section 3.4 (AI Interactive Command Workarounds)
- 2026-01-15T19:35:00+09:00 by Polaris: Added post-rewrite verification and cleanup procedure
- 2026-01-17T15:35:00+09:00 by Canopus: Updated commit message examples to align with "Identifier-First" protocol (v1.4).
- 2026-01-17T17:45:00+09:00 by Canopus: Standardized metadata and root-relative link patterns (v1.5).
- 2026-01-23T06:26:00+09:00 by Canopus: Formalized v2.3 standardization and added Section 7.1.1 (Command Division for Verification).
- 2026-01-24T02:05:00+09:00 by Canopus: Codified "Save-First Principle" and "Soft-First/Stash-Safety" protocols following the Jan 24 data loss incident. (v2.4)
- 2026-01-25T07:10:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch4>> Standardized to v2.3 constitutional standards; removed legacy related frontmatter and navigation footer. (v2.5.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
- 2026-05-08T08:31:04+09:00 by Lico (Sirius): Replaced legacy IDD and issue-branching rules with Federal Strata local-first protocols. (v2.6.0)
