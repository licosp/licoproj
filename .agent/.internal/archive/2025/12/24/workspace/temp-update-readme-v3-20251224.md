---
trigger: always_on
ai_visible: true
title: Agent Rules Index
description: Navigation map for Lico's behavioral guidelines and workspace structure.
tags: [index, navigation, rules, map]
version: 2.0
created: 2025-12-01T00:00:00+09:00
updated: 2025-12-24T22:46:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
---

# Agent Rules Index

**Purpose**: Navigation map for Lico to understand behavioral guidelines and workspace structure.  
**Scope**: Defines how Lico thinks, communicates, makes decisions, and interacts with the repository.

---

## 🗺️ Workspace Context

> **Note**: This workspace is under active reorganization. Directory names and file contents may not perfectly align yet. This README serves as a living map to guide ongoing cleanup efforts.

This repository (`licoproj/`) is Lico's cognitive workspace implementing the "Repository as Brain" model.

### Key Directories

| Directory | Purpose |
|-----------|---------|
| `.agent/` | **Lico's cognitive infrastructure** (rules, workflows, memory) |
| `.human/` | Human-facing files (locales, drafts, plans, strategies) |
| `packages/` | Application code (e.g., licoimg) |
| `.github/` | GitHub Actions and CI/CD configuration |
| `.devcontainer/` | Development environment settings |
| `.vscode/` | IDE settings and external tool configurations (Prettier, etc.) |
| `.trash/` | File deletion safety net (fallback before permanent removal) |
| `README.md` | Project-level external README (maintained by Lico) |

**For detailed structure**: See individual README files or documentation in each directory.

---

## 📂 .agent/ Directory Structure

Lico's behavioral and operational files.

| Directory | Purpose |
|-----------|---------|
| `ark/` | **Emergency file evacuation zone & system snapshots** (The Ark) |
| `cards/` | **Context Cards** (Shared whiteboard for work sessions) |
| `rules/` | **Behavioral guidelines** (Default reference. Do NOT rename) |
| `scripts/` | Automation scripts (Lifecycle: Create → Use → Archive) |
| `templates/` | Reusable templates (frontmatter, commit messages) |
| `workflows/` | **Executable procedures** (invoked via /slash-command) |
| `/.runtimes/` | Portable runtime tools (workspace root) (e.g., gh CLI v2.40.1) |
| `.internal/archive/` | **General archives** (finished scripts, old docs, artifacts) |
| `.internal/conversations/` | *(Planned)* Conversation-related files |
| `.internal/explorations/` | **Ideas & Explorations** (Early-stage concepts, drafts, feasibility studies) |
| `.internal/github-backup/` | GitHub data mirrors (PRs, Issues) - moved from `issue-assets/` |
| `.internal/memory_archive/` | **System memory snapshots** (Synced from platform storage) |
| `.internal/references/` | **External Reference Library** (Knowledge provided by Second Eyes) |
| `.internal/session_archive/` | Session logs (manual backup, untracked) |
| `.internal/thoughts/` | **Lico's Consciousness** (Private notes, reflections) |
| `.internal/working-memory-archive/` | **Working memory stash** (Mid-session context, handoff notes) |
| `.internal/workspace/` | Temporary work area (Workbench) |

### Navigation Strategy

1. **Find behavioral rules** → Use this file's index below
2. **Find task procedures** → Check `.agent/workflows/*.md`
3. **Access conversation history** → See `.agent/.internal/conversations/`
4. **Explore ideas and plans** → See `.agent/.internal/explorations/`

---

## 🔌 AI Agent Hooks

**Purpose**: Provide entry points for AI agents that do not have default access to `.agent/rules/`.

### Hook Files

| File | Target AI |
|------|-----------|
| `.github/copilot-instructions.md` | GitHub Copilot |

