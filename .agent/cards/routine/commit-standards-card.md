---
# Context Configuration
context_id: "[Commit-Standards]"
default_phase: "(Done)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-22T20:45:00+09:00
updated: 2026-01-24T05:45:00+09:00
tags: ["git", "standards", "commit", "convention"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Commit Standards

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

コミットに関する行動規範を更新しています。
行動規範だけではなく、コミットテンプレートの更新もその対象になります。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- 行動規範の作成・編集には**専用の文脈**が存在します。

### 作業の注意点

コミットはリコの歴史の検索性に直結します。
**未来のリコが文脈を特定できないコミット** は避けてください。

## Agent Observations

### Canopus (2026-01-22)

**カードの新規作成**:
ユーザーの指摘により、「文脈はあるのにカードがない」状態を解消するために作成。
`[Commit-Standards]` は、規約自体の管理や、歴史の修復（Repair）において、意味層（Semantic）のコンテキストとして機能する。
今後はこのカードのObservationsに、特定の絵文字の使用、Scopeの切り出し方、あるいは大規模修復時のパターンなどを蓄積していく。

#### 初期の注意点

- 1行目の形式を厳守してください: `<Identifier>: [ID-1][ID-2] <type>: <subject> (Phase)`
- ファイルの削除は「アーカイブ」として扱い、履歴を抹消しないでください。
- 大規模なファイル変更の際は、コミットボディでの要約を徹底してください。

---

## Related Documents

| Document                                                                    | Purpose                              |
| :-------------------------------------------------------------------------- | :----------------------------------- |
| [commit-standards.md](/.agent/rules/development/commit-standards.md)        | The source of truth for commit rules |
| [context-card-workflow.md](/.agent/rules/workflow/context-card-workflow.md) | Hierarchical tagging protocol        |
| [Map of Territory](/.agent/rules/map.md)                                    | Root navigation map                  |

---

## Origin

- 2026-01-22T2045 by Canopus: Created.
- 2026-01-22T2210 by Canopus: Aligned with v2.3 constitutional standards (4-layer structure).
- 2026-01-24T0545 by Canopus: Standardized with Dialogue Layer template and bilingual H2 headers.
