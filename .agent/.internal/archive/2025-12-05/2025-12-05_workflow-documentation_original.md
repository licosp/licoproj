---
ai_visible: true
version: 1.0
created: 2025-12-05T19:30:00+09:00
updated: 2025-12-05T19:30:00+09:00
language: ja
purpose: Document the new work directory workflow
---

# Work Directory Workflow ドキュメント

## 概要
`.agent/.internal/work/`ディレクトリを中間作業スペースとして使用し、全てのファイル作成・更新作業を安全に行うワークフロー。

## ワークフロー

### 1. 中間ファイル作成フェーズ
**場所**: `.agent/.internal/work/`
**命名規則**: `{target-filename}-{timestamp}-{purpose}.md`
**例**: `hallucination-awareness-20251205-verification-protocol.md`

### 2. 作業プロセス
```
アイデア生成 → 中間ファイル作成 → 内容洗練 → レビュー準備
```

### 3. 適用フェーズ
**タイミング**: 中間ファイルの完成後、ユーザーの承認を得てから
**プロセス**: 中間ファイルの内容を本番ファイルに適用

## 利点

### 安全性
- 本番ファイルを直接変更しない
- 作業中の破損リスクを回避
- いつでも中断・再開可能

### 透明性
- 作業過程が全て記録される
- 変更履歴が追跡可能
- ユーザーが内容を確認できる

### 品質保証
- 中間ファイルでの複数回の修正が可能
- レビューを経てから本番適用
- 問題発生時のロールバックが容易

## 実装例

### 既存の例
- `hallucination-awareness copy.md` - ルール退避用

### 新規作業の例
```
作業: Content Verification Protocolの拡張
1. 中間ファイル作成: content-verification-extension-20251205.md
2. 内容開発と洗練
3. ユーザー確認
4. 本番適用: hallucination-awareness.mdに統合
```

## 運用ルール

### ファイル管理
- **成功時の削除**: 本番ファイルの上書きが成功した場合、中間ファイルを削除
- **失敗時の保持**: 上書きに失敗した場合、中間ファイルを`.agent/.internal/archive/work/`に移動
- タイムスタンプを必ず含める（ISO 8601形式: YYYYMMDDTHHMMSS+TZ）
- 目的をファイル名に明記

### 承認プロセス
- 重要な変更はユーザーの明示的な承認を得る
- テストが必要な変更は検証を経る
- 緊急変更は例外的に直接適用可能

### クリーンアップ
- 完了した作業は定期的にアーカイブ
- 不要な中間ファイルは削除
- 作業履歴は保持

このワークフローで、より安全で透明性の高い開発プロセスを実現します。


