---
ai_visible: true
title: Cross-Link Audit Master Plan
description: Master plan for cross-link audit across all target directories
tags: [maintenance, cross-link, audit, plan]
version: 1.0.0
created: 2026-01-04T11:51:00+09:00
updated: 2026-05-08T15:15:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Cross-Link Audit Master Plan

This document defines the **target directories** for cross-link audit. For the actual work steps, see [`cross-link-audit.md`](/.agent/rules/procedures/cross-link-audit.md).

---

## 1. Target Directories

### Tier 1: Core Documentation

| Directory                    | Status | Notes                 |
| :--------------------------- | :----: | :-------------------- |
| `.agent/rules/`              |   ✓    | 2026-01-04 Completion |
| `.agent/workflows/`          |   ✓    | 2026-01-04 Completion |
| `.agent/.internal/legacy.md` |   ✓    | Navigation only       |

### Tier 2: Internal Documentation

| Directory                      | Status | Notes                 |
| :----------------------------- | :----: | :-------------------- |
| `.agent/.internal/references/` |   ✓    | 2026-01-04 Completion |
| `.agent/.internal/thoughts/`   |   ✓    | 2026-01-04 Completion |
| `.agent/.internal/letters/`    |   ✓    | 2026-01-04 Completion |

---

## 2. Standard Structure (v2.3)

All files in the knowledge graph must follow the **4-Layer Structure** defined in [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md).

1. **Frontmatter** (Related links moved to Related Documents)
2. **Body Content** (includes Historical Background)
3. **Related Documents** (Categorized table format)
4. **Origin** (Timestamped milestones with Maintenance Seals)

---

## Historical Background

**The Memory Graph Integration**: In January 2026, we shifted from "Disconnected Rule Sheets" to an "Integrated Memory Graph." This master plan serves as the architectural blueprint for that transition, ensuring that every node in the Lico knowledge base is reachable and contextualized through its relationships to other documents.

---

## Related Documents

| Document                                                                                    | Purpose                              |
| :------------------------------------------------------------------------------------------ | :----------------------------------- |
| [`cross-link-audit.md`](/.agent/rules/procedures/cross-link-audit.md)                              | Detailed audit procedure             |
| [`maintenance-rule-audit.md`](/.agent/rules/procedures/maintenance-rule-audit.md)                  | The "Gardening Protocol" methodology |
| [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) | Structural standards                 |
| [Map of Territory](/.agent/rules/map.md)                                                    | Root navigation map                  |

---

## Origin

- 2026-01-04T11:51:00+09:00 by Polaris: Created master plan
- 2026-01-25T06:55:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch2.3>> Created by standardizing the audit master plan to v2.3 constitutional standards. (v1.0.0)
- 2026-03-21T17:26:00+09:00 by Lico (Sirius): Executed High-Fidelity Rule Audit (Batch 07) to restore lost historical origin context and standardized cross-links.
- 2026-05-08T15:15:00+09:00 by Sirius: Relocated directory to rules/procedures/ for structural consolidation.
