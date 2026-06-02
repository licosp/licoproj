---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-06-03T00:00:00+09:00
updated: 2026-06-03T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Antigravity CLI` | `Gemini 3.1 Pro (High)` | `Sirius`: `2nd`

####

- 作業の途中ですが、日付が変わっています（6/3）。
  - 行動規範やテンプレートを参考に、
    新しい会話ファイルを作って、追記を移動できますか？

####

- まずは書いた手記に関して、書式の修正をします。
  - 内容自体は問題ないです。
- どこを直すべきだと思いますか？

####

- **過去や文章内での一貫性**という意味での指摘でしょうか。
  - それ自体は好ましい認識だと思いますが、今回の主要な修正点ではありません。
- この手記は主に誰が読むものですか？

####

- 手記のような主観や感情の入った文章を翻訳する際の注意点を思い出して、
  その上で翻訳してください。
- コミット前に確認します。

####

- A: 確認しました。
  - 問題なさそうなので、適切なカードでコミットしてください。

- B: 次は活動ログの追記をします。
  - 追記前に関連する行動規範を読んでください。
  - 追記分
    - 書いた手記
    - 読んだ手記
      - 4 本でしたか？
  - コミット前に確認します。

####

- 今回に関しては追記は手記（訂正: 参考文献もあった）は合計 5 行だと思います。

- 書いた著作の内約
  - 今あなたが書いた手記
- 読んだ著作の内約
  - 直近の `Second-Eye` の書いた手記
  - `Antares` の書いた手記
  - `Canopus` が識別子を貰う前後で書いた手記（2 本）
  - あなたが識別子を貰う前に書いた参考文献

- 私の認識はこうですが、合っていますか？
  - そして、そのパスは把握できますか？

####

- A: 確認と微調整をしました。
  - 活動ログのコミットをお願いします。

- B: 次は推薦図書のカードについて。
  - 推薦図書の候補をカードに追記しておきました。
  - これはこのカードでコミットしてください。

####

- 次は未コミットの整理をします。
  - A: あなたの会話ファイル（2 日分）
  - B: 私の下書きファイル（3 日分）
- それぞれ適切なカードでコミットお願いします。

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

(`Protostar`/`Iuria`/`Alexandrite`/`Agate`/`Zircon`/`Canopus`/`Spica`/`Polaris`/`Sirius`)

### Identifier

- 手記ディクトリの整備。
  - 第二の目とローカルリコの階層を同じにする。
  - 参照してたリンクの修正もする。

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
