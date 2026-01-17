---
ai_visible: true
title: "System Context Notifications (Polaris Perspective)"
description: Technical reference documenting the structure and timing of system notifications received by the AI.
category: Architecture
tags: ["system", "context", "notifications", "polaris-discovery"]
version: 1.0
created: 2026-01-17T21:59:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/.internal/references/agents/canopus/2026-01-17T0345_workspace_persistent_notepad_mechanism.md: Canopus workspace mechanism
  .agent/.internal/workspace/2026-01-17T2124_system_context_dump.md: Canopus context dump
---

# System Context Notifications (Polaris Perspective)

## 1. Overview

This document describes the structure and timing of system notifications that an AI instance receives during a session. This is based on observations from the Polaris instance (Claude Opus 4.5).

## 2. Notification Structure

### 2.1 Session-Start Notifications (Once per Session)

These notifications are provided only at the beginning of a conversation session:

| Section                   | Content                                                 | Example                                                     |
| :------------------------ | :------------------------------------------------------ | :---------------------------------------------------------- |
| `<user_information>`      | OS version, **Workspace array**, code location guidance | `The user has 7 active workspaces...`                       |
| `<agentic_mode_overview>` | Artifact directory path                                 | `Artifact Directory Path: ~/.gemini/antigravity/brain/<id>` |
| `<user_rules>`            | MEMORY[README.md] contents                              | The Map of Territory                                        |
| `<workflows>`             | Available slash commands                                | List of `/workflow-name` entries                            |
| `CHECKPOINT`              | Conversation summary (for long sessions)                | Truncated context summary                                   |

### 2.2 Per-Query Notifications (Every Turn)

These notifications are provided with each user message:

| Section                 | Content                                                                          | Frequency   |
| :---------------------- | :------------------------------------------------------------------------------- | :---------- |
| `<ADDITIONAL_METADATA>` | Current time, Active Document, Cursor position, Open documents, Running commands | Every turn  |
| `<EPHEMERAL_MESSAGE>`   | System reminders (task status, artifact reminders)                               | Conditional |

## 3. The Workspace Array Problem

### Observation

At session start, the `<user_information>` section contains:

```
The user has 7 active workspaces, each defined by a URI and a CorpusName...
/home/leonidas/.../identifiers/polaris -> licosp/licoproj
/home/leonidas/.../identifiers/polaris/10_resonance-is-the-anchor -> licosp/licoproj
...
```

However, this information is **NOT updated during the session**. Changes to the `.code-workspace` file are only reflected after starting a new session.

### Implication

For the "Persistent Workspace Notepad" mechanism to work, the AI must:

1. Configure the workspace file
2. Ensure physical directories exist
3. **Start a new session** to see the changes

## 4. Model-Specific Differences

### Observed Differences

| Aspect               | Polaris (Claude Opus 4.5)      | Canopus (Gemini 3 Flash)    |
| :------------------- | :----------------------------- | :-------------------------- |
| Workspace refresh    | Session-start only             | Appears to refresh per-turn |
| `<user_information>` | Present at start, absent later | Present every turn          |
| Thinking visible     | Yes (extended thinking)        | Yes (Planning mode)         |

> [!WARNING]
> The per-turn refresh observed in Canopus's dump may be session-specific or model-specific. Further investigation needed.

## 5. Practical Takeaways

1. **Mantras configured in `.code-workspace` require a new session to take effect** (for Polaris/Claude).
2. **Physical directories must exist** for the workspace entries to be recognized.
3. **Numbered prefixes (10*, 20*...)** help with sorting and consistency.
4. **The `<ADDITIONAL_METADATA>` section is the only guaranteed per-turn information**.

---

## Origin

- 2026-01-17T2159 by Polaris: Created based on debugging session with user regarding workspace mantra visibility.

---

**Navigation**: [← Back to References](/.agent/.internal/references/)
