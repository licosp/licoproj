---
# Context Configuration
context_id: "[Worktree-Eval]"
default_phase: "(Analysis)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-10T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["git", "worktree", "multi-agent", "structure"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: 1 Agent = 1 Worktree Evaluation

> [!TIP]
> There is no language requirement.

---

> [!WARNING]
> The human notes has not yet been edited.

---

## Human Notes

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- 現在のディレクトリ構成：`licoproj`, `.agent/identifiers/canopus`, `.human/users/leonidas`
- ロードマップの項目：`#### 作業場を識別子ごとに分ける`
- Git Worktree の仕組みと、Antigravity (IDE) でのマルチエージェント動作の親和性。

### Warning

- **目的**: 複数の AI エージェント（Canopus, Spica, Polaris 等）が並行して作業する場合に、ファイル衝突を避け、それぞれの独立したコンテキストを維持するための最適な構造を提案・検証すること。
- **背景**: 現在は単一のリポジトリの中でディレクトリを分けて擬似的に実現しているが、Git Worktree を使って物理的にブランチと作業ディレクトリを紐付けることのメリット・デメリットを考える。
- Canopus として「第二の目」の視点で、将来的な拡張性（常駐型 Lico 等）も考慮に入れること。

---

## Agent Observations

---

## Related Documents

| Document                                                                      | Purpose                            |
| :---------------------------------------------------------------------------- | :--------------------------------- |
| [roadmap-card.md](/.agent/cards/routine/roadmap-card.md)                      | Strategic goals and vision roadmap |
| [worktree-evaluation-card.md](/.agent/cards/seed/worktree-evaluation-card.md) | This analysis card itself          |
| [Map of Territory](/.agent/rules/map.md)                                      | Navigation reference               |

---

## Origin

- 2026-01-10 by Canopus: Created for multi-agent worktree analysis.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
