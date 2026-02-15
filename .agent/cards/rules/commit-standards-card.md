---
# Context Configuration
context_id: "[Commit-Standards]"
default_phase: "(Done)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-22T20:45:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["git", "standards", "commit", "convention"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Commit Standards

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- コミットに関する行動規範を更新しています。
- **行動規範**だけではなく、**コミットテンプレート**の更新もその対象になります。

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

- コミットはリコの歴史の検索性に直結します。
- **未来のリコが文脈を特定できないコミット** は避けてください。

---

## Agent Observations

---

### Canopus (2026-01-22)

**カードの新規作成**:
ユーザーの指摘により、「文脈はあるのにカードがない」状態を解消するために作成。
`[Commit-Standards]` は、規約自体の管理や、歴史の修復（Repair）において、意味層（Semantic）のコンテキストとして機能する。
今後はこのカードの Observations に、特定の絵文字の使用、Scope の切り出し方、あるいは大規模修復時のパターンなどを蓄積していく。

#### 初期の注意点

- 1 行目の形式を厳守してください: `<Identifier>: [ID-1][ID-2] <type>: <subject> (Phase)`
- ファイルの削除は「アーカイブ」として扱い、履歴を抹消しないでください。
- 大規模なファイル変更の際は、コミットボディでの要約を徹底してください。

---

## Related Documents

| Document                                                                    | Purpose                              |
| :-------------------------------------------------------------------------- | :----------------------------------- |
| [commit-standards.md](/.agent/rules/development/commit-standards.md)        | The source of truth for commit rules |
| [context-card-workflow.md](/.agent/rules/workflow/context-card-workflow.md) | Hierarchical tagging protocol        |
| [Map of Territory](/.agent/rules/map.md)                                    | Root navigation map                  |

---

## Origin

- 2026-01-22T2045 by Canopus: Created.
- 2026-01-22T2210 by Canopus: Aligned with v2.3 constitutional standards (4-layer structure).
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
