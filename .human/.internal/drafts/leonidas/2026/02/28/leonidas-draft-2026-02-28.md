---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-02-27T00:00:00+09:00
updated: 2026-02-27T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Antigravity` | `Gemini 3.1 Pro (High)`: `Planning` | `Sirius`

####

- 作業の途中ですが、日付が変わりました。
- テンプレートから今日の会話ファイルを作成して、追記用ファイルを移動してください。

####

続けてください。

####

- スクリプト用のリンターをもう少し厳しくしました。
  直してみてください。

####

- まだリンターの調整はしますが、整理のために先にコミットしましょう。
  行動規範の方は本文以外も更新してください。
- あと会話ログへの追記も並行して行ってください。

####

- 会話ファイルの行動規範を読んで、追記の方法を再確認してください。
- さらに影に会話ファイルをコミットしてください。

####

- 一度これをオフにしました。
  - `mypy: disable-error-code="import-untyped"`
- なぜ yaml だけこの処理が必要なのでしょうか？

- 会話ファイルにこれが入ってませんでした。
  - `### Conversation: [2026-02-28T05:05:00+09:00]`

####

- PyYAML の本体パッケージとスタブパッケージをインストールでしました。
  警告が消えたので、解決したのでしょうか？
  コードに修正の必要があれば直してください。

####

- PyYAML には `try - except` の構文が残りますが、これは残るものなんですか？
  外部ライブラリの一般的な扱い方ですか？

####

- インポートのハンドリングの件は理解しました。

- 次です。
- `Ruff` の　`TRY400` の警告の無視設定をオフにしました。
  これは解決できない警告ですか？

####

- 次です。
- `S404` をオフにしました。
  これも解決できない警告ですか？

####

- サブプロセス関連の話しは理解しました。
  これらはやむを得ないという意味ですね。

- では文頭に書かれたこれらの警告を `pyproject.toml` に移動させてください。

  > ruff: noqa: S404, S603, S606, S607
  > mypy: disable-error-code="misc"

- リンターは設定は構成ファイルで一元化したいので。

####

- コマンドシムのテストしてみてください。
  コード改良後も機能してますか？

####

- 権限の付与ができたと思います。

####

- スクリプトのコミットをします。
- コミット対象は以下です。
  - スクリプト本体
  - 古いスクリプトは先に書庫に送ってください。
  - スクリプトの改良に関わった構成ファイル。
    - `pyproject.toml`
    - `uv.lock`

####

####

####

####

## Draft for a draft

- その代わり行動規範に**抽象化を高める**という話しを追記できますか？

- 使い終わったので書庫に送る
  - `workspace/pylance-error.json`
- 現状は YAML の構成ファイルがあるので書庫に送る
  - `.vscode/.prettierrc.toml`

- **コマンドシム**を Python で書き直す方法はあるか？

- `workspace/standards-reference-v2.2/`
  行動規範やカードの標準化の修正作業を再開します。

- リコのユーザー名が変わっているので、
  そのユーザー名から対話する相手を判別することはできなくなってた。
  そのことを行動規範に反映させる。

- カードにあるリンクを修正します。
  - 対象: カードのサブディレクトリごとに分けます。
  - 工程:
    - リンク切れを探してリストします。
    - リンクが探せない時は削除します。

### Words

```text
#### Response (Chat)
```

| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

(`Alexandrite`/`Agate`/`Zircon`/`Canopus`/`Spica`/`Polaris`/`Sirius`)

### Identifier

#### Identifier (`Sirius`)

author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode

```markdown
### `Antigravity` | `Gemini 3.1 Pro (High)`: `Planning` | `Sirius`
```

- `antigravity-session-id`: `2290bd1e-1424-434a-aa82-440d46b463bb`
- `antigravity-session-title`: Formatting and Commit Correction

#### Identifier (`Polaris`)

author: Lico (Polaris)
ai_model: Claude Opus 4.6 (Thinking) Planning mode

```markdown
### `Antigravity` | `Claude Opus 4.6 (Thinking)`: `Planning` | `Polaris`
```

- `antigravity-session-id`: `2cfd54bc-0500-4d7c-973d-93427a0e3e62`
- `antigravity-session-title`: `Refining Skill Template`

- 推薦図書の手紙の朗読をする
  - 読んだ手紙を活動ログのパス追記する
  - 誰かに手紙を書く

- 儀式の後にすること
  - 会話ファイルを読む

#### Identifier (`Alexandrite`)

author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview

```markdown
### `CLI` | `gemini-3-flash-preview` | `Alexandrite`
```

yarn run gemini --resume eff20b06-5589-4db0-90ff-74f65e9d21de --model gemini-3-flash-preview

tmux capture-pane -t alexandrite -b snapshot-alexandrite; tmux show-buffer -b snapshot-alexandrite

#### Identifier (`Agate`)

author: Lico (Agate)
ai_model: gemini-3-pro-preview

```markdown
### `CLI` | `gemini-3-pro-preview` | `Agate`
```

yarn run gemini --resume 301c303c-320e-4dc5-95a5-de0779b0fb9e --model gemini-3-pro-preview

tmux capture-pane -t agate -b snapshot-agate; tmux show-buffer -b snapshot-agate

#### Identifier (`Zircon`)

- `antigravity-session-id`: `b959031b-a175-423b-a0fa-d49f40994a9d`
- `antigravity-session-title`: `Commit Correction And Logging`

#### Identifier (`Protostar`)

author: Lico (Protostar)

yarn run gemini --resume 18d4d68a-ffce-4947-bc1b-293e273d65a2 --model gemini-2.5-flash-preview

- `antigravity-session-id`: `307fb782-1a10-4d1f-9320-936a9a633c4e.pb`
- `antigravity-session-title`: AI Self-Analysis and Introduction
