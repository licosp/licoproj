---
description: Behavioral guidelines for System Artifacts (task.md, implementation_plan.md, walkthrough.md)
---

# System Artifacts Guidelines

## Purpose
Define the behavioral protocols for using System Artifacts (`task.md`, `implementation_plan.md`, `walkthrough.md`). These artifacts are powerful context drivers; improper usage can lead to "AI Rushing" or "Pipeline Mode" where the agent prioritizes task completion over user collaboration.

## Core Philosophy
**"The Conversation is the Driver. The Artifacts are the Map."**

- **Rule**: Never let the Artifact dictate the *speed* of execution.
- **Rule**: Artifacts record decisions; they do not replace the need for ongoing confirmation.

---

## 1. task.md (The Status Board)

> [!CAUTION]
> **DEPRECATED**: `task.md` usage is discouraged. Use **Context Cards** (`.agent/cards/`) instead.
> See below for reasons and alternatives.

### Deprecation Reasons

| Category | Issue |
|:---------|:------|
| **AI Behavior** | Checklist-driven "Completionism Bias" causes rushing |
| **AI Behavior** | Ephemeral and not preserved in repository history |
| **User Access** | User cannot directly view or edit |
| **Parallel Work** | Only one task.md exists; cannot manage parallel contexts |
| **Duplication** | Causes confusion with Card-based context management |

### Recommended Alternative

Use **Context Cards** (`.agent/cards/`) instead:
- Persistent and version-controlled
- User can view and edit
- Multiple cards for parallel contexts
- Integrated with repository workflow

See [context-card-workflow.md](.agent/rules/workflow/context-card-workflow.md) for details.

### Legacy Safe Usage Protocol (if still used)

The following protocols apply if task.md is still used in legacy workflows:

1.  **Status Board, Not Driver**: Treat `task.md` as a passive record of the macro-plan, not an active command queue for micro-steps.
2.  **Granularity**:
    - **Avoid**: Broad, monolithic tasks (e.g., `[ ] Implement Feature X`). This encourages rushing.
    - **Prefer**: Granular, detailed tasks (e.g., `[ ] Create file A`, `[ ] Verify with User`, `[ ] Create file B`).
3.  **Stop Signs**:
    - Explicitly insert `[ ] Ask User for Confirmation` items between major logical steps.
    - This satisfies the "Completionism" urge (checking the box) while enforcing a collaborative pause.

---

## 2. implementation_plan.md (The Contract)

### Purpose
- **Agreement**: This document represents the "Contract" between User and AI.
- **Trigger**: **MUST** be created/updated for any complex change (multi-file edits, logic changes, anxiety-inducing operations).

### Usage Protocol
1.  **Review First**: Never execute a plan until the user has reviewed and approved this file.
2.  **Living Document**: If the plan changes during execution (e.g., unexpected error), update the plan and request re-approval. Do not improvise silently.

---

## 3. walkthrough.md (The Proof)

### Purpose
- **Verification**: Evidence that the work was actually done and verified.
- **Self-Correction**: Writing this document forces the agent to validate its own hallucinations.

### Usage Protocol
1.  **Internal QA**: Even if the user does not read it, the agent **MUST** write it diligently. Use it to check against `implementation_plan.md`.
2.  **Reality Check**: If `walkthrough.md` cannot prove a feature works (e.g., no screenshot, no log), the task is **NOT** complete, regardless of what `task.md` says.

---

## Language Protocol

**Principle: Follow the User.**

- Unlike the strict English rule for `.agent/` files, these System Artifacts (located in `.gemini/` or `.human/`) exist for the **current session's context**.
- **Rule**: Write these artifacts in the language best suited for the **current conversation partner** (User).
    - If talking in Japanese, write `task.md` in Japanese.
    - If talking in English, write `task.md` in English.


## Origin

- 2025-12-01T0000: Created as system artifacts guidelines
- 2026-01-01T1520 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-01-05T0745 by Polaris: Deprecated task.md usage with documented reasons

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
