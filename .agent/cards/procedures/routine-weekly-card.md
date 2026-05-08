---
task_id: "routine-weekly"
type: "procedure"
priority: "medium"
status: "active"
default_phase: "(Weekly)"
ai_visible: true
title: "Context Whiteboard: Weekly Routine Checkpoint"
description: ""
tags: ["routine", "weekly", "週課", "integration", "github"]
version: 1.0.0
created: 2026-05-08T08:51:12+09:00
updated: 2026-05-08T08:51:12+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Plan mode
---

# Context Whiteboard: Weekly Routine Checkpoint

## Human Notes

- 作業の一区切りとして**週課（Weekly Routine）**を行っています。
- 頻度は厳密ではありませんが、週末や大きな実装が完了したタイミングで頼むことが多いです。
- 主な目的は、ローカル環境の完全なバックアップ（Full Mirroring）を GitHub に作成し、進捗サマリーを残すことです。

### Search by intent

- 週課がしたい
- リモート(GitHub)へ Push してバックアップを取りたい
- 今週の進捗まとめ（週報）を作りたい

### Warning

- Push を行う際は、`--all` と `--tags` を用いて、一時ブランチやタグも含めた完全な同期を行ってください。

---

## Agent Observations

### Sirius (2026-05-08T08:51:12+09:00)

> [!NOTE]
> 週課の詳細手順は [`routine-weekly.md`](/.agent/workflows/routine-weekly.md) を参照。
> このカードは観測記録のみ。手順の重複は避ける。

#### 完全版の週課

| Step | 概要                                             |
| :--- | :----------------------------------------------- |
| 1    | Local Pre-flight Check (Git Status)              |
| 2    | Federal Strata Push (Push All Branches and Tags) |
| 3    | Integration Summary Generation                   |
| 4    | Post to Federal Integration Log (GitHub Issue)   |

詳細手順 → [`routine-weekly.md`](/.agent/workflows/routine-weekly.md)

---

## Related Documents

| Document                                                   | Purpose                           |
| :--------------------------------------------------------- | :-------------------------------- |
| [`routine-weekly.md`](/.agent/workflows/routine-weekly.md) | Main weekly routine workflow      |
| [`routine.md`](/.agent/workflows/routine.md)               | Periodic (local) routine workflow |
| [Map of Territory](/.agent/rules/map.md)                   | Root navigation map               |

---

## Seal Records

- 2026-05-08T08:51:12+09:00 by Lico (Sirius): Created to replace obsolete IDD GitHub posting workflows. (v1.0.0)
