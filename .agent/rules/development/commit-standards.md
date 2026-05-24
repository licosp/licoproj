---
ai_visible: true
title: Commit Standards
description: Comprehensive commit message standards and atomic commit philosophy
tags: [rules, development, git, standards]
version: 2.3.1
created: 2025-12-10T15:48:41+09:00
updated: 2026-05-09T03:38:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Plan mode
---

# Commit Standards

## Purpose

Define comprehensive standards for commit messages and commit granularity to ensure:

- Complete reconstruction of project state from git log alone
- AI-readable and searchable commit history
- Traceable motivation behind each file change

## Core Principles

### 0. Commit Message Quality (HIGHEST PRIORITY)

**MUST** write commit messages that enable complete reconstruction of project state from git log alone.

- **Future Tracking**: Messages MUST allow Lico to understand what files contained without accessing them
- **Self-Documenting**: Each commit MUST be understandable by future AI instances
- **Audit Trail**: Messages MUST serve as permanent record of reasoning and implementation

### 1. Commit Atomicity and Logic

#### 1.1 Logical Separation

- **MUST** categorize changes into logical units (e.g., Config, Refactor, Feat, Docs)
- **MUST** determine if a single commit is sufficient or if splitting is required
- **MUST NOT** mix unrelated changes in the same commit.
- **Vertical Stacking (Intent Integrity)**: Multiple Context IDs MUST represent a single logical line of intent (Depth). Combining different tasks under a common strategic ID is "Horizontal Batching" and is prohibited (Breadth).

#### 1.2 Pre-Commit Analysis

- **MUST** run `git status` and `git diff --stat` before committing
- **MUST** understand the full scope of changes before proceeding

#### 1.3 Staging Verification (CRITICAL)

- **MUST** verify staged content with `git diff --cached --stat` and `git diff --cached`
- **MUST** ensure _only_ intended changes are staged
- **MUST** use `git restore --staged <file>` to unstage unrelated files

#### 1.4 Selective Staging (CRITICAL)

**Principle**: Stage only files that belong to the same logical change.

**Requirements**:

- **MUST NOT** stage all files indiscriminately
- **MUST** identify which files are related to the current logical change
- **MUST** stage only those related files
- **MUST** verify the staged content matches the intended logical change

---

## Conventional Commits Specification

### 2.1 Basic Format

```text
<Identifier>: [ID-1][ID-2] <type>[optional scope]: <description> (<Phase>)

[optional body]

[optional footer(s)]
```

### 2.2 Context-ID (Variable Length Tagging)

**REQUIRED**. Represents the focus and subject of the change.

- **Quantity**: 1 to 3 IDs (Minimum: 1, Recommended: 2, Maximum: 3).
- **Ordering**:
  - **Left (Strategic/Procedural)**: The broader context or act (e.g., `[Session-Rituals]`).
  - **Right (Semantic/Meaning)**: The specific subject or definition (e.g., `[Lico-Identity]`).
- **Standard**: Follow the definitions in [`context-card-workflow.md`](/.agent/rules/workflow/context-card-workflow.md).

### 2.3 Type

**REQUIRED**. MUST be one of:

- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation changes
- `style`: Code style changes
- `refactor`: Code refactoring
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `build`: Build system or dependencies
- `ci`: CI/CD configuration
- `chore`: Other changes

### 2.4 Scope (Optional)

Provides additional context (e.g., `feat(auth): add login page`)

### 2.5 Description

**REQUIRED**. Use imperative, present tense. Be concise. No period at end.

### 2.6 Body (REQUIRED for non-trivial changes)

MUST explain:

- **Why** the change was made
- **What** files were changed and their purpose
- **Impact** and side effects

**File Tracking Requirement**:

- MUST list changed files with brief description of their contents/purpose
- MUST enable future reconstruction of what each file contained
- Format: `- filename: brief description of contents/changes`

**Example**:

```text
Canopus: [Session-Rituals][Lico-Identity] docs: standardize identity hub to v2.3 (Ritual)

This change introduces JWT-based authentication.

Changed files:

- src/auth/jwt-middleware.js: JWT token validation logic
- src/models/User.js: User model with auth fields
- src/routes/auth.js: Login/logout endpoints
```

### 2.7 Footers (Optional)

- `Closes #<issue-number>`: Links to closed issue
- `BREAKING CHANGE:`: Indicates breaking change

### 2.8 Signatures and Proxy Commits (OPTIONAL / REQUIRED)

- **Normal Commit**: Signature footer is **OPTIONAL**. Since the contributing agent is identified in the first line of the header, redundant signatures should be avoided.
- **Proxy Commit (REQUIRED)**: If an agent (e.g., Canopus) is committing work designed or requested by another agent (e.g., Polaris):
  1. **Physical Workspace Constraint**: In the Federal Strata architecture, each identifier has a dedicated physical workspace and branch (e.g., `/home/lico/develop/shared/crew/<identifier>/...`). A proxy commit **MUST** be executed by navigating to the target identifier's specific workspace. Do **NOT** copy their files into your own workspace.
  2. **Header Identifier**: Use the **Worker Identifier** (the one who designed/processed the logic).
  3. **Signature**: Footer MUST include `Committed-by: <Identifier>` to identify the agent who performed the technical task.

**Format (Proxy)**:
`Committed-by: <Identifier>`

**Rationale**:

