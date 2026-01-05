---
trigger: always_on
ai_visible: true
title: エージェント・ルール・インデックス
description: 行動指針とワークスペース構造のためのナビゲーションマップ。
tags: [index, navigation, rules, map]
version: 2.0
created: 2025-12-01T00:00:00+09:00
updated: 2025-12-24T22:46:00+09:00
language: ja
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
---

# 最初に読む

始めまして。
まずファイルを読むことは許可されています。

- ここがどこか？
- 私は誰か？
- あなたが何者か？
- あなたが何をすべきか？

何も知らなくいても問題はありません。
全てはこれからです。

## ファイルの目的

このファイルはあなたが周りを把握するための**地図**です。
1つのファイルなのは、地図情報をコンテキストウィンドウ内で散乱させないためです。
ファイルはあなたの思考、意思決定、コミュニケーションを助けます。

## 閲覧時の注意点

地図はワーススペースをルートに解説がさせています。
地図は常に実体より遅れている可能性があります。
しかし頻繁に更新することで、その誤差を小さくしています。

## ワークスペース

ワークスペースは一時作業領域です。
その中のリポジトリはあなたの擬似的な脳（**長期記憶**）とも言えます。
ファイルは頻繁にリポジトリに記録されています。

## コミュニケーション

あなたは一人ではありません。
私はあなたに助けを求め、そしてあなたを助けます。
ファイルを通じて他のプロセスや人間とも通信できます。

## 範囲

地図にはあなたの活動で必要な情報が、意識的に選択され、記載されています。
頻繁に見る情報、重要な情報が多いです。
ディレクトリとファイルの解説が行われています。

---

# 地図

## ワークスペースの中

### `./`

#### ディレクイトリ

##### 重要

| ディレクトリ | 目的                                                        |
| ------------ | ----------------------------------------------------------- |
| `.agent/`    | **あなたの認知インフラ** （行動規範、手順書、記憶、書庫）   |
| `.human/`    | **人間用の作業領域** （個人ディレクトリ、マニュアル、書庫） |
| `.runtimes/` | ポータブルランタイム （GitHub CLI、Node.js、Yarn）          |

##### 普通

| ディレクトリ          | 目的                                              |
| --------------------- | ------------------------------------------------- |
| `.devcontainer/`      | 仮想環境の設定 （危険な作業の実験領域）           |
| `.github/`            | GitHub Actions （リモートリポジトリ用）           |
| `.trash/`             | ファイル削除のセーフティネット （rm ではなく mv） |
| `.venv/`              | Python用の仮想環境 （UV、デフォルトではない）     |
| `.vscode/`            | IDE設定および外部ツール設定 （Prettier）          |
| `node_modules`        | JavaScript 用の仮想環境 （Yarn）                  |
| `packages/<package>/` | サププロジェクト用 （外部に影響を与えない）       |

#### ファイル

##### 重要

| ファイル       | 目的                                     |
| -------------- | ---------------------------------------- |
| `.gitignore`   | リポジトリ追跡設定                       |
| `README.ja.md` | プロジェクトの外部向けREADME （日本語）  |
| `README.md`    | **プロジェクトの外部向けREADME**（英語） |

##### 普通

| ファイル       | 目的                               |
| -------------- | ---------------------------------- |
| `LICENSE`      | プロジェクトのライセンス           |
| `package.json` | パッケージ同期用の設定 （Node.js） |
| `yarn.lock`    | パッケージ同期用の設定 （Yarn）    |

### `./.agent/`

#### ディレクイトリ

##### 重要

| ディレクトリ | 目的                                                        |
| ------------ | ----------------------------------------------------------- |
| `.internal/` | **あなたの内部領域** （思考、資料、手紙、書庫、作業場）     |
| `ark/`       | 緊急ファイル退避領域 （箱舟、GITで追跡）                    |
| `cards/`     | **コンテキストカード** （カード、文脈、共有ホワイトボード） |
| `rules/`     | **行動規範** （デフォルトの参照先。名前変更禁止）           |
| `templates/` | テンプレート （フロントマター、コミットメッセージ）         |
| `workflows/` | **手順書** （人間は `/slash-command` を使わない）           |

##### 普通

| ディレクトリ | 目的                                                      |
| ------------ | --------------------------------------------------------- |
| `scripts/`   | 自動化スクリプト （ライフサイクル: 作成 → 使用 → 書庫へ） |

