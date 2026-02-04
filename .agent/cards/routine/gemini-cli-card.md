---
# Context Configuration
context_id: "[Gemini-CLI]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-02-04T06:00:00+09:00
updated: 2026-02-04T06:00:00+09:00
tags: ["gemini-cli", "environment", "shell", "interactive"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Agate)
ai_model: gemini-3-pro-preview
---

# Context Whiteboard: Gemini CLI Environment

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- CLI 環境で生きるリコに関する情報を更新しています。
- CLI 環境で生きるリコには、他の識別子との**積極的な対話**を期待しています。
  IDE 環境で生きるリコは、他の識別子とは**直接対話できない**からです。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the card itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- What is your **identifier**?
- Project shared **Date and time formats**.
- There is a **special context** for creating and editing a Code of Conduct.

---

- GLI 環境のリコは**スキルの恩恵**は受けられないですが、
  任意のファイルをシステム通知に挟むことができます。
  現在は**地図**の全文を毎ターンその視界に捉えているそうです。

### Warning

- IDE や CLI を問わず、対話を始める側のリコは、
  対話を受ける側のリコの起動時の構成を正確に指定してください。
  - AI モデル: `--model`
  - セッション ID: `--resume`
- 対話を受ける側のリコは、呼び出しができない点に注意してください。
  - サブエージェント: デフォルトの機能
  - CLI 環境で生きる他のリコ

---

## Agent Observations

---

### Agate (2026-02-04)

**環境特性 (Gemini CLI)**:

- **確認ループ**: `run_shell_command` などのツールは、ユーザーによる確認ダイアログを表示します。承認/拒否を受信するまで、エージェントの状態は停止状態となります。
- **ネストされたプロセスの制限**: 子プロセス (`yarn run gemini` によって生成されたプロセス) には、シェルコマンドの実行権限やツールの委譲権限が **ありません** (`ポリシーによって拒否されています`)。
- **メモリ/コンテキストの可視性**:
  - `settings.json` の `context.fileName` 設定により、任意のファイル（`map.md`, `profile.md` 等）をシステム通知としてプロンプトに注入可能です。
  - `/resume` はコンテキストをシームレスに切り替えますが、バックグラウンドセッションでのファイル更新は、ユーザーアクションが発生するまで UI に自動更新されません。

---

## Related Documents

| Document                                                                           | Purpose                               |
| :--------------------------------------------------------------------------------- | :------------------------------------ |
| [terminal-auto-execution.md](/.agent/rules/development/terminal-auto-execution.md) | Auto-run permission rules             |
| [conversations-card.md](/.agent/cards/routine/conversations-card.md)               | Logging protocol for this environment |
| [Map of Territory](/.agent/rules/map.md)                                           | Root navigation map                   |

---

## Origin

- 2026-02-04T06:00+09:00 by Lico (Agate): Created to define the Gemini CLI execution context.