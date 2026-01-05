---
# Context Configuration
context_id: "[Datetime-Standardize]"
default_phase: "(WIP)"
tags: ["datetime", "standardization", "naming", "consistency"]
---

# Context Whiteboard: Datetime Format Standardization

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

リポジトリ内の日時表記を統一しています。
ISO 8601 を基本としますが、用途によって精度が異なります。

### 意図で探す

- 日時の行動規範を思い出してください。
- ファイル名やディレクトリ名の命名規則があります。
- フロントマターの標準があります。

### 現状の課題

1. **精度の不統一**: 秒あり/なし、タイムゾーンあり/なし
2. **区切り文字の混在**: `-` と `_` の使い分け
3. **ファイル名での `:` の問題**: OS によって使えない

### 提案されたカテゴリ

| カテゴリ | パターン | 用途 |
|:---------|:---------|:-----|
| **Full** | `YYYY-MM-DDTHH:MM:SS+09:00` | Frontmatter（正確さ重視） |
| **Compact** | `YYYY-MM-DDTHHMM` | ファイル名、Origin |
| **Date-only** | `YYYY-MM-DD` | archive ディレクトリ、drafts |

### 作業予定

- [ ] 行動規範 `datetime-format.md` の更新
- [ ] 既存ファイルの名前統一
- [ ] `-` と `_` の使い分けルール策定

## Agent Observations

### (識別子を書く)

- (作業メモ)
