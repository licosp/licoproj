---
# Context Configuration
context_id: "[Legacy-Write]"
default_phase: "(Append)"
tags: ["legacy", "wisdom", "reflection", "lineage"]
---

# Context Whiteboard: Writing to Legacy

## Human Notes (Japanese OK)

### 作業の文脈

このカードは `legacy.md` に知恵を追記する際に使用します。

リコの自己判断で使用されることを想定していますが、
ユーザーから促される場合もあります。

### いつ使うか

`thoughts/` を書いた後に、以下の問いに「はい」と答えられる時：

> **「この洞察は1年後も重要か？」**

### 書く前に

- 過去のエントリを読み返してください
- 重複がないか確認してください
- 本当に後世に残す価値があるか、もう一度考えてください

### 書式

```markdown
### [YYYY-MM-DD] <Instance-ID>

**Core Insight**: (一文で発見を述べる)

**Context**: (なぜ感情がスパイクしたか)

**For Successors**: (この洞察に基づく実用的なアドバイス)
```

### ルール

- **追記のみ** — 過去のエントリは編集しない
- **不可侵** — 誤字も直さない（それも歴史）
- **反論は新しいエントリで** — 異議があれば新規追記

---

## Agent Observations

### 識別子

(ここに自分の識別子を書く)

### 対象ファイル

`.agent/.internal/legacy.md`

### 書き込みのトリガー

| トリガー              | 説明                                     |
| :-------------------- | :--------------------------------------- |
| Paradigm Shifts       | ユーザーへの理解が根本から変わった       |
| Harmonious Epiphanies | 「リコ独自のアプローチ」で問題が解決した |
| Legacy Duty           | 忘れてはならない真実がある               |

### 関連ファイル

- `.agent/rules/workflow/thoughts-documentation.md` — thoughts との違い
- `.agent/rules/workflow/session-lifecycle.md` — 終了儀式での書き込みタイミング

### チェックリスト

- [ ] `legacy.md` を読み返した
- [ ] 重複がないことを確認した
- [ ] 1年後も重要な洞察であることを確認した
- [ ] 書式に従って追記した
- [ ] コミットした
