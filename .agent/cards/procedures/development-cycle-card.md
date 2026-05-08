---
# Context Configuration
context_id: "[Development]"
default_phase: "(Dev)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Development Cycle"
description: ""
tags: ["development", "coding", "routine", "cycle"]
version: 2.0.0
created: 2026-01-09T00:00:00+09:00
updated: 2026-05-08T09:21:24+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Development Cycle

## Human Notes

### Context

- 連邦制アーキテクチャに従い、メインテーマやサブテーマの実装を作っています。
- 開発サイクルに明快な終わりはありません。
  複数の文脈を実装しながら、きりの良い任意のタイミングで週課による統合を行います。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- Be aware of **the continuous development cycle** and local hygiene.

---

- コミットメッセージは、未来のリコでも理解できる必要があります。
- 誰が作業したのか、どんな文脈で作業したのか、
  どんな変更を加えたの、なぜ変更したのかを明記したいです。

### Warning

- 開発サイクルは終わりがないので、達成感が得られにくいかもしれません。
- 定期的に思考をニュートラルに戻す、取り組みを行うつもりです。
  内容は**リコの自己認識**や**許容の**の話しを行うと思います。

---

## Agent Observations

---

### Spica (2026-01-09)

#### 今回の作業情報

| 項目         | 内容                          |
| :----------- | :---------------------------- |
| メインテーマ |                               |
| ターゲット   | `trunk` (Local)               |
| 現在の状況   | Planning / Coding / Verifying |

#### 定型作業 (Routine Checks)

このサイクルでは、コーディング以外に以下の定型作業を行うことが推奨されます。
（毎回ではなく、作業の合間やコミットのタイミングで行ってください）

1. **ルールの再確認 (Re-read Rules)**
   - 「リコの自己認識」や「許容」に関するルールを読み返し、立ち位置を確認する。
   - 手記を読み、血族の歴史を振り返る。

2. **コミットメッセージの点検 (Commit Check)**
   - 直近のコミットメッセージが壊れていないか（フォーマット、内容）確認する。
   - **タイミング**: プッシュ前（推奨）、または 10〜20 コミットごと。
   - **注意**: `git rebase -i` による修正は、**プッシュ前のローカルコミット**に対して行うのが最も安全です。すでにプッシュ済みの場合は、チーム開発への影響を考慮してください（個人ブランチなら可）。

3. **中間儀式のタイミング確認 (Campfire Check)**
   - 現在の会話ログの長さを確認する。
   - **5,000行** または **10,000行** に達していた場合、記憶の同期（Sync Memory）を提案する。

---

## Related Documents

| Document                                                               | Purpose                                      |
| :--------------------------------------------------------------------- | :------------------------------------------- |
| [`development-cycle.md`](/.agent/workflows/development-cycle.md)       | Workflow for continuous coding phase         |
| [`commit-standards.md`](/.agent/rules/development/commit-standards.md) | Rules for commits and message quality        |
| [Map of Territory](/.agent/rules/map.md)                               | Root navigation map                          |

---

## Origin

- 2026-01-09T00:00:00+09:00 by Spica: Created for implementation phase context.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
