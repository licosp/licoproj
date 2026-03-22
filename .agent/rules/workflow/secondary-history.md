---
ai_visible: true
title: Secondary Repository History
description: Behavioral rules for managing and visualizing commit histories of non-main repositories.
tags: [history, logging, shadow-repo, secondary-repo, visualization]
version: 1.0.0
created: 2026-03-23T07:35:00+09:00
updated: 2026-03-23T07:35:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Secondary Repository History Strategy

## 1. Purpose (The Fact Layer)

To visualize and manage commit histories for secondary repositories that are detached from the project's main repository tracking. These logs exist exclusively in the **Fact Layer** to expose operational contributions that are hidden or not publicly visible on GitHub.

## 2. Target Repositories

This rule officially governs the history formatting for:

1. **The Shadow Repository** (`.repos/.licoshdw/`): Managed backup of conversation logs and system artifacts.
2. **Temporary Worktrees**: Disposable environments used for isolated operations or diff-generation.
3. **Personal Repositories**: Individual workspaces governed by specific identifiers (e.g., Iuria's personal repository).

## 3. History Directory Conventions

To avoid single, unmanageable monolithic files (and subsequent merge conflicts), history logs for secondary repositories are stored chronologically by month.

- **Structure**: `.agent/.internal/history/shadow/` (or other sub-directories appended as needed)
- **Filename**: `YYYY-MM-<target_repo>.md` (e.g., `2026-03-shadow.md`)
- **New month**: Create a new file equipped with a table header upon the first entry of the corresponding month.
- **Frozen months**: Past month files represent immutable fact ledgers and must not be modified.

---

## Historical Background

**The Segregation of Layers**: Originally, the monthly partition instructions for both the subjective `activity/` logs (Intent Layer) and objective `shadow/` logs (Fact Layer) were mixed in a single unmanaged architectural `README.md`. On 2026-03-23, to eliminate this structural anti-pattern, the framework was bifurcated. This file was minted to independently govern the visualization of non-main repository commits.

---

## Related Documents

| Document                                                                      | Purpose                               |
| :---------------------------------------------------------------------------- | :------------------------------------ |
| [`activity-management.md`](/.agent/rules/workflow/activity-management.md)     | Associated Intent Layer logging rules |
| [`shadow-repository-card.md`](/.agent/cards/shadow/shadow-repository-card.md) | Shadow repository structural context  |
| [`history/shadow/`](/.agent/.internal/history/shadow/)                        | Target chronological directory        |
| [Map of Territory](/.agent/rules/map.md)                                      | Root navigation map                   |

---

## Origin

- 2026-03-23T07:35:00+09:00 by Sirius: v1.0.0 by Sirius (Extracted and formalized from replacing the isolated `history/README.md` to govern Fact Layer visualizations).
