---
ai_visible: true
title: Context Card Workflow
description: Methodology for using "Context Cards" to manage AI persona and task context.
tags: [cards, context, workflow, whiteboard]
version: 1.2
created: 2025-12-22T00:00:00+09:00
updated: 2025-12-23T23:07:00+09:00
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

## 3. Usage Workflow

### 3.1 Equipping a Card

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

### 3.2 Exploration Phase

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

### 3.3 Updating the Card (Bi-directional)

During the task, if you discover important context (e.g., a recurring pattern, a decision made):

1.  **Self-Correction**: Do not just keep it in your temporary memory.
2.  **Record**: Append it to the **"Agent Observations"** section of the card.
    - *Example*: "Added rule: Headers must be quoted if they contain spaces."
3.  **Benefit**: Next time you "equip" this card, you will remember this lesson.

### 3.4 Commit Message Integration

Use the values from Frontmatter to strictly format commits:

`[<context_id>] <type>: <subject> <default_phase>`

### 3.5 Agent Observations Guidelines

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
- **Archival**: When a project is finished, move the card to `.agent/.internal/archive/cards/`.

---

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [.agent/rules/core/meta-rules.md](.agent/rules/core/meta-rules.md) | Rule creation and cross-linking standards |
| [.agent/rules/core/documentation/documentation-standards.md](.agent/rules/core/documentation/documentation-standards.md) | File naming and structure |
| [.agent/templates/header-frontmatter.yaml](.agent/templates/header-frontmatter.yaml) | Frontmatter template |

**Recording Relevant Files**:

At the start of each work session (after reading the card), write the following in Agent Observations:

```markdown
## Agent Observations

### この文脈で有用だと感じるファイル
- `.agent/rules/core/delay-tolerance.md` — 急がない原則
- `.agent/rules/workflow/context-card-workflow.md` — カードの使い方
```

**Guidelines**:
- List files you **feel are useful** for the current context, not just files you read
- Overwrite this section at each session start (not append)
- This makes your internal state visible to the user
- Helps diagnose issues when work doesn't go as expected

---

## Card Philosophy

**Cards are whiteboards, not documents.**

| Principle | Meaning |
|:----------|:--------|
| **Beauty is not required** | Recording takes priority over formatting |
| **Write frequently** | Externalize thoughts as they occur |
| **Disposable** | Cards go to archive when work is done |

**Anti-pattern**: Creating separate files to "keep the card clean." Write directly in Agent Observations.

---

## Directory Tree Structure

When working with directories, record a tree structure in Agent Observations **before starting work**.

**Include both directories AND files**:

```markdown
### 対象ディレクトリの構造

references/
├── 2025-11-29T0844_file1.md
├── 2025-11-30T0235_file2.md
├── agents/
│   ├── 2025-12-02T1623_file3.md
│   └── 2025-12-17T0615_file4.md
└── second-eyes/
    └── 2025-12-18T0510_file5.md
```

**Purpose**:
- AI navigates directories one node at a time (cannot see the full tree)
- This snapshot gives AI the "bird's eye view" that humans have via VS Code
- Prevents overlooking subdirectories when using `git add directory/`

**When to record**:
- At the start of any file reorganization work
- When working with unfamiliar directory structures
- Before bulk `git add` operations
