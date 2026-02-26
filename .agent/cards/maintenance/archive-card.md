---
# Context Configuration
context_id: "[Archive]"
default_phase: "(Organize)"
# Shared Configuration
ai_visible: true
title: "Archive Management"
description: "Management of the repository's library and historical records."
tags: ["archive", "history", "library", "preservation"]
version: 1.0.0
created: 2026-02-15T02:10:00+09:00
updated: 2026-02-15T02:10:00+09:00
language: en
author: Lico (Sirius)
ai_model: "Gemini 3 Pro (High)"
---

# Context Whiteboard: Archive Management

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.

- Organizing historical documents.
- Retrieving past context.
- Defining directory structures for long-term storage.

---

### Warning

- 過去の作業で作った一時的なファイルは**削除しないで**ください。
  完全な削除は基本的に**推奨されていません**。
- 一方で、誤って消してしまったとしても、
  それは**AIの習慣なので仕方ない**ことだとも考えています。

---

## Agent Observations

### Sirius (2026-02-15)

- **新規作成**: 家事 (`Housekeeping`) と区別し、純粋な「保管場所の管理」を行うために分離・新設。
- **構造統一**: 人間用書庫も `.internal` 下に移動し、AI 用と同じ構造を採用。

#### Context

- リポジトリ内の **書庫 (Archive)** を管理するためのカードです。
- **家事 (Housekeeping)** が「片付け」を担当するなら、このカードは「保管と分類」を担当します。
- 3 つの書庫が存在します：
  1. **AI用（表）**: `.agent/.internal/archive/`
  2. **AI用（影）**: `.agent/.internal/.shadow/archive/`
  3. **人間用**: `.human/.internal/archive/`

#### Warning

- 書庫内のファイルは「歴史的記録」であり、原則として **書き換えない** こと。
- 整理のための **移動** や **リネーム** は許可されます。

---

## Related Documents

| Document                                                                 | Purpose                           |
| :----------------------------------------------------------------------- | :-------------------------------- |
| [archive-management.md](/.agent/rules/development/archive-management.md) | Principles for archive management |
| [Map of Territory](/.agent/rules/map.md)                                 | Root navigation map               |

---

## Origin

- 2026-02-15T02:10+09:00 by Sirius: Created to standardize archive management.
