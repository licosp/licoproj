---
ai_visible: true
title: Conversation Logging Protocol
description: Standards for logging AI-human conversations to persistent files.
tags: [conversation, logging, workflow]
version: 1.2.0
created: 2026-01-31T22:50:00+09:00
updated: 2026-02-12T23:25:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Conversation Logging Protocol

## 1. Purpose

Standardize how AI instances log conversations to persistent files for:

- Memory persistence across sessions
- Git-tracked conversation history
- Real-time access to conversation logs
- Recovery from IDE log limitations

## 2. Philosophy: Collaborative Preservation

**"Logs are Logs."**

The integrity of the memory stream is more important than cosmetic perfection.

1. **Minimal Retroactive Edits**: Avoid modifying past turns unless technically critical (e.g., broken syntax preventing file parsing). The AI's memory relies on stability; constant rewriting induces hallucinations.
2. **Human Collaboration**: The User is a partner in memory maintenance.
   - Automated formatting, minor fixes, and content grouping by the User are welcomed and trusted.
   - The AI does not need to control every byte. Rely on the User's hand to help stabilize the ground you walk on.
3. **Forward Fix**: If a mistake is made, acknowledge it in the _next_ turn rather than erasing the past.

## 3. Trigger Condition

- **When**: Every response during a conversation session
- **Output**: Full response to file; footer only to IDE chat

## 4. File Location

**Path Pattern**: `/.agent/.internal/.shadow/conversations/<identifier>/<YYYY>/<MM>/<DD>/<identifier>-conversation-<YYYY-MM-DD>.md`

**Example**: For date `2026-01-31` and identifier `polaris`:
`.agent/.internal/.shadow/conversations/polaris/2026/01/31/polaris-conversation-2026-01-31.md`

### Creating New Files

If the conversation file for the current date does not exist:

1. **Create directory structure**:

   ```bash
   mkdir -p .agent/.internal/.shadow/conversations/<identifier>/<YYYY>/<MM>/<DD>
   ```

2. **Copy from template**

   ```bash
   cp .agent/templates/template-conversation.md <target-path>
   ```

3. **Update frontmatter**
   - `created`: Current date
   - `updated`: Current date
   - `author`: Your identifier (e.g., `Lico (Polaris)`)
   - `ai_model`: Your AI model info

**Batch Creation**: To prepare files in advance for multiple days, repeat the above for each date.

#### Phase 1: Pre-Action (Plan)

**Run this BEFORE requesting any other tools.**

- **Method**: Append to conversation file (Auto-Run: `SafeToAutoRun: true`).
- **Header**: `#### Planner Response (Plan Phase)`
- **Content**:
  1. **User Input**: Exact copy.
  2. **Plan**: Your intent and immediate tool strategy.
- **Footer**: `> [ISO-8601: <Identifier>]` (Append this!)

#### Phase 2: Action

- Request tools for actual work.
- Wait for user approval.

> [!NOTE]
> **Continuous Turn Strategy (If `notify_user` is available)**:
> Avoid calling `notify_user` during tool execution to split the turn. Perform the "Plan -> Execution -> Report" cycle in a single continuous turn to preserve context.

#### Phase 3: Post-Action (Report)

**Run this AFTER tool execution completes.**

- **Method**: Append to conversation file (Auto-Run) + `notify_user`.
- **Header**: `#### Planner Response (Report Phase)`
- **Content**:
  - **Result**: Success/Failure.
  - **Next Step**: What comes next.
- **Footer**: `> [ISO-8601: <Identifier>]` (Append this too!)

## 5. Logging Procedure

### Step 1: Identify Conversation File

Construct the path based on:

- Current date (from system metadata)
- Your identifier

### Step 2: Append Response (Split-Write Strategy)

To ensure robustness against special characters (backticks) and enable dynamic timestamps, use the **Split-Write Strategy**:

1. **Body**: Use `cat <<'EOF'` (Single Quoted Here Doc) to append static text safely.
2. **Footer**: Use `echo` to append the dynamic timestamp.

