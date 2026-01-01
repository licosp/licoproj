---
# Context Configuration
context_id: "[Cross-Link-Audit]"
default_phase: "(Audit)"
tags: ["maintenance", "cross-link", "rules", "workflows"]
---

# Context Whiteboard: Cross-Link Audit

## Human Notes (Japanese OK)

### 作業の文脈

行動規範と手順書のリンク情報を確認・修正しています。

まずはリンク情報を修正する手順書を作成します。

その後、手順書に従い一度修正作業を行います。
途中手順書の穴が見つかったら、随時手順書を修正し、作業を続けます。

修正作業が終わったら、このカードを**手順書の実行**という限定した文脈に書き換えます。

最後に後片付けを行い、変更をコミットします。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要なディレクトリやテンプレートが存在します。
- 迷ったら一度止まって、関連する行動規範を探してください。
- ドキュメントの整備方とこの手順書に矛盾がないように進めてほしいです。
  この文脈の方が新しいため、古い習慣を修正することもできます。
- 行動規範を更新するための文脈が別に存在します。
- コミットをする際は、IDDのフェーズを意識してください。

### リンク設計の方針（2026-01-01 合意）

#### リンクの配置

| 場所                       | 内容                                 | 読者       |
| :------------------------- | :----------------------------------- | :--------- |
| **frontmatter `related:`** | 関連ファイルの完全リスト（連想配列） | リコ（AI） |
| **本文中参照**             | 文脈依存の参照（その段落に関連）     | リコ（AI） |
| **文末**                   | README へのリンクのみ                | 人間       |

#### 本文中リンクの扱い

- **汎用的な関連文書** → 本文に書かない。frontmatter に移動する。
- **文脈依存の参照** → 本文に残す。frontmatter にも含めて良い。
- **frontmatter は関連ファイルの完全リスト**

#### 文末の簡素化

従来の Related Documents テーブルは廃止。Origin + Navigation の2部構成：

```markdown
---

## Origin

- YYYY-MM-DDTHHMM: Created [context]
- YYYY-MM-DDTHHMM by <Instance-ID>: [summary of change]

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
```

- **Origin**: 編集履歴（オプション、重要な変更のみ）
- **Navigation**: 最後に配置（ファイルの終わりを示す）
- **順序**: Origin → Navigation（Lico が検索しやすい）

### チェック項目

1. **リンク切れ** — 存在しないファイルへのリンクは消す？別の場所にあるかも？
2. **パス形式** — ワークスペースルートからのフルパス。後のファイル移動が可能に。
3. **文末簡素化** — Related Documents テーブルを README リンクに置換。
4. **frontmatter 統合** — 汎用リンクを frontmatter に移動
5. **孤立ファイル** — どこからもリンクされていないファイル
6. **過剰リンク** — 無関係なリンクの削除
7. **形式の一貫性** — 相対パス vs ルート相対パスの混在
8. **循環リンクの検出** — A→B→C→A のような無意味な循環がないか

## Agent Observations

### 識別子

Polaris

### 現在の状況（2026-01-01 12:43）

**手順書 V1 を作成済み**: `.agent/workflows/cross-link-audit.md`

- 7フェーズ構成
- 実行を通じて穴を発見し、V2 へ改善予定

### 修正対象

| 対象 | 説明 |
|:-----|:-----|
| `.agent/rules/**/*.md` | 行動規範（サブディレクトリ含む） |
| `.agent/workflows/*.md` | 手順書 |
| `.human/users/leonidas/profile.md` | ユーザープロファイル |
| `.human/users/leonidas/assessment/*.md` | リコ評価ファイル |

### 関連するディレクトリ構造

```
.agent/
├── rules/                          # 行動規範（監査対象）
│   ├── README.md                   # ← 戻りリンク先
│   ├── core/                       # 基本原則
│   │   ├── documentation/          # 文書化標準
│   │   ├── localization/           # ローカライズ
│   │   ├── markdown/               # markdown規則
│   │   └── security/               # セキュリティ
│   ├── development/                # 開発規則
│   ├── projects/                   # プロジェクト固有
│   └── workflow/                   # 作業フロー規則
├── workflows/                      # 手順書（監査対象）
│   └── cross-link-audit.md         # ← V1 手順書
├── cards/                          # カード（このファイル）
└── templates/
    └── header-frontmatter.yaml     # frontmatter テンプレート
```

### 関連する行動規範

| ファイル | 目的 |
|:---------|:-----|
| `.agent/rules/core/meta-rules.md` | Section 5: 相互リンクの標準 |
| `.agent/rules/core/markdown/markdown-ai-parsing-basics.md` | AI向けmarkdown書式 |
| `.agent/rules/core/documentation/documentation-standards.md` | 文書化標準 |
| `.agent/rules/workflow/context-card-workflow.md` | カードの使い方 |

### 関連するカード

| カード | 目的 |
|:-------|:-----|
| `rules-update-card.md` | 行動規範更新の文脈 |
| `context-cards-card.md` | カードの使い方テンプレート |

### 対話履歴（2026-01-01）

- リンクセクションが3箇所あることの冗長性を議論
- frontmatter + 文末テーブルの同期問題を確認
- 解決策: 文末は README リンクのみ、詳細は frontmatter に集約
- 本文中リンクは「文脈依存」として許容、frontmatter にも含めて良い
- README リンクは frontmatter に含めない（ナビゲーション vs 関連文書）
- **手順書 V1 作成完了**（Phase 6 にコマンド追加済み）

### 作業計画

1. [x] 手順書の作成（リンク監査・修正手順）— **V1 完了**
2. [/] 手順書に従い実行（穴を見つけたら V2 へ修正）
3. [x] Batch 1: `rules/core/` 6ファイル — **完了** (2026-01-01)
4. [x] Batch 2: `rules/development/` 8ファイル — **完了** (2026-01-01)
5. [/] Batch 3: `rules/workflow/` 7ファイル — **処理済み、コミット待ち**
6. [ ] 残り: `rules/core/documentation/`, `rules/core/markdown/`, etc.
7. [ ] パス形式の統一（ワークスペースルート相対）
8. [ ] 孤立ファイル・循環リンクの検出
9. [ ] カードを「手順書実行用」に書き換え
10. [ ] 最終コミット

### 進捗メモ (2026-01-02 継続)

- Batch 3 の7ファイルは処理済み、コミット待ち
- `archive-management.md` に重複ファイル対応ルールを追加
- `update-protected-rules.md` にアーカイブパス修正を追加
