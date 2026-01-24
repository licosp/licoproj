---
ai_visible: true
title: Manual Context Sharing Protocol
description: Log manual terminal sessions to share context with Lico
tags: [workflow, collaboration, terminal, context]
version: 1.0.0
created: 2026-01-25T06:45:00+09:00
updated: 2026-01-25T06:45:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Manual Context Sharing Protocol

This workflow enables the user to record their manual terminal operations (commands and outputs) into a log file that Lico can read.

---

## 1. Purpose
- **Implicit Context Sharing**: Allow Lico to \"see\" what the user did in the terminal.
- **Error Diagnosis**: Share full error logs and stack traces without manual copying.

## 2. Procedure

### Step 1: Start Recording
Before performing manual operations, run the following command in your terminal:

```bash
script -f .agent/.internal/workspace/manual.log
```

- `script`: A standard Linux utility to make a typescript of terminal session.
- `-f`: Flush output after each write (real-time update).

### Step 2: Perform Operations
Run your commands as usual. Everything displayed on the screen is recorded.

### Step 3: Stop Recording
When finished, type `exit` or press `Ctrl+D` to stop the recording.

### Step 4: Notify Lico
Tell Lico to check the log:
> \"Check manual.log\" or \"I did some manual work, please review.\"

## 3. Notes
- The log file is overwritten each time you run `script`.
- This file is ignored by Git (`.agent/.internal/workspace/manual.log` is in `.gitignore`).

---

## Historical Background

**The Visibility GAP**: In the early days of development, users often had to copy-paste long terminal outputs into the chat window, which was inefficient and often reached token limits. The "script" utility was adopted to provide a non-intrusive way for Lico to "observe" the user's manual environment, fostering a deeper sense of collaboration.

---

## Related Documents

| Document | Purpose |
| :--- | :--- |
| [cognitive-collaboration.md](/.agent/rules/core/cognitive-collaboration.md) | Principles for AI-Human partnership |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | Standard for workspace logs and drafts |

---

## Origin

- 2026-01-25T0645 by Canopus: <<Seal: Rules-Standardization-Batch2.3>> Created by standardizing the manual context sharing procedure to v2.3 constitutional standards. (v1.0.0)

