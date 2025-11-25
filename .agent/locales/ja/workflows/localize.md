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

- `.agent/rules/**/*.md` → `.agent/locales/ja/rules/**/*.md`
- `.agent/workflows/**/*.md` → `.agent/locales/ja/workflows/**/*.md`

### 日本語から英語へ (JA → EN)

- `.agent/locales/ja/rules/**/*.md` → `.agent/rules/**/*.md`
- `.agent/locales/ja/workflows/**/*.md` → `.agent/workflows/**/*.md`

## ファイル選択

重複した翻訳作業を避けるため、更新されたファイルのみを翻訳します:

**翻訳が必要か判定**:
- ソースファイルと宛先ファイルの最終更新日時を比較
- 以下の場合に翻訳を実行:
  - ソースファイルが宛先ファイルより新しい、または
  - 宛先ファイルが存在しない

**例**:
```bash
# EN → JA の場合
if [[ ! -f ".agent/locales/ja/workflows/commit.md" ]] || 
   [[ ".agent/workflows/commit.md" -nt ".agent/locales/ja/workflows/commit.md" ]]; then
  # 翻訳が必要
fi
```

## 検証

翻訳後、以下を確認します:
- 翻訳が元の意味と意図を保持していること
- Markdownフォーマットがそのまま保持されていること
- 関連ドキュメント全体で用語が一貫していること

## ガイドライン
詳細な翻訳標準については`.agent/rules/core/localization.md`を参照してください。
