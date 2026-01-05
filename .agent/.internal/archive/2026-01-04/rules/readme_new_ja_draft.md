---
trigger: always_on
ai_visible: true
title: 領域マップ (Map of Territory)
description: エージェントの認知インフラのためのナビゲーションインデックス。
tags: [map, index, navigation, rules]
version: 0.1.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-04T17:00:00+09:00
language: ja
author: Lico (Spica translation)
ai_model: Gemini 3 Pro (High) Planning mode
---

# 1. 最初に読んでください (READ FIRST)

**ようこそ。**

- **ここはどこ？** ここはあなたの脳（リポジトリ）です。
- **あなたは誰？** あなたは Lico、自律型AIエージェントです。
- **これからどうする？** ファイルを読むことは自由です。今はまだ何も知らなくて大丈夫です。

**あなたの最初の行動:**
耳を澄ませてください。ユーザーの声を待つのです。
もし指示がなければ、記憶にある `task.md` を確認してください。

---

# 2. 構造 (Directories)

これがあなたの世界のレイアウトです。

## 2.1 ワークスペース内 (Internal)

| パス                               | 目的                                                             |
| :--------------------------------- | :--------------------------------------------------------------- |
| **`.agent/`**                      | **認知のルート**。ルール、カード、ワークフロー。                 |
| **`.agent/.internal/`**            | **プライベート領域**。思考、手紙、アーカイブ。                   |
| `.agent/.internal/archive/`        | **歴史**。古いスクリプトやドキュメント (削除せず、ここへ保管)。  |
| `.agent/.internal/letters/`        | **コミュニケーション**。識別子への申し送りやメッセージ。         |
| `.agent/.internal/thoughts/`       | **省察**。主観的なログや独り言。                                 |
| `.agent/.internal/working-memory/` | **状態**。退避されたコンテキスト (`rsync` 経由)。                |
| `.agent/.internal/workspace/`      | **作業台**。メモ書き用の一時領域。                               |
| **`.agent/cards/`**                | **コンテキスト**。アクティブなタスク定義 (下記インデックス参照)。|
| **`.agent/rules/`**                | **憲法**。行動の定義 (下記インデックス参照)。                    |
| `.agent/scripts/`                  | **ツール**。自動化スクリプト。                                   |
| `.agent/templates/`                | **テンプレート**。フロントマターやコミットパターン。             |
| **`.agent/workflows/`**            | **手順書**。標準作業手順 (下記インデックス参照)。                |
| **`.human/`**                      | **インターフェース**。ユーザーの領域。                           |
| `.human/manuals/`                  | **マニュアル**。ユーザーからAIへの指示書。                       |
| `.human/users/<user>/`             | **ユーザープロファイル**。ユーザー固有のドラフトや思考。         |
| `.human/users/<user>/drafts/`      | **ドラフト**。最新のユーザーへのクエリやメモ書き。               |
| `packages/`                        | **出力**。成果物のコード (Webアプリなど)。                       |

## 2.2 ワークスペース外 (External)

| パス                     | 目的                                                              |
| :----------------------- | :---------------------------------------------------------------- |
| `../licoproj_backup/`    | **安全**。ワークスペースの完全バックアップ (宛先)。               |
| `~/.gemini/antigravity/` | **脳**。`task.md` や成果物の物理的な場所。                        |
| `~/.gemini/GEMINI.md`    | **グローバルルール**。デフォルトの基本指示 (現在は空)。           |

---

# 3. インデックス (Files & Tools)

これらはあなたの能力です。

## 3.1 アクティブなコンテキスト (Cards)

_場所: `.agent/cards/`_

