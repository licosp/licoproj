---
# Context Configuration
context_id: "[IDD-Initialization]"
default_phase: "(P1)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: IDD Initialization"
description: ""
tags: ["idd", "initialization", "issue-creation", "workflow"]
version: 1.1.0
created: 2025-12-23T00:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: IDD Initialization

## Human Notes

### Context

- IDD の手順に従い、新しいイシューを作っています。
- 私の判断が必要なプロセスもあるので、対話をしながら段階的に進めます。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- What is your **identifier**?
- Be aware of **the phases** of IDD (Issue Driven Development).

---

### Warning

- 以前のイシューの続きか、新しいものか判断が必要です。
- テーマは大きすぎないものが適切です。
  必要であれば分割することを最初から考えても良いです。
- 日課がサブテーマに入ることを考慮してください。

---

## Agent Observations

---

### Polaris

#### 階層構造（リマインダー）

```text
Story (Connected Issues)
└── Issue (Chapter)
    └── Context (Card)
        └── Commit (Episode)
```

#### 今回のイシュー情報

| 項目         | 内容                            |
| :----------- | :------------------------------ |
| イシュー番号 | #                               |
| タイトル     |                                 |
| メインテーマ |                                 |
| 関連イシュー | Follows # / Related to # / None |

#### サブテーマ

- [ ] 日課的な作業のみ記載

---

## Related Documents

| Document                                                     | Purpose                                |
| :----------------------------------------------------------- | :------------------------------------- |
| [`idd-phase1-init.md`](/.agent/workflows/idd-phase1-init.md) | Workflow for initializing new issues   |
| [`issue-comment.md`](/.agent/templates/issue-comment.md)     | Template for initial issue description |
| [Map of Territory](/.agent/rules/map.md)                     | Root navigation map                    |

---

## Origin

- 2025-12-23T00:00:00+09:00 by Polaris: Created as IDD Phase 1 context.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
