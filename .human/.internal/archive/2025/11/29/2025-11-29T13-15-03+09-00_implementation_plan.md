---
description: ワークスペース設定のリファクタリング計画
created: 2025-11-29T13:15:03+09:00
---

# 実装計画書：ワークスペース設定の分離とリファクタリング

## 目的

現在 `.vscode/.code-workspace` に混在している「個人設定（フォント・配色など）」と「プロジェクト共有設定（Linterパスなど）」を分離し、管理者が快適に作業できる環境と、チームで共有すべきクリーンな環境を両立させる。

## ユーザーレビュー事項

> [!IMPORTANT]
> **新しい個人設定ファイルの場所**: `.human/.internal/.vscode/leonidas.code-workspace`
> このパスで問題ないかご確認ください。

## 提案される変更

### 1. 個人設定ファイルの移動

**対象**: 現在の `.vscode/.code-workspace`
**アクション**: 以下の新しいパスへ移動（リネーム）します。

- **移動先**: `[NEW] .human/.internal/.vscode/leonidas.code-workspace`
- **内容**: 現在のすべての設定（`UDEV Gothic` フォントや `Dracula` テーマを含む）をそのまま保持します。

### 2. 共有設定ファイルの新規作成

**対象**: `.vscode/.code-workspace`（移動後の跡地）
**アクション**: 新規作成

- **内容**: プロジェクトの動作に必須な設定のみを厳選して記述します。
  - ✅ Linter/Formatter パス (ShellCheck, Prettier, Ruff)
  - ✅ Python 解析パス
  - ✅ テスト設定
  - ❌ フォント、テーマ、配色は**含めません**。

## 検証計画

### 手動検証

1.  **個人環境の確認**:
    - `leonidas.code-workspace` を VS Code で開き、フォントやテーマが維持されているか確認する。
2.  **共有環境の確認**:
    - ルートフォルダを直接開き（または新しい `.code-workspace` を開き）、Prettier や ShellCheck が正常に動作するか確認する。
    - フォントやテーマがデフォルト（またはユーザー設定）に戻っていることを確認する。