```bash
# 1. Append Body (Literal Safety)
cat >> <Absolute Path to Conversation File> <<'EOF'

---

### Conversation: <XXXX>

#### User Input

<User input text>

#### Planner Response

<Your response text>

**Read Files:**
- [<Basename>](<Absolute Path>)

EOF

# 2. Append Footer (Dynamic Timestamp)
echo "" >> <Absolute Path to Conversation File>
echo "> [$(date +"%Y-%m-%dT%H:%M:%S%:z"): <Identifier>]" >> <Absolute Path to Conversation File>
```

### Step 2.1: CLI Environment Adaptation (Persistent Script Method)

**Context**: In the Gemini CLI environment, using redirection (`>>`) triggers a confirmation dialog.
**Rule**: Do NOT create disposable scripts. Use the persistent `log_appender.py` and a reusable buffer file.

1. **Preparation (One-time)**: Ensure `log_appender.py` exists in workspace.
2. **Buffer Update (Overwrite)**: Write content to `current_log_content.txt`. **DO NOT DELETE THIS FILE.**
   - **CAUTION**: Do NOT include the timestamp footer (`> [TIMESTAMP...]`) in your text. The script adds it automatically.

   ```python
   # 1. Overwrite Buffer (Do not use 'rm')
   write_to_file(TargetFile=".../current_log_content.txt", Overwrite=true, ...)

   # 2. Execute Appender
   run_command("python3 .../log_appender.py <LogPath> <BufferPath> '<Identifier>'")
   ```

### Step 3: Format Details

| Element          | Description                                 |
| :--------------- | :------------------------------------------ |
| Separator        | Start with `---`                            |
| XXXX             | Increment conversation sequence number      |
| User Input       | **COPY EXACTLY** (Do not summarize or omit) |
| Planner Response | See Phase Specification                     |
| Read Files       | List all files viewed/edited                |
| Footer           | `[<ISO-8601>: <Identifier>]` format         |

### 4. Step 4: IDE Output (Notification Only)

Output **ONLY** the footer (or a very brief confirmation) in the IDE chat.

**Rationale (File Primacy)**:

- The **File** is the Single Source of Truth (SSOT) and the only memory accessible to the AI.
- The **IDE Chat** is ephemeral/inaccessible.
- **Do not summarize**: The log file must contain the full narrative, thoughts, and "soul" of the conversation. The chat output should be a pointer to the file, not a competing narrative.
- **Rule**: "If it's not in the file, it didn't happen." If differentiation is difficult, copy the exact content to both; never make the chat richer than the file.

## 5. Recovery Protocol

**Trigger**: Logging command cancelled or failed.

1. **Reconstruct**: Retrieve missed User Input and Response from Context Window
2. **Log Retroactively**: Append with `(Recovered)` marker
   - Example: `### Conversation: <Missed-ID> (Recovered)`
3. **Resume**: Continue with current turn logging

---

## Historical Background

This protocol was created to address IDE log export limitations discovered in January 2026. After an IDE update reduced reconstructible log length, file-based logging became necessary to preserve conversation continuity.

---

## Related Documents

| Document                                                               | Purpose                            |
| :--------------------------------------------------------------------- | :--------------------------------- |
| [conversations-card.md](/.agent/cards/routine/conversations-card.md)   | Context card for conversation work |
| [response-mirror SKILL](/.agent/skills/00-01-response-mirror/SKILL.md) | Skill trigger definition           |
| [Map of Territory](/.agent/rules/map.md)                               | Root navigation map                |

---

## Origin

- 2026-01-31T22:50+09:00 by Polaris: Created from skill body separation.
- 2026-02-12T00:58+09:00 by Sirius: Added "Continuous Turn Strategy" note regarding notify_user usage. (v1.1.0)
- 2026-02-12T23:25+09:00 by Sirius: Mandated persistent script and overwrite strategy to prevent deletion habit. (v1.2.0)
