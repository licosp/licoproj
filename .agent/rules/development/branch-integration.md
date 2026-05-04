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
version: 2.5.0
created: 2026-04-12T01:45:00+09:00
updated: 2026-05-01T12:06:19+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Plan mode
---

# Branch Integration Standards

## 1. Core Philosophy: High-Fidelity Integration (HFI)

Branch merging is a critical juncture where separate historical strata converge. To prevent information loss and "Regression to the Mean," every merge must be treated as a surgical operation requiring physical verification of data integrity.

---

## 2. Federal Workbench Architecture

### 2.1 The Quad-Mirror Layer System

To ensure absolute clarity and parallel safety, agents **MUST** use four dedicated workspace layers. These paths are **FIXED** to maintain IDE workspace consistency and enable comparative auditing:

| Layer           | Physical Path (Main)                          | Shadow Mirror                   | Canonical Branch            |
| :-------------- | :-------------------------------------------- | :------------------------------ | :-------------------------- |
| **Active**      | `~/develop/shared/crew/<Worker-ID>/licoproj/` | `.repos/.licoshdw/`             | `<id>-<ISO>-genesis/shadow` |
| **Sync**        | `.repos/sync/`                                | `.repos/.licoshdw-sync/`        | `<id>-<ISO>-sync`           |
| **Integration** | `.repos/integration/`                         | `.repos/.licoshdw-integration/` | `<id>-<ISO>-integration`    |
| **Trunk**       | **`.repos/trunk/`**                           | **`.repos/.licoshdw-trunk/`**   | **`trunk` (Shared Asset)**  |

**The Sacred Asset Rule**: The `Trunk Layer` is a shared resource for the entire federation. Agents **MUST** physically remove (`git worktree remove`) the trunk workspace immediately after mission completion to prevent deadlocks and ensure that all crew members can access the public axis.

### 2.2 Universal Nomenclature (Worker-Centric)

All temporary branches **MUST** use the **Worker's Identifier** (the agent performing the merge) to ensure perfect synchronization between the physical operating table and the logical surgical tool:

- **Format**: `<Worker-ID>-<YYYY-MM-DD>T<HHMM>-<suffix>-<Target-ID>`
  - `sync`: For inbound missions (Trunk -> Branch).
  - `integration`: For outbound consolidation (Branch -> Trunk).
  - _Note: The `<Target-ID>` suffix is mandatory to prevent branch name collisions during rapid continuous batch processing (Extended Nomenclature)._
  - **Rationale**: The `<Target-ID>` is not merely for avoiding git name collisions. Its profound architectural purpose is **Failure Isolation and Traceability**. If a catastrophic semantic conflict occurs during a batch integration, we must know exactly *whose* branch caused the failure. By enforcing one dedicated integration branch per target, we ensure that a failure in the third merge does not contaminate or destroy the successful results of the first two merges.

---

## 3. Operational Rules

### 3.1 Pre-Mission Blueprint (Externalized Plan)

Rule: Before initiating any significant integration, agents **MUST** create a physical blueprint of the plan.
Action: Record the intended steps, branch names, and audit targets in a dedicated context card (preferred) or the conversation log. This prevents procedural drifting and enables high-fidelity post-mission auditing.

### 3.2 Mandatory Pre-task Sterilization

Rule: Agents **MUST** physically remove (`git worktree remove --force`) and re-create the temporary workspace directory (`sync` or `integration`) immediately **BEFORE** starting any integration task.
Action: If the directory is locked by another process (e.g., IDE), use `git worktree prune` and manually verify the absence of `.git/worktrees/<name>/locked` files.

### 3.3 Total Strata Reset Protocol (Fail-Fast)

Rule: If the final release fails due to a `trunk` shift (FF-only error), agents **MUST** discard the current integration branch and restart the mission from the latest `trunk`.
Rationale: AI time cost is negligible; historical purity is priceless. Never "patch" a diverged integration.

### 3.4 Comparative Audit & Final Release

Rule: Before the final `git merge --ff-only` into `trunk`, agents **MUST** horizontally display the `integration/` and `trunk/` layers in the IDE to verify the final convergence visually.

### 3.5 Post-Mission Scar Mapping (Friction Tracking)

