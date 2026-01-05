---
ai_visible: true
title: Archive Management
description: Guidelines for organizing and maintaining archive directories with time-based structure.
tags: [archive, maintenance, organization, file-management]
version: 1.2
created: 2025-12-25T03:43:00+09:00
updated: 2026-01-01T15:13:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/rules/development/file-deletion.md: Archive vs deletion policy
  .agent/rules/core/cognitive-collaboration.md: AI-Human visibility differences
  .agent/workflows/update-protected-rules.md: Protected file workaround using temp files
---

# Archive Management

## Purpose

Define consistent rules for organizing archive directories to support both AI navigation and human visual overview.

---

## 1. Directory Structure

### Time-Based Organization

Archives use a **flat date-based structure**:

```
.agent/.internal/archive/
├── 2025-12-24/
│   ├── workspace/
│   │   └── temp-file.md
│   └── cards/
│       └── completed-card.md
├── 2025-12-25/
│   └── ...
└── ...
```

### Format

- **Date format**: `YYYY-MM-DD` (ISO-8601, Japan timezone)
- **One directory per day**
- **No hierarchical nesting** (not `YYYY/MM/DD/`)

### Date Selection Rule

> **Critical**: The archive directory date is the **date of the move**, not the file creation date.

If a file was created on 12/27 but archived on 12/28, it goes to `2025-12-28/`.

### Rationale

- Flat structure reduces navigation cost for AI
- Consistent naming enables visual scanning for humans
- Date-based grouping limits file count per directory

---

## 2. Internal Organization

### Best-Effort Structure Mirroring

Within each date directory, **attempt to recreate the original directory structure**:

```
2025-12-25/
├── workspace/      # Files from .agent/.internal/workspace/
├── cards/          # Files from .agent/cards/
└── rules/          # Files from .agent/rules/
```

### Principles

- **Best effort, not mandatory** — Mistakes are acceptable
- **Small file count per day** — Easy to understand later
- **Routine-work friendly** — Low cognitive overhead

### Duplicate File Handling

When archiving temp files (e.g., from protected file workaround):

| Situation | Action |
|:----------|:-------|
| Simple file move | No duplicate check needed (Best effort) |
| Complex workflow with many temp files | Check for duplicates before moving |
| Same workflow run multiple times per day | Add timestamp to filename (`-HHMM`) |

**Detection**:
```bash
# Check before moving
ls .agent/.internal/archive/YYYY-MM-DD/workspace/temp-*.md 2>/dev/null
```

**Rationale**: Avoid overwriting previous work, but keep routine moves lightweight.

---

## 3. Metadata Policy

### No Additional Metadata Required

| Field | Decision | Reason |
|:------|:---------|:-------|
| `archive_reason` | Not required | Git commit message is sufficient |
| `successor_path` | Not required | High maintenance cost, rare use case |
| `archived_date` | Not required | Directory name provides this |

### Commit Message as Documentation

The commit message should include:
- Why the file was archived
- What triggered the archival (task completion, deprecation, etc.)

---

## 4. Existing Archives

### Migration Policy

When reorganizing existing archives:

1. **Find date information** from:
   - Filename (e.g., `2025-12-19T0320_...`)
   - Git history (`git log --follow`)
   - File frontmatter (`created:`, `updated:`)

2. **Move to appropriate date directory**

3. **Include archival reason in commit message**

### Commit Granularity

- Group by archival reason or original purpose
- Separate commits for different logical groups

---

## 5. Applies To

| Directory | Scope |
|:----------|:------|
| `.agent/.internal/archive/` | AI-managed archives |
| `.human/archive/` | Human-managed archives |

Both follow the same rules for consistency.

---

## Origin

- 2025-12-25T0343: Created as archive management guidelines
- 2025-12-28T0035 by Polaris: Added date selection rule
- 2026-01-01T1513 by Polaris: Added duplicate file handling section, replaced Related Documents with Navigation

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