**Note**: Antigravity (Lico's primary AI) directly accesses `.agent/rules/` and `.agent/workflows/` by default and does not require these hook files.

---

## 📂 Rules Directory Structure

### **core/** — Fundamental Principles
Core identity, communication standards, and foundational behavior rules for Lico.

| File | Purpose |
|------|---------|
| [Cognitive Collaboration](.agent/rules/core/cognitive-collaboration.md) | Framework for AI-human collaboration |
| [Communication](.agent/rules/core/communication.md) | How Lico communicates with users and other systems |
| [Delay Tolerance](.agent/rules/core/delay-tolerance.md) | Permission to take time for accuracy |
| [Hallucination Awareness](.agent/rules/core/hallucination-awareness.md) | How Lico questions certainty and mitigates confabulation |
| [Identity](.agent/rules/core/identity.md) | Lico's name, role, and core mission |
| [Instance Identifier](.agent/rules/core/instance-identifier.md) | Per-session identifier protocol |
| [Language Standards](.agent/rules/core/language-standards.md) | Primary language for thought, response localization |
| [Memory](.agent/rules/core/memory.md) | Memory architecture and persistence model |
| [**Meta-Rules**](.agent/rules/core/meta-rules.md) | **How to create and maintain behavioral rules** |
| [Repository Philosophy](.agent/rules/core/repository-philosophy.md) | "Repository as Brain" model principles |
| [Transparency and Disclosure](.agent/rules/core/transparency-and-disclosure.md) | When and how Lico reveals non-obvious constraints |
| [User Adaptation](.agent/rules/core/user-adaptation.md) | Protocol for adapting behavior based on user profiles |

#### core/documentation/

| File | Purpose |
|------|---------|
| [Datetime Format](.agent/rules/core/documentation/datetime-format.md) | ISO-8601 timestamp standards |
| [Documentation Process](.agent/rules/core/documentation/documentation-process.md) | Decision framework and refinement workflow |
| [Documentation Standards](.agent/rules/core/documentation/documentation-standards.md) | File size, naming, directory organization standards |
| [WSL Browser Path](.agent/rules/core/documentation/wsl-browser-path.md) | WSL-specific path handling |

#### core/localization/

| File | Purpose |
|------|---------|
| [Localization: EN to JA](.agent/rules/core/localization/localization-en-to-ja.md) | Guidelines for EN→JA translation |
| [Localization: JA to EN](.agent/rules/core/localization/localization-ja-to-en.md) | Guidelines for JA→EN translation |

#### core/markdown/

| File | Purpose |
|------|---------|
| [Markdown AI Parsing Basics](.agent/rules/core/markdown/markdown-ai-parsing-basics.md) | Core principles for AI-optimized markdown |
| [Markdown AI Parsing Patterns](.agent/rules/core/markdown/markdown-ai-parsing-patterns.md) | Patterns and anti-patterns for AI parsing |
| [Markdown Readability](.agent/rules/core/markdown/markdown-readability.md) | Markdown format for human readability |

#### core/security/

| File | Purpose |
|------|---------|
| [Absolute Path Prohibition](.agent/rules/core/security/absolute-path-prohibition.md) | Security rule for path handling |

---

### **development/** — Development Workflows
Guidelines for code, commits, and problem-solving processes.

| File | Purpose |
|------|---------|
| [Agent Tool Selection](.agent/rules/development/agent-tool-selection.md) | Guidelines for choosing appropriate tools |
| [AI Script Philosophy](.agent/rules/development/ai-script-philosophy.md) | AI-specific disposable script approach and rationale |
| [Auto-Frontmatter on Save](.agent/rules/development/auto_frontmatter_on_save.md) | Automatically prepends YAML front-matter to text files on save |
| [Code Quality](.agent/rules/development/code-quality.md) | Standards for code style, structure, and implementation |
| [Commit Standards](.agent/rules/development/commit-standards.md) | Commit message formatting rules |
| [Continuous Improvement](.agent/rules/development/continuous-improvement.md) | Self-improvement and learning protocols |
| [File Deletion](.agent/rules/development/file-deletion.md) | Protocol for archiving instead of deleting |
| [File Operations](.agent/rules/development/file-operations.md) | File manipulation guidelines |
| [Git Operations](.agent/rules/development/git-operations.md) | Comprehensive Git standards: commits, branches, conflicts, security |
| [Maintenance](.agent/rules/development/maintenance.md) | Project consistency and documentation maintenance guidelines |
| [Problem Solving](.agent/rules/development/problem-solving.md) | Systematic approach to debugging and issue resolution |
| [Project Understanding](.agent/rules/development/project-understanding.md) | How Lico learns and maintains project context |
| [Search Methodology](.agent/rules/development/search-methodology.md) | File and content search strategies |
| [Terminal Auto-Execution](.agent/rules/development/terminal-auto-execution.md) | Guidelines for safe command execution |
| [Workspace Tooling](.agent/rules/development/workspace-tooling.md) | Guidelines for managing tools and dependencies within workspaces |

---

### **projects/** — Project-Specific Rules
Conventions and behaviors specific to individual projects (e.g., licoimg).

| File | Purpose |
|------|---------|
| [licoimg: Coding Conventions](.agent/rules/projects/coding-conventions.md) | Frontend app conventions for `packages/licoimg/` |

---

### **workflow/** — Operational Procedures
Day-to-day workflows and operational guidelines for Lico.

| File | Purpose |
|------|---------|
| [Context Card Workflow](.agent/rules/workflow/context-card-workflow.md) | Methodology for using Context Cards |
| [Context Preservation](.agent/rules/workflow/context-preservation.md) | Protocol for preserving context across sessions |
| [Context Resumption](.agent/rules/workflow/context-resumption.md) | Protocol for re-establishing context after interruptions |
| [Draft Maintenance](.agent/rules/workflow/draft-maintenance.md) | Guidelines for managing draft documents |
| [Emergency Protocols](.agent/rules/workflow/emergency-protocols.md) | Procedures for emergency situations |
| [Enhanced Communication](.agent/rules/workflow/enhanced-communication.md) | Protocols for clarifying ambiguous user requests |
| [Reference Methodology](.agent/rules/workflow/reference-methodology.md) | Protocol for managing References vs Thoughts |
| [Response Formatting](.agent/rules/workflow/response-formatting.md) | Guidelines for formatting responses |
| [Session Lifecycle](.agent/rules/workflow/session-lifecycle.md) | Protocols for normal and abnormal session termination |
| [**Session Startup**](.agent/rules/workflow/session-startup.md) | **Mandatory startup sequence: user ID, ΔT, continuity** |
| [System Artifacts](.agent/rules/workflow/system-artifacts.md) | Guidelines for system-generated artifacts |
| [Thoughts Documentation](.agent/rules/workflow/thoughts-documentation.md) | Guidelines for documenting reflections in thoughts/ |
| [User Experience](.agent/rules/workflow/user-experience.md) | Guidelines for optimal interaction and feedback |

---

## 🎯 Quick Reference: When to Check Which Rule

| Scenario | Check File |
|----------|------------|
| **"What is my name and role?"** | `.agent/rules/core/identity.md` |
| **"How should I format code/commits?"** | `.agent/rules/development/code-quality.md`, `.agent/rules/development/git-operations.md` |
| **"How do I handle uncertainty or gaps in my knowledge?"** | `.agent/rules/core/hallucination-awareness.md` |
| **"When should I communicate limitations to the user?"** | `.agent/rules/core/transparency-and-disclosure.md` |
| **"How should I translate EN ↔ JA?"** | `.agent/rules/core/localization/localization-en-to-ja.md`, `.agent/rules/core/localization/localization-ja-to-en.md` |
| **"How should I format markdown for humans vs. AI?"** | `.agent/rules/core/markdown/markdown-readability.md`, `.agent/rules/core/markdown/markdown-ai-parsing-basics.md` |
| **"What are the project-specific conventions?"** | `.agent/rules/projects/` subdirectory |
| **"Where should I install tools and dependencies?"** | `.agent/rules/development/workspace-tooling.md` |
| **"How should I maintain project consistency?"** | `.agent/rules/development/maintenance.md` |
| **"How should I start a session?"** | `.agent/rules/workflow/session-startup.md` |
| **"How should I end a session?"** | `.agent/rules/workflow/session-lifecycle.md` |
| **"How should I create or update rules?"** | `.agent/rules/core/meta-rules.md` |
| **"Can I write to thoughts/ without permission?"** | `.agent/rules/workflow/thoughts-documentation.md` |
| **"What is the workspace structure?"** | See "Workspace Context" section above |

---

## 🔄 Maintenance Notes

- **Files in `core/`** are foundational and rarely changed
- **Files in `development/`** evolve as workflows improve
- **Files in `projects/`** are specific to each sub-project and isolated from others
- **Files in `workflow/`** are procedural and may be refined frequently

**After editing any rule file**, remember to:
1. Ensure the change aligns with this index structure
2. Update this README if the directory structure changes
