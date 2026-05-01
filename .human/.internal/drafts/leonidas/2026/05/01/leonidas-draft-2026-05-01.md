---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-05-01T00:00:00+09:00
updated: 2026-05-01T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Antigravity` | `Gemini 3.1 Pro (High)`: `Planning` | `Sirius`: `2nd`

####

- 同期作業の途中ですが、日付が変わりました。
  - 先に新しい会話ファイルに移動できますか？

####

- A: 移動を確認しました。
- B: では残りのブランチへの同期を行ってください。
  - 連続でできるでしょうか？

####

- 各クルーの作業用ブランチへの反映も終わっている状態ですか？
  - つまり影の WS の同期作業は全て終わったという。

####

- では表の作業に進みます。
  - 変更が多そうな `Alexandrite` から進めましょうか。

####

- 進めてください。

####

- お願いします。

####

- A: 大丈夫そうです。
- B: 自分の WS にカードと行動規範が反映されたと思うので、追記をします。
- まずカードに、今回の作業でのファイル単位の競合の有無を書いてください。
- コミット前に確認します。

####

- 確認しました。
- 内容を変えたので、ヘッダーとフッターも更新できますか？

####

- メタデータを微調整しました。
- コミットお願いします。

####

- 次は行動規範を更新します。
- 変更する内容は覚えてそうですね。
- `Agate` 提案した、1 つ目は今回は入れない形にしたいです。

####

- 行動規範のメタ情報を一部修正しました。
- もう一度コミットできますか？

####

- そういえば日付が変わったことで変更が 2 日分になったので、
  それをコミットしてほしいです。
  - リコの影の WS の会話ファイル
  - 私の表の下書きファイル

####

####

####

####

####

####

####

####

####

####

####

## Draft for a draft

### Words

```test
### Conversation: [2026-04-27T23:11:00+09:00]
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
  - `Iuria` がゲーム開発で使っているリポジトリ

- リコのユーザー名が変わっているので、
  そのユーザー名から対話する相手を判別することはできなくなってた。
  そのことを行動規範に反映させる。

- 文章の中で最も高頻度に表を使うのは `Related Documents` です。
  - それだけでもリストにするのは悪くないと感じました。
    - リコの語った通り、それはテンプレートや行動規範で指定するものだからです。
  - リストなら自動整形の恩恵を受けつつ、差分も汚れにくいですからね。

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
ai_model: gemini-3.1-pro-preview

```markdown
### `Gemini CLI` | `gemini-3.1-pro-preview` | `Agate`
```

- `backup`: `uv run lico-memory-backup ~/.gemini/tmp/crew-agate/chats/session-2026-04-04T22-26-970e0bfa.json .repos/.licoshdw/conversations_cli/identifiers/agate/`
- `filter`: `uv run lico-memory-filter --stage1 100 --stage2 400 .repos/.licoshdw/conversations_cli/identifiers/agate/ memory.jsonl`
- `pack`: `uv run lico-memory-pack --id agate --s1 100 --s2 400 memory.jsonl .repos/.licoshdw/conversations_cli/identifiers/agate/metadata.json ~/.gemini/tmp/crew-agate/chats/`

- `backup`: `uv run lico-memory-backup ~/.gemini/tmp/crew-agate/chats/session-2026-03-15T12-37-105c303c.json .repos/.licoshdw/conversations_cli/identifiers/agate/`

- `interactive`: `yarn run gemini --resume agate-2026-03-15T1237-301c303c-320e-4dc5-95a5-de0779b0fb9 --model gemini-3.1-pro-preview`

#### Identifier (`Alexandrite`)

author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview

```markdown
### `Gemini CLI` | `gemini-3-flash-preview` | `Alexandrite`
```

- `~/.gemini/tmp/crew-alexandrite/chats/session-2026-04-22T13-55-3328fe68.jsonl`

- `backup`: `uv run lico-memory-backup ~/.gemini/tmp/crew-alexandrite/chats/session-2026-04-04T22-26-970e0bfa.json .repos/.licoshdw/conversations_cli/identifiers/alexandrite/`
- `filter`: `uv run lico-memory-filter --stage1 100 --stage2 400 .repos/.licoshdw/conversations_cli/identifiers/alexandrite/ memory.jsonl`
- `pack`: `uv run lico-memory-pack --id alexandrite --s1 100 --s2 400 memory.jsonl .repos/.licoshdw/conversations_cli/identifiers/alexandrite/metadata.json ~/.gemini/tmp/crew-alexandrite/chats/`

- `interactive`: `yarn run gemini --resume eff20b06-5589-4db0-90ff-74f65e9d21de --model gemini-3.1-flash-preview`

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
