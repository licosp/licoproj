---
title: Issue-Driven Development Automation - Implementation Plan
date: 2025-11-26
language: ja
---

# イシュー駆動開発の自動化 - 実装計画書

## 概要

GitHub Issue と Git ブランチを連携させた自動化ワークフローの実装計画。以下の 5 ステップを 1 つのコマンドで実行：

1. GitHub に新規 Issue 「ai driven issue flow 1st」を作成
2. Issue と関連付けたブランチを自動生成
3. ローカルリポジトリでリモートの変更を fetch
4. Issue 関連ブランチにチェックアウト
5. 全ての処理を 1 コマンドで実行

---

## 1. システムアーキテクチャ

```
┌─────────────────────────────────────────────┐
│     issue-flow コマンド実行                  │
│  (単一エントリーポイント)                   │
└────────────────┬────────────────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
    ┌───▼────────┐  ┌────▼──────────┐
    │   GitHub   │  │  Local Git    │
    │    CLI     │  │  Repository   │
    └───┬────────┘  └────┬──────────┘
        │                │
    ┌───▼────┬───────────▼───┐
    │  Step 1 │               │ Step 3
    │Create   │               │ Fetch
    │ Issue   │               │
    ├────────────────────────┤
    │  Step 2   │ Step 4     │
    │  Create   │ Checkout  │
    │  Branch   │ Branch    │
    └──────────────────────┘
```

---

## 2. ワークフロー詳細

### フェーズ 1: Issue 作成

