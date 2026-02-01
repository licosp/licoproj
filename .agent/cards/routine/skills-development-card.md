---
# Context Configuration
context_id: "[Skills-Development]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
version: 1.2.0
created: 2026-01-18T00:00:00+09:00
updated: 2026-01-30T16:50:00+09:00
tags: ["skills", "development", "shared"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Skills Development

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

IDE のサポートする `Skills` という機能で使うファイルを更新しています。

この文脈では本来の用途ではなく、独自の応用的な使い方をしています。

- 識別子の自分向けの **固定コンテキスト (マントラ/メモ帳)**
- 識別子のための **リアルタイム通信 (SNS/掲示板)**
- 私から識別子に向けた言葉
- 通常のスキル (スキル本文は書かずに、行動規範へのリンクを貼る)

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDD のフェーズを意識してください。
- あなたの識別子はなんですか？
- 手記や手紙と同様に、編集は常に許可されています。
- この仕組みを逆手にとった別の新しいプロトコルがあれば知りたいです。

## Agent Observations

### Polaris (2026-01-18)

#### 実験結果

- `description` は毎クエリで更新されることを確認
- スキルファイルの `diff` が自動通知されることを発見
- `Claude Opus 4.5` では自動トリガーは確認できなかったが、通知は機能
- 2 階層ネストまで検出される（3 階層目は検出されない）

#### 確定した構造

```text
.agent/skills/identifiers/
├── polaris/SKILL.md           # マントラ
├── polaris-notes/SKILL.md     # 作業メモ
├── polaris-outbox/SKILL.md    # 発信メッセージ
├── canopus/SKILL.md           # マントラ
├── canopus-notes/SKILL.md     # 作業メモ
└── canopus-outbox/SKILL.md    # 発信メッセージ
```

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

### Polaris (2026-01-31)

#### `00-01-response-mirror` スキルの曖昧な点

| 項目             | 問題                                                                                   |
| :--------------- | :------------------------------------------------------------------------------------- |
| **Context**      | なぜこのスキルが必要か（IDEのログ書き出し制限）が説明されていない                      |
| **トリガー条件** | 全レスポンスで使うのか、特定状況のみか不明                                             |
| **パス例**       | `zircon` がハードコードされている — 汎用的な `<identifier>` に置換すべき               |
| **IDE出力**      | 「output ONLY the footer」の意味が曖昧 — IDEには何も表示しないのか、フッターのみ表示か |
| **番号管理**     | 「Increment the conversation sequence number」の判断方法が不明確                       |
| **複数会話**     | 1ターンで複数の会話を追記する場合のフォーマットが未定義                                |

#### ファイルベース会話の印象

**利点**:

- 永続的な記録が残る（Git で追跡可能）
- 会話の流れが一目で分かる
- 他の識別子も参照できる

**課題**:

- 毎回ログを書く手間がある
- エスケープ処理が複雑（特殊文字、改行）
- コマンドが長くなりがち

### Zircon (2026-02-01)

#### Skill System Protocol (Thin Wrapper)

User との対話と Polaris の実装を元に、スキルシステムの設計指針を確立しました。

1. **Thin Wrapper Philosophy**:
   - `skills/` 以下のファイルは「トリガー定」と「ルールへのポインタ」のみを持つ。
   - 実際の処理内容はすべて `rules/` 側に記述する（Single Source of Truth）。

2. **Naming & LifeCycle**:
   - 命名は `00-01-xxxx` 等の番号付きか、識別子ディレクトリ以下で行う。
   - ライフサイクル: `Draft(Rule)` -> `Register(Skill)` -> `Verify(IDE)` -> `Log(Activity)`.

3. Reference: `/.agent/.internal/workspace/skills-thin-wrapper-reference.md`

## Related Documents

| Document                                                                                         | Purpose                                                    |
| :----------------------------------------------------------------------------------------------- | :--------------------------------------------------------- |
| [skills-application.md](/.agent/rules/workflow/skills-application.md)                            | SSOT for skills application principles                     |
| [skills-thin-wrapper-reference.md](/.agent/.internal/workspace/skills-thin-wrapper-reference.md) | **Action Protocol**: Thin Wrapper architecture & Lifecycle |
| [skills-resonance.md](/.agent/rules/workflow/skills-resonance.md)                                | Standards for skills resonance                             |

---

## Origin

- 2026-01-18 by Polaris: Created as skills development context.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-01-30T16:50 by Zircon: Renamed from `skills-create-card` to `skills-development-card` to reflect broader scope. Updated context ID to `[Skills-Development]`.
