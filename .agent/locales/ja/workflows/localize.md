---
description: 英語と日本語間でファイルを翻訳する
---

# Localize ワークフロー

## 目的
`.agent/rules/core/localization.md`で定義された標準に従って、ドキュメントファイル（`.md`）を英語と日本語間で翻訳します。

## 準備

必要なすべてのディレクトリが存在することを確認します:
```bash
mkdir -p .agent/{rules,workflows} .agent/locales/ja/{rules,workflows}
```

## 翻訳方向

### 英語から日本語へ (EN → JA)

**ソース**: `.agent/rules/**/*.md` と `.agent/workflows/*.md`  
**宛先**: `.agent/locales/ja/` (ディレクトリ構造を保持)

---

### 日本語から英語へ (JA → EN)

**ソース**: `.agent/locales/ja/`  
**宛先**: `.agent/rules/**/*.md` と `.agent/workflows/*.md`

## 検証

翻訳後、以下を確認します:
- 翻訳が元の意味と意図を保持していること
- Markdownフォーマットがそのまま保持されていること
- 関連ドキュメント全体で用語が一貫していること

## ガイドライン
詳細な翻訳標準については`.agent/rules/core/localization.md`を参照してください。
