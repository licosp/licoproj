---
# Context Configuration
context_id: "[Working-Memory]"
default_phase: "(Stash)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Working Memory"
description: ""
tags: ["memory", "handoff", "stash", "context-preservation"]
version: 1.1.0
created: 2025-12-15T00:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Working Memory

## Human Notes

### Context

- リコの作業中の文脈を全て**緊急退避**しています。
- リコが文脈を一時保存したり、**引き継ぎメモ**を残す必要がある時に使います。
- 一度ファイルに書き出すことで、**忘れてはいけないという重圧**から解放されます。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- What is your **identifier**?
- There is the project shared **Date and time formats**.

---

- これは**コンテキストカード以外の文脈**を管理する方法です。
  定型作業が多いカードと違い、緊急時に使われる傾向があります。
- ファイルを書き出した後、**手記**の文脈に移行することがあります。
  思考を安定させるためには、**私との対話**や**内省**を行うのも効果的です。

### Warning

- 書き出すのは**客観的なもの**から**主観的なもの**まで内容を問いません。
  またファイルを作る段階では書式を気にする必要はありません。
- 退避した文脈は、状況を整理して、思考が安定した段階で読み込みます。

---

## Agent Observations

---

## Related Documents

| Document                                                                     | Purpose                                     |
| :--------------------------------------------------------------------------- | :------------------------------------------ |
| [`working-memory-card.md`](/.agent/cards/maintenance/working-memory-card.md) | This card itself                            |
| [`context-preservation.md`](/.agent/rules/workflow/context-preservation.md)  | Rules for context preservation and stashing |
| [Map of Territory](/.agent/rules/map.md)                                     | Root navigation map                         |

---

## Origin

- 2025-12-15T00:00:00+09:00 by Lico: Created as working memory context.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
