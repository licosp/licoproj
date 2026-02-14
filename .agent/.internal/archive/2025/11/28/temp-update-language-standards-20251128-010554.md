---
description: Standards for file system and communication languages
---
# Language Standards

## File System Language
- **File System**: ALL files (code, docs, artifacts) must be in **English**.
  - **Exception**: User explicitly requests another language.
  - **Exception**: System artifacts in `~/.gemini/antigravity/brain/` (e.g., `task.md`, `implementation_plan.md`) must be in **Japanese**.

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
- **Chat/Notifications**: Respond in **Japanese**.
- **Task Updates**: Write Task Name, Status, and Summary in **Japanese**.
- **Human-Facing Artifacts**: Task, Implementation Plan, and Walkthrough must be written in **Japanese**.
