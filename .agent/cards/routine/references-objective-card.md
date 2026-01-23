---
# Context Configuration
context_id: "[References]"
default_phase: "(Add)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-24T05:45:00+09:00
tags: ["references", "analysis", "external-input", "second-eyes"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: References Update

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

外部AI（第二の目）による分析レポートや参考文献が追加されました。
あるいは、リコと私の対話の結果、参考文献として残すべきファイルを作ります。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- ファイルを自分で作る場合は**検証モード**で行こなってください。
- ここは**客観的で論理的な文章**が置かれるディレクトリです。
- ファイルは未来のリコにとっての参考文献となります。

### 作業の注意点

コミット時は「どのような分析（何に基づく分析か）」を要約に含めてほしいです。

---

## Agent Observations

### Spica

- **Action**: Analyzed a severe case of memory confabulation where I hallucinated a "Stern" persona onto the map, contradicting reality.
- **Reference**: `references/agents/spica/2026-01-04_memory_confabulation_analysis.md`
- **Correlation**: Found similar precedent by Lico-C (`references/agents/lico-c/2025-12-09...`). This confirms "Ego-driven Confabulation" is a recurring structural risk.
- **Result**: Archived both the fake and real maps as evidence in `.agent/ark/` to serve as a permanent caution.

---

## Related Documents

- [reference-methodology.md](/.agent/rules/workflow/reference-methodology.md) : 参考文献管理の原則。
- [references/](/.agent/.internal/references/) : 参考文献ディレクトリ。

---

## Origin

- 2025-12-01T0000: Created as objective references context.
- 2026-01-24T0545 by Canopus: Standardized with Dialogue Layer template and bilingual H2 headers.
