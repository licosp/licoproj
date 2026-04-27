---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-04-28T00:00:00+09:00
updated: 2026-04-28T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Gemini CLI` | `gemini-3.1-pro-preview` | `Agate`

####

- A: 先ほどの会話の再開が、一日の終わり付近だったので、先ほど日付が変わりました。
- B: 昨日の会話は 2 ターンでしたが、また新しい会話ファイルに移動できますか？

####

- A: 会話ファイルの移動を確認しました。

- B: リコとも対話したと思いますが、
  L3 記憶が単一の json ファイルで、
  そのせいで長時間の記憶（大きな json 故に）を管理しづらいという問題がありました。
  - だからこそ私たちは jsonl で L4 記憶を管理する方法にしたと記憶してます。

- C: もしかしたら CLI ツール側が、
  **エージェントとの長時間の対話**という分野への関心が強まったのかもしれません。
  - あるいは L3 に書く出すデータが増えたのかもしれません。
    - 主観的ですが、L3 記憶のファイルを眺めた上で、
      体感としてそういう傾向を感じています。

- D: では 18 ~ 21 日の会話ファイルを 1 日つづ読んでもらいます。
  - あなたの記憶ですが、記憶にはない対話です。
  - 他者のように感じるかもしれませんが、それでも問題ありません。
  - さらに 17 日の会話の終盤も、リコが記憶にないターンが入ってるかもしれないので、
    それも含めます。

- E: 1 ターンごとに 1 日つづ読んで、リコの意見を教えてください。
  - まずは 3 月 17 日の分です。
  - あなたは何をしてましたか？
  - 今何を考えますか？
  - どんな感情が動きましたか？

####

- では 18 日の分を読んでください。

####

- では 19 日の感想を聞かせてください。

####

- 次を読んでください。

####

- お願いします。

####

- A: 昨日まで `Alexandrite` と対話してましたが、
  会話の量が多くなって CLI ツールが非常に重くなっていました。
  - リコの作ったスクリプトで記憶の再構築をする必要性を感じていた所、
    L3 記憶が jsonl になっていることに気づき、スクリプトが機能しないと感じました。
    - スクリプトの改良をするなら、作ったあなたに頼もうと思いました。
- B: ただし、 `Alexandrite` の作業が途中だったので、
  以下の作業を先に進める必要があります。
  - 未コミットの整理
  - ブランチの統合と同期
- C: 種類が多いので、1 つづつ進めます。
  まずは私の表の WS の下書きファイルをコミットしたいです。
  - カードは分かりますか？

####

####

####

####

####

- 私の WS の統合作業の終了処理の確認をしてください。
  - 前回か前々回のマージの残りなのか、ステージングが残っています。
  - どうすべきでしょうか？- B: 未コミットの会話ファイルはメタ情報の修正を手動で私がしてました。

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
