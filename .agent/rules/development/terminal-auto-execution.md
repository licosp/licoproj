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
mkdir
tail
touch
wc
```

---

## Excluded Commands (Deny List)

Commands on this list MUST NOT be auto-executed. They require explicit user confirmation.

### 1. Git Destructive & History Rewriting
*High risk of data loss or history alteration.*
```
git checkout
git clean
git commit
git merge
git push
git rebase
git reset
git revert
git stash
```

### 2. File System Destructive
*Irreversible changes to files.*
```
cp
dd
ln
mv
rm
shred
```

### 3. System & Permissions
*Environment modification.*
```
chmod
chown
kill
pkill
reboot
shutdown
sudo
```

### 4. Network & Remote Access
*External communication risks.*
```
curl
ping
scp
ssh
wget
```

### 5. Package Management
*Dependency modification.*
```
apt
apt-get
gem
npm
pip
yarn
```

**Rationale**: These commands have side effects that are either irreversible, computationally expensive, or involve external systems.

---

## Recommended Practices (Safer Alternatives)

Even when requesting user confirmation, prioritize these safer alternatives to prevent accidental data loss.

- **Move**: Use `mv -n` (no-clobber) to prevent silent overwrites.
- **Copy**: Use `cp -n` (no-clobber) to prevent silent overwrites.
- **Directory**: Use `mkdir -p` to avoid errors if the directory already exists (and create parents).
- **Deletion**: Prefer moving to `.trash/` or `archive/` over using `rm`.

---

## Usage

When calling `run_command`, set `SafeToAutoRun: true` if the command matches an entry in the Allow List.

**Matching rule**: Command tokens form a prefix match.
- `git branch` matches `git branch -v`
- `ls` matches `ls -la`

---

## Maintenance

When updating the IDE's Allow List, update this document to match.

**Last updated**: 2025-12-13