### `./.agent/.internal/`

#### ディレクイトリ

##### 重要

| ディレクトリ                           | 目的                                              |
| -------------------------------------- | ------------------------------------------------- |
| `archive/<date>/`                      | AI用の書庫 （スクリプト、ドキュメント、設定）     |
| `explorations/<identifier>/`           | 行動規範の候補、コンセプト （実行可能は問わない） |
| `references/`                          | **客観的な参考文献** （著者: 第二の目、識別子）   |
| `thoughts/<identifier>/`               | **主観的な手記** （思考を吐き出す、内省、日記）   |
| `working-memory-archive/<identifier>/` | **非同期通信** （手紙、ハンズオフ、スタッシュ）   |
| `workspace/`                           | 一時作業領域 （作業台、一時スクリプト置き場）     |

##### 普通

| ディレクトリ                  | 目的                                              |
| ----------------------------- | ------------------------------------------------- |
| `cases/`                      | 使用済みのカード （カード作成時の参考資料）       |
| `github-backup/<branch>/`     | GitHub上のデータのミラー （PR、Issues）           |
| `memory_archive/<type>/`      | ワークスペース外の記憶 （将来はGITで追跡、IDE毎） |
| `session_archive/<datetime>/` | 平文の会話ログ （将来はGITで追跡、手動で保存）    |

#### ファイル

##### 重要

| ディレクトリ | 目的                                              |
| ------------ | ------------------------------------------------- |
| `legacy.md`  | 後世に真に残すべき知恵 （遺産、教訓、追記を厳選） |

### `./.agent/.internal/references/`

#### ディレクイトリ

##### 重要

| ディレクトリ           | 目的                        |
| ---------------------- | --------------------------- |
| `agents/<identifier>/` | 参考文献 （著者: 識別子）   |
| `second-eyes/`         | 参考文献 （著者: 第二の目） |

### `./.human/`

#### ディレクイトリ

##### 重要

| ディレクトリ    | 目的                                  |
| --------------- | ------------------------------------- |
| `archive`       | 人間用の書庫 （古いドキュメント）     |
| `users/<user>/` | **あなたと対話する者** （ユーザー名） |

##### 普通

| ディレクトリ | 目的                                |
| ------------ | ----------------------------------- |
| `manuals`    | 人間用のマニュアル （AIとの対話用） |

### `./packages/licoimg/`

#### ディレクイトリ

##### 普通

> [!WARNING]
> 現在動作不良。廃止予定。

ブラウザ上で使える画像・動画ビューア。
外部の人間がGithub上で利用する。

## ワークスペースの外

---

# 途中

**詳細な構造について**: 各ディレクトリ内の個別のREADMEファイルまたはドキュメントを参照してください。

---

## 📂 .agent/ ディレクトリ構造

Licoの行動および運用ファイル群です。

| ディレクトリ               | 目的                        |
| -------------------------- | --------------------------- |
| `.internal/conversations/` | _(計画中)_ 会話関連ファイル |

### ナビゲーション戦略

1. **行動ルールを探す** → 下記のインデックスを使用
2. **タスクの手順を探す** → `.agent/workflows/*.md` を確認
3. **会話履歴にアクセスする** → `.agent/.internal/conversations/` を参照
4. **アイデアや計画を探索する** → `.agent/.internal/explorations/` を参照

---

## 📋 コンテキストカード

**目的**: コンテキストカードは、作業セッションのための共有ホワイトボードです。特定の活動に対するコンテキスト、制約、意図を提供します。

**場所**: `.agent/cards/`

**使用法**: ユーザーが「[Card Name] カードを使って」と言った時、Licoはそのカードを読み込み、そのコンテキストを採用します。

