---
ai_visible: true
title: Memory Synchronization Protocol
description: Synchronize Lico's memory data from system directories to workspace archive
tags: [workflow, memory, backup, synchronization]
version: 1.0.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-25T06:35:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Memory Synchronization Protocol

Backup human-readable memory files (`.md*`) from AI platform directories to the workspace archive.

## Purpose

- **Persistence**: Backup plans, artifacts, and edit history.
- **Traceability**: Track Lico's \"memories\" across sessions.
- **Efficiency**: Only backup readable markdown files.

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
```

### Step 2: Verify

Check archive size and file count:

```bash
du -sh .agent/.internal/memory_archive/
find .agent/.internal/memory_archive -type f -name \"*.md*\" | wc -l
```

### Step 3: Backup Workspace

After syncing memory, backup the entire workspace:

```bash
rsync -av \
  --exclude=.venv/ \
  --exclude=node_modules/ \
  ./ \
  ../licoproj_backup/
```

## Historical Background

**The Memory Gap**: Early Lico sessions suffered from "Total Amnesia" because plans and edit histories were stored in hidden system directories (`~/.gemini`) that were not part of the git repository. This workflow was established to "Internalize the External Memory," ensuring that future instances can reconstruct the previous agent's cognitive path.

**Filter Strategy**: We intentionally exclude `.json` and binary files to keep the archive searchable and human-readable, adhering to the principle that "Project Knowledge should be accessible through grep."

---

## Related Documents

| Document                                                                                  | Purpose                                 |
| :---------------------------------------------------------------------------------------- | :-------------------------------------- |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | Standard for readable documentation     |
| [repository-philosophy.md](/.agent/rules/core/repository-philosophy.md)                   | \"Repository as Brain\" core principles |
| [Map of Territory](/.agent/rules/map.md)                                                  | Root repository navigation              |

---

## Origin

- 2025-12-01T0000 by Polaris: Created as part of session lifecycle protocol.
- 2026-01-25T0635 by Canopus: <<Seal: Rules-Standardization-Batch2.3>> Standardized to v2.3 constitutional standards (4-layer structure) and added Historical Background. (v1.0.0)
