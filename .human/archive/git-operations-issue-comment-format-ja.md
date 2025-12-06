#### 4.4 Issueコメントフォーマット
**MUST** すべてのIssueコメントを英語でAI最適化フォーマットで記述する：

**理由**: GitHub Issueは、AIの時系列思考追跡のための参照資料として機能します。コメントは将来のセッションでAIエージェントが読めるものでなければなりません。

**言語**: 英語のみ
- AIエージェントは英語で考える（参照: `core/identity.md`）
- セッション間のコンテキストには一貫した言語が必要
- 人間向けドキュメントは `.human/` ディレクトリに配置すべき

**フォーマット要件**:
- 構造化のためにmarkdownを使用（ヘッダー、リスト、コードブロック）
- 関連する場合はISO 8601形式のタイムスタンプを含める
- ファイルは絶対パスまたはリポジトリルートからの相対パスで参照
- 「何を」変更したかだけでなく「なぜ」変更したかを説明

**例**:
```markdown
## Commit History (2025-11-29T19:27+09:00)

Completed 6 atomic commits following `commit-granularity.md` guidelines:

- `b2c3e89` docs(draft): update draft with conversation history
- `0c49074` chore(config): update .gitignore to track rule files

**Summary**: Added conversation logs and updated config files.
**Next Steps**: Add pre-push documentation rule.
```

**再投稿**: コメントに訂正が必要な場合、以下を含む新しいコメントを投稿：
- **Note**（なぜ再投稿するのかの説明）
- 修正された内容
- 元のコメントは削除しない（時系列を保持）
