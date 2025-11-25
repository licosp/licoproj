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

#### ステップ
1. **翻訳と保存**
   - **Rules**: `.agent/rules/**/*.md` → `.agent/locales/ja/rules/**/*.md`
   - **Workflows**: `.agent/workflows/*.md` → `.agent/locales/ja/workflows/*.md`

2. **検証とコミット**
   - 翻訳の正確性とMarkdownフォーマットを確認します
   - 変更をコミットしてプッシュします

---

### 日本語から英語へ (JA → EN)

**ソース**: `.agent/locales/ja/`  
**宛先**: `.agent/rules/**/*.md` と `.agent/workflows/*.md`

> [!WARNING]
> これは既存の英語ファイルを上書きします。実行前に変更をコミットしてください。

#### ステップ
1. **翻訳と上書き**
   - **Rules**: `.agent/locales/ja/rules/**/*.md` → `.agent/rules/**/*.md`
   - **Workflows**: `.agent/locales/ja/workflows/*.md` → `.agent/workflows/*.md`

2. **検証とコミット**
   - 正確な翻訳と正しいフォーマットを確認します
   - 変更をコミットしてプッシュします

## ガイドライン
詳細な翻訳標準については`.agent/rules/core/localization.md`を参照してください。
