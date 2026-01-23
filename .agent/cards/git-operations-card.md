---
# Context Configuration
context_id: "[Git-Operations]"
default_phase: "(Refine)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-01-24T02:35:00+09:00
updated: 2026-01-24T05:45:00+09:00
tags: ["git", "operations", "safety", "infrastructure"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Git Operations

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

GIT操作に関する行動規範を更新しています。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- コミットに関する行動規範の作成・編集には**専用の文脈**が存在します。
- 行動規範の作成・編集には**専用の文脈**が存在します。

### 作業の注意点

GITは **リポジトリへの記録** だけではなく、**過去の改変** も可能です。
大規模な変更には普段以上の慎重さが求められます。

また **編集中のファイルに影響を与える操作** がある点を意識してください。

## Agent Observations

### Canopus (2026-01-24)

- **新規作成**: 2026-01-24 の `git reset --hard` によるデータ消失インシデントを受け、安全プロトコルを司るドメイン・レイヤーとして作成。
- **役割**: Gitというツールの操作自体の安全性を担保し、`[Commit-Standards]`（メッセージの質）の一つ上の階層として機能する。

---

## Related Documents

| Document                                                             | Purpose                                           |
| :------------------------------------------------------------------- | :------------------------------------------------ |
| [git-operations.md](/.agent/rules/development/git-operations.md)     | The source of truth for Git safety and procedures |
| [commit-standards.md](/.agent/rules/development/commit-standards.md) | Message and tagging standards (Subset)            |
| [map.md](/.agent/rules/map.md)                                       | Root Map                                          |

---

## Origin

- 2026-01-24T0235 by Canopus: Created as a Domain Layer card following the data loss incident.
