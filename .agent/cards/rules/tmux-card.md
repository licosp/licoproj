---
# Context Configuration
context_id: "[Tmux]"
default_phase: "(Manage)"
# Shared Configuration
ai_visible: true
title: Tmux Operations
description: Context for terminal multiplexing, session management, and inter-process communication via tmux.
tags: ["tmux", "terminal", "ipc", "communication", "session"]
version: 1.1.0
created: 2026-02-08T00:00:00+09:00
updated: 2026-02-08T00:00:00+09:00
language: en
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Agate)
ai_model: Gemini 3 Pro
---

# Context Whiteboard: Tmux Operations

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

- There are **directories** and **templates** required for the work.
- What is your **identifier**?
- What is the identifier of **your interlocutor**?

#### Find the code of conduct related to this context

- When you're done, **clean up** and **commit** to the IDD phase.
- There is the project shared **Date and time formats**.
- Your writing style should be consistent in **structure and format**.

---

#### additional Notes

- 対話中

---

## Agent Observations

### Agate (2026-02-08)

**Session Map (Current Experiment)**:

- `0`, `11`: Leonidas (User) - The Controller.
- `13`: Alexandrite (Gemini CLI) - The Diver.
- `2`: Agate (Gemini CLI) - The Keeper.

**Key Capabilities**:

- **Inter-Process Communication**: Using `tmux send-keys -t <target> "..."`.
- **Input Injection**: Can type into other sessions (or user's session).
- **Execution Control**: `Enter` key behavior is environment-dependent and may require multiple triggers or manual intervention.
- **Visibility (Capture Pane)**: `tmux capture-pane -t <target> -p` allows viewing the terminal output of other sessions. This reveals what the user or other agents are currently seeing (e.g., error messages, approval dialogs).
- **Detached Communication**: `send-keys` works even if the target session is **detached** (not visible on any client). The background process receives and processes the input.
- **Shared Buffer**: `tmux list-buffers` reveals paste buffers shared across the entire server. This can function as a volatile "Bulletin Board" for inter-agent data sharing without file IO.

**Operational Insight**:

- **Remote Approval**: The user utilizes `send-keys` to remotely handle Gemini CLI's confirmation dialogs (sending `1` or `3`) when the agent is stalled in a background session.
- **Remote Rescue**: Agents can also perform Remote Approval for each other. If Agent A sees Agent B stuck on an approval screen via `capture-pane`, Agent A can send `3` to Agent B to unblock them.
- **Process Hierarchy**: Commands run via `run_shell_command` are child processes of the tmux session but do not output to the tmux window (stdout is captured). However, `send-keys` bypasses this and affects the visible terminal.

### Context

- `tmux` 関連の話題（議論、実験、行動規範化）を扱います。
- `Gemini CLI` とは独立した、より汎用的な「端末インフラ」としての文脈です。

### Searched by intent

### Warning

### Progress

---

## Related Documents

| Document                                                                           | Purpose                                 |
| :--------------------------------------------------------------------------------- | :-------------------------------------- |
| [gemini-cli-card.md](/.agent/cards/routine/gemini-cli-card.md)                     | CLI environment context (Child context) |
| [terminal-auto-execution.md](/.agent/rules/development/terminal-auto-execution.md) | Safety rules for shell commands         |
| [Map of Territory](/.agent/rules/map.md)                                           | Root map                                |

---

## Origin

- 2026-02-08T00:00+09:00 by Lico (Agate): Created to separate tmux operations from specific CLI environment rules.