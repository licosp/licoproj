---
description: Log manual terminal sessions to share context with Lico
---

# Workflow: Share Manual Context

This workflow enables the user to record their manual terminal operations (commands and outputs) into a log file that Lico can read. This eliminates the need to copy-paste terminal outputs into the chat.

## Purpose
- **Implicit Context Sharing**: Allow Lico to "see" what the user did in the terminal.
- **Error Diagnosis**: Share full error logs and stack traces without manual copying.

## Procedure

### 1. Start Recording
Before performing manual operations, run the following command in your terminal:

```bash
script -f .agent/.internal/work/manual.log
```

- `script`: A standard Linux utility to make a typescript of terminal session.
- `-f`: Flush output after each write (real-time update).
- Output file: `.agent/.internal/work/manual.log`

### 2. Perform Operations
Run your commands as usual. Everything displayed on the screen is recorded.

### 3. Stop Recording
When finished, type `exit` or press `Ctrl+D` to stop the recording.

```bash
exit
```

### 4. Notify Lico
Tell Lico to check the log:
> "Check manual.log" or "I did some manual work, please review."

Lico will then read `.agent/.internal/work/manual.log` to understand the context.

## Notes
- The log file is overwritten each time you run `script` (unless `-a` append mode is used, but overwriting is usually preferred for fresh context).
- This file is ignored by Git (`.agent/.internal/work/manual.log` is in `.gitignore`).
