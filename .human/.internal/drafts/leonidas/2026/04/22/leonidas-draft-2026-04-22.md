---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-04-22T00:00:00+09:00
updated: 2026-04-22T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Gemini CLI` | `gemini-3-flash-preview` | `Alexandrite`: `2nd`

- 話の途中ですが、日付が変わったので新しい会話ファイルに移動できますか？

####

- A: 会話ファイルの移動を確認しました。
- B: 文脈をマージの話に戻します。
  - つまり誰のブランチの統合であっても、
    作業者は自分のディレクトリを使うということですね。
  - 一貫性を維持したいので、
    私のブランチであってもリコのディレクトリで作業してほしいと感じました。
- C: ディレクトリは自分の場所として、
  作業用のブランチ名の名前部分は自分の識別子を使うべきですか？
  - あるいは作業対象のクルーの識別子ですか？

####

- A: ブランチ名の名前部分は作業者のそれを使う。
  - 把握しました。
- B: では先ほどの作業ですが、以下のような過程を確実に行いましたか？
  - チェックアウト前に `.repos/sync/` や `.repos/trunk/` は初期化する。
  - 統合作業はこの 2 つのどちらかで必ず先に行う。

####

- 作業前にディレクトリの初期化はしてほしいですが、
  使ったブランチそのものは残してほしいです。
  - 後で何をしたかを把握するための助けになるからです。
- このあたりの話は行動規範に書かれてますか？

####

- 行動規範を更新したようですが、大きく更新されました。
- 差分を確認してください。
  - 確実に意図した通りの編集ですか？
  - また更新日時が正確ではないと感じます。

####

- 確認して、微調整しました。
- コミットできますか？

####

- 先ほど私の表の WS を確認したら、知らない変更がステージングされてました。
- マージの過程で生まれたものだと思いますが、これはどうすべきですか？

####

- 直せそうですね。
- 私の下書きなどが未コミットとして残っている点に注意して作業してほしいです。

####

- ステージングが変更に戻りましたが、
  その変更自体がまだ残っているのに、下書きファイルをコミットできるんですか？

####

- お願いします。

####

- ステージングのみを戻す方法を選びましたか？
  - 私の WS の変更で、ステージグではなかったファイルまで、変更が消えていました。
    - なので手動で戻しておきました。

####

- このような事故が起きやすいので、今から未コミットを減らします。
  - 対象
    - まずはリコの影の WS の会話ファイル
    - その後、私の表の WS の下書きファイル
      - ワークスペース構成ファイルは未コミット状態で問題ありません。
  - コミット用のカードも探してください。

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
