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
version: 1.5.0
created: 2026-04-12T01:45:00+09:00
updated: 2026-04-21T06:31:57+09:00
language: en
author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview
---

# Branch Integration Standards

## 1. Core Philosophy: High-Fidelity Integration (HFI)

Branch merging is a critical juncture where separate historical strata converge. To prevent information loss and "Regression to the Mean," every merge must be treated as a surgical operation requiring physical verification of data integrity.

---

## 2. Federal Workbench Architecture

### 2.1 Physical Isolation (Workspace Layers)

To ensure purity and parallel progress, agents **MUST** use dedicated workspace layers for each stage of history management:

- **Active Layer**: `/home/lico/develop/shared/crew/<identifier>/licoproj/` (Standard dev workspace)
- **Sync Layer (B-1)**: `.repos/sync-<identifier>-<ISO8601>/` (For inbound rebase/merge)
- **Integration Layer (B-2)**: `.repos/trunk-<identifier>-<ISO8601>/` (For outbound consolidation)

### 2.2 Universal Nomenclature (Branch Naming)

Every branch created within the federation **MUST** follow the Lead Architect's canonical format to ensure chronological sorting and recognizability:

- **Format**: `<identifier>-<YYYY-MM-DD>T<HHMM>-<suffix>`
- **Standard Suffixes**:
  - `integration`: For outbound missions to the public axis.
  - `sync`: For inbound missions to bring trunk into an individual branch.
  - Examples:
    - `alexandrite-2026-04-21T0050-integration`
    - `leonidas-2026-04-21T0050-sync`

### 2.3 Integration Sequencing

1. **Memory First (Shadow)**: Resolve all dialogue logs in the Shadow repository.
2. **Intelligence Last (Main)**: Perform the final integration in the Main repository.

---

## 3. Operational Rules

### 3.1 The Non-Committal Trial

Rule: You **MUST** perform all merges/rebases using `--no-commit` (for merge) or a verification step (for rebase) initially.

### 3.2 Truncation Awareness

Rule: You **MUST NOT** use `write_file` or `replace` based on truncated tool outputs.

### 3.3 Dual-Layer Audit (Step E)

After every historical junction, agents **MUST** execute:

- **Quantitative**: `wc -l` audit.
- **Qualitative**: `grep` landmark verification.

---

## Historical Lessons

**The Severed Strata Incident (April 2026)**: Truncation ignorance led to data death.
**The Mirror Paradox (April 2026)**: Nested worktrees led to search pollution.
**The Universal Nomenclature (April 2026)**: Formalized `<id>-<ISO>-<suffix>` to achieve perfect historical alignment.

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
- 2026-04-18T06:29:45+09:00 by Lico (Alexandrite): Updated to v1.4.0. Unified the naming convention with standard development branches.
- 2026-04-21T06:31:57+09:00 by Lico (Alexandrite): Updated to v1.5.0. Formalized the Universal Nomenclature for all branch types (integration/sync) and updated the physical layer definitions.