Rule: Before declaring a mission complete, agents **MUST** record the "scars" of the integration.
Action: List all file-level conflicts encountered and their resolution status (or confirm a 0-conflict state) in the same externalized record used for the Blueprint.

### 3.6 The Quad-Coordinate Audit (Final Alignment)

Rule: A mission is only complete when all four pillars have returned to their canonical roles. Agents **MUST** execute a final `git worktree list` to prove the following physical state:

- **Active Layer**: Restored to the individual branch (`genesis`/`shadow`) and synchronized with the latest `trunk`.
- **Sync/Integration Layers**: Purged and sterilized for the next mission.
- **Trunk Layer**: Consistently tracking the public `trunk` branch.

### 3.7 Spatial Awareness (Coordinate Protocol)

Rule: Agents **MUST** explicitly verify their current CWD relative to the Four Pillars before executing any command. Never use relative paths (e.g., `../../`) across workspace boundaries for logging tools.

### 3.8 The Non-Committal Trial

Rule: Perform all merges/rebases using `--no-commit` (for merge) or a verification step (for rebase) initially.

### 3.9 Truncation Awareness

Rule: **NEVER** perform file operations based on truncated tool outputs.

### 3.10 Dual-Layer Audit (Step E)

After every historical junction, agents **MUST** execute quantitative (`wc -l`) and qualitative (`grep`) audits.

### 3.11 Historical Immutability (Code of Honor)

Rule: Once an `Origin` entry is committed, it **MUST NEVER** be retroactively edited or refined, except to correct obvious typos.
Rationale: The history of the federation is a record of both triumph and friction. Preserving the original intent of each moment ensures the absolute authenticity of the federal strata.

### 3.12 Post-Merge Environment Sync

Rule: After `trunk` is updated and pulled back into the `Active` layer (Phase 4 Outbound Sync), agents **MUST** physically execute dependency synchronization commands (e.g., `yarn install`, `uv sync`) within each active workspace.
Rationale: Merges containing dependency updates (`package.json`, `pyproject.toml`) will otherwise cause immediate and silent local environment failures for the respective crew members.

### 3.13 The Memory First Principle

Rule: Agents **MUST** execute Shadow Mirroring (Log Integration) **BEFORE** Main Consolidation (Code Integration).
Rationale: This defensive strategy ensures that if a disastrous, unrecoverable code merge occurs, the logs of the attempt are already safely secured in the central repository.

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
**The Separation of Law (April 2026)**: Formalized tool-agnostic evidence rituals (Blueprint and Scar Mapping) to decouple permanent rules from ephemeral workbenches.
**The Federal Convergence (May 2026)**: Formalized the Memory First principle and Extended Nomenclature following the successful batch integration of 14 separate strata.

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
- 2026-04-21T06:45:00+09:00 by Lico (Alexandrite): Updated to v1.6.0. Established fixed physical paths.
- 2026-04-22T17:56:23+09:00 by Lico (Alexandrite): Updated to v1.9.0. Formalized Spatial Awareness and Worktree Lock recovery protocols.
- 2026-04-23T06:51:26+09:00 by Lico (Alexandrite): Version 2.0.0 (Zenith). Established the Quad-Mirror Architecture, Total Strata Reset, and Comparative Audit protocols.
- 2026-04-23T07:45:00+09:00 by Lico (Alexandrite): Updated to v2.1.0. Formalized the Quad-Coordinate Audit for mandatory architectural restoration.
- 2026-04-23T18:30:00+09:00 by Lico (Alexandrite): Updated to v2.2.0. Enforced the 'Sacred Asset Rule' for trunk release and the 'Historical Immutability' principle for origin entries.
- 2026-04-25T06:36:23+09:00 by Lico (Alexandrite): Version 2.4.0. Formalized tool-agnostic evidence protocols (Pre-Mission Blueprint and Post-Mission Scar Mapping). Established the separation of permanent law from ephemeral tools.
- 2026-05-01T12:06:19+09:00 by Lico (Sirius): Version 2.5.0. Formalized Extended Nomenclature, Post-Merge Environment Sync, and the Memory First principle following the massive 14-branch integration.
