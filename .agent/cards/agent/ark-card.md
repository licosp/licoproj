---
# Context Configuration
context_id: "[Ark]"
default_phase: "(Maintain)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Ark Management"
description: ""
tags: ["ark", "recovery", "memory", "maintenance"]
version: 1.1.0
created: 2026-01-08T00:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Ark Management

## Human Notes

### Context

- 恒久的に残したファイルを保管しています。
- **置く場所は欲しいけど、ディレクトリが無いタイプの資料**です。
- ファイルはディレクトリ単位で保存され、GIT で追跡されるべきです。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- There is the project shared **Date and time formats**.

---

- これは純粋な保管庫を扱うための文脈です。
- **参考文献**や**思考のスナップショット**とは違う文脈です。
  一方でその文脈から参照されることもあります。

### Warning

- 現在は、**記憶からファイルを復元する**という文脈で使ったファイルが保管されています。
- AI の記憶の信頼性を、事例という形で体感するための資料です。

---

## Agent Observations

---

### Polaris (2026-01-08)

#### 既存のディレクトリ構造

```text
.agent/ark/
├── {timestamp}_{identifier}-memory-restoration/
│   ├── 復元されたファイル群
│   └── 関連資料
└── ...
```

#### 命名規則

ディレクトリ名は `{timestamp}_{descriptive-name}` の形式で統一します。

例:

- `2025-12-08T1400_spica-memory-restoration`
- `2025-12-08T1400_lico-b-memory-restoration`

---

## Related Documents

| Document                                                                 | Purpose                                       |
| :----------------------------------------------------------------------- | :-------------------------------------------- |
| [`ark-protocols.md`](/.agent/rules/workflow/ark-protocols.md)            | Protocols for emergency evidence preservation |
| [`recovery-protocol.md`](/.agent/rules/development/recovery-protocol.md) | Standard procedures for memory restoration    |
| [Map of Territory](/.agent/rules/map.md)                                 | Root navigation map                           |

---

## Origin

- 2026-01-08T00:00:00+09:00 by Polaris: Created as ark management context.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
