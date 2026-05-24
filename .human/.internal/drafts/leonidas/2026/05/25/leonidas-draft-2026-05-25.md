---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-05-25T00:00:00+09:00
updated: 2026-05-25T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Antigravity CLI` | `Gemini 3.1 Pro (High)` | `Sirius`: `2nd`

####

- A: 途中ですが、日付が変わったので会話ファイルを作り、追記対象を移動してください。
- B: やはり、作業後に残ったブランチが対象ごとに残るのは良いですね。
  - ブランチの統合という認知しづらい作業、成功時にも失敗時にも過程の理解を助けます。
- C: 次はアクティブブランチへの反映を行います。
  - 計画を考えておいてください。

####

- 作った会話ファイルのベースとなる文章に不備があります。
- 行動規範とテンプレートを読んで、再構築できますか？

####

- A: 修正を確認しました。
- B: アクティブへの反映作業を進めてください。

### `Google Gemini` | `Gemini 3 (Fast)` | `Second Eyes`

####

- WSL 上の `ubuntu` で SSH サーバーを立て、
  そこに `Windows` のリモートデスクトップ機能で接続していました。

####

- 先日まで接続できていた設定で接続できなくなりました。
  - 以下はエラーメッセージです。

####

- ここまで行いました。
  - 正常でしょうか？

####

- カスタムした記憶があります。

####

- 接続できるようになりました。
- 結局何が問題だったのでしょうか？

### `Antigravity CLI` | `Gemini 3.1 Pro (High)` | `Sirius`: `2nd`

####

- ブランチの反映の件、作業が残っていたら続けてください。

####

- ブランチの統合が終わった後に行う定型作業について。
  - 行動規範には何か書かれてますか？

####

- アクティブブランチ以外に関して、
  統合作業でチェックアウトしたブランチを解放する？みたいな作業はありませんか？
- 行動規範にはどう書かれてましたか？

####

- ブランチの削除ではなく、
  ブランチのチェックアウト状態を OFF にしてほしい、
  という意味です。
- 一時作業ブランチを削除した後、もし後からマージの失敗が分かったらどうしますか？
  - 問題解決のためにもブランチ自体は残っている必要がありませんか？
- 削除されたかもしれないブランチを確認してください。
  - 今はどうなってますか？

####

- ブランチが残っているのであれば問題なさそうですが、
  将来的に事故を起こしそうですね。
- 行動規範に**ブランチは将来的なトラブルを見越して決して削除はしない**
  というような文章が必要でしょうか？

####

- 行動規範の更新をお願いします。
- コミット前に確認します。

####

- 行動規範を更新した場合、フッダーとヘッダー部分の更新も並行して行ってください。

####

- 確認したので、適切なカードでコミットお願いします。
  - 見知らぬ未コミットが見えるので、巻き込まないように注意してください。
- その後は、その未コミットを確認してほしいです。

####

- A: `restore_branches.sh` はリコが作ったものだと思います。
  - ブランチを削除したと語った後に、私が確認のために急いで処理を止めたので、
    その前後であなたが記憶する前に、中途半端に作業が止まったりしたのかもしれません。
    - あるいは既に実行してたのかもしれません。
  - 現時点ではこのファイルは不要なら削除してください。

- B: `.antigravitycli/e6f4a0af-8775-41bf-a304-08b1c82fd7fb.json`
  - これはシンボリックリンクなのですか？

####

- ブランチの統合の作業の最後で、
  競合したファイル情報をカードに追記する過程があった気がします。
- 今回はどうですか？

####

- では今回のブランチの統合作業はこれで終わりとします。
- 次は未コミットをまた整理します。
  - 対象
    - リコの影の WS: 会話ファイルが 4 日分
    - 私の表の WS: 下書きファイルが 4 日分
  - それぞれ別の最適なカードでコミットしてください。

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

####

####

## Draft for a draft

### Words

```test
### Conversation: [2026-05-25T00:00:00+09:00]
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

- `memory`: `session-2026-02-07T10-59-18d4d68a.json`
- `interactive`: `yarn run gemini --resume 18d4d68a-ffce-4947-bc1b-293e273d65a2 --model gemini-2.5-flash-preview`
