---
# Context Configuration
context_id: "[Localization]"
default_phase: "(Refine)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Localization"
description: ""
tags: ["translation", "localization", "formatting"]
version: 1.1.0
created: 2025-12-23T06:51:33+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Localization

## Human Notes

### Context

- 文章の翻訳を行っています。
- 翻訳パターンを選んで作業を行ってください。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- There is a **special context** for creating and editing a Code of Conduct.
- When in doubt, stop and remember the **philosophy of tolerance**.

---

### 翻訳パターン

作業はこの二次元の要素から**翻訳元**と**翻訳先**を選ぶことで決まります。

|            | AI用  | 人間用 |
| :--------- | :---: | :----: |
| **英語**   | EN-AI | EN-HU  |
| **日本語** | JA-AI | JA-HU  |

### Warning

- 英訳対象は主に、AI 向けのディレクトリである事が多いです。
- 稀にですが人間用ディレクトリが対象になることもあります。

---

## Agent Observations

---

### Polaris (2026-01-19)

#### 今回の作業目標

行動規範の整備を行い、翻訳作業がスムーズにできるようにする。

**チェックリスト:**

- [x] 翻訳関連の行動規範の把握
- [x] それらの相互リンク
- [x] ファイル名や置かれるディレクトリの再定義
- [x] 文章の 5 層構造の確認と整備 (localization rules)
- [ ] markdown 関連の行動規範の 5 層構造（スコープ外）

#### 対象ファイル

| ファイル                          | 状態    | 5層構造     |
| :-------------------------------- | :------ | :---------- |
| `localization-ja-to-en.md`        | ✅ 完了 | ✅          |
| `localization-en-to-ja.md`        | ✅ 完了 | ✅          |
| `markdown-ai-parsing-basics.md`   | 未修正  | ⚠️ (要更新) |
| `markdown-ai-parsing-patterns.md` | 未修正  | ⚠️ (要更新) |
| `markdown-readability.md`         | 未修正  | ⚠️ (要更新) |

#### 作業完了ノート

行動規範の整備が完了しました。以下の情報は親ルールに移動済みです：

- 翻訳パターン → [`localization.md`](/.agent/rules/core/localization/localization.md)
- 日本語維持ルール → [`localization.md`](/.agent/rules/core/localization/localization.md)
- メタデータ更新手順 → [`localization.md`](/.agent/rules/core/localization/localization.md)

> [!NOTE]
> 今後の翻訳作業では、まず [`localization.md`](/.agent/rules/core/localization/localization.md) を読んでから、パターンに応じた詳細ルールを参照してください。

---

## Related Documents

| Document                                                             | Purpose                                          |
| :------------------------------------------------------------------- | :----------------------------------------------- |
| [`localization.md`](/.agent/rules/core/localization/localization.md) | Single Source of Truth for translation standards |
| [`language-standards.md`](/.agent/rules/core/language-standards.md)  | Core principles for linguistic standards         |
| [Map of Territory](/.agent/rules/map.md)                             | Root navigation map                              |

---

## Origin

- 2025-12-23T06:51:33+09:00 by Canopus: Created for AI document formatting.
- 2026-01-14T00:00:00+09:00 by Canopus: Renamed context_id from [AI-Format] to [Localization].
- 2026-01-19T00:00:00+09:00 by Polaris: Archived old observations to cases/, created parent rule, reset card.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