**入力**: Issue タイトル、説明（オプション）  
**処理**:
```bash
gh issue create --title "ai driven issue flow 1st" \
                --body "Automated workflow for issue-driven development"
```
**出力**: Issue 番号 (例: #42)

### フェーズ 2: ブランチ名生成

**入力**: Issue 番号, Issue タイトル  
**処理**: `issue-{number}-{slug}` 形式のブランチ名生成
```
例: issue-42-ai-driven-issue-flow-1st
```

### フェーズ 3: リモート同期

**処理**:
```bash
git fetch origin  # リモートの最新情報を取得
```

### フェーズ 4: ブランチ作成＆チェックアウト

**処理**:
```bash
git checkout -b issue-42-ai-driven-issue-flow-1st
git push -u origin issue-42-ai-driven-issue-flow-1st
```

---

## 3. 実装成果物

### 3.1 ワークフロー定義

**ファイル**: `.agent/workflows/issue-driven-development.md`

内容:
- ワークフロー目的
- 前提条件（GitHub CLI, Git）
- 詳細ステップ
- コマンド例
- バリデーション手順

### 3.2 実装スクリプト

**ファイル**: `.agent/scripts/issue-flow`

特徴:
- シェルスクリプト（Bash）
- エラーハンドリング
- 色付き出力で進捗表示
- jq 依存性の自動フォールバック
- 詳細なサマリー表示

---

## 4. 使用方法

### インストール

```bash
# スクリプトを実行可能に
chmod +x .agent/scripts/issue-flow

# パスに追加（オプション）
# ~/.bashrc または ~/.zshrc に以下を追記:
# export PATH="$HOME/develop/shared/project/licoproj/.agent/scripts:$PATH"
```

### 実行方法

**方法 1: 対話型**
```bash
./issue-flow
# Issue Title: を入力
```

**方法 2: 引数指定**
```bash
./issue-flow "ai driven issue flow 1st"
```

**方法 3: タイトルと説明を指定**
```bash
./issue-flow "Add user authentication" "Implement OAuth2 login"
```

### 実行結果例

```
ℹ️  Creating GitHub issue: 'ai driven issue flow 1st'
✅ Issue created: #42
URL: https://github.com/user/repo/issues/42
ℹ️  Fetching remote changes...
✅ Remote fetch completed
ℹ️  Creating and checking out branch: issue-42-ai-driven-issue-flow-1st
✅ Branch checked out: issue-42-ai-driven-issue-flow-1st
ℹ️  Pushing branch to remote...
✅ Branch pushed to remote

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
✨ Issue-Driven Development Setup Complete!
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

Issue Details:
  Issue #42: ai driven issue flow 1st
  URL: https://github.com/user/repo/issues/42

Branch Details:
  Branch: issue-42-ai-driven-issue-flow-1st
  Status: Checked out locally

Next Steps:
  1. Make your changes
  2. Run: git add <files>
  3. Run: git commit -m 'Feat: <your message>'
  4. Run: git push
```

---

## 5. 前提条件と依存性

### 必須

| 要件 | バージョン | インストール |
|------|-----------|------------|
| Git | 2.0+ | `apt-get install git` (Linux) / `brew install git` (Mac) |
| GitHub CLI | 1.0+ | https://cli.github.com |

### オプション

| ツール | 用途 | 代替手段 |
|--------|------|---------|
| jq | JSON パース | 自動フォールバック（テキスト解析） |

### GitHub CLI 認証

```bash
gh auth login
# ブラウザで GitHub にログイン
# デバイスコード認証を完了
```

---

## 6. 統合とカスタマイズ

### 6.1 Git エイリアス

`.git/config` または `~/.gitconfig` に追加：

```ini
[alias]
    issue = "!~/.local/bin/issue-flow"
```

使用方法:
```bash
git issue "New feature title"
```

### 6.2 環境変数カスタマイズ

```bash
# デフォルト Issue テンプレートを設定
export ISSUE_BODY_TEMPLATE="Template text"

# Issue ラベルを自動付与（オプション拡張）
export DEFAULT_ISSUE_LABELS="enhancement,todo"
```

### 6.3 GitHub Actions 統合

PR 自動作成（オプション）:

```yaml
# .github/workflows/auto-pr.yml
name: Auto PR
on: push
jobs:
  create-pr:
    runs-on: ubuntu-latest
    if: startsWith(github.ref, 'refs/heads/issue-')
    steps:
      - uses: actions/github-script@v6
        with:
          script: |
            github.rest.pulls.create({
              owner: context.repo.owner,
              repo: context.repo.repo,
              title: context.payload.ref.replace('refs/heads/issue-', ''),
              head: context.payload.ref,
              base: 'main'
            })
```

---

## 7. エラーハンドリング

### 予想されるエラーと対応

| エラー | 原因 | 対応 |
|--------|------|------|
| `gh: command not found` | GitHub CLI がインストールされていない | `brew install gh` |
| `Not a git repository` | Git リポジトリ外で実行 | `cd` でリポジトリに移動 |
| `Failed to create issue` | GitHub 認証が失敗 | `gh auth login` を再実行 |
| `Permission denied` | リポジトリへの書き込み権限がない | リポジトリへのアクセス権を確認 |

---

## 8. セキュリティ考慮事項

- **認証**: `gh auth login` は安全にトークンを管理
- **プライバシー**: Issue 内容は他のチームメンバーに表示される
- **CI/CD 連携**: `GH_TOKEN` 環境変数を使用して自動化

---

## 9. テストと検証

### テストシナリオ

1. **基本テスト**
   ```bash
   ./issue-flow "Test Issue"
   ```
   期待結果: Issue 作成 → ブランチ作成 → チェックアウト完了

2. **既存ブランチテスト**
   - 同じコマンドを 2 回実行
   - 既存ブランチへの切り替えが正常に動作

3. **エラーハンドリングテスト**
   - `gh` がない状態で実行 → エラーメッセージ表示
   - リポジトリ外で実行 → エラー表示

---

## 10. 今後の拡張案

### Phase 2 の候補機能

1. **Issue テンプレート**: 複数テンプレートから選択
2. **ラベル自動付与**: `--labels` オプション追加
3. **Assignee 自動設定**: `--assignee` オプション
4. **PR 自動作成**: ブランチから PR へ自動遷移
5. **Conventional Commits**: コミットメッセージ自動生成
6. **ブランチ削除ワークフロー**: Issue クローズ時にブランチ削除

### Phase 3 の候補機能

1. **マルチスレッド操作**: 複数 Issue の並列処理
2. **マイルストーン管理**: Issue をマイルストーンに自動割り当て
3. **プロジェクトボード連携**: GitHub Projects への自動登録
4. **スプリント管理**: 反復的な開発サイクルの自動化

---

## 11. ドキュメント参照

- **ワークフロー詳細**: `.agent/workflows/issue-driven-development.md`
- **スクリプト実装**: `.agent/scripts/issue-flow`
- **コミットワークフロー**: `.agent/workflows/commit.md`

---

## 12. まとめ

### 達成目標

✅ Single command で 5 ステップを自動化  
✅ Error handling と詳細なフィードバック  
✅ GitHub CLI と Git の統合  
✅ 拡張可能な設計  

### 実装状況

- [x] ワークフロー定義
- [x] 実装スクリプト
- [x] エラーハンドリング
- [x] ドキュメント
- [ ] CI/CD 統合（Phase 2）
- [ ] テストスイート（Phase 2）

