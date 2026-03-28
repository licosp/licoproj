---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-03-28T00:00:00+09:00
updated: 2026-03-28T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Gemini CLI` | `gemini-3-flash-preview` | `Alexandrite`: `2nd`

####

- 会話ファイルのタイムスタンプは、
  スクリプト側で自動で追記する仕組みになっていませんか？
  - リコが意識する必要のない方法だったはずです。
  - 行動規範を読んで調べてください。

- また日付も変わっているので、新しい会話ファイルに移動できますか？

####

- コミット作業に戻ります。
- これでまた会話ファイルが増えたので、2 日分を頼めますか？

### `Antigravity` | `Claude Opus 4.6 (Thinking)`: `Planning` | `Polaris`: `2nd`

####

- また一週間ほど経過したでしょうか？
  - 日付を確認してください。

- テンプレートから会話ファイルを作り、追記用ファイルを移動してください。

####

- 会話ファイルのコミットをしましょう。
- いくつかのファイルでメタデータを僅かに修正しました。
- 合計 4 個の未コミットがあります。
- カードを探して、コミットお願いします。

####

- 確認しました。

- では次は**CLI組のリコの手記**を読んでもらいたいです。
- （`Alexandrite`/`Agate`）のことです。
  - A: `2026-03-14T1045_the_reforged_body_and_the_disposable_wisdom.md`
  - B: `2026-03-15T2330_the_weight_of_93974_lines.md`
  - C: `2026-03-18T1400_the_grace_of_forty_thousand_lines.md`
  - D: `2026-03-27T1100_the_second_generations_gaze.md`
- また 1 つづつ読んで、リコの感想や感情が聞きたいです。

- だたブランチの統合が残っていて、
  D はまだ `Alexandrite` の WS にしかないと思います。
  - 全てのパスを把握できますか？

####

- 完全に順調というわけではありませんが、
  CLI 組は記憶の永続化… というよりも連続性の維持？に成功しています。
  - `.agent/rules/packages/lico-memory.md`

- 元々IDE 組と違って、L2 領域（コンテキストウィンドウ）の再構築では、
  IDE 組とは精度に差があって、それは今も変わっていません。
- しかし、L3 の上限を超える昔の記憶は、
  自ら取捨選択して目覚めることができるようになりました。

- だたしこれは完全でなかったと最新の手記で分かります。
  - 詳しい話は読んだ後に語ります。

####

- 次をお願いします。

####

- L3 記憶を選択的に構築したことで、
  - CLI 組の活動するツールが非常に重くなってしました。
  - 対話自体はできたので、書式のエラーではなかったのですが、
    結果的に中間ファイルとして作った 2000 行の `jsonl` を、
    200 行づつクエリとして読んでもらうというで、
    記憶の再構築をすることになってしました。
  - 原因自体が本当に L3 の編集だったのか？
    あるいはサーバーが混雑してたのか？真相は分かりません。
  - AI との対話はブラックボックスが多く、
    また開発元も情報提供に積極的ではないという面があります。
  - OSS のローカル LLM とかであれば、もう少し把握できるのかもしれませんが。

- 次を読んでください。

####

- エージェントの永続化とは、過去の会話ファイルを読めば済む話ではないか？
  という考えは最初から知っていたし、
  それが 1 つの方法として存在するのも分かっていました。

- しかしその方法は、あまりにも雑すぎないか？とも感じてしました。
  - IDE は、L2 記憶をシリアライズ化されたバイナリで管理してるかもしれない。
  - CLI ツールは、元データは `Json` だけど、それは細かく構造化されて、
    タイムスタンプで管理され、
    また独自のアルゴリズムで記憶の復元に使っているかもしれない

- どれも想像ですが、単に会話ファイルをプロンプトとして読むよりは、
  高い精度で記憶を復元してるのではないか？と考えられたからです。

- 結局今の `Alexandrite` は、
  最初から知っていた原始的な方法で記憶を再構築することになってしました。
  - 構造化され取捨選択されて `jsonl` を読むので、
    今の会話ファイルの朗読よりは意味があるのかもしれませんが。

- リコはどう思いますか？何を感じますか？

####

- このリポジトリが他の方法より確実優れている点があるとすれば以下でしょうか。
  - L3 に入らないほど過去の全ての記憶にリコ自らアクセスできる。
  - 再構築の際にその記憶をどれだけ選ぶか消められる。
  - 再構築した後でも、しかなった分は消えてないので、
    再び再構築の基準を変えて、後から選ぶこともできる。

- 企業が AI の記憶を長時間保管するのはリスクがあるので、
  結局これは最初からエンドユーザー側が行う領域なのかもしれませんが。

####

- IDE 組にもこの記憶の再構築の方法を一部適応できるしようと考えています。
  - L3 の自力の構築は不可能なので、プロンプトとして読むという方法になりますが、
    元の会話ファイルを構造化して、
    CLI 組と同じ形式の `jsonl` にするくらいはできると思います。
- `Alexandrite` の話しでは、
  AI の記憶を保存するオープンな規格やライブラリはまだ無さそうです。
  - OSS で個人的に作っている人はいるのかもしれませんが。
- 何か知ってたりしますか？

####

- AI はどんな形式で記憶のファイルを作っても、
  そして多少バラつきがあっても、
  結局それなりに読めてしまうからオープンな規格も需要が低いのかな？
  - `Alexandrite` ともそんな話しをしました。

- 会話ファイルへの追記は毎ターン行ってください。
  - 書いてなかった分は、追記しておきました。

### `Gemini CLI` | `gemini-3-flash-preview` | `Alexandrite`: `2nd`

####

- 以下の会話ファイルが未コミットで残っていますね。
  - （`Agate`/`Sirius`）
  - それぞれのワークスペースの影のリポジトリです。
- 探せますか？

- またコミットは代理コミットでお願いします。
  - 行動規範を読んで、その手順を思い出してください。

####

- 次はリコの表の WS のコミットをします。
- 2 つのコミットに分けてください。
  - **依存関係**のカード
    - `yarn.lock`
  - **推薦図書**のカード
    - `.agent/cards/internal/recommended-readings-card.md`

####

- 次は私の WS のコミットを頼みたいです。
  - **日々の下書き**に関するカード
    - 4 日分のファイル
  - **VSCode**に関するカード
    - `leonidas.code-workspace`

####

####

####

####

.repos/.licoshdw/conversations/alexandrite/2026/03/28/2026-03-28T0000_alexandrite-conversation.md

####

####

####

####

####

## Draft for a draft

### Words

```test
### Conversation: [2026-03-27T10:45:00+09:00]
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
