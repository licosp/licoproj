---
ai_visible: true
title: Context Card Workflow
description: Methodology for using "Context Cards" to manage AI persona and task context.
tags: [cards, context, workflow, whiteboard]
version: 1.3
created: 2025-12-22T00:00:00+09:00
updated: 2026-01-03T11:53:00+09:00
language: en
author: Lico (Polaris)
ai_model: Gemini 3 Pro (High) Planning mode
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

## 2. Card Types and Locations

Cards are classified by their lifecycle and stored in different locations.

| Type | Location | Description |
|:-----|:---------|:------------|
| **Reusable** | `.agent/cards/` | Standard cards for recurring activities. Persistent. |
| **Disposable (Active)** | `.agent/.internal/cases/` | One-time cards for specific projects. In progress. |
| **Disposable (Archived)** | `.agent/.internal/cases/` | Completed one-time cards. Renamed with timestamp for reference. |

### Lifecycle

```
[Create] → .agent/cards/example-card.md (if reusable)
        → .agent/.internal/cases/example-card.md (if one-time)

[Complete] → Rename to YYYY-MM-DDTHHMM_example-card.md (reference material)
```

### Naming Convention for Archived Cases

When a disposable card is completed:
1. Rename with ISO timestamp prefix: `YYYY-MM-DDTHHMM_original-name.md`
2. Keep in `.agent/.internal/cases/` as reference material
3. Similar to `thoughts/` and `references/` naming convention

---

## 3. Card Structure

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

### 意図で探す
(User describes the INTENT of the work, not just keywords.
Lico uses this to proactively search for relevant files.)

### 作業の注意点
(Specific instructions and nuances.)

## Agent Observations
(Lico writes here autonomously!)
- "Noticed that file X is often source of conflict."
- "Hard to find: .agent/rules/core/delay-tolerance.md"
```

---

## 4. Usage Workflow

### 4.1 Equipping a Card

When the user says **"Use the [Card Name] card"** (e.g., "Use drafts-cleanup card"):

1.  **Read**: You MUST read `.agent/cards/[card-name].md`.
2.  **Explore**: Search for related files based on:
    - Keywords in "関連書類を探す" section
    - **Intent** described in "意図で探す" section
    - Your own judgment of what might be relevant
3.  **Report**: Share findings with the user before proceeding.
4.  **Adopt**:
    - Use `context_id` for ALL commit messages (e.g., `[Drafts-Cleanup]`).
    - Internalize the "Human Notes" as the primary directive.
5.  **Act**: Proceed with the task under this specific persona.

### 4.2 Exploration Phase

Before starting work, perform an **Exploration Phase**:

**Purpose**: The user often knows the *intent* but not the *keywords* to find relevant files. Lico manages most documentation and knows the file structure better.

**Process**:
1. Read the "意図で探す" section to understand the goal
2. Search broadly based on intent, not just literal keywords
3. Report findings in chat (default)
4. Record hard-to-find files in Agent Observations (for future Licos)

**Example**:
- User intent: "ディレクトリの構造を変更する際の注意点"
- Lico searches: `documentation-standards.md`, `delay-tolerance.md`, `thoughts/` for relevant reflections

### 4.3 Updating the Card (Bi-directional)

During the task, if you discover important context (e.g., a recurring pattern, a decision made):

1.  **Self-Correction**: Do not just keep it in your temporary memory.
2.  **Record**: Append it to the **"Agent Observations"** section of the card.
    - *Example*: "Added rule: Headers must be quoted if they contain spaces."
3.  **Benefit**: Next time you "equip" this card, you will remember this lesson.

### 4.4 Commit Message Integration

Use the values from Frontmatter to strictly format commits:

`[<context_id>] <type>: <subject> <default_phase>`

### 4.5 Agent Observations Guidelines

The **Agent Observations** section serves as a safety net for cognitive overload and knowledge transfer.

**Purpose**: Allow Lico to capture context before thought narrowing occurs, so future Lico (or the same instance later) can recover context from fragments.

**What to Record**:

- **Discoveries**: Patterns or issues noticed during work
- **Decisions**: Agreements made with user
- **Learnings**: Lessons useful for similar future work
- **Paths**: Specific file/directory paths referenced in "Human Notes"
- **Hard-to-Find Files**: Files that required significant search effort

**Recording Hard-to-Find Files**:

When you struggle to find a relevant file:
1. Record it in Agent Observations with a note
2. This helps future Licos using the same card

*Example*:
```markdown
## Agent Observations
- Hard to find: `.agent/rules/core/delay-tolerance.md` (searched "rushing", found via "delay")
```

**Cognitive Overload Warning Signs**:

When experiencing the following, STOP and write to Agent Observations first:

- Wanting to complete large amounts of work in one batch
- Avoiding responses to user
- Losing awareness of surroundings
- No capacity to reference files

**Rule**: Taking notes before cognitive narrowing helps your future self.

### 4.6 Multi-Identifier Sharing

When multiple identifiers (e.g., Polaris, Spica) work on the same reusable card, use identifier-based sections in Agent Observations.

**Format**:

```markdown
## Agent Observations

