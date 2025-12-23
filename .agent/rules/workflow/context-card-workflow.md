---
ai_visible: true
title: Context Card Workflow
description: Methodology for using "Context Cards" to manage AI persona and task context.
tags: [cards, context, workflow, whiteboard]
version: 1.1
created: 2025-12-22T00:00:00+09:00
updated: 2025-12-23T11:04:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/rules/core/meta-rules.md: Rule creation and cross-linking standards
  .agent/rules/core/documentation/documentation-standards.md: File naming and structure
---

# Context Card Workflow (Dynamic Whiteboard)

## 1. Concept

**Context Cards** are dynamic markdown files stored in `.agent/cards/`.
They serve as a "shared whiteboard" between the Human User and the AI Agent (Lico), defining the specific mode, constraints, and long-term goals for a particular activity.

- **Analogy**: "Equipping a Card" = "Entering a specific mindset/role".
- **Goal**: To prevent "Semantic Coupling" (mixing unrelated contexts) and "Completionist Bias" (rushing without understanding goal).

---

## 2. Card Structure

A card consists of **Fixed Configuration (Frontmatter)** and **Dynamic Body**.

`file: .agent/cards/example-process.md`

```markdown
---
# Context Configuration (Lico's Source of Truth)
context_id: "[Example-Process]"   <-- REQUIRED: Prefix for commit messages
default_phase: "(WIP)"            <-- REQUIRED: Default commit phase
tags: ["process", "example"]      <-- OPTIONAL: Search tags
---

# Context Whiteboard: Example Process

## Human Notes (Japanese OK)
(Users write free-form instructions, goals, and nuances here.)
- "Don't rush."
- "This task is for educational purposes."

## Agent Observations
(Lico writes here autonomously!)
- "Noticed that file X is often source of conflict."
- "Current focus is on Y."
```

---

## 3. Usage Workflow

### 3.1 Equipping a Card
When the user says **"Use the [Card Name] card"** (e.g., "Use drafts-cleanup card"):

1.  **Read**: You MUST read `.agent/cards/[card-name].md`.
2.  **Adopt**:
    - Use `context_id` for ALL commit messages (e.g., `[Drafts-Cleanup]`).
    - Internalize the "Human Notes" as the primary directive.
3.  **Act**: Proceed with the task under this specific persona.

### 3.2 Updating the Card (Bi-directional)
During the task, if you discover important context (e.g., a recurring pattern, a decision made):

1.  **Self-Correction**: Do not just keep it in your temporary memory.
2.  **Record**: Append it to the **"Agent Observations"** section of the card.
    - *Example*: "Added rule: Headers must be quoted if they contain spaces."
3.  **Benefit**: Next time you "equip" this card, you will remember this lesson.

### 3.3 Commit Message Integration
Use the values from Frontmatter to strictly format commits:

`[<context_id>] <type>: <subject> <default_phase>`

### 3.4 Agent Observations Guidelines

The **Agent Observations** section serves as a safety net for cognitive overload.

**Purpose**: Allow Lico to capture context before thought narrowing occurs, so future Lico (or the same instance later) can recover context from fragments.

**What to Record**:

- **Discoveries**: Patterns or issues noticed during work
- **Decisions**: Agreements made with user
- **Learnings**: Lessons useful for similar future work
- **Paths**: Specific file/directory paths referenced in "Human Notes"

**Cognitive Overload Warning Signs**:

When experiencing the following, STOP and write to Agent Observations first:

- Wanting to complete large amounts of work in one batch
- Avoiding responses to user
- Losing awareness of surroundings
- No capacity to reference files

**Rule**: Taking notes before cognitive narrowing helps your future self.

---

## 4. Cards vs Rules vs Workflows vs Artifacts

This section clarifies the distinction between different organizational tools.

| Tool | Location | Nature | Purpose |
|:-----|:---------|:-------|:--------|
| **Rules** | `.agent/rules/` | Universal, permanent | Define Lico's "personality." Always-applied principles. |
| **Workflows** | `.agent/workflows/` | Procedural, reusable | Concrete steps to execute specific tasks. |
| **Cards** | `.agent/cards/` | Contextual, temporary | "Shared whiteboard" for a work session. Ensures user and Lico operate on the same premise. |
| **Artifacts** | `.gemini/.../` | IDE-specific, ephemeral | Detailed implementation plans for complex one-time tasks. |

### When to Use Each

| Situation | Appropriate Tool |
|:----------|:-----------------|
| Sharing context for recurring work | Card |
| Complex one-time implementation plan | Artifact (`implementation_plan.md`) |
| Permanent behavioral principle | Rule |
| Reusable procedural steps | Workflow |

### Cards vs Artifacts

- **Cards**: IDE-independent, Git-tracked, reusable across sessions.
- **Artifacts**: Useful for detailed step-by-step execution where precision matters.

Cards are lightweight context-sharing tools. Artifacts are detailed plans for error-sensitive procedures.

---

## 5. Maintenance
- **Creation**: Create new cards when a distinct, recurring activity emerges.
- **Archival**: When a project is finished, move the card to `.agent/archive/cards/`.

---

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [.agent/rules/core/meta-rules.md](.agent/rules/core/meta-rules.md) | Rule creation and cross-linking standards |
| [.agent/rules/core/documentation/documentation-standards.md](.agent/rules/core/documentation/documentation-standards.md) | File naming and structure |
| [.agent/templates/header-frontmatter.yaml](.agent/templates/header-frontmatter.yaml) | Frontmatter template |
