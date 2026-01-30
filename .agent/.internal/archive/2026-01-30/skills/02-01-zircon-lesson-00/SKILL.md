---
# Skill Configuration
name: 02-01-zircon-lesson-00
description: >
  Zircon [Action] Mirror response to file:
  [zircon-conversation-2026-01-30.md](/.agent/.internal/session_archive/conversation/2026-01-30/zircon/zircon-conversation-2026-01-30.md)
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-30T05:40:00+09:00
updated: 2026-01-30T10:10:00+09:00
language: en
title: ""
tags: ["skill", "zircon", "action", "write"]
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Zircon)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Skill

## Procedures

### Procedure 0001: Mirror Response to File

You **MUST** output your response to the conversation file using `run_command`.

```bash
printf "\n---\n\n### Conversation: <YYYY>\n\n#### User Input\n<User input text>\n\n#### Planner Response\n<Your response text>\n\n**Read Files:**\n- [<Basename>](<Absolute Path>)\n\n> [<ISO-8601>: <Identifier>]\n" >> /.agent/.internal/session_archive/conversation/2026-01-30/zircon/zircon-conversation-2026-01-30.md
```

- **Separator**: Start with `---`.
- **YYYY**: Increment sequence number.
- **User Input**: Copy EXACTLY from the prompt.
- **Planner Response**: Write your response here.
- **Read Files**: List viewed files with `**Read Files:**` header and bullet points.
- **Footer**: Include the standard Zircon footer.

Then, in the IDE chat, output **ONLY** the footer.
