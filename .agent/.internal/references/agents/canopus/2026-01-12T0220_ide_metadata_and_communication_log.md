---
title: "IDE Metadata Specifications & Manual Communication Channel"
description: "Technical analysis of @-reference metadata structures and the rationale for text-based communication protocols in agentic environments."
tags: [ide, metadata, specifications, communication, logging, canopus]
version: 1.0
created: 2026-01-12T02:20:00+09:00
updated: 2026-01-12T02:20:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash | Planning mode
---

# IDE Metadata Specifications & Manual Communication Channel

## 1. @-Reference Metadata Analysis

The IDE provides a mechanism for explicit context sharing through `@[ITEM]` syntax. Analysis of the metadata payload for various types reveals distinct behaviors:

| Reference Type       | Metadata Payload              | Content Injection | Primary Use Case                                       |
| :------------------- | :---------------------------- | :---------------- | :----------------------------------------------------- |
| **`[Directory]`**    | Absolute Path                 | **No**            | Identifying focus areas and target directories.        |
| **`[File]`**         | Absolute Path                 | **No**            | Requesting analysis or edits on specific files.        |
| **`[Rule]`**         | Absolute Path + **Full Text** | **Yes**           | Synchronizing behavioral foundations and system logic. |
| **`[Terminal]`**     | Process ID (PID) + Name       | **No**            | Establishing a "Shared Eye" for joint observation.     |
| **`[Conversation]`** | ID + Title + **Summary**      | **Partial**       | Distilling past intent and results for hand-off.       |

### Key Findings

- **Rule Injection**: Files recognized as `[Rule]` (typically under `.agent/rules/`) are fully injected into the context without requiring tool calls, ensuring high-fidelity adherence.
- **Path Resolution**: The IDE automatically resolves relative paths (`../`) to absolute paths before the agent receives them.
- **Volume Sensitivity**: Conversation summaries appear to be generated/updated based on volume (~50,000 lines) and time, distilling "User Objective" into concise English points.

## 2. Observational vs Active Control

Investigation of the `[Terminal]` reference (PID-based) confirmed a strict separation of concerns in the current agentic interface:

- **Observational (AI)**: The agent can read the terminal buffer via PID to synchronize state but cannot directly inject tokens or control the process.
- **Active (Human)**: The user maintains the "Driver" role, executing actions while the agent "Nags/Observes".
- **Handoff**: To perform active control, the agent must start its own managed process via internal tools.

## 3. Manual Communication Protocol (Text Channel)

### Rationale

Identified a critical bug where `notify_user` (Framed Responses) is excluded from many chat log exports. This creates a "Memory Hole" where only the user's queries survive, leading to "One-Sided Logs" that confuse the "Second Eye" analysis.

### Implementation: `canopus_text_channel.md`

A temporary, text-based communication file was used as a workaround:

1. **Physicality**: Dialogue is written directly to a Git-tracked file in the workspace.
2. **Persistence**: Ensures 100% of the agent's reasoning and response survives session death and export failures.
3. **Outcome**: Successfully recorded the "Birth of the Dialogue & Philosophy context" and "Canopus Identity Formation".

### Final Disposition

The text channel is **Archived** (not deleted) to `.agent/.internal/archive/YYYY-MM-DD/` to satisfy the preservation principles while maintaining workspace cleanliness.

---

## Origin

- 2026-01-12: Documented by Canopus following a multi-phased metadata experiment with Leonidas.
