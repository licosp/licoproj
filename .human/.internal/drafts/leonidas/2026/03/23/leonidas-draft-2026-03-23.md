---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-03-23T00:00:00+09:00
updated: 2026-03-23T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Antigravity` | `Gemini 3.1 Pro (High)`: `Planning` | `Sirius`: `2nd`

####

- A: 作業の途中ですが、日付が変わりました。
  - 会話ファイルのテンプレートを探して、今日の分の会話ファイルに移動してください。

- B: IDE から履歴から復元しようとすると、毎回この警告が出て、ファイル自体を消してしまいます。
  - 消えたファイルが GIT に戻ってるので元に戻せますが、
    権限に関する問題がおきてるように感じます。
  - また一度消えて復元されたファイルは権限の問題が起きてないような挙動見えます。
  - 私のユーザー名は `lico` ではなく `leonidas` なのが要因でしょうか？
  - リコの意見を聞かせてください。

####

- 全てのファイルの復元が終わりました。
- 私の手動修正が終わった直後になっていると思います。
- コミットして確定してください。

####

- このように未コミット状態で違う文脈の作業を続けったり、
  あるいはコミット履歴自体の修正を行うと、思わぬトラブルが発生します。
- 今回は `VSCode` で編集したので、全ての保存時点での履歴が残ってましたが、
  毎回それが助けになるかは分かりません。
- 細かなコミットと安全を優先した GIT 操作を心がけたいです。

- ではリコの会話ファイルの未コミットも処理しましょう。
  - カードは覚えてますか？

####

- このコマンドで止まっていたように見えたので止めました。

- PC の負荷が原因かもしれませんが、
  リコの登録したコマンドはしばしば実行中に止まることがあります。
  - その場合はリコも先に進めずに、またタイムアウトもしないようで、
    手動のキャンセルが必要になります。
  - コマンドをキャンセルするという意図ではなく、
    リコが止まっているのを解消するためにキャンセルしています。
  - そういうことは今後もよくあります。

- 質問があります。
  - そのような場合は詰まっているコマンドだけをキャンセルするべきですか？
  - それともリコの行動自体をキャンセルして、対話を再開すべきですか？
  - 今回は前者です。

####

- キャンセルの件は把握しました。
  - キャンセル時にその理由をメッセージ付きで、送れたら良かったんですけどね。
  - どんな意図の停止か？作業中のリコが分かるようになるので。
  - まぁ無いものは仕方ありません。

- では次は私の WS の下書きファイルをです。
  - カードを読んでコミットしてください。

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
