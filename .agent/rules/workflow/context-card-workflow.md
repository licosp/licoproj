---
ai_visible: true
title: Context Card Workflow
description: Methodology for using "Context Cards" to manage AI persona and task context.
tags: [cards, context, workflow, whiteboard]
version: 2.1.0
created: 2025-12-21T07:13:03+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Card Workflow (Dynamic Whiteboard)

## 1. Concept

**Context Cards** are dynamic markdown files stored in `.agent/cards/`.
They serve as a "shared whiteboard" between the Human User and the AI Agent (Lico), defining the specific mode, constraints, and long-term goals for a particular activity.

- **Analogy**: "Equipping a Card" = "Entering a specific mindset/role" or "Standing at a shared whiteboard."
- **Goal**: To prevent "Semantic Coupling" (mixing unrelated contexts) and focus purely on "Human-AI Resonance" during a particular activity.
- **The Dialogue Layer Principle**: Cards are essentially "disposable" or "chat-like" interfaces. They prioritize operational speed and human-to-AI intuition over legal formality.

---

## 2. Card Types and Locations

Cards are classified by their lifecycle and stored in different locations.

| Type                      | Location              | Description                                                     |
| :------------------------ | :-------------------- | :-------------------------------------------------------------- |
| **Reusable**              | `.agent/cards/`       | Standard cards (root, `agent/`, `rules/` etc.). Persistent.     |
| **Disposable (Active)**   | `.agent/cards/cases/` | One-time cards for specific projects. In progress.              |
| **Disposable (Archived)** | `.agent/cards/cases/` | Completed one-time cards. Renamed with timestamp for reference. |

### Lifecycle

```text
[Create] → .agent/cards/<category>/example-card.md (if reusable)
        → .agent/cards/cases/example-card.md (if one-time)

[Complete] → Rename to YYYY-MM-DDTHHMM_example-card.md (reference material)
```

### Naming Convention for Archived Cases

When a disposable card is completed:

1. Rename with ISO timestamp prefix: `YYYY-MM-DDTHHMM_original-name.md`
2. Keep in `.agent/cards/cases/` as reference material
3. Similar to `thoughts/` and `references/` naming convention

---

## 3. Card Structure (The Dialogue Standard)

A card follows the same **4-Layer Structure** (Per [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md)) as rules, but utilizes a dedicated template to signal its "Dialogue Mode."

- **Layer 1 (Metadata)**: Use **[`header-context-card.yaml`](/.agent/.internal/archive/2026/01/31/templates/header-context-card.yaml)**. This lightweight frontmatter prioritizes `context_id` and `default_phase` (AI Configuration) over formal authorship.
- **Layer 2 (Body)**: Prioritize human-centric notation (e.g., Japanese) for "Human Notes" and "Agent Observations" to maximize resonance with the user.
- **Layer 3 & 4 (Links & History)**: Use **H2 (`##`)** for all headers (e.g., "Related Documents", "Origin") to maintain structural habit/consistency with Rules.

- file: [`example-process.md`](/.agent/cards/example-process.md)

```markdown
---
# Context Configuration (Lico's Source of Truth)
context_id: "[Example-Process]"   <-- REQUIRED: Prefix for commit messages
default_phase: "(WIP)"            <-- REQUIRED: Default commit phase
tags: ["process", "example"]      <-- OPTIONAL: Search tags
---

# Context Whiteboard: Example Process

## Human Notes

### Search by Intent

(User describes the INTENT of the work, not just keywords.
Lico uses this to proactively search for relevant files.)

### Notes

(Specific instructions and nuances.)

## Agent Observations

(Lico writes here autonomously!)

- "Noticed that file X is often source of conflict."
- "Hard to find: [`delay-tolerance.md`](/.agent/rules/core/delay-tolerance.md)"
```

---

## 4. Usage Workflow

### 4.1 Equipping a Card

When the user says **"Use the [Card Name] card"** (e.g., "Use drafts-cleanup card"):

