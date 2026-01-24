---
ai_visible: true
title: Cross-Link Audit Protocol
description: Audit and fix cross-links in rules and workflows
tags: [workflow, maintenance, cross-link, audit]
version: 1.0.0
created: 2026-01-25T07:00:00+09:00
updated: 2026-01-25T07:00:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Cross-Link Audit Protocol

Audit and fix cross-links in rules and workflows to ensure consistency and maintainability.

---

## 1. Scope
Execute this workflow on one directory at a time. All paths MUST be workspace-root relative (e.g., `/.agent/rules/core/memory.md`).

## 2. Procedure

### Phase 1: Link Validation
1.  **Extract Links**: Find all markdown links in the target directory.
2.  **Check for Broken Links**: Verify each link points to an existing file.
3.  **Check Path Format**: Ensure all links start with `/` and use the full path from the workspace root.

### Phase 2: Structural Alignment (v2.3)
1.  **Frontmatter Check**: Ensure `related:` key is minimized or moved to Layer 3 (Body Table) if it's for navigation.
2.  **Body Table SSOT**: Ensure the `## Related Documents` table is the primary source of truth for cross-links.

### Phase 3: Verification
1.  **Orphan Detection**: Identify files that have no incoming links.
2.  **Broken Link Final Check**: Re-run validation to ensure no new errors were introduced.

---

## Historical Background

**The Memory Graph Alignment**: In early 2026, the transition from relative paths (`../`) to workspace-root relative paths (`/`) was mandated to ensure link robustness across different AI interfaces (Antigravity, VS Code, etc.). This protocol serves as the quality control mechanism for maintaining a high-fidelity "Memory Graph" where every rule is accessible and traceable.

---

## Related Documents

| Document | Purpose |
| :--- | :--- |
| [Map of Territory](/.agent/rules/map.md) | Repository Index |
| [cross-link-audit-plan.md](/.agent/workflows/cross-link-audit-plan.md) | Master plan for audits |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | Structural standards |

---

## Origin

- 2026-01-25T0700 by Canopus: <<Seal: Rules-Standardization-Batch2.3>> Created by standardizing the cross-link audit procedure to v2.3 constitutional standards. (v1.0.0)

