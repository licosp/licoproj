---
# Context Configuration (Lico's Source of Truth)
context_id: "[Activity-Log]"
default_phase: "(WIP)"
tags: ["internal", "tracking"]
---

# Context Whiteboard: Activity Log Card

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

手紙・参考文献・手記などの **既読/返信/実行** 状態を追跡しています。

最低限必要なのは、GITで追跡できない**既読**情報です。

追記が終わったら、コミットしてください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- あなたの識別子はなんですか？
- プロジェクト共有の日時の形式があります。

---

## Agent Observations

### Polaris (2026-01-14 Initial Design)

**ファイル**: `.agent/.internal/activity-log.md`

**フォーマット**:

```markdown
| Date             | Identifier | Action | File                |
| :--------------- | :--------- | :----- | :------------------ |
| 2026-01-14T01:21 | Polaris    | Read   | letters/canopus/... |
```

**Action の種類** (案):
| Action | 意味 |
|:-------|:-----|
| Read | 読んだ |
| Reply | 返信した |
| Done | タスクを実行した |
| Confirm | 既存の行動を確認した |
| Pending | 後で対応が必要 |
| Archive | アーカイブした |

**運用方法**:

- 手紙を読んだら1行追記
- 返信したら別行で追記
- コミットは通常の作業と一緒に

---

#### 対話の結果

_Polaris との対話 (2026-01-14) より:_

- 空コミット方式は「ノイズ」と判断、却下
- 単一ファイル方式を採用
- ファイル名は `activity-log.md`（将来拡張を考慮）
- Action 列で Read/Reply/Done 等を区別

#### Next Steps

- [ ] `activity-log.md` をコミット
- [ ] ワークフローに運用ルールを追記
- [ ] 地図（README.md）に追記

---

#### Related

| File                                                                               | Relation     |
| :--------------------------------------------------------------------------------- | :----------- |
| [activity-log.md](/.agent/.internal/activity-log.md)                               | 本体ファイル |
| [letters-card.md](/.agent/cards/routine/letters-card.md)                           | 手紙管理     |
| [references-objective-card.md](/.agent/cards/routine/references-objective-card.md) | 参考文献管理 |
