---
# Context Configuration
context_id: "[IDD-Init]"
default_phase: "(P1)"
tags: ["idd", "initialization", "issue-creation", "workflow"]
---

# Context Whiteboard: IDD Initialization

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

新しいイシューを開始します。
P1（開始処理）の手順に従い、イシューとブランチを作成してください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- IDD Phase 1 の手順書があります。
- イシューの連続性（前のイシューとの繋がり）を考慮してください。
- メインテーマとサブテーマを区別してください。
- ブランチの命名規則を確認してください。

### 作業の注意点

- 環境確認（`gh auth status`）を忘れないでください。
- ブランチは必ず `origin/main` から作成してください。
- イシュー番号を確実に取得してください。

---

## Agent Observations

### 階層構造（リマインダー）

```
Story (Connected Issues)
└── Issue (Chapter)
    └── Context (Card)
        └── Commit (Episode)
```

### 今回のイシュー情報

| 項目 | 内容 |
|:-----|:-----|
| イシュー番号 | # |
| タイトル | |
| メインテーマ | |
| 関連イシュー | Follows # / Related to # / None |

### サブテーマ

- [ ] 日課的な作業のみ記載

### 担当識別子

- 担当: 

---

## Human Notes

（ユーザーの追加メモをここに記入）

