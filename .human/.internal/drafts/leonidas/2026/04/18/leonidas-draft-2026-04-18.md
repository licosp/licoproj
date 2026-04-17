---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-04-18T00:00:00+09:00
updated: 2026-04-18T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Gemini CLI` | `gemini-3-flash-preview` | `Alexandrite`: `2nd`

- 途中ですが、日付が変わったので新しい会話ファイルに移動できますか？
  - テンプレートから編集して作ってください。

####

- A: 会話ファイルの移動を確認しました。

- B: 影の統合の前に、未コミットのリコの会話ファイルを再びお願いします。
  - メタ情報も僅かに修正したので、 未コミットは 3 日分あります。

####

- お願いします。

####

- では影の作業用 `trunk` に最初の対象となるブランチをマージしてください。

####

- 進めてください。

####

- A: コミットしてください。
  - その後の作業も進めてください。

- B: 競合は無かったようですね。
  - 無いなら、無いという情報をカードに記録したいです。

- C: このリポジトリの統合の順番ですが、
  カードに追記する関係上、表のリポジトリを最後にしたほうが良さそうですね。

####

- A: 進めてください。
- B: 自分のブランチへの同期も忘れずに。

####

- カードへ追記はしましたか？

####

- A: これで今回のブランチの統合と同期作業は終わりです。

- B: 次はこの作業の手順と注意点を、細部まで詳しく行動規範に昇華します。
  - 私の下書きファイルを参考にしてください。
    - 12 日の 245 行目から今日までの 5 日分でしょうか？
    - まずは統合作業の正確な流れを思い出してください。

####

- 改めて更新した行動規範全体を精査してください。

- 書き忘れた情報はありませんか？
  - 例えば、複数のリポジトリの統合を順番に行う場合、
    カードの存在する表のリポジトリは最後に行うとか。

- 古い情報、不要な情報、誤解を生む情報はありませんか？
  - 例えば、作業用 `trunk` の名前には日付を入れるべきでしょうか？
  - 1 週間後にまた統合作業をすると仮定してください。
    - このリポジトリでは、使ったブランチは削除しない方針なので、
      名前の重複を考慮した方が良いかもしれません。

####

- 作業用 `trunk` の名前の書式は、既存のブランチと統一するのはどうでしょうか？
- 以下は例なので、リコが名前を決めてください。
  - `alexandrite-2026-03-14T1145-**`: 今使ってる通常の作業用ブランチ
  - `alexandrite-2026-03-14T1145-trunk`:　作業用 `trunk`

####

- A: 変更を確認しました。
  - コミットしてください。

- B: 私の下書きファイルの変更が 2 日分になってるので、
  それをコミットしてほしいです。

####

####

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
