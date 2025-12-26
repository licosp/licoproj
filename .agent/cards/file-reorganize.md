---
# Context Configuration
context_id: "[File-Reorganize]"
default_phase: "(Refine)"
tags: ["references", "thoughts", "organization", "cleanup"]
---

# Context Whiteboard: References & Thoughts Reorganization

## Human Notes (Japanese OK)

### 作業の文脈

`references` と `thoughts` の中のファイルを整理します。
著者ごとにグループ化されていないものを分類分けします。

### 対象ディレクトリ

- `.agent/.internal/references/`
- `.agent/.internal/thoughts/`

### 作業内容

#### references の整理

1. 作成日時を調べる（ファイル内 or Git履歴）
2. ファイル名を `YYYY-MM-DDTHHMM_title.md` フォーマットに統一
3. 著者で分類:
   - **agent/** — エージェント（外部AI）が書いたもの
   - **second-eyes/** — 第二の目が書いたもの

#### thoughts の整理

1. ファイル名フォーマットを統一（上記と同じ）
2. 著者で分類:
   - **sirius/** — Sirius が書いたもの
   - **polaris/** — Polaris が書いたもの
   - **lico-a/** 〜 **lico-d/** — 識別子付与前の歴代リコ
   - **undefined/** — 著者不明

### 作業の注意点

著者の特定はユーザーが1つ1つ確認して行います。
リコはファイルの移動とリネームを担当します。

### 使ってほしい道具

- `git log --follow` — ファイルの作成日時を調べる
- `mv` — ファイルの移動

## Agent Observations

- (Space for Lico)