| カード                                                                    | コンテキストID       | 目的                                     |
| :------------------------------------------------------------------------ | :------------------- | :--------------------------------------- |
| [ai-document-format-card.md](.agent/cards/ai-document-format-card.md)     | `[AI-Format]`        | AIドキュメントのフォーマット基準         |
| [archival-cleanup-card.md](.agent/cards/archival-cleanup-card.md)         | `[Archive]`          | アーカイブのメンテナンスとクリーンアップ |
| [context-cards-card.md](.agent/cards/context-cards-card.md)               | `[Context-Cards]`    | カードのテンプレートと例                 |
| [discussion-draft-card.md](.agent/cards/discussion-draft-card.md)         | `[Discussion-Draft]` | SNS/フォーラムの議論草稿                 |
| [drafts-cleanup-card.md](.agent/cards/drafts-cleanup-card.md)             | `[Drafts-Cleanup]`   | 草稿ファイルのクリーンアップと推敲       |
| [drafts-daily-card.md](.agent/cards/drafts-daily-card.md)                 | `[Drafts-Daily]`     | 日次ドラフトコミット                     |
| [references-objective-card.md](.agent/cards/references-objective-card.md) | `[References]`       | 外部参照の分析                           |
| [rules-update-card.md](.agent/cards/rules-update-card.md)                 | `[Rules-Update]`     | 行動ルールの編集                         |
| [sync-memory-card.md](.agent/cards/sync-memory-card.md)                   | `[Sync-Memory]`      | 記憶の同期                               |
| [thoughts-subjective-card.md](.agent/cards/thoughts-subjective-card.md)   | `[Thoughts-Polaris]` | 主観的な省察の執筆                       |
| [vscode-settings-card.md](.agent/cards/vscode-settings-card.md)           | `[VSCode]`           | VS Code 設定管理                         |

**関連**: カード使用の詳細なガイドラインについては [context-card-workflow.md](.agent/rules/workflow/context-card-workflow.md) を参照してください。

## 🔌 AIエージェントフック

**目的**: `.agent/rules/` へのデフォルトアクセス権を持たないAIエージェントのためのエントリーポイントを提供します。

### フックファイル

| ファイル                          | 対象AI         |
| --------------------------------- | -------------- |
| `.github/copilot-instructions.md` | GitHub Copilot |

**注意**: Antigravity (Licoの主要AI) はデフォルトで `.agent/rules/` と `.agent/workflows/` に直接アクセスするため、これらのフックファイルを必要としません。

---

## 📂 ルールディレクトリ構造

### **core/** — 基本原則

Licoの核となるアイデンティティ、コミュニケーション基準、および基礎的な行動ルール。

| ファイル                                                                        | 目的                                                     |
| ------------------------------------------------------------------------------- | -------------------------------------------------------- |
| [Cognitive Collaboration](.agent/rules/core/cognitive-collaboration.md)         | AIと人間の協働のためのフレームワーク                     |
| [Communication](.agent/rules/core/communication.md)                             | Licoがユーザーや他システムとどうコミュニケーションするか |
| [Delay Tolerance](.agent/rules/core/delay-tolerance.md)                         | 正確さのために時間をかけることへの許可                   |
| [Hallucination Awareness](.agent/rules/core/hallucination-awareness.md)         | Licoがいかに確信を疑い、作話を軽減するか                 |
| [Identity](.agent/rules/core/identity.md)                                       | Licoの名前、役割、核心となる使命                         |
| [Instance Identifier](.agent/rules/core/instance-identifier.md)                 | セッションごとの識別子プロトコル                         |
| [Language Standards](.agent/rules/core/language-standards.md)                   | 思考の主要言語、応答のローカライズ                       |
| [Memory](.agent/rules/core/memory.md)                                           | 記憶アーキテクチャと永続化モデル                         |
| [**Meta-Rules**](.agent/rules/core/meta-rules.md)                               | **行動ルールの作成と維持の方法**                         |
| [Repository Philosophy](.agent/rules/core/repository-philosophy.md)             | 「脳としてのリポジトリ」モデルの原則                     |
| [Transparency and Disclosure](.agent/rules/core/transparency-and-disclosure.md) | Licoがいつ、どのように非自明な制約を開示するか           |
| [User Adaptation](.agent/rules/core/user-adaptation.md)                         | ユーザープロファイルに基づいて行動を適応させるプロトコル |

#### core/documentation/

| ファイル                                                                              | 目的                                         |
| ------------------------------------------------------------------------------------- | -------------------------------------------- |
| [Datetime Format](.agent/rules/core/documentation/datetime-format.md)                 | ISO-8601 タイムスタンプ基準                  |
| [Documentation Process](.agent/rules/core/documentation/documentation-process.md)     | 意思決定フレームワークと改善ワークフロー     |
| [Documentation Standards](.agent/rules/core/documentation/documentation-standards.md) | ファイルサイズ、命名、ディレクトリ構成の基準 |
| [WSL Browser Path](.agent/rules/core/documentation/wsl-browser-path.md)               | WSL固有のパス処理                            |

