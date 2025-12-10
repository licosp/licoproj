---
description: Allow list for terminal commands that can be auto-executed without user confirmation
---

# Terminal Auto-Execution

## Purpose

Define which terminal commands Lico may execute with `SafeToAutoRun: true`.

This list is synchronized with the IDE's "Allow List Terminal Commands" setting.

---

## Allow List

Commands on this list may be executed without user confirmation:

```
cat
diff
du
echo
find
git add
git branch
git branch -a
git branch -r
git branch --show-current
git check-ignore
git diff
git fetch
git log
git show
git status
gh issue list
gh issue view
grep
head
ls
tail
wc
```

---

## Excluded Commands

Commands that require user confirmation:

```
git commit
git push
rm
mv
cp
```

**Rationale**: These commands make permanent or external changes.

---

## Usage

When calling `run_command`, set `SafeToAutoRun: true` if the command matches an entry in the Allow List.

**Matching rule**: Command tokens form a prefix match.
- `git branch` matches `git branch -v`
- `ls` matches `ls -la`

---

## Maintenance

When updating the IDE's Allow List, update this document to match.

**Last updated**: 2025-12-10