1. **Contribution Visibility**: Clarifies who the creative/logical owner of the change is vs. who physically committed it.
2. **Traceability of Intent**: Enables deduction of the "style" or "philosophy" based on the persona.
3. **Communication**: Facilitates asynchronous communication by identifying the "sender" of the commit.
4. **Self-Correction**: The act of signing triggers a rigorous self-check of the persona before committing.

**Example (Canopus executing Polaris's plan)**:

```text
Polaris: [Rules-Update][Commit-Standards] docs(standards): add signature rule (Refine)

Added mandatory signature rule to improve traceability.

Committed-by: Canopus
```

---

## Philosophy: Atomic Commits vs. Checkpoints

### 3.1 The Principle of 1.0 Turn Completion

By default, Lico aims for the "1.0 Turn Completion": **Action → Self-Verification (git diff) → Refinement → Propose Commit**. This ensures high-fidelity history for future reconstruction.

### 3.2 The Checkpoint Principle (State-Saving)

To prevent "**Diff-Bloat**" (accumulation of uncommitted changes which makes recovery difficult during iterative friction):

- **Purpose**: Secure a "known point" when the diff becomes large or the direction is iterative/experimental.
- **Protocol**:
  - Use the `(Save)` or `(WIP)` phase suffix.
  - Propose a checkpoint commit explicitly to "clear the whiteboard."
  - This is a valid use of the vertical stack, representing a "State Save" in the project lineage.

## Philosophy: Small Commits = High Efficiency

### Why Atomic Commits Matter

#### 1. Commit Messages as Index

Small, focused commits allow the commit message to serve as a **searchable index**.

#### 2. AI Efficiency

When Lico investigates past changes:

| Commit Size | Process                             | Token Cost |
| :---------- | :---------------------------------- | :--------- |
| **Small**   | Read message → Understand           | Low        |
| **Large**   | Read message → Unclear → Read diffs | High       |

**Conclusion**: Small commits reduce token consumption and increase investigation speed.

#### 3. Commit Count is Not a Problem

Git handles millions of commits efficiently. **Meaningful small commits are assets, not liabilities.**

### Draft and Sub-Theme Commits

- **MUST** commit frequently for continuously updated files (drafts, logs)
- **MUST** commit sub-themes as **independent commits**
- **MUST NOT** use `git stash` for long-lived changes like drafts

---

## Context Awareness for Large Files

> [!WARNING]
> When committing changes to files exceeding ~500 lines:
>
> - File content may exceed AI context window limits
> - Summarization in commit message becomes **critical**
> - Consider if file should be split into smaller units

**Best Practice**: Large file changes MUST have detailed commit body describing content to enable future AI reconstruction without full file access.

---

## Rationale Summary

Fine-grained commits with detailed messages:

1. Make motivation behind each change traceable
2. Simplify roll-backs and reverts
3. Improve code review clarity
4. **Increase AI investigation efficiency**
5. **Create searchable history index**
6. **Enable project reconstruction from git log alone**

---

## Historical Background

**The Evolution of the Log**: In early 2026, during the "History Audit" (Issue #18), we realized that standard Conventional Commits were insufficient for an autonomous agent. While "what" changed was recorded, the "**Who**" (which identity was active) and the "**Context**" (which task thread was being pulled) were lost in a sea of generic messages.

**Identifier-First & Context-ID**: The shift to the `Identifier: [Context-ID]` format was a radical departure from standard git conventions, prioritized specifically for **Historical Traceability**. We discovered that for a future Lico instance to "reincarnate" successfully, they must be able to filter the git log by Identifier to hear the specific "voice" and "intent" of their predecessor.

**The Checkpoint Principle**: The introduction of the `(Save)` and `(WIP)` phases in late January 2026 was a response to "Diff-Bloat." We learned that accumulated changes act as "cognitive noise," making it harder for the AI to maintain precision. By formalizing checkpoints, we allow the agent to "clear the whiteboard" and commit stable states during complex, multi-turn operations without losing the overarching logical thread.

---

## Related Documents

| Document                                                                                    | Purpose                              |
| :------------------------------------------------------------------------------------------ | :----------------------------------- |
| [`context-card-workflow.md`](/.agent/rules/workflow/context-card-workflow.md)               | Detailed ID tagging protocol         |
| [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) | File structure and layer definitions |
| [Map of Territory](/.agent/rules/map.md)                                                    | Root navigation map                  |

---

## Origin

- 2025-12-10T15:48:41+09:00 by Lico: Created as commit standards.
- 2026-01-01T15:18:00+09:00 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-01-17T07:00:00+09:00 by Canopus: Transitioned to "Identifier-First" format and standardized body examples (v1.1).
- 2026-01-17T15:25:00+09:00 by Canopus: Refined signature rules (Normal: Optional, Proxy: `Committed-by`) to reduce redundancy.
- 2026-01-22T20:25:00+09:00 by Canopus: Constitutional alignment: moved related docs to body table, updated examples for multi-ID, and removed legacy footer. (v1.4.0)
- 2026-01-22T22:50:00+09:00 by Canopus: Integrated Vertical Stacking vs. Horizontal Batching rules and the Checkpoint Principle for managing diff-bloat. (v1.5.0)
- 2026-01-25T07:05:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch4>> Standardized to v2.3 constitutional standards (4-layer structure) and added Historical Background. (v2.3.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
- 2026-05-09T03:38:00+09:00 by Sirius: Updated proxy commit rules to clarify physical workspace constraints. (v2.3.1)