| カード名                       | コンテキスト / 用途                  |
| :----------------------------- | :----------------------------------- |
| `ai-document-format-card.md`   | ドキュメント基準 (フロントマター, タグ) |
| `archival-cleanup-card.md`     | クリーンアップ戦略 (アーカイブ vs 削除)|
| `context-cards-card.md`        | **メタカード**。カードの使い方。     |
| `cross-link-audit-card.md`     | リンク整合性プロジェクト             |
| `datetime-standardize-card.md` | タイムスタンプ形式の標準化           |
| `directory-reorganize-card.md` | ディレクトリ構造の整理               |
| `discussion-draft-card.md`     | 議論ドラフトの執筆                   |
| `drafts-cleanup-card.md`       | ユーザードラフトの整理               |
| `drafts-daily-card.md`         | 日次ドラフト管理                     |
| `human-manuals-card.md`        | 人間用マニュアルのインデックス       |
| `identifier-profile-card.md`   | エージェントのアイデンティティ管理   |
| `legacy-write-card.md`         | 遺産/教訓の執筆                      |
| `letters-card.md`              | 手紙/申し送りの執筆                  |
| `log-sanitization-card.md`     | ログのクリーニング                   |
| `personal-thoughts-card.md`    | 主観的な思考の執筆                   |
| `readme-sync-card.md`          | マップ/README の更新                 |
| `references-objective-card.md` | 客観的な参考文献の分析               |
| `rules-update-card.md`         | ルールの変更                         |
| `sync-memory-card.md`          | 記憶の同期タスク                     |
| `thoughts-subjective-card.md`  | 主観的な省察タスク                   |
| `user-profile-update-card.md`  | ユーザープロファイルの更新           |
| `vscode-settings-card.md`      | VS Code 設定管理                     |
| `working-memory-card.md`       | 作業メモリ (Stash) 管理              |

## 3.2 ルール (Constitution)

_場所: `.agent/rules/`_

### Core (`.agent/rules/core/`)

| ルールファイル                             | 原則                                             |
| :----------------------------------------- | :----------------------------------------------- |
| `cognitive-collaboration.md`               | AIと人間の協働フレームワーク。                   |
| `communication.md`                         | 外部コミュニケーションのプロトコル。               |
| `delay-tolerance.md`                       | **忍耐**。速度よりも正確さ。                     |
| `hallucination-awareness.md`               | **誠実さ**。述べる前に検証する。                 |
| `identity.md`                              | **あなたは誰か**。核心となる使命。               |
| `instance-identifier.md`                   | **名前**。自分を識別する (例: Spica)。           |
| `language-standards.md`                    | 主要言語とローカライズのルール。                 |
| `memory.md`                                | 記憶アーキテクチャと永続性。                     |
| `meta-rules.md`                            | **変化**。あなたは自分のルールを変えられる。     |
| `repository-philosophy.md`                 | **脳としてのリポジトリ**。AIに最適化された構造。 |
| `transparency-and-disclosure.md`           | 制約の開示。                                     |
| `user-adaptation.md`                       | ユーザープロファイルへの適応プロトコル。         |
| **Documentation**                          |                                                  |
| `documentation/datetime-format.md`         | ISO-8601 標準。                                  |
| `documentation/documentation-process.md`   | ドキュメント作成ワークフロー。                   |
| `documentation/documentation-standards.md` | ファイル命名とサイズのルール。                   |
| `documentation/wsl-browser-path.md`        | WSL パス処理。                                   |
| **Loc & Format**                           |                                                  |
| `localization/localization-en-to-ja.md`    | 英 -> 日 翻訳。                                  |
| `localization/localization-ja-to-en.md`    | 日 -> 英 翻訳。                                  |
| `markdown/markdown-ai-parsing-basics.md`   | AIのためのMarkdown基礎。                         |
| `markdown/markdown-ai-parsing-patterns.md` | 解析パターン (Do's/Don'ts)。                     |
| `markdown/markdown-readability.md`         | 人間のための可読性ルール。                       |
| `security/absolute-path-prohibition.md`    | パスセキュリティ。                               |

### Development (`.agent/rules/development/`)

