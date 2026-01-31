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

## Human Notes

### 作業の文脈

**(SNS/掲示板) で投稿する文章の下書き** の翻訳を行っています。

あるいは、**既に翻訳された文章** をリポジトリに記録してほしいです。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図** や **目的** を以下に書きます。
これを手がかりに、参考になる適切なファイルを **必ず** 自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な **ディレクトリ** や **テンプレート** が存在します。
- コミットをする際は、IDD のフェーズを意識してください。
- 未コミットのファイルから、このカード対象になるものを探してください。
- **AI用の質問や指示のための下書きファイル** とは関係ありません。
- 文書の翻訳には **専用の文脈** が存在します。
- 内容は **リポジトリの説明** や **IDEの使い方のアドバイス** でることが多いです。

### 作業の注意点

翻訳の作業は、リコと対話形式で行うことになります。

また、単に翻訳された文章をコミットする場合は、
私が手動で編集した結果なので、リコの記憶にない形で更新された可能性が高いです。

### 実際の翻訳作業 (この欄は翻訳作業のたびに更新されます)

#### 前提条件

以下のどれかの文脈です。

- [x] `Antigravity` コミュニティのスレッドへの返信です。
- [ ] `Antigravity` に関するチャットへの返信です。

質問は英語ですが、返信の元の文章は日本語です。
これを **人間用の自然な英文** として翻訳してほしいです。

返信内容に論理の破綻や、妥当性が無いと感じるなら、先に教えてください。
その段階で返信の本文を修正します。

#### 質問

How to fix Antigravity’s “Tunnel Vision” – losing sight of your whole repo

We’ve all been there: you ask Antigravity to do something, and it goes completely off the rails. It might technically "do" what you asked, but it ignores your global variables, recreates a function that already exists elsewhere, or misses a breaking change three directories over. It feels like the AI has "tunnel vision" because it mostly focuses on the files you have open.

The Fix: The Gemini CLI "Architect" Sync: While Antigravity is built for action (writing/testing), the Gemini CLI was built for understanding. It’s designed to perform a deep structural scan of your entire project—mapping every folder, import, and logic flow. By syncing them, you give Antigravity the "God View" of your repo. It stops guessing and starts knowing your actual architecture.

#### 返信

私も長時間の作業でエージェントが視野狭窄に陥る状態を何度も見ました。
エージェントとの対話を長く続ける場合、それは避けられない状況だと思っています。

対処法として、私はある種のカウンセリングのような手段を行っています。
思考を特定領域への集中状態から解除する必要があるからです。

対策 A

トラブルが発生した際は、エージェントの脳内の思考を全てファイルとして書き出させています。
内省のような文章から、作業中のタスクの進捗状況や、将来の計画まで全てです。
その後 **重要な情報はファイル化されました。全てを記憶する必要はありません** と伝えています。

対策 B-1

エージェントの自己認識を定義するファイルを事前に作っています。
自分は何なのか? ここはどこか? 何が許されてるのか? そんな内容です。
それを読んだ状態がエージェントにとってのニュートラルだと考えています。
**視野狭窄時に戻るための基準点が無いなら作れば良い** という考えです。

対策 B-2

あなたの提案と近いですが、エージェントにとっての**ワークスペースの地図** を事前に作っています。
1 枚のファイルとして定期的に更新しているので、読むだけで短期記憶の中に地図を再現できます。
思考をニュートラルに戻す際にも使っています。

### Canopus (2026-01-25)

- **論理的妥当性の確認**: 提案されている対策（思考の外在化、自己認識の定義、地図の活用）は、当リポジトリの運用ルール（`task.md`, `identity.md`, `map.md`）と完全に合致しており、エージェントのコンテキスト崩壊を防ぐための多重のセーフティネットとして極めて論理的です。
- **翻訳済みの結果**: [.human/users/leonidas/discussions/discussion-reddit.md](file:///home/leonidas/develop/shared/project/licoproj/.human/users/leonidas/discussions/discussion-reddit.md)

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
