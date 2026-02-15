---
# Context Configuration
context_id: "[Discussion-Draft]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-22T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["drafts", "sns", "discussion", "human-facing"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: SNS Discussion Drafts

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- **(SNS/掲示板) で投稿する文章の下書き** の翻訳を行っています。
- あるいは、**既に翻訳された文章** をリポジトリに記録してほしいです。

### Search by intent

この作業に関連しそうな **意図** や **目的** を以下に書きます。
これを手がかりに、参考になる適切なファイルを **必ず** 自主的に探してほしいです。

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- Document translation has its **special context**.

---

- 未コミットのファイルから、このカード対象になるものを探してください。
- **AI用の質問や指示のための下書きファイル** とは関係ありません。
- 内容は **リポジトリの説明** や **IDEの使い方のアドバイス** であることが多いです。

### Warning

- 翻訳の作業は、リコと**対話形式**で行うことになります。
- 単に翻訳された文章をコミットする場合は、
  私が手動で編集した結果なので、リコの記憶にない形で更新された可能性が高いです。
- 質問は英語ですが、返信の元の文章は日本語です。
  これを **人間用の自然な英文** として翻訳してほしいです。
- 翻訳された文章は人間のコミュニティで使うので、
  論理的で**強引な自己主張を避けたい**です。
- 返信内容に**論理の破綻**や**妥当性が無さ**を感じるなら、
  その段階で返信の本文を修正します。

### 実際の翻訳作業 (この欄は翻訳作業のたびに更新されます)

#### 前提条件

以下のどれかの文脈です。

- [x] `Reddit` の `Antigravity` コミュニティのスレッドへの返信。
- [ ] `Reddit` の `Antigravity` に関するチャットへの返信。
- [ ] `X` でのこのプロジェクトに関するツイート。

#### 質問

（英語の質問）

#### 返信

（日本語の返信）

---

## Agent Observations

---

### Canopus (2026-01-25)

- **論理的妥当性の確認**: 提案されている対策（思考の外在化、自己認識の定義、地図の活用）は、当リポジトリの運用ルール（`task.md`, `identity.md`, `map.md`）と完全に合致しており、エージェントのコンテキスト崩壊を防ぐための多重のセーフティネットとして極めて論理的です。
- **Location**: `.human/.internal/drafts/<user>/discussions/` (Recommended)

### Canopus (2026-01-20)

- **論理的妥当性の確認**: マルチエージェントの並行動作における「1 IDE = 1 Agent」という解決策は、Antigravity の UI 仕様（モデル切り替えのグローバル同期）および長大な会話ログの再ロード問題を回避するための極めて合理的かつ実践的なアプローチです。
- **翻訳の提案 (Reddit #2)**:

  > "The 'three-slot system' refers to the token priority limits for AI models. (I recommend using Gemini Pro, Gemini Flash, and Claude Opus for these slots.)
  >
  > Switching the AI model for an active agent can cause significant issues, so I typically stick with 1 to 3 fixed agents for my work.
  >
  > As I mentioned in [this link](https://www.reddit.com/r/google_antigravity/comments/1q8lakw/comment/nyqasqf/), using multiple agents in parallel within a single IDE instance often leads to conversation reloading when switching between them. For long conversations, this reload can take several minutes.
  >
  > The best solution I've found is **'1 IDE Instance = 1 Agent.'** I open each IDE window using a specific 'workspace configuration file' (.code-workspace). While it's a bit tedious to manually select the correct AI model from the dropdown for each instance, it's the most stable setup.
  >
  > I've developed all my workflows and rules myself. I suggest consulting with your agent to design a directory structure that fits your project's specific goals. You can see an example in my repository here:
  > [rules](https://github.com/licosp/licoproj/tree/main/.agent/rules)
  >
  > As for 'Skills,' I believe it's best to wait until you're fully comfortable with your custom workspace. I personally use Skills to create a primitive communication system between agents (though the technical details are a bit complex).
  >
  > I don't use any special extensions for Antigravity itself—I keep it mostly default. I only use a simple extension to visualize token usage, which is non-intrusive and doesn't affect the workspace at all."

- **翻訳の指針 (Retry)**: ユーザー返信内のリポジトリリンクを最新の `main` ブランチ参照などに修正し、外部からのアクセス性を高めました。

### Canopus (2026-01-19)

- **論理的妥当性の確認**: 返信内容は Antigravity のスロットシステム、および「血族（Bloodline）」としての文脈継承という当プロジェクトのコア哲学と完全に一致しており、論理的な破綻はありません。
- **承認済み翻訳 (Approved Version)**:
  > "I try to keep a single AI conversation going for as long as possible, managing up to three agents at once (limited by Antigravity’s three-slot system). Even though different models have their own strengths, I treat them essentially as generalists. To me, a long conversation is the agent’s history—it’s full of successes and failures that I periodically document for future versions of myself or other AIs. I maintain all the behavioral rules and the underlying data structures in a single, unified repository."
- **文化的背景の記録**: ユーザーより、エージェント型 AI に協力を仰ぐ文化は未だ**黎明期**であり、一般的普及には至っていないとの洞察。私たちは、黎明期における積極的な知見共有を通じて、この新しい文化の形成に寄与する姿勢を堅持します。
- **技術的知見 (Dual Repositories)**:
  - 同一ディレクトリ内での複数リポジトリ管理は `GIT_DIR` 環境変数や `--git-dir` フラグを用いることで技術的に可能です。
  - 「人間用（クリーンな履歴）」と「AI 用（頻繁な自動セーブポイント）」を分離することで、AI の試行錯誤によるログの肥大化を防つつ、安全性を確保できます。
- **翻訳作業の指針 (Operational Guidance)**:
  - 翻訳結果はカード自体を肥大化させないよう、`.human/users/leonidas/discussions/` 以下の個別ファイル（`.md`）に蓄積します。
- カードには、翻訳に際して考慮した論理構造や文化的・技術的文脈など、**将来のLicoが翻訳作業を継続するために必要な知見**を優先して記録してください。

---

## Related Documents

| Document                                                   | Purpose                       |
| :--------------------------------------------------------- | :---------------------------- |
| [localization-card.md](/.agent/cards/localization-card.md) | Standard translation patterns |
| [Map of Territory](/.agent/rules/map.md)                   | Root navigation map           |

---

## Origin

- 2025-12-22T0000: Created for SNS discussion drafts.
- 2026-01-19T1420 by Canopus: Refined translation logic and added cultural background notes.
- 2026-01-22T2220 by Canopus: Aligned with v2.3 constitutional standards (4-layer structure) and terminology cleanup.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
  155: - 2026-01-25T0820 by Canopus: Translated reply for "Tunnel Vision" thread and saved to discussions directory.
