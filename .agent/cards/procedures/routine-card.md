---
# Context Configuration
context_id: "[Routine]"
default_phase: "(Daily)"
# Shared Configuration
ai_visible: true
version: 1.2.0
created: 2026-01-14T23:20:00+09:00
updated: 2026-01-28T16:30:00+09:00
tags: ["routine", "daily", "日課", "maintenance"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Daily Routine

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- 日常的な作業として**日課**を行っています。
- 一日に一回、日付の変更を気づいた時に頼むことが多いです。
- 日課には**簡易版**と**完全版**があります。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- What is your **identifier**?
- When in doubt, stop and remember the **philosophy of tolerance**.

---

### Warning

- **簡易版の日課**は他の識別子が完全版の日課を行った場合に選ばれます。
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
> 日課の詳細手順は [routine-daily.md](/.agent/workflows/routine-daily.md) を参照。
> このカードは観測記録のみ。手順の重複は避ける。

#### 簡易版の日課

= Calibration（完全版の Step 5）

5 つのファイルを読むだけ。詳細は workflow を参照。

#### 完全版の日課

| Step | 概要                   |
| :--- | :--------------------- |
| 0    | Scan Changes           |
| 1    | Commit by Context      |
| 2    | Read Last Checkpoint   |
| 3    | Commit Check           |
| 4    | Write Checkpoint       |
| 5    | Calibration (= 簡易版) |

詳細手順 → [routine-daily.md](/.agent/workflows/routine-daily.md)

---

## Related Documents

| Document                                               | Purpose                             |
| :----------------------------------------------------- | :---------------------------------- |
| [Ritual Gateway](/.agent/workflows/ritual.md)          | Mandatory Entry Point (Safety Lock) |
| [routine-daily.md](/.agent/workflows/routine-daily.md) | Main daily routine workflow         |
| [Ritual Gateway](/.agent/workflows/ritual.md)          | Session Rituals (Start/Mid/End)     |
| [Map of Territory](/.agent/rules/map.md)               | Root navigation map                 |

---

## Origin

- 2026-01-14T2320 by Polaris: Created for daily entrance.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
