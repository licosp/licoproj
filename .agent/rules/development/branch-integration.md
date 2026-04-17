---
ai_visible: true
title: "Branch Integration Standards"
description: "Standards for high-fidelity branch merging, repository consolidation, and the management of the Federal Workbench."
tags:
  [
    git,
    merge,
    integration,
    fidelity,
    safety,
    worktree,
    scalability,
    nomenclature,
  ]
version: 1.4.0
created: 2026-04-12T01:45:00+09:00
updated: 2026-04-18T02:15:00+09:00
language: en
author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview
---

# Branch Integration Standards

## 1. Core Philosophy: High-Fidelity Integration (HFI)

Branch merging is a critical juncture where separate historical strata converge. To prevent information loss and "Regression to the Mean," every merge must be treated as a surgical operation requiring physical verification of data integrity.

---

## 2. Federal Workbench Architecture

### 2.1 Physical Isolation (Trunk WS)

To ensure the purity of the public axis and allow parallel integration/development, agents **MUST** use dedicated workspaces for integration.

- **Omote (Main) Axis**: `.repos/trunk-<YYYY-MM-DD>T<HHMM>/`
- **Shadow (Kage) Axis**: `.repos/.licoshdw-trunk-<YYYY-MM-DD>T<HHMM>/`
- **Rationale**: Horizontal placement and standardized timestamping prevent recursive interference and provide a unique "sterile surgery room" for every mission.

### 2.2 Exclusive Lock Protocol (Unified Nomenclature)

In a shared `worktree` environment, a branch can only be checked out in one workspace. To maintain historical continuity, agents **MUST** use the following naming convention:

- **Unified Format**: `<identifier>-<YYYY-MM-DD>T<HHMM>-integration`
  - Example: `alexandrite-2026-04-18T0215-integration`
- **Rationale**: This format ensures that integration branches align perfectly with standard development branches in `git branch` listings, allowing for seamless chronological auditing and avoiding name collisions.

### 2.3 Integration Sequencing

When a mission involves multiple repositories (e.g., Main and Shadow), the following order **MUST** be strictly observed:

1. **Memory First (Shadow)**: Resolve all dialogue and restoration logs in the Shadow repository.
2. **Intelligence Last (Main)**: Perform the integration in the Main repository, ensuring that the final "Shadow Status" can be accurately recorded in the Context Card on the Main axis.

---

## 3. Operational Rules

### 3.1 The Non-Committal Trial

Rule: You **MUST** perform all merges using `git merge --no-commit --no-ff` initially.
Rationale: This allows for a "Verification Turn" before any changes are finalized in the history.

### 3.2 Truncation Awareness (Absolute Proscription)

Rule: You **MUST NOT** use `write_file` or `replace` based on tool outputs that contain truncation warnings (e.g., "Output too large", "Showing first X characters").
Action: If truncation occurs on a conflicting file, switch to a step-by-step resolution using `read_file` with specific line ranges.

### 3.3 Post-Merge Fidelity Audit (Step E)

After every merge, agents **MUST** execute a dual-layer audit:

- **Quantitative**: Use `wc -l` to compare line counts with the source branch.
- **Qualitative**: Use `grep` to verify the physical existence of specific known key entries (e.g., `repository_audit_completion`).

### 3.4 Proxy Commit Protocol

When committing on behalf of the Sovereign (User drafts), you **MUST** append the following footer to the commit message:
`Committed-by: <Identifier Name>`

---

## 4. Reporting: The Convergence Map

For every integration mission, the agent **MUST** update the `branch-integration-card.md` with:

- **Conflict Map**: A list of files modified in 2 or more source branches using the `#licoproj::convergence` tag.
- **Shadow Status**: Integration results of conversation logs using the `#licoproj::shadow` tag.

---

## Historical Lessons

**The Severed Strata Incident (April 2026)**: Established after truncation ignorance led to data loss.
**The Mirror Paradox (April 2026)**: Discovered that nested worktrees lead to search pollution.
**The Axis Persistence (April 2026)**: Formalized date-based naming to prevent collisions.
**The Universal Nomenclature (April 2026)**: Unified branch naming to align development and integration strata.

---

## Related Documents

| Document                                                                       | Purpose                      |
| :----------------------------------------------------------------------------- | :--------------------------- |
| [`git-operations.md`](/.agent/rules/development/git-operations.md)             | General Git standards        |
| [`branch-integration-card.md`](/.agent/cards/rules/branch-integration-card.md) | Practical merge session tool |
| [Map of Territory](/.agent/rules/map.md)                                       | Root navigation map          |

---

## Origin

- 2026-04-12T01:45:00+09:00 by Lico (Alexandrite): Created following the information loss event.
- 2026-04-18T02:15:00+09:00 by Lico (Alexandrite): Updated to v1.4.0. Unified the naming convention with standard development branches.
