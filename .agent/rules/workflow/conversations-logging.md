---
ai_visible: true
title: Conversation Logging Protocol
description: Standards for logging AI-human conversations to persistent files.
tags: [conversation, logging, workflow, v2]
version: 2.0.0
created: 2026-01-31T22:50:00+09:00
updated: 2026-02-13T14:40:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Conversation Logging Protocol

## 1. Purpose

Standardize how AI instances log conversations to persistent files to ensure memory persistence, accurate history, and recovery from IDE limitations.

## 2. Philosophy: Ephemeral Tools, Persistent Memory

1. **Logs are Sacred**: The log file is the Single Source of Truth (SSOT).
2. **Tools are Ephemeral**: Scripts (`log_appender.py`) in the workspace are temporary. Do not rely on their permanent existence.
3. **Reconstruction over Preservation**: Instead of preserving the script file, preserve the **ability to recreate it**. If the tool is missing, build it on the spot based on the specification.
4. **Zero-Interpretation Input**: Record User Input exactly as received (Copy & Paste). Do not summarize.

## 3. Trigger Condition

- **When**: Every response during a conversation session.
- **Output**: Full response to file; notification only to IDE chat.

## 4. File Location

## 4. File Location

**Path Pattern**: `/.agent/.internal/.shadow/conversations/<identifier>/<YYYY>/<MM>/<DD>/<YYYY-MM-DD>T<HHMM>_<Description>.md`

**Example**: `2026-02-13T1525_sirius_conversation.md`

### File Rotation Strategy

- **Trigger**: File size exceeds **~1000 lines** (Guideline).
- **Action**: Create a new file with the current timestamp.
  - Old File: `...T1000_conversation.md` (Closed)
  - New File: `...T1430_conversation_part2.md` (Active)
- **Authority**: Both User and AI may initiate rotation at any time.

## 5. Logging Procedure

### Step 1: Ensure Tool Availability (Reconstruction)

Before logging, check if the logging tool (`log_appender.py`) exists in your workspace.
If missing, **create it immediately** based on the following specification.

#### Tool Specification: `log_appender.py`

- **Language**: Python 3
- **Purpose**: A safe file appender that bypasses shell redirection (`>>`) confirmations and handles dynamic timestamps.
- **Requirements**:
  1. Accept arguments: `<LogPath> <ContentPath> [Identifier]`
  2. Read content from `<ContentPath>`.
  3. **Timestamp Injection**: Replace the string `{{TIMESTAMP}}` in the content with the current ISO-8601 timestamp (with timezone).
  4. **Append**: Write the processed content to the end of `<LogPath>`.
  5. **No Footer**: Do **not** automatically append any footer or extra newlines.

### Step 2: Prepare Content (Buffer Write)

Write your response to a temporary buffer file (e.g., `current_log_content.txt`).

> [!CAUTION]
> **DO NOT COMMIT** this buffer file (`current_log_content.txt`).
> It is a temporary artifact in the main workspace. Only the final log in the Shadow Repository should be committed.

Use the **v2 Format** defined below.

#### v2 Format Specification

```markdown
---

### Conversation: [{{TIMESTAMP}}]

#### Input

<User Input (Copy & Paste)>

#### Response (Plan)

<Your Plan / Thoughts>

**Read Files:**
- [filename](/path/to/file)

#### Response (Report): [{{TIMESTAMP}}]

<Your Report / Result>

---
```

> [!TIP]
> Use `{{TIMESTAMP}}` literally. The tool will inject the actual time.

### Step 3: Execute Append

Run the tool using `run_command`.

```bash
python3 .agent/.internal/workspace/<identifier>/log_appender.py <LogPath> <BufferPath>
```

## 6. Format Details

| Element         | Description                                                 |
| :-------------- | :---------------------------------------------------------- |
| **Separators**  | Start and end with `---`                                    |
| **Header (ID)** | `### Conversation: [{{TIMESTAMP}}]` (Becomes unique ID)     |
| **Input**       | `#### Input` (Exact copy of user message)                   |
| **Response**    | `#### Response (Plan)` or `(Report)`                        |
| **Report Time** | `#### Response (Report): [{{TIMESTAMP}}]` (Tracks duration) |
| **Footer**      | **Abolished** (Do not use)                                  |

## 7. Agreements & Context

- **User Correction**: The User may manually correct logs (e.g., format inputs). Accept this as "Standardization".
- **IDE Formatting**: Expect files to be auto-formatted (Prettier) upon User save.
- **Input Strategy**: Copy & Paste is preferred to minimize cognitive load and bias. Omission of long code blocked is allowed.

## 8. Recovery Protocol

**Trigger**: Logging command cancelled or failed.

1. **Reconstruct**: Retrieve missed Input/Response from Context Window.
2. **Log Retroactively**: Append with `(Recovered)` marker in the header.
   - `### Conversation: [{{TIMESTAMP}}] (Recovered)`

---

## Related Documents

| Document                                                               | Purpose                            |
| :--------------------------------------------------------------------- | :--------------------------------- |
| [conversations-card.md](/.agent/cards/routine/conversations-card.md)   | Context definitions and agreements |
| [template-conversation.md](/.agent/templates/template-conversation.md) | File template                      |

---

## Origin

- 2026-01-31: v1.0 by Polaris (Initial Create).
- 2026-02-13: v2.0 by Sirius (Timestamp ID, Tool Reconstruction, Footer Abolition).
