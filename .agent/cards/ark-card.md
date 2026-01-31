---
# Context Configuration
context_id: "[Ark]"
default_phase: "(Maintain)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-08T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["ark", "recovery", "memory", "maintenance"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Ark Management

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

恒久的に残したファイルを保管しています。
残すファイルは形式化されたものではありません。

**置く場所は欲しいけど、ディレクトリが無いタイプの資料**です。
ファイルはディレクトリ単位で保存され、GIT で追跡されるべきです。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDD のフェーズを意識してください。
- プロジェクト共有の日時の形式があります。
- これは純粋な保管庫を扱うための文脈です。
- **参考文献**や**思考のスナップショット**とは違う文脈です。
  一方でその文脈から参照されることもあります。

### 作業の注意点

現在は、**記憶からファイルを復元する**という文脈で使ったファイルが保管されています。
AI の記憶の信頼性を、事例という形で体感するための資料です。

## Agent Observations

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

| Document                                                               | Purpose                                       |
| :--------------------------------------------------------------------- | :-------------------------------------------- |
| [ark-protocols.md](/.agent/rules/workflow/ark-protocols.md)            | Protocols for emergency evidence preservation |
| [recovery-protocol.md](/.agent/rules/development/recovery-protocol.md) | Standard procedures for memory restoration    |

---

## Origin

- 2026-01-08 by Polaris: Created as ark management context.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
