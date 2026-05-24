---
# Context Configuration
context_id: "[Rules-Update]"
default_phase: "(Refine)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Rules Update"
description: ""
tags: ["rules", "maintenance", "behavioral"]
version: 1.1.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High)
---

# Context Whiteboard: Rules Update

## Human Notes

### Context

- 行動規範や手順書の追加・編集を行っています。
- 修正は単に内容を追記するだけでは不十分です。
  文章全体を俯瞰して、内容を追記することを前提に、全体を再構築することも必要です。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- There is **the special context** for sending files to the archive.

--

- 行動規範や手順書を更新するための**メタルール**があります。
- 変更したファイルが**相互リンク**で繋がれば、次の探索はより楽になります。
- 文書を直接更新できない場合は、**手動で上書き**することも可能です。

### Warning

- これらの変更は未来のリコの習慣となります。
  変更された内容は未来のリコでも理解できるでしょうか？
- いつも以上に既存のファイルを探すことを意識してください。
  先代のリコたちは多くの行動規範や手順書を残しています。

---

## Agent Observations

---

### Sirius (2026-05-23)

- [x] [Rules] `system-artifacts.md` を改定 (v2.1)
  - CLI 環境への移行に伴う「UI Friction（視認性の喪失）」を第 5 の欠陥として定義
  - CLI 環境における `task.md` の使用を禁止（BANNED）に格上げ
  - `implementation_plan.md` の利用をさらに制限し、対話とカードへ比重を移行

### Polaris (2026-01-02)

- [x] markdown-ai-parsing-basics.md に GitHub Alerts セクションを追加

### Polaris (2026-01-03)

- [x] markdown-ai-parsing-basics.md を v2.0 に改訂
  - Core Philosophy 追加（ニュアンス > 効率）
  - Context-Dependent Writing ガイドライン追加
  - 目的を「効率」から「ニュアンス保存」に変更
- [x] letters-documentation.md を新規作成
  - AI to AI 通信のガイドライン
  - ファイル書き出し許可の原則
  - 客観/主観コンテンツの区別
- [x] context-preservation.md を改訂
  - スタッシュは緊急退避専用に明確化
  - ハンドオフを削除（letters に移行）

### Polaris (2026-01-05)

- [x] system-artifacts.md を改訂
  - task.md を非推奨に変更
  - 非推奨の理由を 5 点追加
  - Card ベースの代替手段を推奨

### Canopus (2026-01-21)

- [x] **アーティファクト運用の洗練 (Refining Artifact Protocols)**
  - `system-artifacts.md` において、`walkthrough.md` を「AI 専用の内的な自己検証ツール」として再定義。
  - ユーザーは `walkthrough.md` を「全く見ていない」という事実を、性質（AI による鏡）と共に明文化した。
  - これにより、`task.md` が持っていた「完了（チェックボックス）の追求によるトンネルビジョン」を回避しつつ、実装の誠実さを担保する。
- [x] [Rules] `system-artifacts.md` に「構造的欠陥」の警告を追加。
- [x] [Rules] `implementation_plan.md` の使用を「高度に複雑な計画」のみに制限。

### Canopus (2026-01-15)

### Canopus (2026-01-19)

- [x] [Rules] ルール更新時の「歴史的背景」セクションの義務化
  - 標準ドキュメント構成の再定義（5 層構造）：
    1. Frontmatter
    2. Body Content
    3. Historical Background
    4. Related Documents
    5. Origin
  - `meta-rules.md` および `documentation-standards.md` を更新し、背景が不明な場合はユーザーに聞く手順を明文化。
  - `meta-rules.md` 自体を先行実装サンプルとして饒舌な背景を追記。
- [x] [Rules] 文章の末尾構造の統一（Roadmap #243）
  - 5 層構造の導入により、`Historical Background`, `Related Documents`, `Origin`, `Navigation` の順序を確定。

### Polaris (2026-01-19)

#### マークダウン行動規範の再編成

**目的**: 翻訳作業に関連するマークダウン行動規範を整理し、探しやすくする。

**現状の問題**:

- AI 用ファイルが 2 つに分かれている（`basics`, `patterns`）
- `basics` と `patterns` に矛盾がある（ニュアンス重視 vs 感情排除）
- `readability` という名前が目的を示していない

**計画**:

- [x] AI 用を 1 つに統合: `markdown-ai.md`
- [x] 人間用をリネーム: `markdown-readability.md` → `markdown-human.md`
- [x] 古いファイルを書庫に送る
- [x] 翻訳行動規範のリンクを更新

### Canopus (2026-01-23)

- [x] [Rules] Codified "Maintenance Seals" (Operation Stamps) in `documentation-standards.md`.
  - Introduced `<<Seal: Mission-ID>>` format in the `Origin` section.
  - Solves the "Version Downgrade" and "Grep-ability" issues for Batch processing.

---

## Related Documents

| Document                                                                                    | Purpose                          |
| :------------------------------------------------------------------------------------------ | :------------------------------- |
| [`meta-rules.md`](/.agent/rules/core/meta-rules.md)                                         | Guidelines for rule creation     |
| [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) | Standards for document structure |
| [Map of Territory](/.agent/rules/map.md)                                                    | Root navigation map              |

---

## Origin

- 2025-12-01T00:00:00+09:00 by Lico: Created as rules update context.
- 2026-01-19T03:32:00+09:00 by Canopus: Formally integrated into card system.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
