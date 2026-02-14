---
# Context Configuration
context_id: "[Directory-Reorganize]"
default_phase: "(Plan)"
tags: ["reorganization", "structure", "cleanup"]
---

# Context Whiteboard: Default Directory Reorganization

## Human Notes (Japanese OK)

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

### 識別子

(未割り当て)

### 経緯

2025-12-31〜2026-01-01の対話で Polaris とユーザーが議論：
- 手順書と行動規範のフォーマット差異
- ユーザーがスラッシュコマンドを使わない事実
- デフォルトディレクトリの存在理由

### 次のステップ

- [ ] 詳細な移行計画を作成
- [ ] 既存の手順書のフロントマターを更新
- [ ] ディレクトリ構造を変更
- [ ] READMEを更新