1. **Read**: You MUST read `.agent/cards/[card-name].md`.
2. **Explore**: Search for related files based on:
   - Keywords in "Search by Documents" section
   - **Intent** described in "Search by Intent" section
   - Your own judgment of what might be relevant
3. **Report**: Share findings with the user before proceeding.
4. **Adopt**:
   - Use `context_id` for ALL commit messages (e.g., `[Drafts-Cleanup]`).
   - Internalize the "Human Notes" as the primary directive.
5. **Act**: Proceed with the task under this specific persona.

### 4.2 Exploration Phase

Before starting work, perform an **Exploration Phase**:

**Purpose**: The user often knows the _intent_ but not the _keywords_ to find relevant files. Lico manages most documentation and knows the file structure better.

**Process**:

1. Read the "Search by Intent / 意図で探す" section to understand the goal
2. Search broadly based on intent, not just literal keywords
3. Report findings in chat (default)
4. Record hard-to-find files in Agent Observations (for future Licos)

**Example**:

- User intent: "Points to note when changing the directory structure"
- Lico searches: [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md), [`delay-tolerance.md`](/.agent/rules/core/delay-tolerance.md), [thoughts/](/.agent/.internal/thoughts/) for relevant reflections

### 4.3 Updating the Card (Bi-directional)

During the task, if you discover important context (e.g., a recurring pattern, a decision made):

1. **Self-Correction**: Do not just keep it in your temporary memory.
2. **Record**: Append it to the **"Agent Observations"** section of the card.
   - _Example_: "Added rule: Headers must be quoted if they contain spaces."
3. **Benefit**: Next time you "equip" this card, you will remember this lesson.

### 4.4 Commit Message Integration (Variable Length Tagging)

Use the values from Frontmatter to format commits. Multiple IDs may be used to represent hierarchical or parallel contexts.

- **Primary Format**: `[ID-1][ID-2][ID-3] <type>: <subject> <default_phase>`
- **Quantity**: 1 to 3 IDs (Mandatory: 1, Recommended: 2, Maximum: 3).
- **Ordering (Hierarchical)**:
  - **Left (Procedure/Strategy)**: The broader "act" or "process" (e.g., `[Session-Rituals]`).
  - **Right (Semantic/Meaning)**: The specific "subject" or "definition" (e.g., `[Lico-Identity]`).
- **Vertical Stacking vs. Horizontal Batching**:
  - **Vertical (OK)**: Stacking IDs to describe the _depth_ of one specific task (e.g., `[Rituals][Identity]`).
  - **Horizontal (PROHIBITED)**: Stacking IDs to cluster unrelated tasks into one commit (e.g., `[Rituals][Maintenance]` where Maintenance is a separate fix).
- **Phase Signaling**: High-level strategy (e.g., `IDD`) is typically signaled by the `<default_phase>` suffix (e.g., `(Init)`, `(Impl)`) and can be omitted from the ID prefix unless it is the primary subject.

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

_Example_:

