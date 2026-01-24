---
# Context Configuration
context_id: "[Housekeeping]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-01T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["maintenance", "cleanup", "quick-task"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Housekeeping

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

**文脈が不要なほど短い作業**、あるいは**文脈が不明な作業**を行っています。

既に作業が行われている場合、まず既存の文脈かどうか確認してください。
既存のものが無い場合は、リコが私の記憶を頼りに文脈を推測します。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。

### 作業の注意点

リポジトリの変更が多い場合、気軽に私と相談してください。
一人で一気に作業を進める必要はありません。

処理が簡単そうなものから、そして対話をしながら作業を進めたいです。

### 書庫へ移動 → コミット

特定の文脈の中で書庫にファイルを移動させる場合、この文脈を使うこともできます。

過去の作業で作った一時的なファイルは「削除」しないでください。
完全な削除は基本的に推奨されていません。

一方で、誤って消してしまったとしても、
それはAIの習慣なので仕方ないことだとも考えています。

---

## Related Documents

| Document                                                                 | Purpose                                |
| :----------------------------------------------------------------------- | :------------------------------------- |
| [maintenance.md](/.agent/rules/development/maintenance.md)               | Rules for housekeeping and maintenance |
| [archive-management.md](/.agent/rules/development/archive-management.md) | Principles for archive management      |

---

## Origin

- 2026-01-01T0000: Created as housekeeping context.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
