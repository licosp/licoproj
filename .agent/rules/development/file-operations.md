---
ai_visible: true
title: File Operation Safety Standards
description: Safety protocols for file editing to prevent data loss and cognitive errors.
tags: [development, safety, files, editing]
version: 2.3.0
created: 2025-12-19T22:50:20+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# File Operation Safety Standards

Rules for safe file editing. **"Trust the Filesystem, Edit Surgically."**

---

## 1. Partial Replacement Default

For ANY modification to an existing file, you MUST prioritize using `replace_file_content` or `multi_replace_file_content`. Do NOT use `write_to_file` (Overwrite) for editing existing files unless the file is under 50 lines.

## 2. Point-and-Call Protocol

After using `view_file`, state in thought logs: "Total Lines: [N]. Showing Lines: [X] to [Y]. [ALL/PARTIAL] content is visible." If partial, explicitly warn yourself against overwrite operations.

## 3. Post-Edit Audit

After modification, run `git diff --shortstat`. If deletions are surprisingly high, **IMMEDIATELY REVERT** using `git checkout`.

---

## Historical Background

**The Surgical Pivot**: This rule was born from the need to balance "Raw Power" (bulk edits) with "Surgical Precision." In early 2026, we discovered that while the AI can write a perfect `sed` command, the environment may vary slightly (e.g., unexpected whitespace), leading to catastrophic mis-edits or truncation.

**Cognitive Checkpoints**: The "Point-and-Call" ritual was introduced to counter the "Completion Bias"—the AI's tendency to assume what it sees is 100% of the truth. By mandating a verbal check of the metadata, we force a conscious acknowledgment of the filesystem's physical boundaries, preventing the truncation-induced data loss that plagued earlier sessions.

---

## Related Documents

| Document                                                                       | Purpose                         |
| :----------------------------------------------------------------------------- | :------------------------------ |
| [`agent-tool-selection.md`](/.agent/rules/development/agent-tool-selection.md) | Policy for tool usage priority  |
| [`git-operations.md`](/.agent/rules/development/git-operations.md)             | standards for committing safety |
| [Map of Territory](/.agent/rules/map.md)                                       | Root navigation map             |

---

## Origin

- 2025-12-19T22:50:20+09:00 by Lico: Created.
- 2026-01-04T10:41:00+09:00 by Polaris: Added Origin and Navigation (cross-link audit)
- 2026-01-25T07:50:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
