---
description: Comprehensive commit message standards and atomic commit philosophy
tags: [rules, development, git, standards]
version: 1.2
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-17T15:40:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
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
- **MUST NOT** mix unrelated changes in the same commit

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

\`\`\`
<Identifier>: [<Context-ID>] <type>[optional scope]: <description> (<Phase>)

[optional body]

[optional footer(s)]
\`\`\`

### 2.2 Type

**REQUIRED**. MUST be one of:

- \`feat\`: New feature
- \`fix\`: Bug fix
- \`docs\`: Documentation changes
- \`style\`: Code style changes
- \`refactor\`: Code refactoring
- \`perf\`: Performance improvements
- \`test\`: Adding or updating tests
- \`build\`: Build system or dependencies
- \`ci\`: CI/CD configuration
- \`chore\`: Other changes

### 2.3 Scope (Optional)

Provides additional context (e.g., \`feat(auth): add login page\`)

### 2.4 Description

**REQUIRED**. Use imperative, present tense. Be concise. No period at end.

### 2.5 Body (REQUIRED for non-trivial changes)

MUST explain:

- **Why** the change was made
- **What** files were changed and their purpose
- **Impact** and side effects

**File Tracking Requirement**:

- MUST list changed files with brief description of their contents/purpose
- MUST enable future reconstruction of what each file contained
- Format: \`- filename: brief description of contents/changes\`

**Example**:
\`\`\`
Canopus: [Feat-Auth] feat: add user authentication module (Done)

This change introduces JWT-based authentication.

Changed files:

- src/auth/jwt-middleware.js: JWT token validation logic
- src/models/User.js: User model with auth fields
- src/routes/auth.js: Login/logout endpoints
  \`\`\`

### 2.6 Footers (Optional)

- \`Closes #<issue-number>\`: Links to closed issue
- \`BREAKING CHANGE:\`: Indicates breaking change

### 2.7 Signatures and Proxy Commits (OPTIONAL / REQUIRED)

- **Normal Commit**: Signature footer is **OPTIONAL**. Since the contributing agent is identified in the first line of the header, redundant signatures should be avoided.
- **Proxy Commit (REQUIRED)**: If an agent (e.g., Canopus) is committing work designed or requested by another agent (e.g., Polaris):
  1.  **Header Identifier**: Use the **Worker Identifier** (the one who designed/processed the logic).
  2.  **Signature**: Footer MUST include `Committed-by: <Identifier>` to identify the agent who performed the technical task.

**Format (Proxy)**:
`Committed-by: <Identifier>`

**Rationale**:

1.  **Contribution Visibility**: Clarifies who the creative/logical owner of the change is vs. who physically committed it.
2.  **Traceability of Intent**: Enables deduction of the "style" or "philosophy" based on the persona.
3.  **Communication**: Facilitates asynchronous communication by identifying the "sender" of the commit.
4.  **Self-Correction**: The act of signing triggers a rigorous self-check of the persona before committing.

**Example (Canopus executing Polaris's plan)**:

```
Polaris: [Rules-Update] docs(standards): add signature rule (Refine)

Added mandatory signature rule to improve traceability.

Committed-by: Canopus
```

---

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
- **MUST NOT** use \`git stash\` for long-lived changes like drafts

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

## Origin

- 2025-12-01T0000: Created as commit standards
- 2026-01-01T1518 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-01-17T0700 by Canopus: Transitioned to "Identifier-First" format and standardized body examples (v1.1).
- 2026-01-17T1525 by Canopus: Refined signature rules (Normal: Optional, Proxy: `Committed-by`) to reduce redundancy.

---

**Navigation**: [← Back to Rules Index](/.agent/rules/README.md)
