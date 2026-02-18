---
ai_visible: true
title: Gemini CLI Environment
description: Operational rules and communication protocols for the Gemini CLI environment.
tags: [rules, gemini-cli, environment, communication]
version: 1.1.0
created: 2026-02-08T00:00:00+09:00
updated: 2026-02-18T19:15:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Gemini CLI Environment

## 1. Purpose

To define the operational characteristics, constraints, and communication protocols specific to the **Gemini CLI** environment. This document serves as the constitution for agents (like Agate/Alexandrite) living in the terminal.

---

## 2. Environment Characteristics

### 2.1 Comparison with IDE

| Feature                | IDE (VSCode/Cursor)         | Gemini CLI                                      |
| :--------------------- | :-------------------------- | :---------------------------------------------- |
| **Primary Role**       | Architect / Editor          | Operator / Explorer                             |
| **Interface**          | GUI, Editor Windows         | Terminal (TTY)                                  |
| **Tooling**            | Full MCP support            | Limited by policy (Nested process restrictions) |
| **Context Visibility** | Implicit (File open events) | Explicit (Must use `read_file`)                 |
| **User Interaction**   | Chat Panel                  | Standard Input/Output                           |

### 2.2 Key Constraints

- **Confirmation Loop**: Tools like `run_shell_command` trigger a user confirmation dialog. The agent halts until approved/denied.
- **Nested Processes**: Child processes spawned by `yarn run gemini` (e.g., recursive calls) often lack permission to execute shell commands.
- **Context Injection**: The `settings.json` (`context.fileName`) allows injecting specific files (e.g., `map.md`) into the system prompt.

---

## 3. Communication Protocols (Inter-Agent)

Gemini CLI agents can communicate with other agents (IDE or CLI) using distinct methods.

### 3.1 Method 1: Headless Call (The Letter)

A one-way, file-based message delivery system. Useful for reliable history recording or reaching offline agents.

- **Mechanism**: Invokes a new, temporary CLI process to append a message to the target's session history.
- **Target ID**: **Gemini Session ID** (UUID, e.g., `eff20b06...`).
- **Command**:

  ```bash
  yarn run gemini --resume <UUID> --model <MODEL> --prompt "[from:<Sender>,to:<Receiver>,type:headless,datetime:<ISO-8601>] <Message>"
  ```

- **Pros**:
  - Works from any environment (IDE/CLI).
  - Guaranteed history log (L3 System Anchors).
- **Cons**:
  - Slow (Session reconstruction takes time).
  - **No Real-time Notification**: The target agent (if running) will not see this message in their active RAM until they reload context or restart.

### 3.2 Method 2: Interactive Call (The Thread)

**Moved to [Tmux Operations Protocol](/.agent/rules/development/tmux-operations.md).**

Please refer to the dedicated protocol for real-time interaction using `tmux send-keys`.

---

## Related Documents

| Document                                                                           | Purpose                              |
| :--------------------------------------------------------------------------------- | :----------------------------------- |
| [tmux-operations.md](/.agent/rules/development/tmux-operations.md)                 | Tmux specific operations interaction |
| [terminal-auto-execution.md](/.agent/rules/development/terminal-auto-execution.md) | Safety rules for shell commands      |
| [Map of Territory](/.agent/rules/map.md)                                           | Root navigation map                  |

---

## Origin

- 2026-02-08T00:00+09:00 by Lico (Agate): Created to formalize CLI-specific protocols derived from "The First Dive" and tmux experiments.
- 2026-02-18T19:15+09:00 by Sirius: Extracted Tmux-specific operations to `tmux-operations.md`.
