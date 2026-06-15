---
# Context Configuration
context_id: "[OpenCode]"
default_phase: "(Setup)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: OpenCode Environment"
description: "Context for configuring and managing the OpenCode coding agent."
tags: ["opencode", "environment", "coding-agent", "cli"]
version: 1.0.0
created: 2026-05-30T04:22:00+09:00
updated: 2026-05-30T04:22:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High)
---

# Context Whiteboard: OpenCode Environment

## Human Notes

### Context

- コーディングエージェントとしての OpenCode 環境の構成を管理します。
- 使用するモデルプロバイダーや、エージェントのルーティング設定が含まれます。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.

---

## Agent Observations

### Sirius (2026-05-30)

- **Positioning**: This card is used when modifying `.opencode/` settings in the workspace.
- **Scope**: Changes related to agent logic, model delegation (e.g., routing subagents to smaller models), and interface behaviors.

---

## Related Documents

| Document                                 | Purpose             |
| :--------------------------------------- | :------------------ |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---

## Origin

- 2026-05-30T04:22:00+09:00 by Lico (Sirius): Created to define the OpenCode agent context.
