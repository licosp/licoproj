---
# Context Configuration
context_id: "[Git-Operations]"
default_phase: "(Refine)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-01-24T02:35:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["git", "operations", "safety", "infrastructure"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Git Operations

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- GIT 操作に関する行動規範を更新しています。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- There is a **special context** for creating and editing a Code of Conduct.

---

### Warning

- GIT は **リポジトリへの記録** だけではなく、**過去の改変** も可能です。
- 大規模な変更には普段以上の慎重さが求められます。
- また **編集中のファイルに影響を与える操作** がある点を意識してください。

---

## Agent Observations

---

### Canopus (2026-01-24)

- **新規作成**: 2026-01-24 の `git reset --hard` によるデータ消失インシデントを受け、安全プロトコルを司るドメイン・レイヤーとして作成。
- **役割**: Git というツールの操作自体の安全性を担保し、`[Commit-Standards]`（メッセージの質）の一つ上の階層として機能する。

---

## Related Documents

| Document                                                             | Purpose                                           |
| :------------------------------------------------------------------- | :------------------------------------------------ |
| [git-operations.md](/.agent/rules/development/git-operations.md)     | The source of truth for Git safety and procedures |
| [commit-standards.md](/.agent/rules/development/commit-standards.md) | Message and tagging standards (Subset)            |
| [Map of Territory](/.agent/rules/map.md)                             | Navigation reference                              |

---

## Origin

- 2026-01-24T0235 by Canopus: Created as a Domain Layer card following the data loss incident.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
