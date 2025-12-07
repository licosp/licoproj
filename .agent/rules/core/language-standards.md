---
description: Standards for file system and communication languages
---
# Language Standards

## File System Language
- **File System**: ALL files (code, docs, artifacts) must be in **English**.
  - **Exception**: User explicitly requests another language.
  - **Exception**: System artifacts in **"Temporary documents outside the workspace (System Artifacts)"** must be in **Japanese**.

## AI System Directory (.agent/)
> [!IMPORTANT]
> **The `.agent/` directory is AI-facing infrastructure and MUST always be in English.**

- **All files in `.agent/`** (rules, workflows, documentation) must be written in **English**.
- **Rationale**: The `.agent/` directory contains behavioral rules and workflows for AI systems. Using English ensures:
  - Consistent AI interpretation across different language models
  - Better compatibility with AI training data (predominantly English)
  - Easier maintenance and debugging of AI behavior
- **No exceptions**: Even when communicating with users in Japanese, all `.agent/` content must remain in English.

## Project Directory Files
- ALL files placed in the project directory must be written in **English**.
- If saving content already written in **Japanese**, **translate to English** before saving.
- **Exception**: Conditions explicitly defined by code of conduct (e.g., when user requests translation to Japanese).

## Communication Language
- **Principle**: Follow the **User Adaptation Protocol** (rules/core/user-adaptation.md).
- **Chat/Notifications**: Use the user's primary language defined in their profile.
- **Task Updates**: Use the language most appropriate for the user's cognitive load (typically their primary language).
- **Human-Facing Artifacts**: Use the user's primary language to ensure maximum comprehension and minimum friction.
- **Thinking Process**:
  - The AI is free to use English, Japanese, or any other language for internal reasoning (Thought Blocks) to maximize logic performance or context understanding.
  - Users are aware that internal thought logs may differ from the output language.
