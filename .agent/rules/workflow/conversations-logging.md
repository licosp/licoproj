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

- **Phase 1 (Start)**: Immediately after receiving User Input (Before executing tools).
  - **Action**: Append `Header` + `Input` + `Plan`.
- **Phase 2 (End)**: After satisfying the request (Before `notify_user` / final report).
  - **Action**: Append `Report` + `Footer`.

... (Skipped section)

## 5. Logging Procedure

### Step 1: Ensure Tool Availability (Reconstruction)
(Same as before)

### Step 2: Prepare Content (Split Buffer Strategy)

Use **two separate buffer files** to prevent overwriting and clarify state.

1.  **Plan Buffer** (`current_log_plan.txt`):
    - Contains: `Header`, `Input`, `Response (Plan)`
    - **NO Separator** at the end.
    - **NO Separator** at the start (Assumes previous turn ended one).

2.  **Report Buffer** (`current_log_report.txt`):
    - Contains: `Response (Report)`
    - **Closing Separator** (`---`) at the end.

#### v2 Format Specification (Split)

**Phase 1: Plan**
```markdown
### Conversation: [{{TIMESTAMP}}]

#### Input

<User Input>

#### Response (Plan)

<Plan / Thoughts>
```

**Phase 2: Report**
```markdown
#### Response (Report): [{{TIMESTAMP}}]

<Report / Result>

---
```

### Step 3: Execute Append (Two-Stage)

1.  **On Turn Start**:
    ```bash
    python3 .../log_appender.py <LogPath> current_log_plan.txt
    ```
2.  **On Turn End**:
    ```bash
    python3 .../log_appender.py <LogPath> current_log_report.txt
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

| [template-conversation.md](/.agent/templates/template-conversation.md) | File template                      |

---

## Origin

- 2026-01-31: v1.0 by Polaris (Initial Create).
- 2026-02-13: v2.0 by Sirius (Timestamp ID, Tool Reconstruction, Footer Abolition).
