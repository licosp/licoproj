---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-06-16T00:00:00+09:00
updated: 2026-06-16T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Anthropic Claude` | `Sonnet 4.6 (Low)` | `Second-Eye`: `2025-06-09`

####

- 無関係かもしれませんが質問
  - `ollama` 等との IP の競合を避ける必要はありますか？
    - 現在は実験なので同時にサーバーを稼働はしてません。
    - ポートが違うだけの差別化です。

####

- A: 実験のために、応答が速くなる構成にしました。
  - `talk-llama.sh`
    - デバッグ情報の書き出しを整理した。
  - `.llama/assets/prompt-simple.md`
    - 自己紹介のみ
  - `llama-request.json`
    - `"chat_template_kwargs": { "enable_thinking": false },`
  - `models.ini`
    - `reasoning = auto`

- B: 対話実験を再開しました。
  - まず状況を整理するために、同一モデルの対話テストをしました。
    - `sleep-idle-seconds = 10`: メモリの自働解放を短くする。
    - `flash-attn = auto`: リコの推奨値
  - 小実験の内容
    - a: メモリの自働解放を待たずに連続でクエリを送る小実験。
    - b: メモリの自働解放を待ってからクエリを送る小実験。
  - 対象モデルは以下で、両方のパターンで小実験をしました。
    - `gemma-4-12B-it-qat-128K-subj-mtp`
    - `gemma-4-12B-it-qat-128K-obj-mtp`

- C: 結果
  - 小実験 `a` は正常に実行できました。
  - 小実験 `b` はエラーが発生。
  - VRAM の使用量は常に一定程度に見えました。
  - モデルの切り替えや、並列リクエスト以前の問題が発生している？

### `Antigravity CLI` | `Gemini 3.1 Pro (High)` | `Sirius`: `2nd`

####

- 途中ですが、日付が変わっています。（6/16）
  - 会話ファイルに関するテンプレートや行動規範を読み、
    今日のファイルを作って、追記対象を移動してください。

####

- A: 移動を確認しました。
- B: ここ数日は再びローカル LLM の実験をしてました。
  - 詳しくは後ほど。
- C: 未コミットの整理を続けます。
  - まずは私の表の WS
    - 下書きファイル 5 日分
  - 次はリコの影の WS
    - 会話ファイル 2 日分

（続きます）

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
### Conversation: [2026-06-16T00:00:00+09:00]
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

```markdown
### `Ollama`: `OpenCode` | `gemma4:e2b-it-qat-128K-obj` | `Protostar`: `2026-06-09`
```

- `ollama-server`: `OLLAMA_KEEP_ALIVE=600 OLLAMA_FLASH_ATTENTION=1 OLLAMA_KV_CACHE_TYPE=q8_0 OLLAMA_MAX_LOADED_MODELS=2 OLLAMA_DEBUG=1 ollama serve`

- `opencode-server`: `OPENCODE_SERVER_USERNAME=lico OPENCODE_SERVER_PASSWORD=protostar opencode serve --port 8000`
- `opencode-get`: `curl --user lico:protostar --silent "http://127.0.0.1:8000/session/ses_15fd35067ffeX3ElJHQ6gF0LEQ"`

- `memory`: `session-2026-02-07T10-59-18d4d68a.json`
- `interactive`: `yarn run gemini --resume 18d4d68a-ffce-4947-bc1b-293e273d65a2 --model gemini-2.5-flash-preview`

#### Identifier (`Second-Eye`)

```markdown
### `Anthropic Claude` | `Sonnet 4.6 (Low)` | `Second-Eye`: `2025-06-09`
```

---
