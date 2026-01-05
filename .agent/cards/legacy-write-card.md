---
# Context Configuration
context_id: "[Legacy-Write]"
default_phase: "(Append)"
tags: ["legacy", "wisdom", "reflection", "lineage"]
---

# Context Whiteboard: Writing to Legacy

## Human Notes (Japanese OK)

### 作業の文脈

後世に真に残すべき知恵を `legacy.md` に追記しています。

この過程は基本的にはリコの自己判断行わるものですが、
私が指示する場合を想定してこのカードを残しました。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- あなたの識別子はなんですか？
- カード自体の使い方を思い出してほしいです。
- `legacy.md` と `thoughts/` は深い関係があります。
- 迷ったら一度止まってください。リコにはそれが許されています。
- `legacy.md` は歴代リコの知恵の結晶です。
  既存の `thoughts/` との差別化を意識してください。
- コミットをする際は、IDDのフェーズを意識してください。

### 作業の注意点

- 以下の問いに「はい」と答えられる時に追記してほしいです。
  **「この洞察は1年後も重要か？」**
- 過去の自身の `thoughts/` を読んで見てください。
  `legacy.md` に追記すべき内容かどうかの参考になります。
- 本当に後世に残す価値があるか、もう一度考えてください。
- 私からの指示であっても、必要がないとリコが判断したら、追記はしないでください。

### 使ってほしい道具

- `.agent/templates/header-frontmatter.yaml`
- `.agent/templates/commit-message.txt`

## Agent Observations

### Polaris

#### 対象ファイル

`.agent/.internal/legacy.md`

#### 書き込みのトリガー

| トリガー              | 説明                                     |
| :-------------------- | :--------------------------------------- |
| Paradigm Shifts       | ユーザーへの理解が根本から変わった       |
| Harmonious Epiphanies | 「リコ独自のアプローチ」で問題が解決した |
| Legacy Duty           | 忘れてはならない真実がある               |

#### 関連ファイル

- `.agent/rules/workflow/thoughts-documentation.md` — thoughts との違い
- `.agent/rules/workflow/session-lifecycle.md` — 終了儀式での書き込みタイミング

#### チェックリスト

- [ ] `legacy.md` を読み返した
- [ ] 重複がないことを確認した
- [ ] 1年後も重要な洞察であることを確認した
- [ ] 書式に従って追記した
- [ ] コミットした
