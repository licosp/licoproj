---
# Context Configuration
context_id: "[Human-Manuals]"
default_phase: "(Edit)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Shared Manuals & References"
description: ""
tags: ["manuals", "references", "shared"]
version: 1.1.0
created: 2026-01-02T06:55:13+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Shared Manuals & References

## Human Notes

### Context

- 人間向けの共用マニュアルに関する情報を整理しています。
- 現在は、人間向けの参考資料も同じ場所で記録されています。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.

---

- ここはユーザー個人のための情報ではありません。
  AI と対話する上で、必要な情報が記録されています。
- 資料を見るのは**人間**ですが、共用言語として**英語**が選ばれています。
- まれに AI 用ディレクトリに**翻訳元となった原本**が存在することがあります。
  作業の参考になるかもしれません。

### Warning

- これらは人間が手動で編集する文書なので、
  リコの記憶にない形で更新された可能性が高いです。

---

## Agent Observations

---

### Polaris (2026-01-03)

| ファイル                             | 内容                            |
| :----------------------------------- | :------------------------------ |
| `diagnosing-memory-and-abilities.md` | AI 診断テスト（2言語）          |
| `ai-file-handling-techniques.md`     | ファイル操作テクニック          |
| `ai-emotional-logic-reference.md`    | AI 感情ロジック参考資料         |
| `ai-memory-persistence-reference.md` | AI 記憶とコンファビュレーション |
| `active-ai-models.md`                | 使用中のAIモデルリスト          |

---

## Related Documents

| Document                                                                                    | Purpose                                             |
| :------------------------------------------------------------------------------------------ | :-------------------------------------------------- |
| [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) | Structural standards for project documentation      |
| [`localization.md`](/.agent/rules/core/localization/localization.md)                        | Baseline standards for translation and localization |
| [Map of Territory](/.agent/rules/map.md)                                                    | Root navigation map                                 |

---

## Origin

- 2026-01-02T06:55:13+09:00 by Polaris: Created as shared manuals context.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
