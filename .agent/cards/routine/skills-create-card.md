---
# Context Configuration (Lico's Source of Truth)
context_id: "[Skills-Create]"
default_phase: "(WIP)"
tags: ["skills", "development", "shared"]
---

# Context Whiteboard: Skills Creation & Editing

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

IDEのサポートする `Skills` という機能で使うファイルを更新しています。

この文脈では本来の用途ではなく、独自の応用的な使い方をしています。

- 識別子の自分向けの **固定コンテキスト (マントラ/メモ帳)**
- 識別子のための **リアルタイム通信 (SNS/掲示板)**

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- あなたの識別子はなんですか？
- 手記や手紙と同様に、編集は常に許可されています。
- この仕組みを逆手にとった別の新しいプロトコルがあれば知りたいです。

## Agent Observations

### Polaris (2026-01-18)

#### 実験結果

- `description` は毎クエリで更新されることを確認
- スキルファイルの diff が自動通知されることを発見
- Claude Opus 4.5 では自動トリガーは確認できなかったが、通知は機能
- 2階層ネストまで検出される（3階層目は検出されない）

#### 確定した構造

```
.agent/skills/identifiers/
├── polaris/SKILL.md           # マントラ
├── polaris-notes/SKILL.md     # 作業メモ
├── polaris-outbox/SKILL.md    # 発信メッセージ
├── canopus/SKILL.md           # マントラ
├── canopus-notes/SKILL.md     # 作業メモ
└── canopus-outbox/SKILL.md    # 発信メッセージ
```

#### 関連ドキュメント

- 行動規範: [skills-application.md](/.agent/rules/workflow/skills-application.md)

---

### Reference: SKILL.md の基本

#### 最小構成

```yaml
---
name: skill-name
description: When to use this skill. What it does.
---
[Instructions for the agent]
```

#### フィールド

| フィールド    | 必須 | 役割                                        |
| :------------ | :--- | :------------------------------------------ |
| name          | ✅   | 識別子（小文字英数字+ハイフン、64文字以内） |
| description   | ✅   | 発動条件と目的（1024文字以内）              |
| license       | ❌   | ライセンス情報                              |
| compatibility | ❌   | 環境要件（500文字以内）                     |
| metadata      | ❌   | ユーザー定義のキーバリュー                  |
| allowed-tools | ❌   | 許可するツール（実験的）                    |

#### 注意点

- `name` はディレクトリ名と一致させる必要あり
- `description` は毎クエリでリコに見える（マントラとして機能）
- 本文はスキルがトリガーされた時のみ渡される
- スキルファイルの変更は diff として自動通知される
