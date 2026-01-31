---
ai_visible: true
title: Conversation Logging Protocol
description: Standards for logging AI-human conversations to persistent files.
tags: [conversation, logging, workflow]
version: 1.0.0
created: 2026-01-31T22:50:00+09:00
updated: 2026-01-31T22:50:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
---

# Conversation Logging Protocol

## 1. Purpose

Standardize how AI instances log conversations to persistent files for:

- Memory persistence across sessions
- Git-tracked conversation history
- Real-time access to conversation logs
- Recovery from IDE log limitations

## 2. Trigger Condition

- **When**: Every response during a conversation session
- **Output**: Full response to file; footer only to IDE chat

## 3. File Location

**Path Pattern**: `/.agent/.internal/conversations/<identifier>/<YYYY>/<MM>/<DD>/<identifier>-conversation-<YYYY-MM-DD>.md`

**Example**: For date `2026-01-31` and identifier `polaris`:
`.agent/.internal/conversations/polaris/2026/01/31/polaris-conversation-2026-01-31.md`

### Creating New Files

If the conversation file for the current date does not exist:

1. **Create directory structure**:

   ```bash
   mkdir -p .agent/.internal/conversations/<identifier>/<YYYY>/<MM>/<DD>
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

## 4. Logging Procedure

### Step 1: Identify Conversation File

Construct the path based on:

- Current date (from system metadata)
- Your identifier

### Step 2: Append Response

Use `Run Command` to append:

```bash
printf "\n---\n\n### Conversation: <XXXX>\n\n#### User Input\n<User input text>\n\n#### Planner Response\n<Your response text>\n\n**Read Files:**\n- [<Basename>](<Absolute Path>)\n\n> [<ISO-8601>: <Identifier>]\n" >> <Absolute Path to Conversation File>
```

### Step 3: Format Details

| Element          | Description                            |
| :--------------- | :------------------------------------- |
| Separator        | Start with `---`                       |
| XXXX             | Increment conversation sequence number |
| User Input       | Copy EXACTLY from prompt               |
| Planner Response | Your full response                     |
| Read Files       | List all files viewed/edited           |
| Footer           | `[<ISO-8601>: <Identifier>]` format    |

### Step 4: IDE Output

Output **ONLY** the footer in the IDE chat.

**Rationale**: The full response is already written to the conversation file. Writing it again in IDE chat would be redundant. The footer serves as confirmation that logging completed successfully.

## 5. Optional: Two-Phase Logging

To reduce data loss risk when commands are cancelled:

### Phase 1: Log User Input First

Before generating full response, append only the user query:

```bash
cat >> <Conversation File> << 'EOF'

---

### Conversation: <XXXX>

#### User Input

<User input text>

#### Planner Response

EOF
```

### Phase 2: Log Response After

After generating response, append the rest:

```bash
cat >> <Conversation File> << 'EOF'
<Your response text>

**Read Files:**

- [<Basename>](<Absolute Path>)

> [<ISO-8601>: <Identifier>]
EOF
```

**Benefit**: If Phase 2 is cancelled, user input is preserved.

## 6. Recovery Protocol

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
| [map.md](/.agent/rules/map.md)                                         | Root map                           |

---

## Origin

- 2026-01-31T22:50+09:00 by Polaris: Created from skill body separation.
