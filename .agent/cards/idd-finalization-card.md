---
# Context Configuration
context_id: "[IDD-Finalization]"
default_phase: "(P3)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-23T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["idd", "finalization", "cleanup", "workflow"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: IDD Finalization

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- イシューの各種テーマが達成されたので、イシューを完結させてています
- IDD の手順に従い、リモートメインへのマージを行ってください。

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

- かつてリモートブランチを削除してしまったリコがいました、
  コミット内容はぼぼ文章なので、容量を気にする必要はありません。

---

## Agent Observations

---

### Polaris

#### 今回のイシュー情報

| 項目         | 内容 |
| :----------- | :--- |
| イシュー番号 | #    |
| PR 番号      | #    |
| ブランチ名   |      |

#### 完了前チェックリスト

- [ ] すべての Issue 要件が実装済み
- [ ] サブテーマがすべてコミット済み
- [ ] 作業ディレクトリがクリーン
- [ ] Issue コメントに進捗報告済み

---

## Related Documents

| Document                                                   | Purpose                                    |
| :--------------------------------------------------------- | :----------------------------------------- |
| [idd-phase3-fini.md](/.agent/workflows/idd-phase3-fini.md) | Workflow for finalizing and merging issues |
| [issue-comment.md](/.agent/templates/issue-comment.md)     | Template for final progress reports        |
| [Map of Territory](/.agent/rules/map.md)                   | Navigation reference                       |

---

## Origin

- 2025-12-23 by Polaris: Created as IDD Phase 3 context.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
