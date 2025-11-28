---
description: Issue-Driven Developmentに基づくコミット前準備手順
---

# 📋 コミット事前準備ワークフロー

このワークフローは、以下の**4つの関係性**を確実に確立することを目的とします：

```
Issue ↔ Branch (Remote) ↔ Branch (Local) ↔ HEAD (Local)
```

---

## ⚙️ 前提条件

> **必須要件**
> 
> - GitHub CLIが認証済みであること (`gh auth status`)
> - Gitリポジトリ内にいること
> - ローカルに未コミットの変更が存在すること

---

## 📝 手順

### 1. 環境チェック

```bash
# GitHub CLI認証状態の確認
gh auth status

# リポジトリコンテキストの確認
git rev-parse --is-inside-work-tree
```

**✅ 期待される結果**:
- `gh auth status`: `✓ Logged in to github.com` が表示される
- `git rev-parse`: `true` が返される

---

### 2. 変更内容の調査

```bash
# 変更状況の確認
git status

# 変更の概要確認
git diff --stat
```

**✅ 期待される結果**:
- `git status`: 変更または未追跡ファイルが存在する
- ⚠️ 変更が存在しない場合は処理を中止

---

### 3. GitHub Issueの作成

**🔗 確立する関係**: `Issue` の作成

```bash
# Issueを作成
gh issue create --title "[Type]: [Short Description]" --body "[Detailed description]"
```

**パラメータ**:
- `--title`: `[Type]: [Description]` 形式（例: `refactor: Consolidate Git Rules`）
- `--body`: 変更内容の詳細説明
- **Type**: `feat`, `fix`, `docs`, `refactor`, `chore` など（Conventional Commits準拠）

**確認コマンド**:
```bash
# 作成されたIssueの確認
gh issue view <issue-number>
```

**✅ 期待される結果**:
- GitHub上にIssue #N が作成される
- Issue番号を控える（例: `#3`）

---

### 4. Issue関連ブランチの作成とチェックアウト

**🔗 確立する関係**: `Issue ↔ Branch (Remote) ↔ Branch (Local) ↔ HEAD`

```bash
# gh issue developコマンドでブランチを作成しチェックアウト
gh issue develop <issue-number> --name <issue-number>-<issue-title-kebab-case> --checkout
```

**パラメータ例**:
```bash
gh issue develop 3 --name 3-refactor-agent-rules-and-git-operations --checkout
```

> **⚠️ 重要な注意事項**
> 
> - **必ず `gh issue develop` を使用してください**
> - `git checkout -b` + `git push -u origin` では **Issue ↔ Branch (Remote) の関連付けが行われません**
> - ブランチ名形式: `<issue-number>-<title-in-kebab-case>`

**✅ 期待される結果**:
```
github.com/<owner>/<repo>/tree/<branch-name>
From https://github.com/<owner>/<repo>
 * [new branch]      <branch-name> -> origin/<branch-name>
```

---

### 5. 関係性の検証

#### 5.1 Branch (Local) ↔ HEADの確認

```bash
git branch
```

**✅ 期待される結果**:
```
* 3-refactor-agent-rules-and-git-operations
  main
```

💡 `*` がついているブランチが現在のHEADです。

---

#### 5.2 Branch (Remote) ↔ Branch (Local)の確認

```bash
git branch -vv
```

**✅ 期待される結果**:
```
* 3-refactor-agent-rules-and-git-operations a1b2c3d [origin/3-refactor-agent-rules-and-git-operations] Commit message
```

💡 `[origin/...]` が表示されていれば、リモート追跡（upstream）が設定されています。

---

#### 5.3 Issue ↔ Branch (Remote)の確認

##### 📱 方法1: GitHub CLI

```bash
gh issue view <issue-number> --web
```

ブラウザでIssueページを開き、**「Development」セクション**にブランチ名が表示されることを確認します。

##### 🔧 方法2: GitHub API（CLI経由）

```bash
gh api repos/:owner/:repo/issues/<issue-number>/timeline | jq '.[] | select(.event=="connected") | .source.issue.pull_request.html_url // .source'
```

> **💡 ヒント**
> 
> Issue-Branch関連付けは、GitHub UI上の「Development」セクションで視覚的に確認するのが最も確実です。

---

### 6. 変更の分析と文書化

**🎯 目的**: Issueコメントと今後のコミット参考用に、すべてのリポジトリ変更の包括的なサマリーを作成します。

#### 6.1 すべての変更の調査

```bash
# 短縮ステータスの表示
git status --short

# 詳細な統計情報の表示
git diff --stat
```

---

#### 6.2 カテゴリ化と文書化

`.agent/.internal/issue-<N>-changes-summary.md` に変更サマリーファイルを作成します。

**📋 必須構成**:

1. **概要**: 変更されたファイルの総数、追加/削除された行数
2. **コンポーネント別の変更**: ファイルを論理的なコンポーネント（例: rules, workflows, config）でグループ化
3. **属性の割り当て**: 各グループに **Added/Modified/Deleted** のタグを付与
4. **主要な変更**: 重要な変更と理由を強調

**📝 テンプレート**:
```markdown
# Repository Changes Summary

## Overview
- **Total Files**: X changed
- **Lines Added**: +Y
- **Lines Deleted**: -Z

## Changes by Component

### 1. Component Name

#### Added
- file1.md - Description

#### Modified
- file2.md - Description

#### Deleted
- file3.md - Rationale

## Summary by Attribute
| Attribute | Count | Description |
|-----------|-------|-------------|
| Added     | X     | ...         |
| Modified  | Y     | ...         |
| Deleted   | Z     | ...         |

## Key Changes
1. Major change description
```

---

#### 6.3 サマリーをIssueに投稿

```bash
# サマリーをコメントとして投稿
gh issue comment <issue-number> --body-file .agent/.internal/issue-<N>-changes-summary.md
```

**📌 目的**: 
- GitHub上で作業範囲を文書化
- コミット計画の参考資料を提供
- 変更の監査証跡を作成

---

## ✅ 完了条件チェックリスト

以下が**全て満たされている**ことを確認してください：

- [ ] **Issue**: GitHub Issue #N が作成されている（`gh issue view N`）
- [ ] **Issue ↔ Branch (Remote)**: GitHub UIの「Development」セクションにブランチ名が表示される
- [ ] **Branch (Remote)**: `origin/N-issue-title` が存在する（`git branch -r | grep N-issue-title`）
- [ ] **Branch (Remote) ↔ Branch (Local)**: 追跡設定が確立されている（`git branch -vv` で `[origin/...]` 表示）
- [ ] **Branch (Local) ↔ HEAD**: 目的のブランチがチェックアウトされている（`git branch` で `*` 表示）
- [ ] **Changes Documented**: サマリーファイルが作成され、Issueに投稿されている（`gh issue view N` でコメント表示）

---

## 🔧 トラブルシューティング

### ❌ 問題: Issue ↔ Branch (Remote)の関連付けが確認できない

**原因**: `git checkout -b` + `git push -u` を使用した

**✅ 解決策**:

1. ブランチを削除してやり直す
   ```bash
   git checkout main
   git branch -D <branch-name>
   git push origin --delete <branch-name>
   ```

2. `gh issue develop` で再作成
   ```bash
   gh issue develop <issue-number> --name <branch-name> --checkout
   ```

---

### ❌ 問題: 作業中の変更が消えた

**原因**: ブランチ切り替え時にstashされた

**✅ 解決策**:
```bash
git stash list
git stash pop
```

---

## 🚀 次のステップ

この準備が完了したら、**コミットワークフロー**を実行します。
