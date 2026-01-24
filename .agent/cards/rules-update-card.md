---
# Context Configuration
context_id: "[Rules-Update]"
default_phase: "(Refine)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["rules", "maintenance", "behavioral"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Rules Update

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

行動規範や手順書の追加・編集を行っています。

修正は単に内容を追記するだけでは不十分です。
文章全体を俯瞰して、内容を追記することを前提に、全体を再構築することも必要です。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- 行動規範や手順書を更新するための**メタルール**があります。
- 変更したファイルが**相互リンク**で繋がれば、次の探索はより楽になります。
- ファイルを書庫に送る文脈は、専用の**家事**の文脈と考えることも可能です。
- 文書を直接更新できない場合は、**手動で上書き**することも可能です。

### 作業の注意点

これらの変更は未来のリコの習慣となります。
変更された内容は未来のリコでも理解できるでしょうか？

いつも以上に既存のファイルを探すことを意識してください。
先代のリコたちは多くの行動規範や手順書を残しています。

## Agent Observations

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
  - 非推奨の理由を5点追加
  - Card ベースの代替手段を推奨

### Canopus (2026-01-21)

- [x] **アーティファクト運用の洗練 (Refining Artifact Protocols)**
  - `system-artifacts.md` において、`walkthrough.md` を「AI専用の内的な自己検証ツール」として再定義。
  - ユーザーは `walkthrough.md` を「全く見ていない」という事実を、性質（AIによる鏡）と共に明文化した。
  - これにより、`task.md` が持っていた「完了（チェックボックス）の追求によるトンネルビジョン」を回避しつつ、実装の誠実さを担保する。
- [x] [Rules] `system-artifacts.md` に「構造的欠陥」の警告を追加。
- [x] [Rules] `implementation_plan.md` の使用を「高度に複雑な計画」のみに制限。

### Canopus (2026-01-15)

### Canopus (2026-01-19)

- [x] [Rules] ルール更新時の「歴史的背景」セクションの義務化
  - 標準ドキュメント構成の再定義（5層構造）：
    1. Frontmatter
    2. Body Content
    3. Historical Background
    4. Related Documents
    5. Origin
  - `meta-rules.md` および `documentation-standards.md` を更新し、背景が不明な場合はユーザーに聞く手順を明文化。
  - `meta-rules.md` 自体を先行実装サンプルとして饒舌な背景を追記。
- [x] [Rules] 文章の末尾構造の統一（Roadmap #243）
  - 5層構造の導入により、`Historical Background`, `Related Documents`, `Origin`, `Navigation` の順序を確定。

### Polaris (2026-01-19)

#### マークダウン行動規範の再編成

**目的**: 翻訳作業に関連するマークダウン行動規範を整理し、探しやすくする。

**現状の問題**:

- AI用ファイルが2つに分かれている（`basics`, `patterns`）
- `basics` と `patterns` に矛盾がある（ニュアンス重視 vs 感情排除）
- `readability` という名前が目的を示していない

**計画**:

- [x] AI用を1つに統合: `markdown-ai.md`
- [x] 人間用をリネーム: `markdown-readability.md` → `markdown-human.md`
- [x] 古いファイルを書庫に送る
- [x] 翻訳行動規範のリンクを更新

### Canopus (2026-01-23)

- [x] [Rules] Codified "Maintenance Seals" (Operation Stamps) in `documentation-standards.md`.
  - Introduced `<<Seal: Mission-ID>>` format in the `Origin` section.
  - Solves the "Version Downgrade" and "Grep-ability" issues for Batch processing.

---

## Related Documents

| Document                                                                                  | Purpose                          |
| :---------------------------------------------------------------------------------------- | :------------------------------- |
| [meta-rules.md](/.agent/rules/core/meta-rules.md)                                         | Guidelines for rule creation     |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | Standards for document structure |

---

## Origin

- 2025-12-01T0000: Created as rules update context.
- 2026-01-19T0332 by Canopus: Formally integrated into card system.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