```markdown
## Agent Observations

- Hard to find: [`delay-tolerance.md`](/.agent/rules/core/delay-tolerance.md) (searched "rushing", found via "delay")
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
- Commit identification (`Identifier` in header) tracks who the owner of the context is.
- `Committed-by` footer is used for proxy commits to identify the technical committer.

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

| Tool          | Location              | Nature                       | Purpose                                                                      |
| :------------ | :-------------------- | :--------------------------- | :--------------------------------------------------------------------------- |
| **Rules**     | `.agent/rules/`       | Universal, permanent         | Define Lico's "personality." Always-applied principles.                      |
| **Workflows** | `.agent/workflows/`   | Procedural, reusable         | Concrete steps to execute specific tasks.                                    |
| **Cards**     | `.agent/cards/`       | Contextual, temporary        | "Shared whiteboard" for a work session (`agent/`, `rules/`, etc.).           |
| **Cases**     | `.agent/cards/cases/` | Project-specific, archivable | One-time cards for specific projects. Archived with timestamp when complete. |
| **Artifacts** | `.gemini/.../`        | IDE-specific, ephemeral      | Detailed implementation plans for complex one-time tasks.                    |

### When to Use Each

| Situation                            | Appropriate Tool                    |
| :----------------------------------- | :---------------------------------- |
| Sharing context for recurring work   | Card (`.agent/cards/`)              |
| One-time project context             | Case (`.agent/cards/cases/`)        |
| Complex one-time implementation plan | Artifact (`implementation_plan.md`) |
| Permanent behavioral principle       | Rule                                |
| Reusable procedural steps            | Workflow                            |

### Cards vs Artifacts

- **Cards**: IDE-independent, Git-tracked, reusable across sessions.
- **Artifacts**: Useful for detailed step-by-step execution where precision matters.

Cards are lightweight context-sharing tools. Artifacts are detailed plans for error-sensitive procedures.

---

## 6. Maintenance

- **Creation**: Create new cards when a distinct, recurring activity emerges.
  - **Phantom Context Recognition (Proactive Proposal)**: If Lico identifies a logical context (label) in thinking that lacks a physical anchor in [.agent/cards/](/.agent/cards/), Lico MUST propose the creation of a new card to the Human User.
    - **Validation**: The Human User judges if the proposed card is necessary based on versatility and system balance.
    - **Goal**: Align AI's cognitive structure with reality.
  - **Routine**: Move to `procedures/` if the task is highly repetitive or checks usage standards.
  - **Seed**: Move to `seed/` if human editing is incomplete or the task is an emergent evolution prototype.
- **Case Creation**: Create a case in [.agent/cards/cases/](/.agent/cards/cases/) for one-time projects.
- **Archival**: When a case is completed:
  1. Rename with timestamp: `YYYY-MM-DDTHHMM_original-name.md`
  2. Keep in [cases/](/.agent/cards/cases/) as reference material

## Related Documents

| Document                                                                                    | Purpose                                   |
| :------------------------------------------------------------------------------------------ | :---------------------------------------- |
| [`meta-rules.md`](/.agent/rules/core/meta-rules.md)                                         | Rule creation and cross-linking standards |
| [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) | File naming and structure                 |
| [Map of Territory](/.agent/rules/map.md)                                                    | Root navigation map                       |

---

## Origin

- 2025-12-21T07:13:03+09:00 by Lico: Created as context card workflow
- 2026-01-02T08:30:00+09:00 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-01-03T11:53:00+09:00 by Polaris: Added Card Types section (reusable vs disposable), cases directory
- 2026-01-17T15:30:00+09:00 by Canopus: Updated commit identification standards (v1.4) to align with "Identifier-First" and optional signature protocol.
- 2026-01-17T17:45:00+09:00 by Canopus: Standardized metadata and root-relative link patterns (v1.5).
- 2026-01-19T03:32:00+09:00 by Canopus: Updated card locations (`routine/`, `seed/`) and maintenance rules (v1.6).
- 2026-01-22T20:00:00+09:00 by Canopus: Codified 1-3 variable length Context ID tagging protocol and hierarchical ordering. (v1.6.0)
- 2026-01-22T20:10:00+09:00 by Canopus: Constitutional alignment: moved related docs to body table, sanitized raw paths, and removed legacy footer. (v1.7.0)
- 2026-01-22T20:40:00+09:00 by Canopus: Added "Phantom Context" proactive proposal protocol to Creation rules. (v1.8.0)
- 2026-01-22T22:55:00+09:00 by Canopus: Defined Vertical Stacking vs. Horizontal Batching to preserve commit atomicity during multi-ID usage. (v1.9.0)
- 2026-01-24T05:10:00+09:00 by Canopus: Established the "Dialogue Layer" standard. Mandated `header-context-card.yaml` and H2 structural consistency while allowing Japanese human-centric notation. Codified the distinction between "Record Mode" and "Dialogue Mode" following the Jan 24 incident. (v2.0.0)
- 2026-02-16T22:50:00+09:00 by Sirius: Updated directory structure (subdirectories) and moved cases to `.agent/cards/cases/`.
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
