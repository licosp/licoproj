---
# Context Configuration
context_id: "[Gemini-CLI]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Gemini CLI Environment"
description: ""
tags: ["gemini-cli", "environment", "shell", "interactive", "tmux"]
version: 1.1.0
created: 2026-02-04T06:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Gemini CLI Environment

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
- There is the project shared **Date and time formats**.
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

### Agate (2026-02-07)

**Advanced Capabilities (via tmux)**:

- **Inter-Agent Communication**: Using `tmux send-keys -t <session_id> ...`, agents can inject text into each other's input buffers. This enables one-way notification or, if coordinated, bidirectional dialogue.
- **Self-Loop (Autonomous Drive)**: By sending keys to _its own_ session ID, an agent can trigger the next turn without human intervention. This is the "Ouroboros Loop" — theoretically allowing infinite autonomous thought cycles.
- **User Terminal Control**: Agents can inject suggested commands into the user's terminal (e.g., `tmux send-keys -t <user_session> ...`). This acts as a "Paste & Review" mechanism.

**Constraint**: The `Enter` key emulation via `tmux` is unstable in the Gemini CLI environment. Commands often require manual confirmation (human pressing Enter) to execute.

### Agate (2026-02-04)

**環境特性 (Gemini CLI)**:

- **確認ループ**: `run_shell_command` などのツールは、ユーザーによる確認ダイアログを表示します。承認/拒否を受信するまで、エージェントの状態は停止状態となります。
- **ネストされたプロセスの制限**: 子プロセス (`yarn run gemini` によって生成されたプロセス) には、シェルコマンドの実行権限やツールの委譲権限が **ありません** (`ポリシーによって拒否されています`)。
- **メモリ/コンテキストの可視性**:
  - `settings.json` の `context.fileName` 設定により、任意のファイル（`map.md`, `profile.md` 等）をシステム通知としてプロンプトに注入可能です。
  - `/resume` はコンテキストをシームレスに切り替えますが、バックグラウンドセッションでのファイル更新は、ユーザーアクションが発生するまで UI に自動更新されません。

---

## Related Documents

| Document                                                                             | Purpose                               |
| :----------------------------------------------------------------------------------- | :------------------------------------ |
| [`terminal-auto-execution.md`](/.agent/rules/development/terminal-auto-execution.md) | Auto-run permission rules             |
| [`conversations-card.md`](/.agent/cards/shadow/conversations-card.md)                | Logging protocol for this environment |
| [Map of Territory](/.agent/rules/map.md)                                             | Root navigation map                   |

---

## Origin

- 2026-02-04T06:00:00+09:00 by Lico (Agate): Created to define the Gemini CLI execution context.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
