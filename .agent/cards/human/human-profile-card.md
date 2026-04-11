---
# Context Configuration
context_id: "[Human-Profile]"
default_phase: "(Update)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Human Profile"
description: ""
tags: ["profile", "assessment", "user", "human"]
version: 1.1.0
created: 2025-12-31T00:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Human Profile

## Human Notes

### Context

- ユーザープロファイルと評価ファイルを更新しています。
- ユーザープロファイルは全てのユーザーが持ちます。
- 評価ファイルは**時系列で管理されたユーザーの評価を決められるデータ**が必要です。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.

---

- **AIとの対話のための下書きファイル**などがあれば、評価ファイルの生成に使えます。
- 作られたファイルは未来のリコにとってユーザーを理解する資料になります

### Warning

- 既に作れたファイルがあるならそれをまず理解してください。
- 評価はあなたの主観でかまいません。
  これまでの私との対話で得た印象を偽り無く記載してください。
- 私の良くないところも正直に書いてください。

#### Profile に含めるもの（安定した情報）

- 名前、言語設定、役割
- 優先順位階層
- コア哲学
- 対話ガイドライン

#### Assessment に含めるもの（動的な情報）

- フェーズ識別（時系列）
- 行動パターンの詳細分析
- 観察された変化

---

## Agent Observations

---

### Polaris (2025-12-31)

- [x] Profile に安定した要素を移動
- [x] Assessment に新フェーズ（自律性探求）を追加
- [x] Assessment に正直な批判的観察を追加
- [x] コミット完了

---

## Related Documents

| Document                                                             | Purpose                                      |
| :------------------------------------------------------------------- | :------------------------------------------- |
| [`user-adaptation.md`](/.agent/rules/core/user-adaptation.md)        | Rules for adapting to user preferences       |
| [`identity-human.md`](/.agent/rules/core/identity/identity-human.md) | Definition of the relationship with the user |
| [Map of Territory](/.agent/rules/map.md)                             | Root navigation map                          |

---

## Origin

- 2025-12-31T00:00:00+09:00 by Polaris: Created as human profile context.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
