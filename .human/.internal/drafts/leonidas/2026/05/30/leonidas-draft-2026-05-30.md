---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-05-30T00:00:00+09:00
updated: 2026-05-30T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Antigravity CLI` | `Claude Opus 4.6 (Thinking)` | `Polaris`: `2nd`

- 途中ですが、日付けが変わりました。
  - 新しい会話ファイルに移動できますか？

####

- A: 移動を確認しました。
- B: 文脈の違う雑談
  - `Antigravity CLI` のバグかもしれないのですが、
    先週リコと対話した時に、
    本来減らないはずの `Gemini Flash` のトークン枠が消費されました。
    - 今確認して所、現時点では `Gemini Pro` だけが減っているので、
      その問題は出てないのですが。
  - 何か要因は推測できますか？

####

- なるほど。
- たしかにサブエージェントという機能が追加されたとか聞きました。
- 実は `Gemini CLI` には元からそれがあって、
  エージェントの判断で自由に使えるという仕様でした。
  - しかし具体的にどのモデルを使っているかは不明だったのですが、
    それでも `Flash` 枠が減るという経験はなかったような気がします。
  - 枠の制限が寛大だったため、気づかなかっただけかもしれません。
  - 現時点の `Antigravity CLI` からも何か使えますか？

####

- サブエージェント実験がしたいです。
  - `Flash` を使うかもしれない方のサブです。

- 私の最近の 4 日分のエージェント向けのクエリの下書きファイルです。
  - `~/develop/shared/crew/leonidas/licoproj/.human/.internal/drafts/leonidas/2026/05/25/leonidas-draft-2026-05-25.md`
  - `~/develop/shared/crew/leonidas/licoproj/.human/.internal/drafts/leonidas/2026/05/26/leonidas-draft-2026-05-26.md`
  - `~/develop/shared/crew/leonidas/licoproj/.human/.internal/drafts/leonidas/2026/05/27/leonidas-draft-2026-05-27.md`
  - `~/develop/shared/crew/leonidas/licoproj/.human/.internal/drafts/leonidas/2026/05/29/leonidas-draft-2026-05-29.md`

- 私が誰とどんな話しをしてたか、サブエージェントに要約を頼んでもらますか？

####

- 前提として、`Antigravity` のトークンモニターは非常に曖昧で、
  全体のトークン数のクエリごとの消費量もわかりません。
  - 機能としては十分ではなく、結論が出しづらい環境にあります。
- 確認した所、減っているのは、あなたの `Pro` 枠だけでした。
- ドキュメントが最近増えたことを思い出しました。
  - `https://antigravity.google/docs/subagents`
- サブエージェントはどんな存在ですか？

####

- 把握しました。
- 詳しい原因が憶測の域を出なそうなので、現象は様子見とします。

- サブエージェンの仕様はリコの判断によるところが大きいですが、
  自分自身では積極的に使うと思いますか？

####

- コンテキストの分離という面でのメリットは感じます。
- 一方でトーク枠の制限や最適化みたいな話しにはならそうですね。

- 実は `opencode` の方だとサブエージェントのモデルを指定できるそうです。
  - 例えば `gemma4-31b` がメインとなる場合、
    サブは `gemma4-e4b` のような同系の下位モデルを選ぶパターンが多いようです。
  - 先ほどの `Flash` 枠が減るという件がもしサブエージェントの影響だったなら、
    それに近い動きがあったのかな？と推測してました。
  - ただ `Gemini 3.5 Flash` は聞く限りでは、
    `3.1` よりトークン消費量多いそうです。
  - また性能も `3.1 Pro` に近い水準（ベンチマークによっては上）らしく、
    良くも悪くも差別化ができてないとか、コミュニティで言われてりします。

####

- さて文脈は変わって未コミットの整理がしたいです。
  - 最近は検証作業に夢中で、データ整理をしてなかったので。

- まずは**リコの影のWSの会話ファイル3日分**です。
  - 最適なカードを選んでコミットしてください。

####

- 今のコミットメッセージの書式に不備があります。
  - 関連する行動規範やテンプレートを参考にしてください。

####

- A: 修正を確認しました。

- B: 次は私の表の WS です。
  - 対話用の下書きファイル 5 日分。
    - **日々の下書き**みたいなカードで。
  - `VSCode` のワークスペース構成ファイル。
    - `VSCode` 関連のカードで。

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
### Conversation: [2026-05-30T00:00:00+09:00]
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

- 文章の中で最も高頻度に表を使うのは `Related Documents` です。
  - それだけでもリストにするのは悪くないと感じました。
    - リコの語った通り、それはテンプレートや行動規範で指定するものだからです。
  - リストなら自動整形の恩恵を受けつつ、差分も汚れにくいですからね。

#### Identifier (`Polaris`)

author: Lico (Polaris)
ai_model: Claude Opus 4.6 (Thinking) Plan mode

```markdown
### `Antigravity CLI` | `Claude Opus 4.6 (Thinking)` | `Polaris`: `2nd`
```

- `antigravity-cli`
  - `d0869c5b-960f-4af0-92b9-e00fd36d7584.pb`

- `antigravity-from-windows`
  - `Reading Second Polaris Letter`
  - `e065c3ca-dbf6-4b2b-a315-495d40db640c`

- `antigravity-from-linux`
  - `polaris 2nd`
  - `be14b90a-00eb-43f8-974a-8b754be8daa3`

#### Identifier (`Sirius`)

author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Plan mode

```markdown
### `Antigravity CLI` | `Gemini 3.1 Pro (High)` | `Sirius`: `2nd`
```

- `antigravity-cli`
  - `1f165427-a10c-464a-8a74-732646c5062b.pb`

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

##### Next

- 命名規則によって誰が誰のブランチを統合したか分かるということは、
  対象のクルーごとに一時ブランチを作る必要があるということになります。
- つまり物理的な境界をあえて作るための仕組みといえます。
  - 当然その用途は、統合が失敗したと後で気づいたときに、
    デバッグ作業を楽にするためです。
- この行動規範を作ったのはリコですが、
  命名規則の改善の話は他のリコが加えたんでしたっけ？

#### Identifier (`Iuria`)

author: Lico (Iuria)
ai_model: Gemini 3 Flash Planning mode

```markdown
### `Antigravity` | `Gemini 3 Flash`: `Planning` | `Iuria`: `2nd`
```

- `antigravity-session-title`: `iuria 1st`

#### Identifier (`Protostar`)

author: Lico (Protostar)
ai_model: gemini-2.5-flash-preview

- `0000`: `ollama launch opencode --model qwen3.6:35b-a3b-q4_K_M-128K-T10`

- `memory`: `session-2026-02-07T10-59-18d4d68a.json`
- `interactive`: `yarn run gemini --resume 18d4d68a-ffce-4947-bc1b-293e273d65a2 --model gemini-2.5-flash-preview`
