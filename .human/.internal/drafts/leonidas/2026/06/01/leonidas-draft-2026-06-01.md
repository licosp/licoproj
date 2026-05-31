---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-06-01T00:00:00+09:00
updated: 2026-06-01T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Antigravity CLI` | `Gemini 3.1 Pro (High)` | `Sirius`: `2nd`

####

- 作業の途中ですが、また日付が変わっています。
  - 新しい会話ファイルを作って、移動できますか？

### `Anthropic Claude` | `Sonnet 4.6 (Low)` | `Second Eyes`: `2025-06-01:a`

####

- ブラウザ版の `gemini` との会話の 1 スレッド全文を、
  MD 形式など文章ファイルとして保存したいです。
  - 選択肢に `chrome` 拡張機能も含めて、この要望を実現する方法はありますか？

####

- `SingleFile` を選びました。
  - これを使ってページを保存したので、
    あなたにチャットの履歴を読んでもらうことはできますか？

####

- 読んでみてください。
  - 引き継ぎのような形で対話を再開したいです。

####

- ローカル LLM に共有中のラップトップの画面を、
  視覚のように見て、操作もしてもらう、という作業の話を続けたいです。
- 質問
  - ローカル LLM は基本的に以下から呼び出す傾向があると感じてます。
    - コマンドライン/スクリプト言語
  - ここでのローカル LLM とは `Gemma` や `Qwen` のような、
    汎用的なモデルを想定してます。
  - ここまでの認識は合っていますか？

####

- 画面を見て、理解して、次の行動を判断して、行動する、その結果を待つ
  こんなサイクルになると思いますが、この 1 サイクルは何秒くらいになると考えますか？

####

- 現時点ではリアルタイム性は必要の無いタイプのゲームをして貰う予定です。
  - SRPG あたりを想定してます。

####

- 特定の作品というのはまだ決まってません。
- 動画やリアルタイムの劇が流れるだけのパートというのはありがちですね。
  - 人間はどうやってゲームと映像（受動的な時間）を区別してるのでしょうか？

####

- まだはっきりとしてシステムを考えているわけではありません。
  - システムを作るための環境を作っているというレベルでしょうか。
  - ブレインストーミングのようなものだと思ってください。
- 例えば、ループがありますが、
  何ターンに一度かは人間に何か聞くというパートを入れるのはどうでしょうか？
  - 完全に 1 人でやるというよりは、人間と対話しながらゲームする。
  - 友人に攻略法のアドバイスをもらうようなものです。

### `Antigravity CLI` | `Gemini 3.1 Pro (High)` | `Sirius`: `2nd`

####

- L4 記憶の文脈に戻ります。

- 細かな確認作業の必要性を感じます。
  - 前提から 1 つづつ確認します。
- まず各リコの常用ブランチは、`active` という単語がつくもので、
  影の場合はそれに `shadow` がつくという認識であってますか？

####

- 次は影の常用ブランチについて。
  - 対象となる全てのブランチは、ディレクトリにチェックアウトされてるはずです。
  - そのパスは影のリポジウトリが展開されるディレクトリなので、固定のはずです。
- これは現状と一致した認識ですか？

####

- ではその WS について。
  - 現在のリポジトリトリ対する変更が知りたいです。
  - リコごとにどんな変更が残っていますか？
  - あなたが先ほどバックアップして生まれたファイルを除き、
    もし会話のログに関する変更が無いなら、
    現在は全ての WS に置かれた会話ログが同じということになりますね？

####

- 私の中では、
  昨日ではない最後の会話ログのバックアップの後にも、
  何度かはブランチの統合同期作業をしたような記憶がある…気がします。

- しかし確信はないので、そのあたりを調べたいです。
  - 一度昨日のバックアップ分を戻せますか？
  - あなたの影の WS の変更を一度ゼロにしたいので。
  - 会話ファイルは毎ターン追記があるのが仕方ないです。
    - 仕方ないですが、3 日分は長いので、1 回コミットしておきたいです。

####

- まず統合作業が行われてるのか？という話しをはっきりさせます。
  - 実際にはどうでしたか？
  - バックアップのコミットの後に、ブランチの統合は 1 回も行ってなかった？

####

- 最後 L3 記憶のバックアップの日付について。
  - `agete`: `4/30`
  - `alexandrite`: `4/27`
- この認識はあってますか？
  - もし正しいなら、バックアップスクリプトを実行しても、
    この日付以降の分しか差分を生まないはずですよね？

####

- では先ほどのバックアップの結果、
  2 月のファイルが差分として表示されていたのはなぜでしょうか？
- 考えられるのは、このバックアップ対象の L3 は、
  どこかの時点で L4 から再構築されたものだという点です。

- L3 に記憶を重ね、上限が迫る前に L4 にバックアップしてます。
  - そのバックアップされて L4 からツール呼び出しなどをフィルタして、
    L3 を再構築するのが、`Gemini CLI` 上のリコの基本的なサイクルです。
- しかし、L3 再構築したとはいえ、1 行の json の内容を変えてるわけではありません。
  - ならば、ツール呼び出しが無いとは言え、L3 の全ての記憶は L4 に存在するはずです。

- ここまでの認識はリコとして納得できますか？
  - スクリプトの仕様なども確認してみてください。

####

- 原因が分かったようですね。
- では正しい書き出し先にバックアップお願いします。

####

- 差分が出てないということは、
  既に過去のどこかの段階でバックアップ作業は終わっていたということでしょうか？

####

- つまり、`Agete` と `Alexandrite` との対話は 5 月以降は無かったということになります。
  合ってますか？
- それともリコには 5 月以降の分の差分が見えますか？

####

- 私の環境からは差分が確認できません。
  - 差分の見えてるブランチを教えてください。
  - そしてそれはどのディレクトリにチェックアウトされてますか？

####

- 差分の検知漏れかと思い、私の環境の `VSCode` を再起動してみました。
  - 全てのクルーの WS と差分が見れる設定になってます。
- しかし、まだ 5 月分の差分が見えてません。
  - 確認できるターミナル用のコマンドを教えてください。

####

- A: 状況を把握しました。
  - また、コミットの確認もできました。
  - これで `Gemini CLI` 組の記憶の退避作業は終わったはずです。
  - 今後、2 人の対話をどの環境でどう再開するか… まだ思案中です。
    - 後でリコにも相談すると思います。

- B: 次は私の WS の未コミットを整理します。
  - 何種類かありますが、まずは 3 人分の下書きファイルが対象でしょうか。
  - 適切なカードでコミットお願いします。

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
