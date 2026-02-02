---
# Context Configuration
context_id: "[Conversations-IDE]"
default_phase: "(Archive)"
# Shared Configuration
ai_visible: true
title: "System Archive Management"
description: "Context for handling system artifacts and manual exports"
tags: ["system-archive", "backup", "manual", "routine"]
version: 1.0.0
created: 2026-02-02T05:05:00+09:00
updated: 2026-02-02T05:05:00+09:00
language: en
author: Lico (Zircon)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Context Whiteboard: System Archive

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- IDE から手動でエクスポートした会話ログを、ファイルとしてバックアップしています。
- **手動作業の結果置き場**なので、リコが能動的に何かを編集することは稀です。
- **地図への反映** 等で参照する必要があります。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- The directory where conversation logs are stored has its **special context**.
- Card files are tracked in **the shadow repository**.

---

- ここで保存される会話ログは副次的なものになりました。
  正式な会話ログ管理のための**専用の文脈**があります。

### Warning

- この文脈は 2 つのリポジトリに跨ったものです。
  文脈 ID はその両方で使われます。
- バックアップは人間が手動で行うものなので、
  リコが記憶にない形で更新された可能性が高いです。

---

## Agent Observations

---

### Zircon (2026-02-02)

- **位置づけ**: `[Sync-Memory]` の一部とも取れるが、より静的で手動依存の強い領域として分離。
- **現状**: Shadow Repository (.agent/.internal/.shadow/) の管理下にある。

---

## Related Documents

| Document                                                             | Purpose                          |
| :------------------------------------------------------------------- | :------------------------------- |
| [sync-memory-card.md](/.agent/cards/routine/sync-memory-card.md)     | Related context: Usage of memory |
| [shadow-repository-card.md](/.agent/cards/shadow-repository-card.md) | Parent context: Strategy         |
| [Map of Territory](/.agent/rules/map.md)                             | Root navigation map              |

---

## Origin

- 2026-02-02T05:05+09:00 by Lico (Zircon): Created as a dedicated card for manual memory archives.
