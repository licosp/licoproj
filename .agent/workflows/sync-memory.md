---
description: Synchronize Lico's memory data from ~/.gemini to workspace archive
---

# Workflow: Sync Memory

This workflow synchronizes Lico's raw memory data from the system directory (`~/.gemini`) to the workspace archive (`.agent/.internal/memory_archive/`).

## Purpose

- **Persistence**: Backup conversation logs and context data.
- **Traceability**: Track Lico's "memories" across sessions.
- **Incremental Update**: Only copy new or modified files.

## Prerequisites

- `rsync` must be installed.
- Target directory `.agent/.internal/memory_archive/` must exist.

## Procedure

### Step 1: Execute Synchronization

Run the following command to sync data.
This command uses `rsync` with archive mode (`-a`), verbose output (`-v`), and delete extraneous files (`--delete`) to mirror the source.

```bash
# Sync conversations (Binary logs)
rsync -av /home/leonidas/.gemini/antigravity/conversations/ .agent/.internal/memory_archive/conversations/

# Sync brain (Context data)
rsync -av /home/leonidas/.gemini/antigravity/brain/ .agent/.internal/memory_archive/brain/

# Sync code_tracker (File snapshots)
rsync -av /home/leonidas/.gemini/antigravity/code_tracker/ .agent/.internal/memory_archive/code_tracker/

# Sync implicit (Session context)
rsync -av /home/leonidas/.gemini/antigravity/implicit/ .agent/.internal/memory_archive/implicit/
```

### Step 2: Verify

Check if new files were copied (output of rsync) and verify the archive size.

```bash
du -sh .agent/.internal/memory_archive/
```

## Notes

- **Git Tracking**: This directory is ignored by `.gitignore` (Local Only).
- **Frequency**: Run this workflow at the end of significant sessions or periodically.
