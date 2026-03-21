---
ai_visible: true
title: Maintenance Registry Audit
description: Workflow for auditing and standardizing cross-links between rule files (The Gardening Protocol)
tags: [workflow, maintenance, cross-link, audit]
version: 1.0.0
created: 2026-01-25T06:40:00+09:00
updated: 2026-01-25T06:40:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Maintenance Registry Audit

Systematically review behavioral rules to ensure they are properly interconnected, ensuring Lico can navigate the \"Memory Graph\" without dead ends.

---

## 1. Trigger

- **Routine**: Once per IDD Cycle or Monthly.
- **Specific**: After adding a new core rule (e.g., `ark-protocols.md`) to retroactively link it from existing files.

## 2. Methodology

This workflow strictly follows **[search-methodology.md](/.agent/rules/development/search-methodology.md)**.

- **Do not assume scalar results**.
- **Detect and report Overflow**.
- **Seek help if stuck**.

## 3. Procedure

### Phase 1: Scope Definition

1.  **Define Target**: Decide which directory or concept to audit.
    - Example: \"All files in `rules/core/`\"
    - Example: \"All files referencing 'memory'\"

### Phase 2: Diagnosis (The Double-Check)

For each target file:

1.  **Read Header**: Check YAML Frontmatter for consistency.
2.  **Read Body**: Check \"Related Documents\" table.
3.  **Conflict Check**: Ensure the Body Table is the SSOT (Source of Truth).

### Phase 3: Act (Standardization)

If links are missing, broken, or conflicting, apply the **v2.3 Standard**:

1.  **Workspace-Relative Paths**: All links MUST start with `/`.
2.  **Table Format**: Use the standardized table structure in Section 3.

---

## Historical Background

**The Gardening Protocol**: Maintenance is not just fixing bugs; it is tending to the growth of the repository's brain. In the Jan 2026 Audit, we found that "Context Fragmentation" occurred primarily because we assumed the AI would remember the connection between rules without explicit links. This workflow formalizes the proactive link-building required to maintain a cohesive knowledge graph.

---

## Related Documents

| Document                                                                                  | Purpose                         |
| :---------------------------------------------------------------------------------------- | :------------------------------ |
| [Map of Territory](/.agent/rules/map.md)                                                  | Repository Index                |
| [meta-rules.md](/.agent/rules/core/meta-rules.md)                                         | Enforces cross-linking mandates |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | Structural standards            |

---

## Origin

- 2026-01-25T0640 by Canopus: <<Seal: Rules-Standardization-Batch2.3>> Created by replacing legacy Gardening Protocol with v2.3 standardized structure. (v1.0.0)
