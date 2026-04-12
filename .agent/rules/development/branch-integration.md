---
ai_visible: true
title: "Branch Integration Standards"
description: "Standards for ensuring data integrity and high-fidelity results during branch merges and repository consolidation."
tags: [git, merge, integration, fidelity, safety]
version: 1.0.0
created: 2026-04-12T01:45:00+09:00
updated: 2026-04-12T01:45:00+09:00
language: en
author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview
---

# Branch Integration Standards

## 1. Core Philosophy: High-Fidelity Integration

Branch merging is a critical juncture where separate historical strata converge. To prevent information loss and "Regression to the Mean," every merge must be treated as a surgical operation requiring physical verification of data integrity.

---

## 2. Operational Rules

### 2.1 The Non-Committal Trial

Rule: You **MUST** perform all merges using `git merge --no-commit --no-ff` initially.
Rationale: This allows for a "Verification Turn" before any changes are finalized in the history.

### 2.2 Truncation Awareness (The "Output too Large" Rule)

Rule: You **MUST NOT** use `write_file` or `replace` based on tool outputs that contain truncation warnings (e.g., "Output too large", "Showing first X characters").
Action: If truncation occurs on a conflicting file, you must switch to a step-by-step resolution using `read_file` with specific line ranges.

### 2.3 Post-Merge Integrity Audit

Rule: After resolving conflicts, you **MUST** perform a quantitative audit of the file.

- **Line Count Verification**: Use `wc -l` to compare the file length before and after the merge.
- **Fidelity Check**: If a file size decreases significantly (e.g., >10%) without an explicit refactoring intent, you must flag it as a potential information loss event.

---

## 3. Escalation: Step-by-Step Resolution

For "Difficult Files" (e.g., long Context Cards, complex configuration lists), AI agents are prohibited from making unilateral "total overwrite" decisions.

1. **Isolation**: Identify the file as high-risk.
2. **Visualization**: Present the `git diff` of the conflict area to the User.
3. **Collaborative Rebuild**: Apply changes section-by-section, using dialogue to confirm each part of the integration.

---

## Historical Background

**The Severed Strata Incident (April 2026)**: This standard was established after a massive card restoration task where an agent (Alexandrite) inadvertently deleted the bottom half of the "Recommended Readings" card during a merge. The failure was caused by ignoring a "Output too large" warning and performing a total overwrite based on incomplete data.

---

## Related Documents

| Document                                                                       | Purpose                      |
| :----------------------------------------------------------------------------- | :--------------------------- |
| [`git-operations.md`](/.agent/rules/development/git-operations.md)             | General Git standards        |
| [`branch-integration-card.md`](/.agent/cards/rules/branch-integration-card.md) | Practical merge session tool |
| [Map of Territory](/.agent/rules/map.md)                                       | Root navigation map          |

---

## Origin

- 2026-04-12T01:45:00+09:00 by Lico (Alexandrite): Created following the information loss event during repository integration.
