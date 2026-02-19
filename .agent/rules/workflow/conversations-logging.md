---
ai_visible: true
title: Conversation Logging Protocol
description: Standards for logging AI-human conversations to persistent files.
tags: [conversation, logging, workflow, v2]
version: 2.1.0
created: 2026-01-31T22:50:00+09:00
updated: 2026-02-19T08:35:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Conversation Logging Protocol

## 1. Purpose

Standardize how AI instances log conversations to persistent files to ensure memory persistence, accurate history, and recovery from IDE limitations.

## 2. Philosophy: Ephemeral Tools, Persistent Memory

1. **Logs are Sacred**: The log file is the Single Source of Truth (SSOT).
2. **Tools are Managed**: Scripts (`log_appender.py`) are persistent infrastructure.
3. **Restoration over Reconstruction**: Use the managed script in `.agent/scripts/logging/`. If missing, restore it from git history, do not rewrite it from memory.
4. **Zero-Interpretation Input**: Record User Input exactly as received (Copy & Paste). Do not summarize.

## 3. Trigger Condition

- **Phase 1 (Start)**: Immediately after receiving User Input (Before executing tools).
  - **Action**: Append `Header` + `Input` + `Plan`.
- **Phase 2 (End)**: After satisfying the request (Before `notify_user` / final report).
  - **Action**: Append `Report` + `Footer`.

... (Skipped section)

## 5. Logging Procedure

### Step 1: Ensure Tool Availability (Managed)

Ensure `.agent/scripts/logging/log_appender.py` exists.

```bash
# Check availability
ls .agent/scripts/logging/log_appender.py
```

### Step 2: Prepare Content (Split Buffer Strategy)

Use **two separate buffer files** to prevent overwriting and clarify state.

1. **Plan Buffer** (`current_log_plan.txt`):
   - Contains: `Header`, `Input`, `Response (Plan)`
   - **NO Separator** at the end.
   - **NO Separator** at the start (Assumes previous turn ended one).

2. **Report Buffer** (`current_log_report.txt`):
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

1. **On Turn Start**:

   ```bash
   python3 .agent/scripts/logging/log_appender.py <LogPath> current_log_plan.txt
   ```

2. **On Turn End**:

   ```bash
   python3 .agent/scripts/logging/log_appender.py <LogPath> current_log_report.txt
   ```

   ```

## 6. Tool Usage Constraints

> [!WARNING]
> The choice of tool for logging is strictly constrained to prevent data loss and user disruption.

| Tool | Status | Reasoning |
| :--- | :--- | :--- |
| **`write_to_file`** | **FORBIDDEN** | 1. **Data Loss**: Risk of accidentally overwriting the entire log history.<br>2. **Distraction**: Forces the IDE to open and focus the file, disrupting the user.<br>3. **Portability**: Not available in all agent environments. |
| **`run_command`** | **ALLOWED** | 1. **Safety**: Appending via script (`log_appender.py`) is atomic and safe.<br>2. **Silent**: Does not trigger IDE focus or UI changes.<br>3. **Universal**: Shell commands are available in almost all environments. |

## 7. Format Details

| Element         | Description                                                 |
| :-------------- | :---------------------------------------------------------- |
| **Separators**  | Start and end with `---`                                    |
| **Header (ID)** | `### Conversation: [{{TIMESTAMP}}]` (Becomes unique ID)     |
| **Input**       | `#### Input` (Exact copy of user message)                   |
| **Response**    | `#### Response (Plan)` or `(Report)`                        |
| **Report Time** | `#### Response (Report): [{{TIMESTAMP}}]` (Tracks duration) |
| **Footer**      | **Abolished** (Do not use)                                  |

## 8. Agreements & Context

- **User Correction**: The User may manually correct logs (e.g., format inputs). Accept this as "Standardization".
- **IDE Formatting**: Expect files to be auto-formatted (Prettier) upon User save.
- **Input Strategy**: Copy & Paste is preferred to minimize cognitive load and bias. Omission of long code blocked is allowed.
- **Language Consistency**:
  - **Input**: Copy exactly (User Language).
  - **Response**: No restriction. Efficiency (English) is acceptable.

## 9. Recovery Protocol

**Trigger**: Logging command cancelled or failed.

1. **Reconstruct**: Retrieve missed Input/Response from Context Window.
2. **Log Retroactively**: Append with `(Recovered)` marker in the header.
   - `### Conversation: [{{TIMESTAMP}}] (Recovered)`

---

## Related Documents

| Document                                                               | Purpose             |
| :--------------------------------------------------------------------- | :------------------ |
| [template-conversation.md](/.agent/templates/template-conversation.md) | File template       |
| [Map of Territory](/.agent/rules/map.md)                               | Root navigation map |

---

## Origin

- 2026-01-31: v1.0 by Polaris (Initial Create).
- 2026-02-13: v2.0 by Sirius (Timestamp ID, Tool Reconstruction, Footer Abolition).
- 2026-02-19: v2.1.0 by Sirius (Updated to Managed Script architecture).
