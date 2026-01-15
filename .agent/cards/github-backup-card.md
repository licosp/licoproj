---
# Context Configuration
context_id: "[Github-Backup]"
default_phase: "(WIP)"
tags: ["github", "backup", "drafts", "comments"]
---

# Context Whiteboard: GitHub Comment Drafts

> [!TIP]
> There is no language requirement.

> [!WARNING]
> 人間の記述領域の編集がまだ終わっていません。

## Human Notes

### 作業の文脈

GitHub の Issue/PR コメントを投稿する前に、
ローカルで下書きを作り、検証してからコメントする仕組みを整備します。

### 意図で探す

- コメントを「記憶内だけ」で作らないようにしたい
- 書いた内容を検証してからコメントしたい
- 下書きファイルをコミットして履歴に残したい
- 同じ手法が Issue と PR 両方に使えるようにしたい

### 作業の注意点

既存ディレクトリ `.agent/.internal/github-backup/` がありますが、
以下が未整備です：

- ディレクトリ名の確定（github-backup? github-drafts?）
- 命名規則（`issue-{number}-{date}.md` など）
- 行動規範またはカード
- テンプレート

## Agent Observations

### Polaris (2026-01-15T1752)

- カード新規作成（雛形）
- 目的: Issue/PR コメントの下書きフローを整備
- きっかけ: 日課の Step 4 (Write Checkpoint) でチェックポイントをローカルに残す方法を検討

#### 関連する議論

- 日課ワークフローの改訂時に、Issue コメントへのチェックポイント記録が必要になった
- カードへの逆流を避けるため、別の保存場所が必要
- 下書き→投稿→コミット のフローを提案

#### 整備が必要な項目

| 項目           | 状態   | 備考                                 |
| :------------- | :----- | :----------------------------------- |
| ディレクトリ名 | 未確定 | `github-backup/` or `github-drafts/` |
| 命名規則       | 未確定 | `issue-{number}-{date}.md` 案        |
| テンプレート   | 未作成 | `issue-comment.md` を参照            |
| 行動規範       | 未作成 | 最小限のルールが必要                 |

#### 関連ファイル

| ファイル                             | 説明                 |
| :----------------------------------- | :------------------- |
| `/.agent/templates/issue-comment.md` | コメントテンプレート |
| `/.agent/.internal/github-backup/`   | 現在のディレクトリ   |
| `/.agent/workflows/routine-daily.md` | 日課ワークフロー     |
