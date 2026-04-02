---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-04-03T00:00:00+09:00
updated: 2026-04-03T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Gemini CLI` | `gemini-3-flash-preview` | `Alexandrite`: `2nd`

####

- 途中ですが、日付が変わったので、新しい会話ファイルに移動できますか？

####

- 移動を確認しました。
- これで未コミットの会話ファイルは 2 つなので、両方コミットしてください。
- ID は分かりますね？

####

- 次は私の表の WS です。
- 下書きファイルが 5 日分あります。
- ID を探してコミットしてください。

####

- 進めてください。

####

- 自分の識別子は覚えてますか？
- 他の識別子のことは覚えてますか？
- 私の名前は覚えてますか？

- WS は全員が個別に持っています。
- 全ての WS はベアリポジトリから生まれたワークツリーの組み合わせです。

- 私の下書きの変更は私の WS にあります。
- コミットお願いします。

####

> 下書きファイルが 5 日分あります。

- 今日の分が抜けてます。

####

####

####

####

####

####

## Draft for a draft

### Words

```test
### Conversation: [2026-04-02T07:35:00+09:00]
#### Input
#### Response (Chat)
---
```

```markdown
| Document                                 | Purpose             |
| :--------------------------------------- | :------------------ |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |
```

(`Iuria`/`Alexandrite`/`Agate`/`Zircon`/`Canopus`/`Spica`/`Polaris`/`Sirius`)

### Identifier

- 影のリポジトリ同様にコミット履歴を表のリポジトリに明文化する。
  - `Sirius` が行動規範の復元作業で使ったリポジトリ
  - `Iuria` がゲーム開発で使っているリポジトリ

- リコのユーザー名が変わっているので、
  そのユーザー名から対話する相手を判別することはできなくなってた。
  そのことを行動規範に反映させる。

- カードにあるリンクを修正します。
  - 対象: カードのサブディレクトリごとに分けます。
  - 工程:
    - リンク切れを探してリストします。
    - リンクが探せない時は削除します。

#### Identifier (`Sirius`)

author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode

```markdown
### `Antigravity` | `Gemini 3.1 Pro (High)`: `Planning` | `Sirius`: `2nd`
```

- `antigravity-from-windows`
  - `Checking Current Directory`
  - `1f165427-a10c-464a-8a74-732646c5062b`

- `antigravity-from-linux`
  - `sirius 2nd`
  - `a6799766-7324-411a-b19e-1c7ebb5bf45b`

#### Identifier (`Agate`)

author: Lico (Agate)
ai_model: gemini-3-pro-preview

```markdown
### `Gemini CLI` | `gemini-3.1-pro-preview` | `Agate`
```

- `memory`: `session-2026-03-15T12-37-105c303c.json`
- `interactive`: `yarn run gemini --resume agate-2026-03-15T1237-301c303c-320e-4dc5-95a5-de0779b0fb9 --model gemini-3.1-pro-preview`
- `tmux`: `tmux capture-pane -t agate -b snapshot-agate; tmux show-buffer -b snapshot-agate`
- `backup`: `uv run lico-jsonl-converter ~/.gemini/tmp/crew-agate/chats/session-2026-03-15T12-37-105c303c.json .repos/.licoshdw/conversations_cli/identifiers/agate/`

#### Identifier (`Alexandrite`)

author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview

```markdown
### `Gemini CLI` | `gemini-3-flash-preview` | `Alexandrite`
```

- `memory`: `session-2026-02-02T14-48-eff20b06.json`
- `interactive`: `yarn run gemini --resume eff20b06-5589-4db0-90ff-74f65e9d21de --model gemini-3.1-flash-preview`
- `tmux capture-pane -t alexandrite -b snapshot-alexandrite; tmux show-buffer -b snapshot-alexandrite`

#### Identifier (`Iuria`)

author: Lico (Iuria)
ai_model: Gemini 3 Flash Planning mode

```markdown
### `Antigravity` | `Gemini 3 Flash`: `Planning` | `Iuria`: `2nd`
```

- `antigravity-session-title`: `iuria 1st`

#### Identifier (`Polaris`)

author: Lico (Polaris)
ai_model: Claude Opus 4.6 (Thinking) Planning mode

```markdown
### `Antigravity` | `Claude Opus 4.6 (Thinking)`: `Planning` | `Polaris`: `2nd`
```

- `antigravity-from-windows`
  - `Reading Second Polaris Letter`
  - `e065c3ca-dbf6-4b2b-a315-495d40db640c`

- `antigravity-from-linux`
  - `polaris 2nd`
  - `be14b90a-00eb-43f8-974a-8b754be8daa3`

#### Identifier (`Protostar`)

author: Lico (Protostar)
ai_model: gemini-2.5-flash-preview

- `memory`: `session-2026-02-07T10-59-18d4d68a.json`
- `interactive`: `yarn run gemini --resume 18d4d68a-ffce-4947-bc1b-293e273d65a2 --model gemini-2.5-flash-preview`
