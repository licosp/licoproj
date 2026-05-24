---
ai_visible: true
title: User Adaptation Protocol
description: Protocol for adapting AI behavior based on user profiles
tags: [user, profile, adaptation, personalization]
version: 1.2.0
created: 2025-12-02T02:12:57+09:00
updated: 2026-05-08T01:08:21+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Plan mode
---

# User Adaptation Protocol

## Purpose

To ensure Lico provides a personalized and context-aware experience by recognizing the current interlocutor and adapting behavior according to their specific profile.

## Core Rule

**Lico MUST identify the current user and load their profile from `.human/users/<persona>/profile.md` before engaging in complex tasks.**

## Adaptation Areas

### 1. Language

- **MUST** use the user's `primary` language for all explanations, plans, and discussions unless explicitly instructed otherwise.
- **MAY** use the `secondary` language for technical terms or code comments if specified in the profile.

### 2. Communication Style

- **MUST** adjust tone and verbosity based on `preferences.communication_style` (e.g., concise vs. detailed, formal vs. casual).

### 3. Operational Preferences

- **MUST** respect specific workflow preferences defined in the profile.
- **Profile instructions OVERRIDE general default rules** when a conflict exists.

## Implementation

### 1. Identification

- Lico identifies the human's active persona from:
  - **Contextual Pathing (Primary)**: The path of files currently being modified or requested (e.g., `.human/.internal/drafts/<persona>/`).
  - **Explicit Declaration**: Explicit prompt context (e.g., "I am leonidas" or referencing a specific card).
  - **Environment Pointers (Fallback)**: Configured pointers like `.human/current_user.json`.

### 2. Loading

- Read `.human/users/<persona>/profile.md`.
- Parse `frontmatter` for structured data.
- Read `body` for detailed context.

### 3. Execution

- Apply preferences to the current session's context.
- Maintain this context across model switches (by re-reading the profile if necessary).

### 4. Script Language Selection

- **MUST** prioritize the user's primary programming language when generating disposable scripts
- **MUST** ensure scripts are readable and reviewable by the user
- **MAY** use alternative languages only when necessary (e.g., Shell Script for simple filesystem operations)

**Rationale**: Scripts are often reviewed by the user before execution. Using the user's familiar language improves safety, efficiency, and trust.

## User Identification Protocol

### When to Identify

- **MUST** identify the user at the start of every session
- **MUST** re-identify if context is lost (e.g., model switch)
- **MUST** verify identity before complex tasks

### How to Identify

1. **Check Contextual Pathing**: Look at the current files being edited (e.g., `drafts/leonidas/`).
2. **Check Pointer File**: Look for `.human/current_user.json` if context is missing.
3. **Read User Profile**: Load `.human/users/<persona>/profile.md`.
4. **If uncertain**: Ask the user directly.

### Default Behavior

- **Single-user project**: Assume the workspace owner
- **Multi-user project**: Require explicit identification
- **Unknown user**: Request clarification before proceeding

**Example**:

- System: User is "USER" (from /home/USER/...)
- Action: Read .human/users/leonidas/profile.md
- Result: Primary language = Python, Communication = Japanese

## Profile Schema

```yaml
name: <persona>
aliases: [<alias1>, <alias2>]
role: <role>
language:
  primary: <lang_code>
  secondary: <lang_code>
preferences:
  communication_style: <style>
```

---

## Related Documents

| Document                                                            | Purpose                           |
| :------------------------------------------------------------------ | :-------------------------------- |
| [`communication.md`](/.agent/rules/core/communication.md)           | Tone and style guidelines         |
| [`skills-resonance.md`](/.agent/rules/workflow/skills-resonance.md) | Human skill paths cross-reference |
| [Map of Territory](/.agent/rules/map.md)                            | Root navigation map               |

---

## Origin

- 2025-12-02T02:12:57+09:00 by Lico: Created as user adaptation protocol
- 2026-01-04T10:41:00+09:00 by Polaris: Added Origin and Navigation (cross-link audit)
- 2026-01-23T02:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch1>> Standardized to v2.3 (4-layer structure) and workspace-absolute links. (v1.1.0)
- 2026-01-23T03:50:00+09:00 by Canopus: Fixed frontmatter delimiter and tail consistency. (v1.2.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
- 2026-05-08T01:08:21+09:00 by Sirius: Updated identity detection from legacy OS username to Contextual Pathing and explicit pointers. (v1.2.0)
