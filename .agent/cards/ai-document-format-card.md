---
# Context Configuration
context_id: "[AI-Format]"
default_phase: "(Refine)"
tags: ["formatting", "ai-document", "markdown"]
---

# Context Whiteboard: AI Document Formatting

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

誤って人間向けに書かれた文書を、AI向けの書式に整えてています。
対象は主に、`.agent/` ディレクトリである事が多いです。

ファイルの修正が終わった後は、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- 迷ったら一度止まって、関連する行動規範を探してください。
- この文章はAIが読むので、それに最適化する必要があります。

### 作業の注意点

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
  - 日本語原本（*.ja.md）を `.agent/.internal/archive/2026-01-10/thoughts/canopus/` へ書庫（アーカイブ）送り。
  - ルート相対パスおよびヘッダーテンプレートの適用を確認。
