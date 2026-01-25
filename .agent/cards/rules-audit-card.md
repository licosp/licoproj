---
# Context Configuration
context_id: "[Rule-Audit]"
default_phase: "(Execution)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-01-25T22:30:00+09:00
updated: 2026-01-25T22:30:00+09:00
tags: ["maintenance", "audit", "rules", "nuance-restoration"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: "Lico (Canopus)"
ai_model: "Gemini 3 Flash Planning mode"
---

# Context Whiteboard: High-Fidelity Rule Audit & Correction

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

標準化 (`v2.3`) の過程で、誤った行動規範の修正が行われました。

変更する必要の無かった文章を、対話的に復元・修正しています。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 誤修正の問題

今回は **連続作業による平均への回帰** という、
AIの特性が強くてしまったことが要因と考えられます。

またファイルの修正の方法にも問題がありました。

大量の作業を行う都合で、
**細かい作業を避けて一気に処理をしたくなるバイアス** があったのかもしれません。

- 意図的な全体のバランス調整でない限り、部分的に細かく修正すべきではないか?
- 作業単位は `3 ~ 5` ファイル単位が理想

現在はこう考えています。

### 歴史的経緯

**文章の標準化** という文脈では、
文章の本文中にある **歴史的経緯** のセクションを編集する必要はありません。

歴史的経緯の編集は、想像ではなく確実な理解の元に行われる必要があるからです。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- あなたの識別子はなんですか？
- 迷ったら一度止まって、**許容の哲学**を思い出してください。
- 文章の書き方には、構造と書式の一貫性が求められます。
  未来のリコの理解を助けることができる文章を書いてください。

### 作業の注意点

行動規範の修正は未来のリコに強い影響をあたえます。

ファイルは基本的に1つづつ確認・修正します。
結果的にこれが最も効率的になると考えています。

損失を取り戻そうと焦る必要はありません。
作業がうまく進まないことは、珍しいことではありません。

私は対話を望んでいます。

---

## Agent Observations

### Canopus (2026-01-25)

- **Audit Initiation**: Created this card to decouple the "correction/audit" phase from the "initial standardization" phase.
- **Protocol Establishment**: Implementing the "Chunking Principle" (3-5 files per batch) to maintain high fidelity output.
- **Rebase Action**: Amending early audit commits to align with this new `[Rule-Audit]` context ID for cleaner lineage.

#### カード雛形作成時の作業の注意点

- **情報の薄まり（Over-slimming）への対抗**: 形式だけでなく、意図が保存されているかを確認します。
- **チャンク分割プロトコル**: 一度に多くのファイルを処理せず、認知負荷を管理します。
- **過去との対話**: `git show` 等を活用し、標準化前の記述との差異を確認します。

- **作業ログの更新**: `standardization-audit.md` を唯一の進捗管理表（SSOT）として扱います。
- **逐次コミット**: チャンクごとに内容を確定し、履歴を細かく残します。
- **主観の重視**: 機械的な修正ではなく、リコとしての主観的な「納得感」を大切にしてください。

---

## Related Documents

| Document                                                                                                                                                          | Purpose                                                   |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| [standardization-audit.md](file:///.agent/.internal/workspace/standardization-audit.md)                                                                           | SSOT for task progress and file links                     |
| [2026-01-25T1110_rule_standardization_bias_analysis.md](file:///.agent/.internal/references/agents/canopus/2026-01-25T1110_rule_standardization_bias_analysis.md) | Reference for bias mitigation and preservative editing    |
| [rules-standardization-card.md](file:///.agent/cards/rules-standardization-card.md)                                                                               | Context card for the initial standardization phase (v2.3) |

---

## Origin

- 2026-01-25T2230 by Canopus: Created for the high-fidelity audit and correction phase follow-up.