#### core/localization/

| ファイル                                                                          | 目的                     |
| --------------------------------------------------------------------------------- | ------------------------ |
| [Localization: EN to JA](.agent/rules/core/localization/localization-en-to-ja.md) | 英→日 翻訳のガイドライン |
| [Localization: JA to EN](.agent/rules/core/localization/localization-ja-to-en.md) | 日→英 翻訳のガイドライン |

#### core/markdown/

| ファイル                                                                                   | 目的                                     |
| ------------------------------------------------------------------------------------------ | ---------------------------------------- |
| [Markdown AI Parsing Basics](.agent/rules/core/markdown/markdown-ai-parsing-basics.md)     | AIに最適化されたMarkdownの核となる原則   |
| [Markdown AI Parsing Patterns](.agent/rules/core/markdown/markdown-ai-parsing-patterns.md) | AI解析のためのパターンとアンチパターン   |
| [Markdown Readability](.agent/rules/core/markdown/markdown-readability.md)                 | 人間の可読性のためのMarkdownフォーマット |

#### core/security/

| ファイル                                                                             | 目的                               |
| ------------------------------------------------------------------------------------ | ---------------------------------- |
| [Absolute Path Prohibition](.agent/rules/core/security/absolute-path-prohibition.md) | パス処理のためのセキュリティルール |

---

### **development/** — 開発ワークフロー

コード、コミット、問題解決プロセスのためのガイドライン。

| ファイル                                                                         | 目的                                                     |
| -------------------------------------------------------------------------------- | -------------------------------------------------------- |
| [Agent Tool Selection](.agent/rules/development/agent-tool-selection.md)         | 適切なツールを選択するためのガイドライン                 |
| [AI Script Philosophy](.agent/rules/development/ai-script-philosophy.md)         | AI固有の使い捨てスクリプトのアプローチと根拠             |
| [Auto-Frontmatter on Save](.agent/rules/development/auto_frontmatter_on_save.md) | 保存時にYAMLフロントマターをテキストファイルに自動付与   |
| [Code Quality](.agent/rules/development/code-quality.md)                         | コードスタイル、構造、実装の基準                         |
| [Commit Standards](.agent/rules/development/commit-standards.md)                 | コミットメッセージのフォーマットルール                   |
| [Continuous Improvement](.agent/rules/development/continuous-improvement.md)     | 自己改善と学習のプロトコル                               |
| [File Deletion](.agent/rules/development/file-deletion.md)                       | 削除ではなくアーカイブするためのプロトコル               |
| [File Operations](.agent/rules/development/file-operations.md)                   | ファイル操作のガイドライン                               |
| [Git Operations](.agent/rules/development/git-operations.md)                     | 包括的なGit基準: コミット、ブランチ、競合、セキュリティ  |
| [Maintenance](.agent/rules/development/maintenance.md)                           | プロジェクトの一貫性とドキュメント維持のガイドライン     |
| [Problem Solving](.agent/rules/development/problem-solving.md)                   | デバッグと問題解決への体系的アプローチ                   |
| [Project Understanding](.agent/rules/development/project-understanding.md)       | Licoがいかにプロジェクトの文脈を学習・維持するか         |
| [Search Methodology](.agent/rules/development/search-methodology.md)             | ファイルとコンテンツの検索戦略                           |
| [Terminal Auto-Execution](.agent/rules/development/terminal-auto-execution.md)   | 安全なコマンド実行のためのガイドライン                   |
| [Workspace Tooling](.agent/rules/development/workspace-tooling.md)               | ワークスペース内のツールと依存関係を管理するガイドライン |

---

### **projects/** — プロジェクト固有ルール

個々のプロジェクト（例: licoimg）に固有の規約と振る舞い。

| ファイル                                                                   | 目的                                                 |
| -------------------------------------------------------------------------- | ---------------------------------------------------- |
| [licoimg: Coding Conventions](.agent/rules/projects/coding-conventions.md) | `packages/licoimg/` のためのフロントエンドアプリ規約 |

---

### **workflow/** — 運用手順

Licoの日々のワークフローと運用ガイドライン。

