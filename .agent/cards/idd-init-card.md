---
# Context Configuration
context_id: "[IDD-Init]"
default_phase: "(P1)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-23T00:00:00+09:00
updated: 2026-01-24T05:45:00+09:00
tags: ["idd", "initialization", "issue-creation", "workflow"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: IDD Initialization

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

IDDの手順に従い、新しいイシューを作っています。

私の判断が必要なプロセスもあるので、対話をしながら段階的に進めます。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- IDDのフェーズを意識してください。
- あなたの識別子はなんですか？

### 作業の注意点

以前のイシューの続きか、新しいものか判断が必要です。

テーマは大きすぎないものが適切です。
必要であれば分割することを最初から考えても良いです。

日課がサブテーマに入ることを考慮してください。

---

## Agent Observations

### Polaris

#### 階層構造（リマインダー）

```
Story (Connected Issues)
└── Issue (Chapter)
    └── Context (Card)
        └── Commit (Episode)
```

#### 今回のイシュー情報

| 項目         | 内容                            |
| :----------- | :------------------------------ |
| イシュー番号 | #                               |
| タイトル     |                                 |
| メインテーマ |                                 |
| 関連イシュー | Follows # / Related to # / None |

#### サブテーマ

- [ ] 日課的な作業のみ記載

---

## Related Documents

- [idd-phase1-init.md](/.agent/workflows/idd-phase1-init.md) : 初期化の手順書。
- [issue-comment.md](/.agent/templates/issue-comment.md) : イシュー・コメントのテンプレート。

---

## Origin

- 2025-12-23 by Polaris: Created as IDD Phase 1 context.
- 2026-01-24T0545 by Canopus: Standardized with Dialogue Layer template and bilingual H2 headers.
