---
ai_visible: true
title: Archive Management
description: Guidelines for organizing and maintaining archive directories with time-based structure.
tags: [archive, maintenance, organization, file-management]
version: 2.4.0
created: 2025-12-25T03:43:00+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Archive Management

Define consistent rules for organizing archive directories to support both AI navigation and human visual overview.

---

## 1. Directory Structure

### Time-Based Organization

Archives use a **nested date-based structure**: `.agent/.internal/archive/YYYY/MM/DD/`.
The nested structure properly groups archives by year and month, maintaining clean directories as history accumulates.

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

**Searchability First**: This management rule was established to treat the archive as a "Chronological Ledger." By using a nested, date-based hierarchy (`YYYY/MM/DD`), we provide a predictable path for `grep` and `find` operations, allowing Lico to reconstruct "what happened on which day" systematically.

---

## Related Documents

| Document                                                                      | Purpose                                    |
| :---------------------------------------------------------------------------- | :----------------------------------------- |
| [`file-deletion.md`](/.agent/rules/development/file-deletion.md)              | Archive vs deletion policy                 |
| [`cognitive-collaboration.md`](/.agent/rules/core/cognitive-collaboration.md) | AI-Human visibility differences            |
| [`update-protected-rules.md`](/.agent/workflows/update-protected-rules.md)    | Protected file workaround using temp files |
| [Map of Territory](/.agent/rules/map.md)                                      | Root navigation map                        |

---

## Origin

- 2025-12-25T03:43:00+09:00 by Polaris: Created as archive management guidelines
- 2025-12-28T00:35:00+09:00 by Polaris: Added date selection rule
- 2026-01-01T15:13:00+09:00 by Polaris: Added duplicate file handling section, replaced Related Documents with Navigation
- 2026-01-25T07:30:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
- 2026-02-22T03:15:00+09:00 by Sirius: Updated directory structure from flat (`YYYY-MM-DD/`) to nested (`YYYY/MM/DD/`). (v2.4.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
