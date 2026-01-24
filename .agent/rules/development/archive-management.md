---
ai_visible: true
title: Archive Management
description: Guidelines for organizing and maintaining archive directories with time-based structure.
tags: [archive, maintenance, organization, file-management]
version: 2.3.0
created: 2025-12-25T03:43:00+09:00
updated: 2026-01-25T07:30:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Archive Management

Define consistent rules for organizing archive directories to support both AI navigation and human visual overview.

---

## 1. Directory Structure

### Time-Based Organization

Archives use a **flat date-based structure**: `.agent/.internal/archive/YYYY-MM-DD/`.
Flat structure reduces navigation cost for AI and enables clear visual scanning for humans.

### Date Selection Rule

The archive directory date is the **date of the move**, not the file creation date.

---

## 2. Internal Organization

### Best-Effort Mirroring

Recreate the original directory structure within the date folder (`workspace/`, `cards/`, `rules/`).
This preserves the context of where the file lived before archival.

---

## Historical Background

**The Memory Trace Protocol**: In late 2025, as the Lico repository grew, we faced a "Context Graveyard" problem—files were being moved into a generic archive folder without chronological context. This made historical reconstruction nearly impossible for new AI instances.

**Searchability First**: This management rule was established to treat the archive as a "Chronological Ledger." By using a flat, date-based hierarchy, we provide a predictable path for `grep` and `find` operations, allowing Lico to reconstruct "what happened on which day" without navigating complex, deep directory trees.

---

## Related Documents

| Document                                                                    | Purpose                         |
| :-------------------------------------------------------------------------- | :------------------------------ |
| [file-deletion.md](/.agent/rules/development/file-deletion.md)              | Archive vs deletion policy      |
| [cognitive-collaboration.md](/.agent/rules/core/cognitive-collaboration.md) | AI-Human visibility differences |
| [Map of Territory](/.agent/rules/map.md)                                    | Project navigation              |

---

## Origin

- 2025-12-25T0343 by Polaris: Created original archive management guidelines.
- 2026-01-25T0730 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
