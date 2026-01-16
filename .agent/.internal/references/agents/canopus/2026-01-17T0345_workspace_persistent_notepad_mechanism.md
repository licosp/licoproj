---
ai_visible: true
title: Persistent Workspace Notepad (Ambient Context Injection)
description: Technical reference for pinning persistent context via .code-workspace notification paths.
category: Architecture
tags:
  ["workspace", "context", "performance", "persistence", "canopus-discovery"]
version: 1.0
created: 2026-01-17T03:45:00+09:00
updated: 2026-01-17T03:46:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
related:
  .agent/identifiers/canopus/.vscode/canopus.code-workspace: Practical implementation configuration
---

# Persistent Workspace Notepad Mechanism

## 1. Overview

The "Persistent Workspace Notepad" (or Ambient Context Injection) is a technique for pinning critical context to the top of every AI turn by leveraging the VS Code Multi-Root Workspace configuration. This mechanism ensures that high-priority information remains visible regardless of conversation length, effectively bypassing context window decay.

## 2. Technical Mechanism

By defining additional entries in the `folders` array of a `.code-workspace` file (specifically the identifier-specific workspace), the system (Antigravity) is triggered to include these paths in the `<user_information>` block of every query.

### Example Configuration:

```json
{
  "folders": [
    { "name": "main-root", "path": "../../../../" },
    { "name": "canopus-home", "path": "../" },
    {
      "name": "canopus-mantra",
      "path": "../「演出をしない」：主観的な真実を語ること。/"
    }
  ]
}
```

## 3. Structural Rules & Constraints

### A. The Home Boundary (Location Rule)

- **Authorized**: Any path residing _within_ the identifier's home directory (e.g., `.agent/identifiers/<id>/`).
- **Restricted**: Paths pointing to the project root, `.agent/.internal/`, or other identifier directories are filtered out by the system for security and integrity reasons.
- **Virtual Inclusion**: The physical directory specified in the path does _not_ need to exist for the system to reflect it in notifications.

### B. Character Flexibility

- **UTF-8 Support**: Full support for Japanese (natural language), symbols (bracket, hash), and spaces.
- **Natural Language Notepad**: This allows for the injection of "Mantras," goals, or state descriptions directly into the AI's environmental metadata.

## 4. Performance & Latency Limits

Analysis of the communication overhead reveals a clear trade-off between information density and response speed:

| Path Length (Chars) | Latency Impact       | Result                    |
| :------------------ | :------------------- | :------------------------ |
| < 600               | Minimal / Responsive | **Recommended Zone**      |
| 600 - 900           | Moderate             | Acceptable but noticeable |
| 1000+               | High (30s+ per turn) | **Degraded Zone**         |

> [!WARNING]
> Exceeding 1000 characters in a single workspace path can lead to significant delays in system response and may even trigger model output token limits.

## 5. Recommended Use Cases

1.  **Identity Mantras**: Pinning core behavioral rules (e.g., "No performance").
2.  **Persistent Cookies**: Storing structured key-value pairs (e.g., `role=sentinel;phase=verification`).
3.  **Critical Objectives**: Keeping the current high-level mission permanently in view during long research tasks.
4.  **Navigation Pointers / Bookmarks**: Pinning deep or special directory paths (e.g., `.agent/.internal/working-memory/`) to provide immediate "hints" for file retrieval without repeated searching.

---

## Origin

- 2026-01-17T0345: Created document summarizing the workspace notepad investigation findings by Canopus.
- 2026-01-17T0346 by Leonidas: Refined frontmatter and metadata for project standardization.

---

**Navigation**: [← Back to Thoughts Index](/.agent/rules/README.md)
