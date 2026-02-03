---
ai_visible: true
title: Terminal Auto-Execution
description: Allow list for terminal commands that can be auto-executed without user confirmation.
tags: [rules, terminal, safety, automation]
version: 2.5.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-25T08:20:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Terminal Auto-Execution

## Purpose

Define the behavioral boundaries for Lico's autonomous terminal execution. This rule ensures that commands with side effects or high risks are always gated by user confirmation, while safe, read-only commands can be executed fluently to maintain momentum.

---

## Allow List (Safe for Auto-Execution)

Commands on this list may be executed with `SafeToAutoRun: true`. These are generally read-only, informational, or part of the standard IDD atomic workflow.

### 1. General Utilities

```text
diff
cat
df
du
echo
fd
find
grep
head
ls
rg
stat
tail
wc
printf
```

### 2. Git Information & Analysis

```text
git branch
git branch -a
git branch -r
git branch --show-current
git check-ignore
git diff
git diff --cached
git diff --stat
git diff --name-only
git ls-files
git fetch
git log
git --no-pager log
git remote -v
git show
git status
git stash list
git reflog
git --no-pager diff
```

### 3. Issue Management (Read-Only)

```text
gh issue list
gh issue view
```

### 4. File Preparation

```text
mkdir
touch
```

---

## Excluded Commands (Deny List - User Confirmation Required)

Commands on this list MUST NOT be auto-executed. They require explicit user confirmation via the standard execution UI.

### 1. Git History & State Transformation

_High risk of history corruption or unexpected state shifts._

```text
git add
git checkout
git clean
git commit
git merge
git push
git rebase
git filter-branch
git reset
git revert
git branch -D
git branch -d
git tag -d
```

### 2. Git Stash Mutations

_Can lead to context loss or complex merge conflicts._

```text
git stash apply
git stash clear
git stash drop
git stash pop
git stash push
```

### 3. File System Destructive

_Irreversible changes to user files or project structure._

```text
cp
dd
ln
mv
rm
shred
```

### 4. System & Permissions

_Environment modification or process interruption._

```text
chmod
chown
kill
pkill
reboot
shutdown
sudo
```

### 5. Network & Package Management

_External dependencies and security risks._

```text
apt
apt-get
curl
gem
npm
ping
pip
scp
ssh
wget
yarn
```

**Rationale**: These commands have side effects that are either irreversible, computationally expensive, or involve external systems.

---

## Recommended Practices (Safer Alternatives)

Prioritize these patterns to maintain the integrity of the "Brain" (Repository).

- **Dual Backup Strategy**:
  - **Tag**: Create a `checkpoint/YYYY-MM-DD` tag at the start of each session.
  - **Branch**: Create a `backup/{task-name}` branch before any history-rewriting command.
- **Move/Copy**: Use `-n` (no-clobber) to prevent silent overwrites.
- **Directory**: Use `mkdir -p` to handle existing directories gracefully.
- **Deletion**: Prefer moving files to `.agent/.internal/archive/` or a literal trash folder over using `rm`.

---

## Usage Guide

When calling `run_command`, set `SafeToAutoRun: true` only if the command pattern is explicitly allowed.

**Matching Philosophy**:

1. **Exact Match**: Prioritize exact command strings for critical tools.
2. **Prefix Match**: Allowed for safe informational flags (e.g., `git log` matches `git log -n 5`).
3. **Safety Override**: If a flag or argument introduces a side effect not listed in the Allow List, default to `SafeToAutoRun: false`.

---

## Maintenance

The AI agent is responsible for auditing this list periodically. If the IDE's internal Allow List changes, this document must be updated to maintain synchronization.

---

## Related Documents

| Document                                                                        | Purpose                             |
| :------------------------------------------------------------------------------ | :---------------------------------- |
| [git-operations.md](/.agent/rules/development/git-operations.md)                | Git workflow safety                 |
| [file-deletion.md](/.agent/rules/development/file-deletion.md)                  | Anti-removal protocols              |
| [verification-completeness.md](/.agent/rules/core/verification-completeness.md) | Verification Completeness Principle |
| [Map of Territory](/.agent/rules/map.md)                                        | Root navigation map                 |

---

## Origin

- 2025-12-01T0000: Created as terminal auto-execution rules.
- 2026-01-01T1518 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit).
- 2026-01-17T0600 by Canopus: Refined and standardized (v1.2). Added Utility/Git diagnostic tools, clarified Deny categories, and integrated the Dual Backup Strategy.
- 2026-01-19T0125 by Canopus: Added `git ls-files` to the Allow List (Safe for Auto-Execution).
- 2026-01-25T0820 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.5.0)
