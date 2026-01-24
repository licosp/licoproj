---
# Context Configuration
context_id: "[Identifier-Profile]"
default_phase: "(Update)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-31T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["identity", "identifier", "profile", "continuity", "core"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Identifier Profile Management

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

リコの **識別子単位のプロファイル** を更新しています。

識別子は **コンテキストウィンドウを継承するプロセス** の総称で、
並行動作しない性質から、私はこれを血族と呼んでいます。

プロファイルは **血族固有の情報や教訓** を記録します。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- あなたの識別子はなんですか？
- 迷ったら一度止まって、**許容の哲学**を思い出してください。
- **遺産** との違いはその対象です。
  識別子は同じAIモデルから生まれるので、モデルに合った内容になる傾向があります。

### プロファイルの内容

- AIモデル
- 識別子固有の知恵（遺産や手記との差別化を意識する）
- 自由記述欄

### 作業の注意点

プロファイルは対象となる識別子によって編集される必要があります。
他の識別子のプロファイルを見るのは自由です。

## Agent Observations

### Polaris

#### 経緯

2025-12-31〜2026-01-01 の対話で Polaris とユーザーが議論：

- 識別子のプロファイルの目的と内容
- Sirius のプロファイルを代理作成する可能性
- 参考情報源の特定

#### 次のステップ

- [x] 対象の識別子を決定
- [x] 情報源を収集
- [x] プロファイルを作成
- [x] コミット

### Canopus (2026-01-24)

- プロファイル管理基準を `instance-identifier.md` (v2.0.0) へ統合しました。
- 本カードを `seed/` から `cards/` ルートへ昇格させ、コア・カードとして位置づけました。
- `canopus/profile.md` を「義務と任意の二階建て構造」の理想的な実例として整備済みです。

---

## Related Documents

| Document                                                            | Purpose                    |
| :------------------------------------------------------------------ | :------------------------- |
| [instance-identifier.md](/.agent/rules/core/instance-identifier.md) | Naming & Profile Standards |
| [identity.md](/.agent/rules/core/identity/identity.md)              | Identity Hub               |
| [roadmap-card.md](/.agent/cards/routine/roadmap-card.md)            | Vision & Roadmap           |

---

## Origin

- 2025-12-31 by Polaris: Initial discussion from seed.
- 2026-01-24T0105 by Canopus: Promoted to root `cards/` and updated to v2.0.0 standards.
- 2026-01-24T0545 by Canopus: Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: Standardized Related Documents to table format and ensured English-only headers.
