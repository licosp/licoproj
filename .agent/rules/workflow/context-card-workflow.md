---
description: Methodology for using "Context Cards" to manage AI persona and task context.
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

---

## 4. Maintenance
- **Creation**: Create new cards when a distinct, recurring activity emerges.
- **Archival**: When a project is finished, move the card to `.agent/archive/cards/`.
