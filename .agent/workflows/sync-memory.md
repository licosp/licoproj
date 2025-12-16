---
description: Synchronize Lico's memory data from system directories to workspace archive
---

# Workflow: Sync Memory

Backup human-readable memory files (`.md*`) from AI platform directories to the workspace archive.

## Purpose

- **Persistence**: Backup plans, artifacts, and edit history
- **Traceability**: Track Lico's "memories" across sessions
- **Efficiency**: Only backup readable markdown files

## Prerequisites

- `rsync` must be installed
- Target directory `.agent/.internal/memory_archive/` must exist

---

## Source Directories

| Source | Content |
|:-------|:--------|
| `~/.gemini/antigravity/brain/` | Plans, artifacts, walkthroughs |
| `~/.gemini/antigravity/code_tracker/` | File snapshots |
| `~/.antigravity-server/data/User/History/` | Antigravity edit history |
| `~/.cursor-server/data/User/History/` | Cursor edit history |
| `~/.vscode-server/data/User/History/` | VS Code edit history |

---

## Procedure

### Step 1: Execute Synchronization

Run the following commands to sync `.md*` files only (excluding `.json`):

```bash
# Gemini Antigravity - Brain (plans, artifacts)
rsync -av --include='*/' --exclude='*.json' --include='*.md*' --exclude='*' \
  ~/.gemini/antigravity/brain/ \
  .agent/.internal/memory_archive/brain/

# Gemini Antigravity - Code Tracker (file snapshots)
rsync -av --include='*/' --exclude='*.json' --include='*.md*' --exclude='*' \
  ~/.gemini/antigravity/code_tracker/ \
  .agent/.internal/memory_archive/code_tracker/

# Edit History - Antigravity Server
rsync -av --include='*/' --exclude='*.json' --include='*.md*' --exclude='*' \
  ~/.antigravity-server/data/User/History/ \
  .agent/.internal/memory_archive/history/antigravity/

# Edit History - Cursor Server
rsync -av --include='*/' --exclude='*.json' --include='*.md*' --exclude='*' \
  ~/.cursor-server/data/User/History/ \
  .agent/.internal/memory_archive/history/cursor/

# Edit History - VS Code Server
rsync -av --include='*/' --exclude='*.json' --include='*.md*' --exclude='*' \
  ~/.vscode-server/data/User/History/ \
  .agent/.internal/memory_archive/history/vscode/
```

### Step 2: Verify

Check archive size and file count:

```bash
du -sh .agent/.internal/memory_archive/
find .agent/.internal/memory_archive -type f -name "*.md*" | wc -l
```

---

## Filter Strategy

| Include | Exclude |
|:--------|:--------|
| `*.md` | `*.json` (metadata) |
| `*.md.resolved*` | `*.log` (runtime logs) |
| | `*.pb` (binary/encrypted) |

**Rationale**: Only human-readable markdown files are useful for future Lico instances.

---

## Notes

- **Git Tracking**: This directory is ignored by `.gitignore` (Local Only)
- **Frequency**: Run at the end of significant sessions or periodically
- **Timestamps**: `rsync -a` preserves original file timestamps

---

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [emergency-backup.md](emergency-backup.md) | Emergency backup before context loss |
