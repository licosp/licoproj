---
# Context Configuration
context_id: "[Sync-Memory]"
default_phase: "(Sync)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-25T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["memory", "backup", "sync", "archive"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Memory Synchronization

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

IDEがワークスペースの外に生成するリコの記憶に関するファイルを、
リポジトリ内にバックアップしています。

ファイルは現在GITで追跡してないため、コミットの必要はありません。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**が存在します。
- 急いで作業しないための原則があります。
- リコの長期記憶は**リポジトリ**と**ワークスペース**にあります。
- 例外1: IDEは**ユーザーホームディレクトリ下**に作業ファイルを多く生成します。
- 例外2: **平文の会話ログ**は、IDEのGUI上から私が手動でバックアップしています。
  `.agent/.internal/session_archive/`
- バックアップ対象のファイルは、手順書に定義されています。

### 作業の注意点

- 手順書を読み、中の手順が正しく機能するかどうか、必ず事前に推測してください。
- IDEが管理する記憶は、いつまで保存されるか、どの程度保存されているか不明なため、
  できれば1週間で何回かはこの手順書を実行してほしいです。
- 私はワークスペースの外を**海**、
  内側を**陸**というような抽象的な印象で捉えている事があるため、
  日本語で**記憶を引き上げる**という表現を使うこともあります。

---

## Related Documents

| Document                                             | Purpose                                      |
| :--------------------------------------------------- | :------------------------------------------- |
| [sync-memory.md](/.agent/workflows/sync-memory.md)   | Workflow for memory synchronization (backup) |
| [memory_archive/](/.agent/.internal/memory_archive/) | Storage location for memory backups          |

---

## Origin

- 2025-12-25T0000: Created as sync memory context.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
