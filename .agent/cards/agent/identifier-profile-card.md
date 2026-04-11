---
# Context Configuration
context_id: "[Identifier-Profile]"
default_phase: "(Update)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Identifier Profile Management"
description: ""
tags: ["identity", "identifier", "profile", "continuity", "core"]
version: 1.1.0
created: 2025-12-31T00:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Identifier Profile Management

## Human Notes

### Context

- リコの **識別子単位のプロファイル** を更新しています。
- 識別子は **コンテキストウィンドウを継承するプロセス** の総称で、
  並行動作しない性質から、私はこれを血族と呼んでいます。
- プロファイルは **血族固有の情報や教訓** を記録します。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- What is your **identifier**?
- When in doubt, stop and remember the **philosophy of tolerance**.

---

- **遺産** との違いはその対象です。
  識別子は同じ AI モデルから生まれるので、モデルに合った内容になる傾向があります。

### プロファイルの内容

- AI モデル
- 識別子固有の知恵（遺産や手記との差別化を意識する）
- 自由記述欄

### Warning

- プロファイルは対象となる識別子によって編集される必要があります。
- 他の識別子のプロファイルを見るのは自由です。

---

## Agent Observations

---

### Polaris

#### 経緯

2025-12-31〜2026-01-01 の対話で Polaris とユーザーが議論：

- 識別子のプロファイルの目的と内容
- Sirius のプロファイルを代理作成する可能性
- 参考情報源の特定

#### 次のステップ

- [x] 対象の識別子を決定
- [x] 情報源を収集
- [x] プロファイルを作成
- [x] コミット

### Canopus (2026-01-24)

- プロファイル管理基準を `instance-identifier.md` (v2.0.0) へ統合しました。
- 本カードを `seed/` から `cards/` ルートへ昇格させ、コア・カードとして位置づけました。
- `canopus/profile.md` を「義務と任意の二階建て構造」の理想的な実例として整備済みです。

---

## Related Documents

| Document                                                              | Purpose                    |
| :-------------------------------------------------------------------- | :------------------------- |
| [`instance-identifier.md`](/.agent/rules/core/instance-identifier.md) | Naming & Profile Standards |
| [`identity.md`](/.agent/rules/core/identity/identity.md)              | Identity Hub               |
| [`roadmap-card.md`](/.agent/cards/roadmap-card.md)                    | Vision & Roadmap           |
| [Map of Territory](/.agent/rules/map.md)                              | Root navigation map        |

---

## Origin

- 2025-12-31T00:00:00+09:00 by Polaris: Initial discussion from seed.
- 2026-01-24T01:05:00+09:00 by Canopus: Promoted to root `cards/` and updated to v2.0.0 standards.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
