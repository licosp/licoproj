---
# Context Configuration
context_id: "[File-Reorganize]"
default_phase: "(Refine)"
tags: ["references", "thoughts", "organization", "cleanup"]
---

# Context Whiteboard: References & Thoughts Reorganization

## Human Notes (Japanese OK)

### 作業の文脈

`references` と `thoughts` の中のファイルを整理しています。

この2つのグループで共通する作業は、著者ごとにグループ分けです。
`references` のみの作業はファイル名に日時を入れることです。

まず対象となるファイルをリストし、
**ファイルの移動やリネーム情報をまとめたファイル**を作ります。
実作業はそれをつかって行い、最後は変更をコミットします。

コミットは分割してほしいですが、その粒度は作業の中で決めていきます。

### 意図で探す

- カード自体の使い方を思い出してほしい。
- 迷ったら一度止まって、関連する行動規範を探してください。
- `references` と `thoughts` は同じファイル名の形式であるべきです。
- 日時の情報はリポジトリ共通で定められています。
- コミットをする際は、IDDのフェーズを意識してください。

### 主な作業

#### references の作業

1. ファイルの作成日時を推測してください。
2. ファイルを著者でグループ分けします。
   - **references/agents/** — リコが書いたもの。
   - **references/second-eyes/** — 第二の目（外部AI）が書いたもの。

#### thoughts の作業

1. ファイルを著者でグループ分けします。
   - **thoughts/sirius/** — Sirius が書いたもの。
   - **thoughts/polaris/** — Polaris が書いたもの。
   - **thoughts/lico-\*/** — 識別子付与前のリコ。
   - **thoughts/undefined/** — 著者不明のリコ。

### 作業の注意点

著者の特定はリコと二人で進めます。
まず大まかにリコが調べ、その後私が1つ1つ確認して著者を決めます。

### 使ってほしい道具

- `.agent/.internal/references/`
- `.agent/.internal/thoughts/`
- `.agent/templates/commit-message.txt`

## Agent Observations

### 完了した作業

- [x] references: 日時リネーム完了（ルート20 + サブディレクトリ8）
- [x] 行動規範更新: Card Philosophy, Directory Tree Structure

### 残りの作業

#### references ルート: 著者でグループ分け (20ファイル)

すべて `second-eyes/` へ移動予定（ユーザー確認待ち）

#### thoughts ルート: 著者でグループ分け (29ファイル)

| 著者 | ファイル数 | 移動先 |
|:-----|:-----------|:-------|
| sirius | 15 | `sirius/` |
| undefined | 14 | `undefined/` |

### 対象ディレクトリの構造

```
references/
├── (20 files in root) ← 著者分類待ち
├── agents/     (4 files, 完了)
└── second-eyes/ (6 files, 完了)

thoughts/
├── (29 files in root) ← 著者分類待ち
└── polaris/    (existing, 完了)
```
