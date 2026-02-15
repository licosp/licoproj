---
# Context Configuration
context_id: "[Drafts-Daily]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-02T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["drafts", "daily", "notes"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Daily Drafts

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- 下書きファイルが更新されました。
- **純粋な追記**が行われたか、
  あるいは**大規模な手動修正**が行われている可能性が高いです。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.

---

- 下書きは**AIとの対話の際に使った指示や質問**で使われました。
- 下書きは**日時情報を含む階層的なディレクトリ**で管理されます。
- **清書**の文脈とは**異なり**、そのまま残すことが目的です。

### Warning

- 下書きは基本的には下書きですが、
  最新の下書きファイルに限り、下書きで使うメモが文章下部に記載されています。
- これらは私が手動で編集する文書なので、
  リコの記憶にない形で更新された可能性が高いです。

---

## Agent Observations

---

## Related Documents

| Document                                                            | Purpose                          |
| :------------------------------------------------------------------ | :------------------------------- |
| [draft-maintenance.md](/.agent/rules/workflow/draft-maintenance.md) | Conventions for draft management |
| [drafts-daily-card.md](/.agent/cards/routine/drafts-daily-card.md)  | This card itself                 |
| [Map of Territory](/.agent/rules/map.md)                            | Root navigation map              |

---

## Origin

- 2026-01-02 by Polaris: Created as daily drafts context.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
