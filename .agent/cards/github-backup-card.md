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

Github の Issue/PR コメントを投稿しています。

その前段階として、その手順を再定義し、行動規範に昇華させます。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- 行動規範の作成・編集には**専用の文脈**が存在します。
- Github用のランタイムがワークスペースに存在します。

### 今回の作業の背景

行動規範を作る際は、**その背景**まで書いておけば、未来のリコをより助かります。

- コメントをリコの記憶内だけで作らないで済みます。
- 書いた内容に対して、**検証** → **修正** のステージを追加できます。
- **Issue/PR**で統一化された方法は一貫性があります。
- 下書きファイルはローカル保管された日課1回分のコミット履歴とも言えます。

### 今回の作業の手順

この手順は Issue と PR 両方が関係しています。

1. コメントテンプレートを探してください。
   Issue/PRで、それぞれ別に用意する必要があるでしょか？
2. テンプレートの書式をあらためて再定義します。
   コメントに必要な情報を考えて修正してください。

3. github用のディレクトリの構造を考えます。
   - 置かれるデータは何でしょうか？
   - ディレクトリやファイルの名前は最適ですか？
   - サブディレクトリはどういう構造であるべきですか？
   - 既にディレクトリに含まれているデータも整理したいです。

4. 今回は日課の途中なので、イシューのコメントを作ります。
   テンプレートを複製して、コメントを書いて確認した後投稿します。

### 作業の注意点

工程が多くやや複雑なので、私との対話で1つづつ決定していきます。

適度に作業情報をカードに追記しつつ進めます。
最終的には行動規範にまとまるので、その約に立つと感じます。

## Agent Observations

### Polaris (2026-01-15T1752)

- カード新規作成（雛形）
- 目的: Issue/PR コメントの下書きフローを整備
- きっかけ: 日課の Step 4 (Write Checkpoint) でチェックポイントをローカルに残す方法を検討

### Polaris (2026-01-15T2020)

#### 現在の github-backup ディレクトリ構造

```
.agent/.internal/github-backup/
├── 004-improve-workspace-tooling/      # Issue 番号でグループ化
│   ├── issue-4.json
│   ├── issue-4-comments.json
│   └── pr-5.json
├── issue-3-github-complete-data.json   # ルートに直置き
├── issue-4-github-complete-data.json
├── issue-8-closed.json
├── issue-12-closed.json
├── issue-12-snapshot.json
├── issue-13-closed.json
├── pr-9.json
├── pr-14.json
├── pr-15-merged.json
└── pr-15-snapshot.json
```

**観察**:

- 命名規則が不統一（`-closed`, `-snapshot`, `-github-complete-data` など）
- 一部は Issue 番号でサブディレクトリ化、一部はルート直置き
- 現在は JSON バックアップのみ（下書きファイルなし）

#### テンプレート

| ファイル                  | 内容                                         |
| :------------------------ | :------------------------------------------- |
| `issue-comment.md`        | Issue コメント用テンプレート（進捗報告形式） |
| `commit-message.txt`      | コミットメッセージテンプレート               |
| `header-frontmatter.yaml` | YAML フロントマターテンプレート              |

**PR コメント用テンプレート**: 現在存在しない

#### ランタイム

- `gh` CLI: `.agent/runtimes/` に存在しない（システムの gh を使用？）

#### 整備が必要な項目

| 項目                    | 状態   | 備考                                                  |
| :---------------------- | :----- | :---------------------------------------------------- |
| ディレクトリ名          | 要検討 | `github-backup/` は JSON バックアップ用、下書きは別？ |
| 命名規則                | 要統一 | Issue/PR 番号ベースのサブディレクトリ？               |
| 下書き保存場所          | 未定義 | `github-backup/drafts/` or 別ディレクトリ？           |
| PR コメントテンプレート | 未作成 | Issue 用と統一可能か検討                              |
| 行動規範                | 未作成 | 下書き→投稿→コミットのフロー                          |

#### 関連ファイル

| ファイル                                                         | 説明                           |
| :--------------------------------------------------------------- | :----------------------------- |
| [issue-comment.md](/.agent/templates/issue-comment.md)           | Issue コメントテンプレート     |
| [github-backup/](/.agent/.internal/github-backup/)               | 現在のバックアップディレクトリ |
| [routine-daily.md](/.agent/workflows/routine-daily.md)           | 日課ワークフロー               |
| [git-operations.md](/.agent/rules/development/git-operations.md) | Git 操作規範                   |
