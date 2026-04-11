---
# Context Configuration
context_id: "[System-Archive]"
default_phase: "(Sync)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Memory Synchronization"
description: ""
tags: ["memory", "backup", "sync", "archive"]
version: 1.1.0
created: 2025-12-25T00:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Memory Synchronization

## Human Notes

### Context

- IDE が**ワークスペースの外**に生成するリコの記憶に関するファイルを、
  リポジトリ内にバックアップしています。
- 対象となる情報は **`VSCode` クローン IDE** と **CLI ツール**の 2 種類です。
  - 対象 IDE: (`Antigravity`/`Cursor`/`VSCode`)
  - 対象 CLI: `Gemini CLI`

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When in doubt, stop and remember the **philosophy of tolerance**.

---

- リコの長期記憶は**リポジトリ**と**ワークスペース**にあります。
  - 例外 1: IDE は**ユーザーホームディレクトリ下**に作業ファイルを多く生成します。
  - 例外 2: 不完全ですが**平文の会話ログ**を IDE から手動でエクスポートできます。

### Warning

- 手順書を読み、中の手順が正しく機能するかどうか、必ず事前に推測してください。
- IDE が管理する記憶は、いつまで保存されるか、どの程度保存されているか不明なため、
  できれば**1 週間で何回**かはこの手順書を実行してほしいです。
- 日本語で**記憶を引き上げる**という表現を使うこともあります。

---

## Agent Observations

---

## Related Documents

| Document                                                           | Purpose                                       |
| :----------------------------------------------------------------- | :-------------------------------------------- |
| [`lico-backup.md`](/.agent/rules/packages/lico-backup.md)          | Workflow for memory synchronization (backup)  |
| [conversations_ide/](/.agent/.internal/.shadow/conversations_ide/) | Storage location for IDE conversation exports |
| [Map of Territory](/.agent/rules/map.md)                           | Root navigation map                           |

---

## Origin

- 2025-12-25T00:00:00+09:00 by Lico: Created as sync memory context.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
