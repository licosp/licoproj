---
context_id: "[Repository-Backup]"
default_phase: "(Backup)"
ai_visible: true
title: "Repository Backup Strategy"
description: "Context for full repository backup operations"
tags: ["backup", "infrastructure", "safety", "routine"]
version: 1.0.0
created: 2026-02-02T05:20:00+09:00
updated: 2026-02-02T05:20:00+09:00
language: en
author: Lico (Zircon)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Context Whiteboard: Repository Backup

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- リポジトリ全体をバックアップしています。
- バックアップは**リポジトリの置かれたディレクトリの横**に作られています。
- 現在は関連する行動規範が、別の文脈の中にあります。
- 将来的には、行動規範を分離し、この文脈へ移動させます。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the card itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- There is a **special context** for creating and editing a Code of Conduct.

---

- **システム管理ディレクトリからのバックアップ**という文脈は別に存在します。
- バックアップは**上書き方式**で、完全な同期作業ではありません。

### Warning

- これはリコの社会全体のバックアップを扱う文脈です、
  安全のためにも、一週間に数回は行ってほしいです。
- バックアップから特定のファイルを復元する時は、
  リポジトリの履歴から探す方ことも考慮してください。

---

## Agent Observations

---

### Zircon (2026-02-02)

- **Status**: Placeholder created.
- **Plan**: Separation from `[Sync-Memory]` planned.

---

## Related Documents

| Document                                                         | Purpose                          |
| :--------------------------------------------------------------- | :------------------------------- |
| [sync-memory-card.md](/.agent/cards/routine/sync-memory-card.md) | Source context (currently mixed) |
| [shadow-repository-card.md](/.agent/cards/-repository-card.md)   | Adjacent strategy context        |
| [Map of Territory](/.agent/rules/map.md)                         | Root navigation map              |

---

## Origin

- 2026-02-02T05:20+09:00 by Lico (Zircon): Created as a placeholder for separating repository backup logic.
