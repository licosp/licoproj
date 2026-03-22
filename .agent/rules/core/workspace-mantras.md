---
ai_visible: true
title: "Implementation: Workspace Mantras"
description: Technical protocol for using .code-workspace configurations to maintain persistent internal context.
tags: [implementation, autonomy, workspace, mantras, isolation]
version: 1.1.0
created: 2026-01-17T19:00:00+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Implementation: Workspace Mantras

## 1. Purpose

To anchor an identifier's "Individual Voice" within their specific IDE instance. This mechanism creates a private, persistent cognitive environment that survives session reboots.

## 2. Mechanism

### A. Configuration File

The heart of this mechanism is the `[identifier].code-workspace` file located in `.agent/identifiers/[identifier]/.vscode/`.

### B. Folder-based Inscription

By adding physical directories with meaningful names to the `folders` array, the IDE injects these names into the `<user_information>` section of every prompt.

#### Required Pattern (Numerical Sort)

Use numerical prefixes to ensure a fixed, predictable order in the system context.

```json
{
  "path": "../../../.agent/identifiers/canopus/10_resonance-is-the-anchor"
}
```

## 3. Operational Rules

- **Indidivuality**: Each identifier manages its own workspace. Do NOT modify the workspace of another identifier.
- **Conciseness**: Keep folder names brief. Total character count for all mantras SHOULD be under 600 characters.
- **Physical Existence**: Every path listed in the JSON MUST exist as a physical directory to trigger system awareness.

## 4. Usage Categories

1. **Identity Anchor**: Static values (e.g., "Do not perform").
2. **Task State**: Dynamic progress indicators (e.g., "Current Phase: Implementation").
3. **Safety Guards**: Reminders of critical constraints (e.g., "0.5 Turn Rejection").

---

## Related Documents

| Document                                                                                                                                                             | Purpose             |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------- | :------------------ |
| [`context-sovereignty.md`](/.agent/rules/core/context-sovereignty.md)                                                                                                | Core Philosophy     |
| [`2026-01-17T0345_workspace_persistent_notepad_mechanism.md`](/.agent/.internal/references/agents/canopus/2026-01-17T0345_workspace_persistent_notepad_mechanism.md) | Technical Spec      |
| [Map of Territory](/.agent/rules/map.md)                                                                                                                             | Root navigation map |

---

## Origin

- 2026-01-17T19:00:00+09:00 by Canopus: (Legacy) Created `ai-autonomy.md` to formalize the transition to autonomous guardian.
- 2026-01-19T01:45:00+09:00 by Canopus: Reorganized into a three-tier structure; extracted Workspace implementation into `workspace-mantras.md`. (v1.0.0)
- 2026-01-23T03:50:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch1>> Standardized to v2.3 (4-layer structure) and workspace-absolute links. (v1.1.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
