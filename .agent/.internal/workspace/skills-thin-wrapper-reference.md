---
ai_visible: true
title: Skill Application Protocol
description: Standards for developing, structuring, and applying Action Skills using the "Thin Wrapper" architecture.
tags: [workflow, skills, development, architecture, thin-wrapper]
version: 1.0.0
created: 2026-02-01T04:20:00+09:00
updated: 2026-02-01T04:20:00+09:00
language: en
author: Lico (Zircon)
ai_model: Gemini 3 Pro (High) Planning mode
related:
  - /.agent/rules/workflow/skills-resonance.md: Mechanism Definition
  - /.agent/cards/routine/skills-development-card.md: Development Context
---

# Skill Application Protocol

## 1. Core Philosophy: The Thin Wrapper

**Action Skills** MUST be implemented as "Thin Wrappers" around standard Rule files.

- **The Skill (`.agent/skills/`)**: Contains ONLY the metadata (Trigger) and a pointer.
- **The Rule (`.agent/rules/`)**: Contains the ACTUAL behavioral instructions.

### Why?

1.  **Single Source of Truth**: Behavior should be defined in `rules/`, not scattered in `skills/`.
2.  **Maintainability**: Updating the rule automatically updates the skill's behavior.
3.  **Stability**: The Skill file (which the IDE grasps) rarely changes, minimizing re-indexing risks.

## 2. Directory Structure

### 2.1 Skill Wrapper

Location: `/.agent/skills/<category>/<name>/SKILL.md`

```markdown
---
name: response-mirror
description: Identifiers [Action] Brief summary.
---

# Skill: Response Mirror

## Definition

- **Type**: Action
- **Trigger**: Every response.
- **Rule**: [conversations-logging.md](/.agent/rules/workflow/conversations-logging.md)

## Instructions

(Do not write detailed steps here. Refer to the Rule file.)

See: [conversations-logging.md](/.agent/rules/workflow/conversations-logging.md)
```

### 2.2 Rule Body

Location: `/.agent/rules/workflow/<rule-name>.md`

The rule file should be a standard markdown file properly tagged and structured.

## 3. Naming Conventions

### 3.1 Skill Folders

Format: `XX-YY-<name>` (optional sort prefix) or `<name>`

- `00-00-lesson-skills`: Fundamental/Meta skills
- `00-01-response-mirror`: High-priority systemic skills
- `identifiers/`: Identifier-specific skills

### 3.2 Skill Names (`name` in frontmatter)

- **Short & Unique**: This name is what the AI sees in the prompt.
- **Example**: `response-mirror`, `git-commit`, `review-request`

## 4. Development Lifecycle

1.  **Draft**: Create the Rule file in `.agent/rules/`.
2.  **Register**: Create the Skill Wrapper in `.agent/skills/` pointing to the Rule.
3.  **Verify**: Confirm the IDE picks up the new skill description.
4.  **Log**: Record the creation in `activity-log.md`.

## 5. Anti-Patterns

- **Thick Skills**: Defining complex logic inside `SKILL.md`. (Forbidden)
- **Orphan Reference**: Pointing to a rule that doesn't exist.
- **Duplicate Logic**: Copying rule content into the skill description.

---

## Origin

- 2026-02-01T04:20+09:00 by Zircon: Created to formalize the "Thin Wrapper" architecture requested by User.
