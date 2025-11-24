---
description: 新しいプロンプトドラフトを作成
---

# プロンプトドラフト作成

このワークフローは、タイムスタンプベースの命名規則で `.agent/.draft/` に新しいプロンプトドラフトファイルを作成します。

## ステップ

1. `.agent/.draft/` ディレクトリが存在しない場合は作成:

```bash
mkdir -p .agent/.draft
```

// turbo 2. 現在のタイムスタンプで新しいドラフトファイルを作成:

```bash
cat > .agent/.draft/draft_$(date -Iseconds).md << EOF
---
date: $(date -Iseconds)
user: $(whoami)
---

## Prompt

[Ai への指示をここに記述]

## Additional Notes

[背景情報、期待される結果、コンテキストなど]
EOF
```

3. ドラフトファイルは以下の場所に作成されます: `.agent/.draft/draft_YYYY-MM-DDTHH:MM:SS+HH:MM.md`

## ファイル命名規則

- フォーマット: `draft_YYYY-MM-DDTHH:MM:SS+HH:MM.md` (ISO 8601)
- 例: `draft_2025-11-24T17:37:42+09:00.md`
