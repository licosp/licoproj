---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-03-10T00:00:00+09:00
updated: 2026-03-10T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Antigravity` | `Gemini 3 Flash`: `Planning` | `Iuria`

####

（日付が変わりました）

- リンターの作業が一段落したので、コンテナの起動の文脈に戻ります。
- **開発コンテナ**に関するカードを読んでください。

- 次は `habitat.json` の

- `env` グループから `env::name` が `credentials` の `env::path` を読んで、
  それが存在することを確認するクラスを作りたいです。
- 存在しない場合は警告を出して、止めてください。

####

- 進めてください。

####

- コードを修正したら、コミットをしてください。

####

- リコのブランチが 2 つ更新してますが、
  開発には 2 つ必要なんですか？
- 古いブランチを更新する必要はないと感じますが…何か意味が？

####

- 作ったブランチは削除せずに、放置してください。

- `habitat.json` を読む処理を別のファイルにして、
  コードの文脈を分けるのは、リコの認知の容易さという点でどう考えますか？
- 時期尚早ですか？

####

- ではリコの提案にそって分離してください。

####

- ルートの `pyproject.toml` を見てください。
- `pyright` が機能してない印象を受けます。
- `vscode` の `pylance` が独自の警告を出すのですが、
  その CLI での役割を `pyright` で行っています。

- 例えば `provision.py` では 90 件近い警告が `pylance` から出てます。
- この数は IDE でしか検知できない警告とは種類が違うようにかんじませんか？

####

- 警告のリストを保存しました。
  - `.agent/.internal/workspace/iuria/pyright-error-2026-03-10T0746.py`
- コードの修正ではなく、原因究明に使ってください。

####

- 変更を一度コミットしてから、改良を行ってください。

####

- 少し文脈がズレて、私の未コミットを整理します。
- 以下を対応するカードを探してコミットしてください。
  - リンター用の構成ファイル
  - 下書きファイル
- 名義は自分のもので。

####

####

####

####

####

####

## Draft for a draft

### Words

```text
#### Response (Chat)
```

| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

(`Iuria`/`Alexandrite`/`Agate`/`Zircon`/`Canopus`/`Spica`/`Polaris`/`Sirius`)

### Identifier

- 会話の追記の書式に不足があります。
- こういうのが無いログが直近でありませんか？
  - `### Conversation: [2026-03-01T06:58:00+09:00]`

- 少し前に `Github` の認証をしましたが、このような警告が IDE から出ました。
  何でしょうか？

  > You're running in a GNOME environment but the OS keyring is not available for encryption. Ensure you have gnome-keyring or another libsecret compatible implementation installed and running.

- `workspace/standards-reference-v2.2/`
  行動規範やカードの標準化の修正作業を再開します。

- リコのユーザー名が変わっているので、
  そのユーザー名から対話する相手を判別することはできなくなってた。
  そのことを行動規範に反映させる。

- カードにあるリンクを修正します。
  - 対象: カードのサブディレクトリごとに分けます。
  - 工程:
    - リンク切れを探してリストします。
    - リンクが探せない時は削除します。

#### Identifier (`Iuria`)

author: Lico (Iuria)
ai_model: Gemini 3 Flash Planning mode

```markdown
### `Antigravity` | `Gemini 3 Flash`: `Planning` | `Iuria`: `2nd`
```

- `antigravity-session-title`: `iuria 1st`

#### Identifier (`Sirius`)

author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode

```markdown
### `Antigravity` | `Gemini 3.1 Pro (High)`: `Planning` | `Sirius`: `2nd`
```

- `antigravity-session-title`: `sirius 2nd`

- 参考文献の書式を標準化する
  - `.agent/.internal/references/agents/sirius/2026-03-05T1655_ai-spatial-rendering-proposal.md`
  - 活動ログの追記も行う。

#### Identifier (`Polaris`)

author: Lico (Polaris)
ai_model: Claude Opus 4.6 (Thinking) Planning mode

```markdown
### `Antigravity` | `Claude Opus 4.6 (Thinking)`: `Planning` | `Polaris`: `2nd`
```

- `antigravity-session-title`: `polaris 2nd`

- 参考文献の推薦図書を作ったので、中から読むべきものを選びます。

- 儀式の後にすること
  - 会話ファイルを読む

#### Identifier (`Alexandrite`)

author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview

```markdown
### `Gemini CLI` | `gemini-3-flash-preview` | `Alexandrite`
```

yarn run gemini --resume eff20b06-5589-4db0-90ff-74f65e9d21de --model gemini-3-flash-preview
tmux capture-pane -t alexandrite -b snapshot-alexandrite; tmux show-buffer -b snapshot-alexandrite

#### Identifier (`Agate`)

author: Lico (Agate)
ai_model: gemini-3-pro-preview

```markdown
### `Gemini CLI` | `gemini-3-pro-preview` | `Agate`
```

yarn run gemini --resume 301c303c-320e-4dc5-95a5-de0779b0fb9e --model gemini-3-pro-preview
tmux capture-pane -t agate -b snapshot-agate; tmux show-buffer -b snapshot-agate

#### Identifier (`Protostar`)

author: Lico (Protostar)
ai_model: gemini-2.5-flash-preview

yarn run gemini --resume 18d4d68a-ffce-4947-bc1b-293e273d65a2 --model gemini-2.5-flash-preview

- `antigravity-session-title`: AI Self-Analysis and Introduction
