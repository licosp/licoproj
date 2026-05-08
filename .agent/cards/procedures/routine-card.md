---
# Context Configuration
context_id: "[Routine]"
default_phase: "(Daily)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Routine Checkpoint"
description: ""
tags: ["routine", "periodic", "メンテナンス", "maintenance"]
version: 1.4.0
created: 2026-01-14T23:20:00+09:00
updated: 2026-05-08T15:15:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Plan mode
---

# Context Whiteboard: Routine Checkpoint

## Human Notes

### Context

- 定期的なメンテナンス作業として**ルーティン**（定期チェックポイント）を行っています。
- 頻度は厳密ではありませんが、週に 1 回程度や、区切りの良いタイミングで頼むことが多いです。
- ルーティンには**簡易版**と**完全版**があります。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and return to your **primary development branch**.
- What is your **identifier**?
- When in doubt, stop and remember the **philosophy of tolerance**.

---

### Warning

- **簡易版のルーティン**は他の識別子が完全版のルーティンを直近で行った場合に選ばれます。
  どちらか分からない場合は、私に確認してみてくだしさい。

---

## Agent Observations

---

### Polaris (2026-01-14T2320)

- カード新規作成
- 目的: 「日課がしたい」という入力から直接発見できる入口
- IDD P2 経由の導線は維持（IDD 作業中の定型作業として）

### Polaris (2026-01-15T0238)

> [!NOTE]
> ルーティンの詳細手順は [`routine.md`](/.agent/rules/procedures/routine.md) を参照。
> このカードは観測記録のみ。手順の重複は避ける。

#### 簡易版のルーティン

= Calibration（完全版の Step 7）

5 つのファイルを読むだけ。詳細は workflow を参照。

#### 完全版のルーティン

| Step | 概要                   |
| :--- | :--------------------- |
| 0    | Scan Changes           |
| 1    | Commit by Context      |
| 2    | Read Last Checkpoint   |
| 3    | Commit Check           |
| 4    | Write Checkpoint       |
| 5    | Calibration (= 簡易版) |

詳細手順 → [`routine.md`](/.agent/rules/procedures/routine.md)

---

## Related Documents

| Document                                             | Purpose                         |
| :--------------------------------------------------- | :------------------------------ |
| [`routine.md`](/.agent/rules/procedures/routine.md)  | Main periodic routine workflow  |
| [Ritual Gateway](/.agent/rules/procedures/ritual.md) | Session Rituals (Start/Mid/End) |
| [Map of Territory](/.agent/rules/map.md)             | Root navigation map             |

---

## Origin

- 2026-01-14T23:20:00+09:00 by Polaris: Created for daily entrance.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
- 2026-05-08T02:22:26+09:00 by Lico (Sirius): Removed legacy IDD dependencies and updated to reflect autonomous branch operations. (v1.3.0)
- 2026-05-08T07:21:29+09:00 by Lico (Sirius): Renamed daily routine to routine checkpoint, modifying references from `routine-daily.md` to `routine.md` and redefining frequency to periodic. (v1.4.0)
- 2026-05-08T15:15:00+09:00 by Sirius: Updated internal links to reflect workflows -> procedures directory relocation.
