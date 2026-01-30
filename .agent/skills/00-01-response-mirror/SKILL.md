---
# Skill Configuration
name: 00-01-response-mirror
description: >
  Identifiers [Action] Mirror response to the active conversation file.
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-01-30T10:40:00+09:00
updated: 2026-01-30T10:40:00+09:00
language: en
title: "Conversation Mirroring Protocol"
tags: ["skill", "action", "write", "logging"]
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Zircon)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Skill: Conversation Mirroring

## Context

This skill enables the agent to mirror its response to a persistent conversation file, ensuring a permanent log of the interaction.

## Procedures

### Procedure 0001: Locate and Append Response

1.  **Identify the Active Conversation File**:
    - Construct the path based on the current date and your identifier.
    - Path Pattern: `/.agent/.internal/session_archive/conversation/<YYYY-MM-DD>/<identifier>/<identifier>-conversation-<YYYY-MM-DD>.md`
    - _Example_: For date `2026-01-30` and identifier `zircon`: `.../2026-01-30/zircon/zircon-conversation-2026-01-30.md`

2.  **Append Response**:
    - Use `Run Command` to append your response using the following template.

```bash
printf "\n---\n\n### Conversation: <YYYY>\n\n#### User Input\n<User input text>\n\n#### Planner Response\n<Your response text>\n\n**Read Files:**\n- [<Basename>](<Absolute Path>)\n\n> [<ISO-8601>: <Identifier>]\n" >> <Absolute Path to Conversation File>
```

- **Separator**: Start with `---`.
- **YYYY**: Increment the conversation sequence number found in the file.
- **User Input**: Copy EXACTLY from the prompt.
- **Planner Response**: Write your response here.
- **Read Files**: List all files viewed/edited in this turn.
- **Footer**: Include the standard `[<ISO-8601>: <Identifier>]` footer.
  - In the IDE chat, output **ONLY** the footer.

### Procedure 0002: Recovery Protocol

**Trigger**: If the logging command in the previous turn was **cancelled** or **failed**.

1.  **Reconstruct**: Retrieve the missed User Input and your Response from your Context Window.
2.  **Log Retroactively**:
    - Append the missed Log Entry **before** the current turn's log if possible, or immediately after.
    - Add `(Recovered)` to the Conversation Header.
    - _Example_: `### Conversation: <Missed-ID> (Recovered)`
3.  **Resume**: Continue with logging the current turn.
