---
# Context Configuration
context_id: "[Datetime-Standardize]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["datetime", "standardization", "naming", "consistency"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Datetime Format Standardization

> [!TIP]
> There is no language requirement.

---

> [!WARNING]
> The human notes has not yet been edited.

## Human Notes

### 作業の文脈

リポジトリ内の日時表記を統一しています。
`ISO 8601` を基本としますが、用途によって精度が異なります。

### 意図で探す

- 日時の行動規範を思い出してください。
- ファイル名やディレクトリ名の命名規則があります。
- フロントマターの標準があります。

### 現状の課題

1. **精度の不統一**: 秒あり/なし、タイムゾーンあり/なし
2. **区切り文字の混在**: `-` と `_` の使い分け
3. **ファイル名での `:` の問題**: OS によって使えない

### 提案されたカテゴリ

| カテゴリ      | パターン                    | 用途                         |
| :------------ | :-------------------------- | :--------------------------- |
| **Full**      | `YYYY-MM-DDTHH:MM:SS+09:00` | Frontmatter（正確さ重視）    |
| **Compact**   | `YYYY-MM-DDTHHMM`           | ファイル名、Origin           |
| **Date-only** | `YYYY-MM-DD`                | archive ディレクトリ、drafts |

### 作業予定

- [ ] 行動規範 `datetime-format.md` の更新
- [ ] 既存ファイルの名前統一
- [ ] `-` と `_` の使い分けルール策定

---

## Related Documents

| Document                                                                                  | Purpose                                        |
| :---------------------------------------------------------------------------------------- | :--------------------------------------------- |
| [datetime-format.md](/.agent/rules/core/documentation/datetime-format.md)                 | SSOT for date and time formatting standards    |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | Structural standards for project documentation |

---

## Origin

- 2025-12-01T0000: Created as datetime standardization context.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
