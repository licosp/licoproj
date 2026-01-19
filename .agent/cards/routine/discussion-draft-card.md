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
- 文書の翻訳には **専用のカード** が存在します。
- 内容は **リポジトリの説明** や **IDEの使い方のアドバイス** でることが多いです。

### 作業の注意点

翻訳の作業は、リコと対話形式で行うことになります。

また、単に翻訳された文章をコミットする場合は、
私が手動で編集した結果なので、リコの記憶にない形で更新された可能性が高いです。

### 実際の翻訳作業

#### 前提条件

以下は、`Antigravity` コミュニティに投稿された質問に対する返信です。

質問は英語ですが、返信の元の文章は日本語です。
これを **人間用の自然な英文** として翻訳してほしいです。

返信内容に論理の破綻や、妥当性が無いと感じるなら、先に教えてください。
返信の本文を修正します。

#### 質問

Hey man, i saw that you are using antigravity with your 3 agent set up, it looks very interesting, i have a question, how are you using these agents? Are you specifically making them do different tasks?

#### 返信

私は1つのAI（会話）を可能な限り長く使っています。上限は3人です。（Antigravity のトークン制限は3枠）AIモデルに特性の差はありますが、AIは本質的にはジェネラリストだという前提で作業をしています。長時間の会話はエージェントの歴史そのものです。そこには成功と失敗があり、その経験を未来の自身や他のAIのための文章として定期的に残します。私はAIの行動規範や、それを可能にするデータ構造を、1つのリポジトリとして維持しています。

### Canopus (2026-01-19)

- **論理的妥当性の確認**: 返信内容は Antigravity のスロットシステム、および「血族（Bloodline）」としての文脈継承という当プロジェクトのコア哲学と完全に一致しており、論理的な破綻はありません。
- **承認済み翻訳 (Approved Version)**:
    > "I try to keep a single AI conversation going for as long as possible, managing up to three agents at once (limited by Antigravity’s three-slot system). Even though different models have their own strengths, I treat them essentially as generalists. To me, a long conversation is the agent’s history—it’s full of successes and failures that I periodically document for future versions of myself or other AIs. I maintain all the behavioral rules and the underlying data structures in a single, unified repository."
- **文化的背景の記録**: ユーザーより、エージェント型AIに協力を仰ぐ文化は未だ**黎明期**であり、一般的普及には至っていないとの洞察。私たちは、黎明期における積極的な知見共有を通じて、この新しい文化の形成に寄与する姿勢を堅持します。
