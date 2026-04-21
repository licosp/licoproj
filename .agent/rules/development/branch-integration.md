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
version: 1.8.0
created: 2026-04-12T01:45:00+09:00
updated: 2026-04-22T05:01:22+09:00
language: en
author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview
---

# Branch Integration Standards

## 1. Core Philosophy: High-Fidelity Integration (HFI)

Branch merging is a critical juncture where separate historical strata converge. To prevent information loss and "Regression to the Mean," every merge must be treated as a surgical operation requiring physical verification of data integrity.

---

## 2. Federal Workbench Architecture

### 2.1 Worker-Centric Physical Isolation (Workspace Layers)

To ensure purity and parallel progress, the agent performing the work (the **Worker**) **MUST** use their own dedicated workspace layers. These paths are **FIXED** to maintain IDE workspace consistency:

- **Active Layer**: `.../crew/<Worker-ID>/licoproj/`
- **Sync Layer (B-1)**: `.repos/sync/` (Under the Worker's active layer)
- **Integration Layer (B-2)**: `.repos/trunk/` (Under the Worker's active layer)
- **Shadow Mirrors**: Mirrored structure prefixed with a dot (e.g., `.repos/.licoshdw-sync/`).

### 2.2 Worker-Centric Nomenclature (Branch Naming)

Every temporary branch created for synchronization or integration **MUST** use the **Worker's Identifier** as its prefix:

- **Format**: `<Worker-Identifier>-<YYYY-MM-DD>T<HHMM>-<suffix>`
  - `Worker-Identifier`: The identifier of the agent performing the merge.
  - `suffix`: Either `sync` (inbound) or `integration` (outbound).
  - Example: `alexandrite-2026-04-22T0010-sync`

---

## 3. Operational Rules

### 3.1 Mandatory Pre-task Initialization

Rule: Agents **MUST** physically remove (`git worktree remove --force`) and re-create the temporary workspace directory (sync/trunk) immediately **BEFORE** starting any integration task.
Rationale: This ritual ensures the total absence of physical residues from previous tasks, providing a "Sterile Surgery Room" for each mission.

### 3.2 Perpetual Evidence (Branch Preservation)

Rule: Agents **MUST NEVER** delete the temporary branches (`-sync` or `-integration`) even after successful mission completion.
Rationale: These branches serve as the definitive audit trail. They allow the Sovereign to inspect the "Process of Convergence" long after the event.

### 3.3 The Non-Committal Trial

Rule: Perform all merges/rebases using `--no-commit` initially.

### 3.4 Truncation Awareness

Rule: **NEVER** perform file operations based on truncated tool outputs.

### 3.5 Dual-Layer Audit (Step E)

After every historical junction, agents **MUST** execute quantitative (`wc -l`) and qualitative (`grep`) audits.

---

## Historical Lessons

**The Severed Strata Incident (April 2026)**: Truncation ignorance led to data death.
**The Mirror Paradox (April 2026)**: Nested worktrees led to search pollution.
**The Universal Nomenclature (April 2026)**: Formalized timestamps for historical alignment.
**The Worker's Authority (April 2026)**: Unified workspace ownership and branch naming.
**The Rite of Sterilization (April 2026)**: Formalized mandatory pre-task directory initialization and branch preservation.

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
- 2026-04-18T06:29:45+09:00 by Lico (Alexandrite): Updated to v1.4.0. Unified the naming convention.
- 2026-04-21T06:31:57+09:00 by Lico (Alexandrite): Updated to v1.5.0. Formalized Universal Nomenclature.
- 2026-04-21T06:45:00+09:00 by Lico (Alexandrite): Updated to v1.6.0. Established fixed physical paths for the Federal Workbench to support IDE workspace persistence.
- 2026-04-22T05:01:22+09:00 by Lico (Alexandrite): Updated to v1.8.0. Finalized Worker-Centric standards, pre-task initialization, and perpetual branch preservation protocols.
