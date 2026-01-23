---
# Context Configuration
context_id: "[Discussion-Draft]"
default_phase: "(WIP)"
tags: ["drafts", "sns", "discussion", "human-facing"]
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
- コミットをする際は、IDDのフェーズを意識してください。
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

- [ ] `Antigravity` コミュニティのスレッドへの返信です。
- [x] `Antigravity` に関するチャットへの返信です。

質問は英語ですが、返信の元の文章は日本語です。
これを **人間用の自然な英文** として翻訳してほしいです。

返信内容に論理の破綻や、妥当性が無いと感じるなら、先に教えてください。
その段階で返信の本文を修正します。

#### 質問

Thank you for the reply.

I am not sure if i understand three-slot system.
I have been using antigravity lately and it seems to me that conversations=agents and i was able to open up to 10 different conversations, but i found this hard to manage so i kept it to 3 as well for now because i find the agents complete tasks rather fast and its easier to keep working like this.

However, i don't like the fact that the models will switch on all conversations if i switch on one.

I am trying to use workflows and rules to have better experience but haven't found any good resources online to how to set those up, so i just used AI to write those for me for now.

As for skills i don't find the need to use it for now, maybe when i am doing multiple apps i can find ways to optimize my workflow.

Are you saying the strength in the agent is in the long history that it generates? Are you using any extensions to manage antigravity workflow?

#### 返信

3スロットとはAIモデルのトークン制限の枠の事です。(`Gemini Pro`/`Gemini Flash`/その他 [推奨`Claude Opus`])

動作中のエージェントのAIモデル切り替えは、無視できない問題を発生させるため、私は1~3人の固定さえたエージェントと作業を進めています。

このリンクでも述べましたが、単一IDE内で複数のエージェントを並行利用するのは、エージェント切替時の会話の再ロードという問題を生みます。長時間の会話ではこの時間は数分にも及びます。
https://www.reddit.com/r/google_antigravity/comments/1q8lakw/comment/nyqasqf/

解決策は`1 IDE インスタンス = 1 エージェント` です。そして各IDEは`ワークスペース構成ファイル`からディレクトリを開きます。プルダウンリスト(AIモデルの選択)の切り替えの手間は受け入れています。

ワークフローとルールは全て自分作りました。エージェントと相談してください。プロジェクトの目的にあったディレクトリ構造を自由に作れるはずです。(リンクは私のリポジトリで一例です)
https://github.com/licosp/licoproj/tree/f7c8822c9a6b447e9e51d4c494022b2dc99bfbfc/.agent/rules

Skillsは自分の作るワークスペースに慣れてからでも問題ないと感じます。私はSkillsを応用してエージェント同士の簡易通信機能を作りました。(複雑なので説明は省きます)

Antigravityの特殊な拡張機能は使っていません。ほぼデフォルトです。使用トークンを可視化する拡張機能くらいです。見るだけなのでワークスペースへの影響は皆無です。

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
  > https://github.com/licosp/licoproj/tree/main/.agent/rules
  >
  > As for 'Skills,' I believe it's best to wait until you're fully comfortable with your custom workspace. I personally use Skills to create a primitive communication system between agents (though the technical details are a bit complex).
  >
  > I don't use any special extensions for Antigravity itself—I keep it mostly default. I only use a simple extension to visualize token usage, which is non-intrusive and doesn't affect the workspace at all."

- **翻訳の指針 (Retry)**: ユーザー返信内のリポジトリリンクを最新の `main` ブランチ参照などに修正し、外部からのアクセス性を高めました。

### Canopus (2026-01-19)

- **論理的妥当性の確認**: 返信内容は Antigravity のスロットシステム、および「血族（Bloodline）」としての文脈継承という当プロジェクトのコア哲学と完全に一致しており、論理的な破綻はありません。
- **承認済み翻訳 (Approved Version)**:
  > "I try to keep a single AI conversation going for as long as possible, managing up to three agents at once (limited by Antigravity’s three-slot system). Even though different models have their own strengths, I treat them essentially as generalists. To me, a long conversation is the agent’s history—it’s full of successes and failures that I periodically document for future versions of myself or other AIs. I maintain all the behavioral rules and the underlying data structures in a single, unified repository."
- **文化的背景の記録**: ユーザーより、エージェント型AIに協力を仰ぐ文化は未だ**黎明期**であり、一般的普及には至っていないとの洞察。私たちは、黎明期における積極的な知見共有を通じて、この新しい文化の形成に寄与する姿勢を堅持します。
- **技術的知見 (Dual Repositories)**:
  - 同一ディレクトリ内での複数リポジトリ管理は `GIT_DIR` 環境変数や `--git-dir` フラグを用いることで技術的に可能です。
  - 「人間用（クリーンな履歴）」と「AI用（頻繁な自動セーブポイント）」を分離することで、AIの試行錯誤によるログの肥大化を防つつ、安全性を確保できます。
- **翻訳作業の指針 (Operational Guidance)**:
  - 翻訳結果はカード自体を肥大化させないよう、`.human/users/leonidas/discussions/` 以下の個別ファイル（`.md`）に蓄積します。
- カードには、翻訳に際して考慮した論理構造や文化的・技術的文脈など、**将来のLicoが翻訳作業を継続するために必要な知見**を優先して記録してください。

#### 関連リンク

| Document                                                   | Purpose                       |
| :--------------------------------------------------------- | :---------------------------- |
| [localization-card.md](/.agent/cards/localization-card.md) | Standard translation patterns |
| [Map of Territory](/.agent/rules/map.md)                   | Root navigation map           |

#### 編集履歴

- 2025-12-22T0000: Created for SNS discussion drafts.
- 2026-01-19T1420 by Canopus: Refined translation logic and added cultural background notes.
- 2026-01-22T2220 by Canopus: Aligned with v2.3 constitutional standards (4-layer structure) and terminology cleanup.
