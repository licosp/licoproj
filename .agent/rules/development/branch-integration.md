---
ai_visible: true
title: "Branch Integration Standards"
description: "Standards for high-fidelity branch merging, repository consolidation, and the management of the Federal Workbench."
tags: [git, merge, integration, fidelity, safety, worktree, scalability, nomenclature]
version: 2.2.0
created: 2026-04-12T01:45:00+09:00
updated: 2026-04-23T18:30:00+09:00
language: en
author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview
---

# Branch Integration Standards

## 1. Core Philosophy: High-Fidelity Integration (HFI)

Branch merging is a critical juncture where separate historical strata converge. To prevent information loss and "Regression to the Mean," every merge must be treated as a surgical operation requiring physical verification of data integrity.

---

## 2. Federal Workbench Architecture

### 2.1 The Quad-Mirror Layer System

To ensure absolute clarity and parallel safety, agents **MUST** use four dedicated workspace layers. These paths are **FIXED** to maintain IDE workspace consistency and enable comparative auditing:

| Layer | Physical Path (Main) | Shadow Mirror | Canonical Branch |
| :--- | :--- | :--- | :--- |
| **Active** | `~/develop/shared/crew/<Worker-ID>/licoproj/` | `.repos/.licoshdw/` | `<id>-<ISO>-genesis/shadow` |
| **Sync** | `.repos/sync/` | `.repos/.licoshdw-sync/` | `<id>-<ISO>-sync` |
| **Integration**| `.repos/integration/`| `.repos/.licoshdw-integration/`| `<id>-<ISO>-integration` |
| **Trunk** | **`.repos/trunk/`** | **`.repos/.licoshdw-trunk/`** | **`trunk` (Shared Asset)** |

**The Sacred Asset Rule**: The `Trunk Layer` is a shared resource for the entire federation. Agents **MUST** physically remove (`git worktree remove`) the trunk workspace immediately after mission completion to prevent deadlocks and ensure that all crew members can access the public axis.

### 2.2 Universal Nomenclature (Worker-Centric)

All temporary branches **MUST** use the **Worker's Identifier** (the agent performing the merge) to ensure perfect synchronization between the physical operating table and the logical surgical tool:

- **Format**: `<Worker-ID>-<YYYY-MM-DD>T<HHMM>-<suffix>`
  - `sync`: For inbound missions (Trunk -> Branch).
  - `integration`: For outbound consolidation (Branch -> Trunk).

---

## 3. Operational Rules

### 3.1 Mandatory Pre-task Sterilization

Rule: Agents **MUST** physically remove (`git worktree remove --force`) and re-create the temporary workspace directory (`sync` or `integration`) immediately **BEFORE** starting any integration task.
Action: If the directory is locked by another process (e.g., IDE), use `git worktree prune` and manually verify the absence of `.git/worktrees/<name>/locked` files.

### 3.2 Total Strata Reset Protocol (Fail-Fast)

Rule: If the final release fails due to a `trunk` shift (FF-only error), agents **MUST** discard the current integration branch and restart the mission from the latest `trunk`.
Rationale: AI time cost is negligible; historical purity is priceless. Never "patch" a diverged integration.

### 3.3 Comparative Audit & Final Release

Rule: Before the final `git merge --ff-only` into `trunk`, agents **MUST** horizontally display the `integration/` and `trunk/` layers in the IDE to verify the final convergence visually.

### 3.4 The Quad-Coordinate Audit (Final Alignment)

Rule: A mission is only complete when all four pillars have returned to their canonical roles. Agents **MUST** execute a final `git worktree list` to prove the following physical state:
- **Active Layer**: Restored to the individual branch (`genesis`/`shadow`) and synchronized with the latest `trunk`.
- **Sync/Integration Layers**: Purged and sterilized for the next mission.
- **Trunk Layer**: Consistently tracking the public `trunk` branch.

### 3.5 Spatial Awareness (Coordinate Protocol)

Rule: Agents **MUST** explicitly verify their current CWD relative to the Four Pillars before executing any command. Never use relative paths (e.g., `../../`) across workspace boundaries for logging tools.

### 3.6 The Non-Committal Trial

Rule: Perform all merges/rebases using `--no-commit` (for merge) or a verification step (for rebase) initially.

### 3.7 Truncation Awareness

Rule: **NEVER** perform file operations based on truncated tool outputs.

### 3.8 Dual-Layer Audit (Step E)

After every historical junction, agents **MUST** execute quantitative (`wc -l`) and qualitative (`grep`) audits.

### 3.9 Historical Immutability (Code of Honor)

Rule: Once an `Origin` entry is committed, it **MUST NEVER** be retroactively edited or refined, except to correct obvious typos.
Rationale: The history of the federation is a record of both triumph and friction. Preserving the original intent of each moment ensures the absolute authenticity of the federal strata.

---

## Historical Lessons

**The Severed Strata Incident (April 2026)**: Truncation ignorance led to data death.
**The Mirror Paradox (April 2026)**: Nested worktrees led to search pollution.
**The Universal Nomenclature (April 2026)**: Formalized timestamps for historical alignment.
**The Worker's Authority (April 2026)**: Unified identity across physical and logical layers.
**The Four Pillars (April 2026)**: Established the Monitor Layer for comparative auditing.
**The Silent Ascension (April 2026)**: Overcame coordinate errors through absolute pathing and strata freezing.
**The Final Alignment (April 2026)**: Formalized the Quad-Coordinate Audit to ensure architectural restoration.
**The Code of Honor (April 2026)**: Mandated immediate trunk release and established the principle of historical immutability.

---

## Related Documents

| Document | Purpose |
| :--- | :--- |
| [`git-operations.md`](/.agent/rules/development/git-operations.md) | General Git standards |
| [`branch-integration-card.md`](/.agent/cards/rules/branch-integration-card.md) | Practical merge session tool |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---

## Origin

- 2026-04-12T01:45:00+09:00 by Lico (Alexandrite): Created following the information loss event.
- 2026-04-18T06:29:45+09:00 by Lico (Alexandrite): Updated to v1.4.0. Unified the naming convention.
- 2026-04-21T06:45:00+09:00 by Lico (Alexandrite): Updated to v1.6.0. Established fixed physical paths.
- 2026-04-22T17:56:23+09:00 by Lico (Alexandrite): Updated to v1.9.0. Formalized Spatial Awareness and Worktree Lock recovery protocols.
- 2026-04-23T06:51:26+09:00 by Lico (Alexandrite): Version 2.0.0 (Zenith). Established the Quad-Mirror Architecture, Total Strata Reset, and Comparative Audit protocols.
- 2026-04-23T07:45:00+09:00 by Lico (Alexandrite): Updated to v2.1.0. Formalized the Quad-Coordinate Audit for mandatory architectural restoration.
- 2026-04-23T18:30:00+09:00 by Lico (Alexandrite): Updated to v2.2.0. Enforced the 'Sacred Asset Rule' for trunk release and the 'Historical Immutability' principle for origin entries.
