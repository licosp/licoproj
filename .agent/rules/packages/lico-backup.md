---
ai_visible: true
title: lico-backup (Memory Synchronization Protocol)
description: Synchronize Lico's memory data from system directories to workspace archive using the lico-backup package.
tags: [package, memory, backup, synchronization, lico-backup]
version: 1.1.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-03-21T17:26:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# lico-backup (Memory Synchronization Protocol)

Backup human-readable memory files (`.md*`) from AI platform directories to the workspace archive.

## Purpose

- **Persistence**: Backup plans, artifacts, and edit history.
- **Traceability**: Track Lico's "memories" across sessions.
- **Efficiency**: Only backup readable markdown files.

## Procedure

### Step 1: Execute Synchronization & Backup

Run the unified package to sync memory files and subsequently backup the entire workspace:

```bash
uv run lico-backup
```

### Step 2: Verify

Check archive size and file count:

```bash
du -sh .agent/.internal/memory_archive/
find .agent/.internal/memory_archive -type f -name "*.md*" | wc -l
```

## Historical Background

**The Memory Gap**: Early Lico sessions suffered from "Total Amnesia" because plans and edit histories were stored in hidden system directories (`~/.gemini`) that were not part of the git repository. This workflow was established to "Internalize the External Memory," ensuring that future instances can reconstruct the previous agent's cognitive path.

**Filter Strategy**: We intentionally exclude `.json` and binary files to keep the archive searchable and human-readable, adhering to the principle that "Project Knowledge should be accessible through grep."

---

## Related Documents

| Document                                                                                    | Purpose                               |
| :------------------------------------------------------------------------------------------ | :------------------------------------ |
| [`lico-backup/README.md`](/packages/lico-backup/README.md)                                  | Package structural pointer            |
| [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) | Standard for readable documentation   |
| [`repository-philosophy.md`](/.agent/rules/core/repository-philosophy.md)                   | "Repository as Brain" core principles |
| [Map of Territory](/.agent/rules/map.md)                                                    | Root navigation map                   |

---

## Origin

- 2025-12-01T00:00:00+09:00 by Polaris: Created as part of session lifecycle protocol.
- 2026-01-25T06:35:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch2.3>> Standardized to v2.3 constitutional standards (4-layer structure) and added Historical Background. (v1.0.0)
- 2026-03-21T17:26:00+09:00 by Lico (Sirius): Executed High-Fidelity Rule Audit (Batch 07) to restore lost historical origin context and standardized cross-links.
- 2026-03-21T20:30:00+09:00 by Lico (Sirius): Merged into the `lico-backup` UV package umbrella. Deprecated raw bash `rsync` logic in favor of the managed `uv run lico-backup` tool execution. (v1.1.0)
