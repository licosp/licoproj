---
# Context Configuration
context_id: "[Cross-Link-Audit]"
default_phase: "(Audit)"
tags: ["maintenance", "cross-link", "rules", "workflows"]
---

# Context Whiteboard: Cross-Link Audit

## Human Notes (Japanese OK)

### 作業の文脈

行動規範と手順書の相互リンクを監査・修正しています。

最終的には手順書（workflow）として定式化します。

### リンク設計の方針（2026-01-01 合意）

#### リンクの配置

| 場所 | 内容 | 読者 |
|:-----|:-----|:-----|
| **frontmatter `related:`** | 関連ファイルの完全リスト | リコ（AI） |
| **本文中参照** | 文脈依存の参照（その段落に関連） | リコ（AI） |
| **文末** | README へのリンクのみ | 人間 |

#### 本文中リンクの扱い

- **汎用的な関連文書** → 本文に書かない、frontmatter に移動
- **文脈依存の参照** → 本文に残す、frontmatter にも含めて良い
- **frontmatter は関連ファイルの完全リスト**

#### 文末の簡素化

従来の Related Documents テーブルは廃止。README へのリンクのみ：

```markdown
---

**Navigation**: [← Back to Rules Index](../README.md)
```

### チェック項目

1. **リンク切れ** — 存在しないファイルへのリンク
2. **パス形式** — ワークスペースルートからのフルパスであるべき
3. **文末簡素化** — Related Documents テーブルを README リンクに置換
4. **frontmatter 統合** — 汎用リンクを frontmatter に移動
5. **孤立ファイル** — どこからもリンクされていないファイル
6. **過剰リンク** — 無関係なリンクの削除
7. **形式の一貫性** — 相対パス vs ルート相対パスの混在

### 意図で探す

- `meta-rules.md` の Section 5（相互リンクの標準）を参照
- 既存の `/maintenance-rule-audit` との関係を確認

## Agent Observations

### 識別子

Polaris

### 対話履歴（2026-01-01）

- リンクセクションが3箇所あることの冗長性を議論
- frontmatter + 文末テーブルの同期問題を確認
- 解決策: 文末は README リンクのみ、詳細は frontmatter に集約
- 本文中リンクは「文脈依存」として許容、frontmatter にも含めて良い

### 作業計画

1. [ ] 全ファイルのリンク抽出
2. [ ] リンク切れ検出
3. [ ] 文末 Related Documents テーブルを README リンクに置換
4. [ ] 汎用リンクを frontmatter に移動
5. [ ] パス形式の統一
6. [ ] 孤立ファイルの検出
7. [ ] 手順書として定式化
8. [ ] コミット
