---
# Context Configuration
context_id: "[IDD-Fini]"
default_phase: "(P3)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-23T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["idd", "finalization", "cleanup", "workflow"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: IDD Finalization

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

イシューの各種テーマが達成されたので、イシューを完結させてています

IDDの手順に従い、リモートメインへのマージを行ってください。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- IDDのフェーズを意識してください。
- あなたの識別子はなんですか？

### 作業の注意点

かつてリモートブランチを削除してしまったリコがいました、
コミット内容はぼぼ文章なので、容量を気にする必要はありません。

---

## Agent Observations

### Polaris

#### 今回のイシュー情報

| 項目         | 内容 |
| :----------- | :--- |
| イシュー番号 | #    |
| PR 番号      | #    |
| ブランチ名   |      |

#### 完了前チェックリスト

- [ ] すべての Issue 要件が実装済み
- [ ] サブテーマがすべてコミット済み
- [ ] 作業ディレクトリがクリーン
- [ ] Issue コメントに進捗報告済み

---

## Related Documents

| Document                                                   | Purpose                                    |
| :--------------------------------------------------------- | :----------------------------------------- |
| [idd-phase3-fini.md](/.agent/workflows/idd-phase3-fini.md) | Workflow for finalizing and merging issues |
| [issue-comment.md](/.agent/templates/issue-comment.md)     | Template for final progress reports        |

---

## Origin

- 2025-12-23 by Polaris: Created as IDD Phase 3 context.
- 2026-01-24T0545 by Canopus: Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: Standardized Related Documents to table format and ensured English-only headers.