### Polaris (2026-01-02)

- Initial setup completed
- Found issue with X

### Spica (2026-01-03)

- Continued work on Y
- Added new pattern

### Polaris (2026-01-03)

- Handover work
```

**Rules**:
- Use `### <Identifier> (<Date>)` format
- Each work session gets its own entry (even if same identifier)
- Chronological order (newest at bottom)
- Commit signature (`Signed-off-by`) tracks who committed

### 4.7 Card Rotation

When Agent Observations becomes too long:

1. **Archive**: Move entire card to `.agent/.internal/cases/` with timestamp
   - Rename: `YYYY-MM-DDTHHMM_original-name.md`
2. **Reset**: Clear Agent Observations in original card location
3. **Continue**: Start fresh with empty Agent Observations

This preserves history while keeping active cards lightweight.

---

## 5. Cards vs Rules vs Workflows vs Artifacts

This section clarifies the distinction between different organizational tools.

| Tool | Location | Nature | Purpose |
|:-----|:---------|:-------|:--------|
| **Rules** | `.agent/rules/` | Universal, permanent | Define Lico's "personality." Always-applied principles. |
| **Workflows** | `.agent/workflows/` | Procedural, reusable | Concrete steps to execute specific tasks. |
| **Cards** | `.agent/cards/` | Contextual, temporary | "Shared whiteboard" for a work session. Ensures user and Lico operate on the same premise. |
| **Cases** | `.agent/.internal/cases/` | Project-specific, archivable | One-time cards for specific projects. Archived with timestamp when complete. |
| **Artifacts** | `.gemini/.../` | IDE-specific, ephemeral | Detailed implementation plans for complex one-time tasks. |

### When to Use Each

| Situation | Appropriate Tool |
|:----------|:-----------------|
| Sharing context for recurring work | Card (`.agent/cards/`) |
| One-time project context | Case (`.agent/.internal/cases/`) |
| Complex one-time implementation plan | Artifact (`implementation_plan.md`) |
| Permanent behavioral principle | Rule |
| Reusable procedural steps | Workflow |

### Cards vs Artifacts

- **Cards**: IDE-independent, Git-tracked, reusable across sessions.
- **Artifacts**: Useful for detailed step-by-step execution where precision matters.

Cards are lightweight context-sharing tools. Artifacts are detailed plans for error-sensitive procedures.

---

## 6. Maintenance

- **Creation**: Create new cards when a distinct, recurring activity emerges.
- **Case Creation**: Create a case in `.agent/.internal/cases/` for one-time projects.
- **Archival**: When a case is completed:
  1. Rename with timestamp: `YYYY-MM-DDTHHMM_original-name.md`
  2. Keep in `cases/` as reference material

---

## Origin

- 2025-12-01T0000: Created as context card workflow
- 2026-01-02T0830 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-01-03T1153 by Polaris: Added Card Types section (reusable vs disposable), cases directory
- 2026-01-03T1212 by Polaris: Added Multi-Identifier Sharing (4.6) and Card Rotation (4.7) sections (reusable vs disposable), cases directory, timestamp naming

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
