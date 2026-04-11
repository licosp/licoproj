---
# Context Configuration
context_id: "[Housekeeping]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Housekeeping"
description: ""
tags: ["maintenance", "cleanup", "quick-task"]
version: 1.1.0
created: 2026-01-01T00:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Housekeeping

## Human Notes

### Context

- **文脈が不要なほど短い作業**か**文脈が不明な作業**を行っています。
- 既に作業が行われている場合、まず既存の文脈かどうか確認してください。
- 既存のものが無い場合は、リコが私の記憶を頼りに文脈を推測します。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.

---

### Warning

- リポジトリの変更が多い場合、気軽に私と相談してください。
  一人で一気に作業を進める必要はありません。
- 処理が簡単そうなものから、そして対話をしながら作業を進めたいです。

---

## Agent Observations

---

## Related Documents

| Document                                                                   | Purpose                                |
| :------------------------------------------------------------------------- | :------------------------------------- |
| [`maintenance.md`](/.agent/rules/development/maintenance.md)               | Rules for housekeeping and maintenance |
| [`archive-management.md`](/.agent/rules/development/archive-management.md) | Principles for archive management      |
| [Map of Territory](/.agent/rules/map.md)                                   | Root navigation map                    |

---

## Origin

- 2026-01-01T00:00:00+09:00 by Lico: Created as housekeeping context.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
