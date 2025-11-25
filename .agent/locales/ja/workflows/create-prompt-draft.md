---
description: 日付ベースのファイル名で新しいプロンプトドラフトを作成する
---

# プロンプトドラフト作成ワークフロー

## 目的
AIへの指示を書くための新しいMarkdownドラフトファイルを `.agent/.draft/` に生成します。

## 手順

1. **ディレクトリ作成**（存在しない場合）
   ```bash
   mkdir -p .agent/.draft
   ```

2. **ファイル生成**
   以下を実行して日付ベースのドラフトを作成します：
   ```bash
   cat > .agent/.draft/draft_$(date +%Y-%m-%d).md << 'EOF'
   ---
   date: $(date -Iseconds)
   user: $(whoami)
   ---

   ## Prompt
   [ここにAiへの指示を入力してください]


   EOF
   ```

## 出力
- **パス**: `.agent/.draft/draft_YYYY-MM-DD.md`
- **使用法**: `## Prompt` セクションを編集してエージェントに指示します。