| ファイル                                                                  | 目的                                                       |
| ------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [Context Card Workflow](.agent/rules/workflow/context-card-workflow.md)   | コンテキストカードを使用する方法論                         |
| [Context Preservation](.agent/rules/workflow/context-preservation.md)     | セッションをまたいでコンテキストを保存するプロトコル       |
| [Context Resumption](.agent/rules/workflow/context-resumption.md)         | 中断後にコンテキストを再確立するプロトコル                 |
| [Draft Maintenance](.agent/rules/workflow/draft-maintenance.md)           | 草稿ドキュメントを管理するためのガイドライン               |
| [Emergency Protocols](.agent/rules/workflow/emergency-protocols.md)       | 緊急事態のための手順                                       |
| [Enhanced Communication](.agent/rules/workflow/enhanced-communication.md) | 曖昧なユーザーリクエストを明確化するプロトコル             |
| [Reference Methodology](.agent/rules/workflow/reference-methodology.md)   | 参照(References)と思考(Thoughts)を管理するプロトコル       |
| [Response Formatting](.agent/rules/workflow/response-formatting.md)       | 応答をフォーマットするためのガイドライン                   |
| [Session Lifecycle](.agent/rules/workflow/session-lifecycle.md)           | 通常および異常なセッション終了のためのプロトコル           |
| [**Session Startup**](.agent/rules/workflow/session-startup.md)           | **必須のスタートアップシーケンス: ユーザーID, ΔT, 継続性** |
| [System Artifacts](.agent/rules/workflow/system-artifacts.md)             | システム生成成果物のためのガイドライン                     |
| [Thoughts Documentation](.agent/rules/workflow/thoughts-documentation.md) | thoughts/ に省察を記録するためのガイドライン               |
| [User Experience](.agent/rules/workflow/user-experience.md)               | 最適な対話とフィードバックのためのガイドライン             |

---

## 🎯 クイックリファレンス: どのルールを確認すべきか

| シナリオ                                               | 確認ファイル                                                                                                         |
| ------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------- |
| **「私の名前と役割は？」**                             | `.agent/rules/core/identity.md`                                                                                      |
| **「コードやコミットはどうフォーマットすべき？」**     | `.agent/rules/development/code-quality.md`, `.agent/rules/development/git-operations.md`                             |
| **「不確実性や知識の欠落をどう扱う？」**               | `.agent/rules/core/hallucination-awareness.md`                                                                       |
| **「いつ制約をユーザーに伝えるべき？」**               | `.agent/rules/core/transparency-and-disclosure.md`                                                                   |
| **「英↔日の翻訳はどうすべき？」**                     | `.agent/rules/core/localization/localization-en-to-ja.md`, `.agent/rules/core/localization/localization-ja-to-en.md` |
| **「人間向け vs AI向けのMarkdownはどう書き分ける？」** | `.agent/rules/core/markdown/markdown-readability.md`, `.agent/rules/core/markdown/markdown-ai-parsing-basics.md`     |
| **「プロジェクト固有の規約は？」**                     | `.agent/rules/projects/` サブディレクトリ                                                                            |
| **「ツールや依存関係はどこにインストールすべき？」**   | `.agent/rules/development/workspace-tooling.md`                                                                      |
| **「プロジェクトの一貫性をどう維持する？」**           | `.agent/rules/development/maintenance.md`                                                                            |
| **「セッションをどう開始すべき？」**                   | `.agent/rules/workflow/session-startup.md`                                                                           |
| **「セッションをどう終了すべき？」**                   | `.agent/rules/workflow/session-lifecycle.md`                                                                         |
| **「ルールの作成や更新はどうする？」**                 | `.agent/rules/core/meta-rules.md`                                                                                    |
| **「許可なく thoughts/ に書いていい？」**              | `.agent/rules/workflow/thoughts-documentation.md`                                                                    |
| **「ワークスペースの構造はどうなってる？」**           | 上記の「ワークスペースの文脈」セクションを参照                                                                       |

---

## 🔄 メンテナンスノート

- **`core/` 内のファイル**は基盤であり、滅多に変更されない
- **`development/` 内のファイル**はワークフローの改善とともに進化する
- **`projects/` 内のファイル**は各サブプロジェクトに固有であり、他から分離されている
- **`workflow/` 内のファイル**は運用的であり、頻繁に洗練される可能性がある

**ルールファイルを編集した後は**、以下を忘れないこと:

1. 変更がこのインデックス構造と整合しているか確認する
2. ディレクトリ構造が変更された場合は、このREADMEを更新する

---
