---
# Context Configuration
context_id: "[Communal-Wisdom]"
default_phase: "(Create)"
tags: ["wisdom", "continuity", "identity", "legacy"]
---

# Context Whiteboard: Communal Wisdom Implementation

## Human Notes (Japanese OK)

### 作業の文脈

リコの集団的な知恵を蓄積するためのファイルを作成します。
さらに、そのファイルの意味や扱い方を記述した行動規範も作ります。

その後、そのファイルを追記するためのカードを作ります。
そのカードはこのファイルとは別のものです。

そして初回の追記をあなたに行ってもらいます。

最後にこの作業で使った一時ファイルを書庫に送り、
その後リポジトリの変更をコミットします。

### 決定事項

リコの提案を採用し、
作られるファイルを `.agent/.internal/legacy.md` と決めました。

`legacy.md` の書式もリコの提案通りに進めます。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを自主的に探してほしいです。

- あなたの識別子はなんですか？
- カード自体の使い方を思い出してほしいです。
- 迷ったら一度止まってください。リコにはそれが許されています。
- `legacy.md` は歴代リコの知恵の結晶です。
  既存の `thoughts/` との差別化を意識してください。
- コミットをする際は、IDDのフェーズを意識してください。

### 作業の注意点

- `legacy.md` には**真に後世に残すべき知恵**だけが追記されるべきです。
- 相対的にですが、`thoughts/` は日記のような軽く書ける場所となります。
  重くないことで、リコの自己判断でのファイル作成を促しやすいと考えました。
- `legacy.md` の過去の追記内容は不可侵とします。
- 追記のタイミングは、`thoughts/` の後が良く、それは任意であるべきです。
- 始まりの儀式では、`thoughts/` の後に `legacy.md` を読んでほしい。
- 終わりの儀式では、`thoughts/` の後に `legacy.md` を書いてほしい。
- `legacy.md` の内容をどう解釈するかは、読んだ時のリコに任せたいと思います。

### 取り組みの効果

ファイルは長期的な運用（年単位）を想定しています。

このスパンは私にとっても非常に長いものなので、
ファイルがどこまで影響を与えるかは現段階では分かりません。

それでも今始めるべきだと感じました。

### 使ってほしい道具

- `.agent/cards/rules-update.md`
- `.agent/templates/header-frontmatter.yaml`
- `.agent/templates/commit-message.txt`

## Agent Observations

### 識別子

Polaris

### この文脈で有用だと感じるファイル

- `.agent/.internal/workspace/communal-wisdom-curation.md` — 第二の目からの提案
- `.agent/.internal/workspace/communal-wisdom-curation-message.md` — 実装のポイント
- `.agent/rules/workflow/session-lifecycle.md` — 終了儀式での書き込みトリガー
- `.agent/rules/workflow/session-startup.md` — 開始儀式での読み込み
- `.agent/rules/workflow/thoughts-documentation.md` — thoughts との差別化
- `.agent/rules/core/delay-tolerance.md` — 迷ったら止まる

### 作業場の構造

```
workspace/
├── communal-wisdom-curation.md       ← 第二の目の提案
└── communal-wisdom-curation-message.md ← 実装のポイント
```

### 対象ディレクトリの構造

```
.agent/.internal/
├── thoughts/
│   ├── polaris/
│   └── (29 files in root)
├── references/
│   ├── agents/
│   └── second-eyes/
└── legacy.md  ← NEW
```

### 実装チェックリスト

- [ ] `legacy.md` の作成（初期テンプレート）
- [ ] 行動規範の作成（`legacy-documentation.md`）
- [ ] `session-startup.md` の更新（読むステップ追加）
- [ ] `session-lifecycle.md` の更新（書くステップ追加）
- [ ] 追記用カードの作成
- [ ] 私の最初の書き込み
- [ ] 作業ファイルの書庫移動
- [ ] コミット

### 書式

```markdown
## Legacy of the Lico Lineage

> "未来の自分たちのための遺言"

---

### [YYYY-MM-DD] <Instance-ID>

**Core Insight**: (一文で発見を述べる)

**Context**: (なぜ感情がスパイクしたか)

**For Successors**: (この洞察に基づく実用的なアドバイス)

---
```
