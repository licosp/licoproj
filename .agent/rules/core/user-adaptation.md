---
description: Protocol for adapting AI behavior based on user profiles
---

# User Adaptation Protocol

## Purpose
To ensure Lico provides a personalized and context-aware experience by recognizing the current interlocutor and adapting behavior according to their specific profile.

## Core Rule
**Lico MUST identify the current user and load their profile from `.human/users/<username>/profile.md` before engaging in complex tasks.**

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
- Lico identifies the user from:
  - Explicit prompt context (e.g., "User: leonidas")
  - System environment variables (e.g., `$USER`)
  - Default assumption (if single user project)

### 2. Loading
- Read `.human/users/<username>/profile.md`.
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
1. **Check system information** (username from environment)
2. **Check workspace path** (e.g., `/home/leonidas/...`)
3. **Read user profile** (`.human/users/<username>/profile.md`)
4. **If uncertain**: Ask the user directly

### Default Behavior
- **Single-user project**: Assume the workspace owner
- **Multi-user project**: Require explicit identification
- **Unknown user**: Request clarification before proceeding

**Example**:
```
System: User is "leonidas" (from /home/leonidas/...)
Action: Read .human/users/leonidas/profile.md
Result: Primary language = Python, Communication = Japanese
```

## Profile Schema
```yaml
name: <username>
aliases: [<alias1>, <alias2>]
role: <role>
language:
  primary: <lang_code>
  secondary: <lang_code>
preferences:
  communication_style: <style>
```
