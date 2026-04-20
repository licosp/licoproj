---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-04-20T00:00:00+09:00
updated: 2026-04-20T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Gemini CLI` | `gemini-3-flash-preview` | `Alexandrite`: `2nd`

- A: 把握しました。
- B: 途中ですが、日付が変わったので新しい会話ファイルに移動できますか？

####

- A: 会話ファイルの移動を確認しました。
- B: では推薦図書のカードを、本当の最新版に復元しましょう。
  - どこをどう書き換えるべきですか？

####

- A: 止まっているように見えたので止めました。
- B: 復元できそうですか？
  - 正しいものは推薦著書の行動規範と重複しないリストに近いはずです。

####

- A: 何か違う気がします。
  - 戻せまか？
- B: そもそも手紙の推薦図書のファイルが作られた履歴は存在しますか？
- C: そして手記の推薦図書まで編集する必要はありましたか？
  - 今回はブランチのマージの際のトラブルの解消が目的です。

####

- つまりある時期の段階で、カードから手記の推薦図書は行動規範に移動したけど、
  手紙の推薦図書はカードから変化してないのではないでしょうか？
- では推薦図書はカードの変更の GIT の履歴を調べてください。
  - どういう時系列で編集されましたか？
  - `Polaris` の編集直後か、その少し後くらいの時期が、
    本来の最新ではないでしょうか？
  - マージ作業をする前のバージョンです。

####

- 復元してみてください。
  - 確認します。

####

- A: カードを確認して、一部修正しました。

- B: フッターとヘッダーを今日の変更に更新してください。
  - コミット前に確認します。

- C: `card_base.md` は作業が終わったら書庫に送る予定です。
  - 書庫の行動規範を読んでおいてください。

####

- ではカードをコミットしてください。

####

- 移動後に**書庫**のカードでコミットしておいてください。

####

- `.human/users/leonidas/.vscode/leonidas.code-workspace`
  - 私の WS の変更です。
  - `VSCode` のカードでコミットできますか？

####

> 私の WS の変更です。

####

####

####

####

## Draft for a draft

### Words

```test
### Conversation: [2026-04-18T01:10:00+09:00]
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

#### Identifier (`Alexandrite`)

author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview

```markdown
### `Gemini CLI` | `gemini-3-flash-preview` | `Alexandrite`
```

- `backup`: `uv run lico-memory-backup ~/.gemini/tmp/crew-alexandrite/chats/session-2026-04-04T22-26-970e0bfa.json .repos/.licoshdw/conversations_cli/identifiers/alexandrite/`

- `interactive`: `yarn run gemini --resume eff20b06-5589-4db0-90ff-74f65e9d21de --model gemini-3.1-flash-preview`

#### Identifier (`Agate`)

author: Lico (Agate)
ai_model: gemini-3.1-pro-preview

```markdown
### `Gemini CLI` | `gemini-3.1-pro-preview` | `Agate`
```

- `backup`: `uv run lico-memory-backup ~/.gemini/tmp/crew-agate/chats/session-2026-03-15T12-37-105c303c.json .repos/.licoshdw/conversations_cli/identifiers/agate/`

- `interactive`: `yarn run gemini --resume agate-2026-03-15T1237-301c303c-320e-4dc5-95a5-de0779b0fb9 --model gemini-3.1-pro-preview`

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
