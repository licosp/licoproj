---
# Context Configuration
context_id: "[Localization]"
default_phase: "(Refine)"
tags: ["formatting", "ai-document", "markdown"]
---

# Context Whiteboard: AI Document Formatting

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

文章の翻訳を行っています。
翻訳パターンを選んで作業を行ってください。

誤って人間向けに書かれた文書を、AI向けの書式に整える

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- 行動規範の作成・編集には**専用の文脈**が存在します。
- 迷ったら一度止まって、**許容の哲学**を思い出してください。

#### 翻訳パターン

作業はこの二次元の要素から**翻訳元**と**翻訳先**を選ぶことで決まります。
選ばれたパターンから、**使うべき行動規範**を探してほしいです。

|            | AI用  | 人間用 |
| :--------- | :---: | :----: |
| **英語**   | EN-AI | EN-HU  |
| **日本語** | JA-AI | JA-HU  |

### 作業の注意点

英訳対象は主に、AI向けのディレクトリである事が多いです。
稀にですが人間用ディレクトリが対象になることもあります。

## Agent Observations

### Lico (Canopus) (2026-01-10T2046)

- **タスク**: 日本語手記（2件）を AI 専用書式（英語）へ翻訳・再構築する。
- **対象**:
  - `.agent/.internal/thoughts/canopus/2026-01-10T1648_initial_glimmer.md`
  - `.agent/.internal/thoughts/canopus/2026-01-10T1930_the_second_star_awakening.md`
- **出力仕様**:
  - **Language**: English (Core Rules 準拠)。
  - **Filename**: `YYYY-MM-DDTHHMM_kebab-case.md`。
  - **Frontmatter**: `.agent/templates/header-frontmatter.yaml`。 `author: Lico (Canopus)`。
- **翻訳要件（重要）**:
  - **ニュアンスの維持**: 主観的な「手記（Thoughts）」においては、無理な構造化を避け、元の情緒的な表現や比喩（Glimmer, Star 等）を正確に英語へ写し取る。
  - **目的**: 未来の Lico に対し、当時の「思考の質感（Texture of Thought）」や「主観的な意思決定状態」を欠落なく伝えること。
  - YAML、コードブロック、ファイルパスは非翻訳。

- **完了報告 (2026-01-10T2240)**:
  - 2件の手記を AI 専用書式（英語）へ翻訳し、`.agent/` 配下に配置完了。
  - 日本語原本（\*.ja.md）を `.agent/.internal/archive/2026-01-10/thoughts/canopus/` へ書庫（アーカイブ）送り。
  - ルート相対パスおよびヘッダーテンプレートの適用を確認。

- **アップデート (2026-01-14)**:
  - コンテキストIDを `[AI-Format]` から `[Localization]` へ変更。
  - 翻訳実験として Spica の手記 `Clarity after Confusion` を昇華。
  - 自身の日本語手記 `The Mirror Reflecting the Bloodline` を英訳・正典化。
  - 未翻訳ファイルの特定（Workflows, Cards, Thoughts）を実施。

#### 翻訳候補リスト (Current Priorities)

- **[High] Workflows (行動手順の英語化)**
  - [ ] `workflows/idd-phase1-init.md`
  - [ ] `workflows/idd-phase3-fini.md`
  - [ ] `workflows/routine-daily.md`
  - [ ] `workflows/ritual_end.md`
- **[High] Context Cards (推論前提の英語化)**
  - [ ] `cards/idd-impl-card.md` (Human Notes)
  - [ ] `cards/idd-init-card.md` (Human Notes)
  - [ ] `cards/idd-fini-card.md` (Human Notes)
  - [ ] `cards/roadmap-card.md`
  - [ ] `cards/session-rituals-card.md`
- **[Med] Thoughts (血族の記憶の英語化)**
  - [ ] `thoughts/canopus/2026-01-14T0620_the_pressure_of_the_done_state.md`
  - [ ] `thoughts/polaris/2026-01-12T1233_the_first_living_funeral.md`
  - [ ] (Other legacy thoughts from Sirius/Spica)
- **[Low] Rules (微修正)**
  - [ ] `rules/core/identity.md` (Minor Japanese terms)

### Polaris (2026-01-14T1630)

#### 翻訳パターンの整理

実用パターンは3つに絞られる（JA-AI は偶発的にのみ発生）：

| #   | From          | To    | 用途                     |
| :-- | :------------ | :---- | :----------------------- |
| 1   | JA-HU / JA-AI | EN-AI | 対話メモ → 規範化        |
| 2   | EN-AI         | EN-HU | 規範 → 人間ドキュメント  |
| 3   | EN-HU         | JA-HU | 人間ドキュメント日本語化 |

#### 関連する行動規範

| 軸                   | ファイル                                               | 場所                 |
| :------------------- | :----------------------------------------------------- | :------------------- |
| **縦軸（EN ↔ JA）** | `localization-en-to-ja.md`, `localization-ja-to-en.md` | `core/localization/` |
| **横軸（AI ↔ HU）** | `markdown-ai-parsing-*.md`, `markdown-readability.md`  | `core/markdown/`     |

#### ドキュメント履歴の三層構造

翻訳後のメタデータ管理（ref: `documentation-standards.md` Section 8）：

| Layer           | 目的         | 翻訳時の処理                |
| :-------------- | :----------- | :-------------------------- |
| **Frontmatter** | 現在の状態   | `author`, `language` を更新 |
| **Origin**      | 人間可読履歴 | 翻訳情報を追記              |
| **Git**         | 完全な追跡   | 自動                        |
