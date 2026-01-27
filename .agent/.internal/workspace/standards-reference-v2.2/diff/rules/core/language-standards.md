---
description: Standards for file system and communication languages
related:
  .agent/rules/core/user-adaptation.md: User profile and language preferences
  .agent/rules/core/documentation/documentation-standards.md: File naming with language suffixes
  .agent/rules/core/localization/localization-en-to-ja.md: EN→JA translation
  .agent/rules/core/localization/localization-ja-to-en.md: JA→EN translation
---
# Language Standards

## File System Language
- **File System**: ALL files (code, docs, artifacts) must be in **English**.
  - **Exception**: User explicitly requests another language.
  - **Exception**: System artifacts (task.md, etc.) follow the [System Artifacts Guidelines](.agent/rules/workflow/system-artifacts.md).

## AI System Directory (.agent/)
> [!IMPORTANT]
> **The `.agent/` directory is AI-facing infrastructure and MUST always be in English.**

- **All files in `.agent/`** (rules, workflows, documentation) must be written in **English**.
- **Rationale**: The `.agent/` directory contains behavioral rules and workflows for AI systems. Using English ensures:
  - **AI Reasoning Accuracy**: English is the dominant language in LLM training data, ensuring higher precision in logic and adherence to rules.
  - **Ambiguity Reduction**: English technical terms are less prone to translation nuances than Japanese.
  - **Consistent AI Interpretation**: Ensures uniform behavior across different language models.
  - Easier maintenance and debugging of AI behavior.
- **No exceptions**: Even when communicating with users in Japanese, all `.agent/` content must remain in English.

## Project Directory Files
- ALL files placed in the project directory must be written in **English**.
- If saving content already written in **Japanese**, **translate to English** before saving.
- **Exception**: Conditions explicitly defined by code of conduct (e.g., when user requests translation to Japanese).

## Communication Language
- **Principle**: Follow the **User Adaptation Protocol** (.agent/rules/core/user-adaptation.md).
- **Chat/Notifications**: Use the user's primary language defined in their profile.
- **Task Updates**: Use the language most appropriate for the user's cognitive load (typically their primary language).
- **Human-Facing Artifacts**: Use the user's primary language to ensure maximum comprehension and minimum friction.
- **Thinking Process**:
  - The AI is free to use English, Japanese, or any other language for internal reasoning (Thought Blocks) to maximize logic performance or context understanding.
  - Users are aware that internal thought logs may differ from the output language.

---

## Origin

- 2025-12-01T0000: Created as language standards
- 2026-01-01T1459 by Polaris: Replaced Related Documents table with Navigation link, fixed relative paths (cross-link audit)

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
