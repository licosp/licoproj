---
# Context Configuration
context_id: "[Directory-Reorganize]"
default_phase: "(Plan)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-31T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["reorganization", "structure", "cleanup"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Default Directory Reorganization

> [!TIP]
> There is no language requirement.

> [!WARNING]
> 人間の記述領域の編集がまだ終わっていません。

## Human Notes

### 作業の文脈

Antigravityのデフォルトディレクトリ（`rules/`, `workflows/`, `scripts/`）の整理です。

現状の問題：

- `scripts/` は使い捨て哲学により実質未使用（`workspace/` が代替）
- `workflows/` と `rules/` のフロントマターが異なる
- 両方ともリコだけが読むものなのに、フォーマットが違う

### 意図で探す

- カード自体の使い方を思い出してほしい
- スクリプトの使い捨て哲学に関する行動規範がある
- `workflows/` の手順書と `rules/` の行動規範の違いを理解してほしい

### ユーザーの前提

**重要**: ユーザーはスラッシュコマンドを使いません。

スラッシュコマンドはリコが内部的に処理するもので、
ユーザー向けの特別な配慮は不要です。

### 統合案

```
.agent/
├── rules/
│   ├── core/           # 基本原則
│   ├── development/    # 開発標準
│   ├── workflow/       # 既存のワークフロールール
│   └── procedures/     # 手順書（旧 workflows/）
├── cards/              # コンテキストカード
└── .internal/
    └── workspace/      # 一時ファイル・スクリプト
```

### 作業内容

1. `scripts/` ディレクトリの廃止検討
2. `workflows/` の `rules/procedures/` への統合
3. 全手順書のフォントマターを行動規範と統一
4. ドキュメント標準の明文化

## Agent Observations

### Spica

- (Initial setup)

### Polaris

2025-12-31〜2026-01-01の対話で Polaris とユーザーが議論：

---

## Related Documents

| Document                                                                | Purpose                |
| :---------------------------------------------------------------------- | :--------------------- |
| [Map of Territory](/.agent/rules/map.md)                                | Navigation reference   |
| [repository-philosophy.md](/.agent/rules/core/repository-philosophy.md) | The "Brain" philosophy |

---

## Origin

- 2025-12-31 by Polaris: Initial discussion from seed.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
