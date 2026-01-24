---
# Context Configuration
context_id: "[Routine]"
default_phase: "(Daily)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-14T23:20:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["routine", "daily", "日課", "maintenance"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Daily Routine (日課)

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

日常的な作業として**日課**を行っています。
一日に一回、日付の変更に気づいた時に頼むことが多いです。

日課には簡易版と完全版があります。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- あなたの識別子はなんですか？
- 迷ったら一度止まって、**許容の哲学**を思い出してください。

### 作業の注意点

**簡易版の日課**は他の識別子が完全版の日課を行った場合に選ばれます。
どちらか分からない場合は、私に確認してみてくだしさい。

## Agent Observations

### Polaris (2026-01-14T2320)

- カード新規作成
- 目的: 「日課がしたい」という入力から直接発見できる入口
- IDD P2 経由の導線は維持（IDD作業中の定型作業として）

### Polaris (2026-01-15T0238)

> [!NOTE]
> 日課の詳細手順は [routine-daily.md](/.agent/workflows/routine-daily.md) を参照。
> このカードは観測記録のみ。手順の重複は避ける。

#### 簡易版の日課

= Calibration（完全版の Step 5）

5つのファイルを読むだけ。詳細は workflow を参照。

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
| [routine-daily.md](/.agent/workflows/routine-daily.md) | Main daily routine workflow         |
| [ritual_start.md](/.agent/workflows/ritual_start.md)   | Session start ritual                |
| [ritual_mid.md](/.agent/workflows/ritual_mid.md)       | Intermediate ritual (+10,000 lines) |
| [ritual_end.md](/.agent/workflows/ritual_end.md)       | Session end ritual                  |

---

## Origin

- 2026-01-14T2320 by Polaris: Created for daily entrance.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
