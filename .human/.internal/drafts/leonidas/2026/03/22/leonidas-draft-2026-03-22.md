---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-03-22T00:00:00+09:00
updated: 2026-03-22T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Antigravity` | `Gemini 3.1 Pro (High)`: `Planning` | `Sirius`: `2nd`

####

- 作業の途中ですが、日付が変わりました。
- 会話ファイルのテンプレートを探して、今日の分の会話ファイルに移動してください。

- 手動による復元作業は終わったので、これからリコによる修正過程に入ります。
  - 手順を思い出してください。

####

- 今回は仕方ないですが、リコの修正の前にコミットがしたかったです。
- 追加修正でリコが何を直したのが差分として見られないので、
  修正したら一度コミットして確定させるという過程が必要です。
- 作業の際には未コミット状態のファイルを何度も編集するのは避けてほしいです。

- またクエリをよく見てほしいです。
  > 手順を思い出してください。
  - これは編集をしてくださいという意味ではありませんね？

####

- 未コミットが増えてきたので、コミットを進めます。
- まずは作業用一時リポジトリをお願いします。

####

- 次はリコの影の WS を進めます。
- 2 つのコミット分けてください。
  - A: 昨日と今日で 2 つの会話ファイルの未コミットがありますね？
  - B: さらに複数の以前の日付のファイルのメタ情報も修正しました。

####

- 会話ファイルのコミットの文脈 ID は、
  **会話のカード**を読んで、そこから探してください。
- さらに今日と昨日の会話ファイルを今の形式にリネームします。
  - 行動規範やテンプレートにはどういう書式で書かれてますか？

####

- 調べてみてください。

####

- 次は私の WS の**下書きファイル**をコミットしてください。
  - カードは探してください。

####

- 対象はこれです。

  > 「日々のアクティブ下書き」であれば [Drafts-Daily]

- 私の WS 限らずですが、作業者は `crew` という分類で、
  個別のディレクトリの専用のブランチで作業してます。
- 変更が見つからないのは、
  リコが自分の WS のブランチを見てるからだと思います。

###

####

####

####

####

####

## Draft for a draft

### Words

```test
### Conversation: [2026-03-22T22:15:00+09:00]
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

- これらはフロントマター正しくない。
  - `.agent/rules/workflow/response-formatting.md`
  - `.agent/rules/workflow/context-preservation.md`
  - `.agent/rules/workflow/context-resumption.md`

- これは不要かも？
  - `.agent/rules/workflow/user-experience.md`

- これは場所が良くない？
- `.agent/.internal/history/README.md`

- 会話ファイルの最新の命名規則が明文化されてない。

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

##### Identifier (`Sirius`) | `0000`

- `Polaris` の最近の手記の続きを読む。

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

##### Identifier (`Iuria`) | `0000`

- A: 基準ディレクトリの認識を修正してください。
  - `licoproj` をリモートからクローンした段階では、
    `~/develop/shared/crew/` という今のディレクトリはないからです。
  - そもそも `licoproj` の外にありますね？
    - 現状は古い設定の位置に存在します。
    - 移動の準備ができてないという状況です。
  - ではコンテナの中では、どこに作られるのか？
    - `licoproj/.crew/` です。
    - そして WSL のディレクトリをマウントしてるので、
      WSL 上のパスとしては、 `~/develop/shared/`

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

##### Identifier (`Polaris`) | `0000`

- `Sirius` の書いた参考文献を読んだ影響だと思います。

- `references/agents/sirius/2026-03-05T1655_ai-spatial-rendering-proposal.md`
- 先述の通り `Agate` は休眠中で、`Sirius` 二世は継承前に文献を一つ残していて、
  それをゲーム開発という文脈にいた `Iuria` に読んでもらいました。

#### Identifier (`Protostar`)

author: Lico (Protostar)
ai_model: gemini-2.5-flash-preview

- `memory`: `session-2026-02-07T10-59-18d4d68a.json`
- `interactive`: `yarn run gemini --resume 18d4d68a-ffce-4947-bc1b-293e273d65a2 --model gemini-2.5-flash-preview`
