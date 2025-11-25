---
description: 日付ベースのファイル名での新しいプロンプトドラフトを作成する
---

# Create Prompt Draft ワークフロー

## 目的
AI向け指示書を書くための新しいMarkdownドラフトファイルを`.agent/.draft/`に生成します。

## ステップ

1. **ディレクトリ作成** (ない場合)
   ```bash
   mkdir -p .agent/.draft
   ```

2. **ファイル生成**
   以下を実行して日付付きドラフトを作成します:
   ```bash
   cat > .agent/.draft/draft_$(date +%Y-%m-%d).md << 'EOF'
   ---
   date: $(date -Iseconds)
   user: $(whoami)
   ---

   ## Prompt
   [Enter your instructions for Ai here]


   EOF
   ```

## 出力
- **パス**: `.agent/.draft/draft_YYYY-MM-DD.md`
- **使い方**: `## Prompt` セクションを編集してエージェントに指示します。
