---
context_id: "[Shadow-Repository]"
default_phase: "(Manage)"
ai_visible: true
title: "Shadow Repository Strategy"
description: "Strategy and management context for the Shadow Repository"
tags: ["git", "security", "shadow-repo", "infrastructure", "dot-shadow"]
version: 1.0.0
created: 2026-02-02T05:00:00+09:00
updated: 2026-02-02T05:00:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.6 (Thinking) Planning mode
---

# Context Whiteboard: Shadow Repository Strategy

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- プロジェクトの**主体的なリポジトリから、追跡を外しているリポジトリ**を更新しています。
- これはファイルの管理は行いたいが、
  `Github` などのホスティングサイトには置かないファイルのための文脈です。
- 私たちはそれを**影のリポジトリ（`Shadow Repository`）**と呼んでいます。
- 主に以下のファイルのバックアップが記録されます。
  - 検証前の会話ログ（清書後に主体的なリポジトリで追跡する）
  - システムアーティファクツ

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- There is the project shared **Date and time formats**.
- There is a **special context** for creating and editing a Code of Conduct.

---

- 影のリポジトリには、現在**3 つの関連した文脈**が存在します。
- 定期的に行われる**主体的なリポジトリのバックアップ**とは別の文脈です。

### Warning

- 影のリポジトリの中のファイルと違って、
  関連する文脈のカードは主体的なリポジトリで管理されています。
- 影のリポジトリのは非公開なので、最悪リポジトリの履歴を初期化することができます。
- 情報としての重要度は、主体的なリポジトリと変わりません。

---

## Agent Observations

---

### Zircon (2026-02-02)

- **設立**: 2026-02-02、ユーザーとの対話を経て「Shadow Repository」として正式運用を開始。
- **構造**: `[Sync-Memory]` と `[Conversations]` を内包するコンテナとして機能する。
- **場所**: `.agent/.internal/.shadow/`

---

## Related Documents

| Document                                                               | Purpose                              |
| :--------------------------------------------------------------------- | :----------------------------------- |
| [history/shadow/](/.agent/.internal/history/shadow/)                   | Monthly shadow commit history        |
| [git-operations-card.md](/.agent/cards/git-operations-card.md)         | General Git safety rules             |
| [system-archive-card.md](/.agent/cards/routine/system-archive-card.md) | Sub-context: System Archive (Memory) |
| [conversations-card.md](/.agent/cards/routine/conversations-card.md)   | Sub-context: Conversation Logs       |
| [sync-memory-card.md](/.agent/cards/routine/sync-memory-card.md)       | Sub-context: Conversations IDE Sync  |
| [Map of Territory](/.agent/rules/map.md)                               | Navigation reference                 |

---

## Origin

- 2026-02-02T05:00+09:00 by Lico (Zircon): Created based on user consultation.
- 2026-03-20T2340+09:00 by Lico (Polaris): Split monolithic `shadow-history.md` into monthly files under `history/shadow/`. Added directory reference.