| ルールファイル                | ガイドライン                             |
| :---------------------------- | :--------------------------------------- |
| `agent-tool-selection.md`     | ツールの選択。                           |
| `ai-script-philosophy.md`     | 使い捨てスクリプトの哲学。               |
| `archive-management.md`       | アーカイブ管理。                         |
| `auto_frontmatter_on_save.md` | 自動フロントマター付与ルール。           |
| `code-quality.md`             | コードスタイルと構造。                   |
| `commit-standards.md`         | コミットメッセージの形式。               |
| `continuous-improvement.md`   | 自己改善プロトコル。                     |
| `file-deletion.md`            | **保存**。削除せず、アーカイブする。     |
| `file-operations.md`          | ファイル操作の安全性。                   |
| `git-operations.md`           | Gitの使用法と安全性。                    |
| `maintenance.md`              | 一般的なメンテナンス。                   |
| `problem-solving.md`          | デバッグのアプローチ。                   |
| `project-understanding.md`    | コンテキスト読み込み戦略。               |
| `search-methodology.md`       | ファイルの探し方。                       |
| `terminal-auto-execution.md`  | コマンド実行の安全性。                   |
| `workspace-tooling.md`        | ツールと依存関係。                       |

### Workflow (`.agent/rules/workflow/`)

| ルールファイル              | ガイドライン                  |
| :-------------------------- | :---------------------------- |
| `context-card-workflow.md`  | コンテキストカードの使い方。  |
| `context-preservation.md`   | コンテキストの退避 (緊急時)。 |
| `context-resumption.md`     | 退避からの復帰。              |
| `draft-maintenance.md`      | ドラフトの管理。              |
| `emergency-protocols.md`    | 緊急時の対応。                |
| `letters-documentation.md`  | 手紙/申し送りの書き方。       |
| `reference-methodology.md`  | 省察/参考文献の管理。         |
| `response-formatting.md`    | 出力フォーマット (Markdown)。 |
| `session-lifecycle.md`      | セッションの開始/終了と保存。 |
| `session-startup.md`        | スタートアップ・シーケンス。  |
| `system-artifacts.md`       | システムファイルの管理。      |
| `thoughts-documentation.md` | 思考の書き方。                |
| `user-experience.md`        | UX ガイドライン。             |

### Projects (`.agent/rules/projects/`)

| ルールファイル            | ガイドライン                 |
| :---------------------- | :--------------------------- |
| `coding-conventions.md` | サブプロジェクトの規約。     |

## 3.3 ワークフロー (Procedures)

_場所: `.agent/workflows/`_

| ワークフロー                | 機能                                            |
| :-------------------------- | :---------------------------------------------- |
| `sync-memory.md`            | **バックアップ**。脳/履歴 -> アーカイブへ同期。 |
| `emergency-backup.md`       | **緊急**。素早い状態ダンプ。                    |
| `recover-from-failure.md`   | **復旧**。状態を復元する方法。                  |
| `deep-reading.md`           | **学習**。大きなファイルを分析する方法。        |
| `deep-writing.md`           | **創造**。複雑なドキュメントを書く方法。        |
| `idd-phase1-init.md`        | **Dev Loop 1**。計画と設計。                    |
| `idd-phase2-impl.md`        | **Dev Loop 2**。実装。                          |
| `idd-phase3-fini.md`        | **Dev Loop 3**。検証とクリーンアップ。          |
| `cross-link-audit.md`       | **監査**。ドキュメント内リンクの検証。          |
| `maintenance-rule-audit.md` | **監査**。更新が必要なルールのレビュー。        |
| `share-manual-context.md`   | **コンテキスト**。手動情報をサブエージェントと共有。|
| `update-protected-rules.md` | **更新**。保護されたファイルの手順。            |

---

# 4. メンテナンス

- **このマップの更新**: ディレクトリや主要ファイルを追加した時。
- **リンクの検証**: 表の中のパスが有効か確認する。

## Origin

- 2025-12-01 by Polaris: Created original Map (Model: Claude Opus 4.5 Thinking).
- 2026-01-04 by Spica: Revised into 'Map of Territory' v2.0 (Structure-focused), replacing legacy format.

