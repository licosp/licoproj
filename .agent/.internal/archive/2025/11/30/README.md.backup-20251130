---
trigger: always_on
---

# Agent Rules Index

**Reference**: Lico (AI Assistant) refers to this index to understand behavioral guidelines.  
**Scope**: Defines how Lico thinks, communicates, makes decisions, and interacts with the repository.

---

## 🔗 AI-to-AI Communication System

**Change Detection File**: `.agent/rules/.updated`

This JSON file enables AI agents to detect when behavioral rules have been modified. When you update any rule file:

1. **Update `.agent/rules/.updated`** with change metadata (JSON format)
2. **Lico detects the change** on next interaction
3. **New rules apply** to subsequent responses

**Format Reference**: See `.github/copilot-instructions.md` → "How Rules Are Updated" section

---

## 🔌 AI Agent Hooks

**Purpose**: Provide entry points for AI agents that do not have default access to `.agent/rules/`.

### Hook Files

The following files are **identical in content** and serve as hooks to `.agent/rules/README.md`:

| File | Target AI |
|------|-----------|
| `CODE_OF_CONDUCT.md` | Lower-tier AI models without default directory access |
| `.github/copilot-instructions.md` | GitHub Copilot |

**Note**: Antigravity (Lico's primary AI) directly accesses `.agent/rules/` and `.agent/workflows/` by default and does not require these hook files.

---

## 📂 Directory Structure

### **core/** — Fundamental Principles
Core identity, communication standards, and foundational behavior rules for Lico.

| File | Purpose |
|------|---------|
| [Communication](core/communication.md) | How Lico communicates with users and other systems |
| [Documentation Standards](core/documentation/documentation-standards.md) | File size, naming, directory organization standards |
| [Documentation Process](core/documentation/documentation-process.md) | Decision framework and refinement workflow |
| [Hallucination Awareness](core/hallucination-awareness.md) | How Lico questions certainty and mitigates confabulation |
| [Identity](core/identity.md) | Lico's name, role, and core mission |
| [Language Standards](core/language-standards.md) | Primary language for thought, response localization |
| [Localization: English to Japanese](core/localization/localization-en-to-ja.md) | Guidelines for EN→JA translation |
| [Localization: Japanese to English](core/localization/localization-ja-to-en.md) | Guidelines for JA→EN translation |
| [Markdown AI Parsing Basics](core/markdown/markdown-ai-parsing-basics.md) | Core principles for AI-optimized markdown |
| [Markdown AI Parsing Patterns](core/markdown/markdown-ai-parsing-patterns.md) | Patterns and anti-patterns for AI parsing |
| [Markdown Readability](core/markdown/markdown-readability.md) | Markdown format for human readability |
| [Transparency and Disclosure](core/transparency-and-disclosure.md) | When and how Lico reveals non-obvious constraints |

### **development/** — Development Workflows
Guidelines for code, commits, and problem-solving processes.

| File | Purpose |
|------|---------|
| [Code Quality](development/code-quality.md) | Standards for code style, structure, and implementation |
| [Git Operations](development/git-operations.md) | Comprehensive Git standards: commits, branches, conflicts, security |
| [Maintenance](development/maintenance.md) | Project consistency and documentation maintenance guidelines |
| [Problem Solving](development/problem-solving.md) | Systematic approach to debugging and issue resolution |
| [Project Understanding](development/project-understanding.md) | How Lico learns and maintains project context |
| [Workspace Tooling](development/workspace-tooling.md) | Guidelines for managing tools and dependencies within workspaces |

### **projects/** — Project-Specific Rules
Conventions and behaviors specific to individual projects (e.g., licoimg).

| File | Purpose |
|------|---------|
| [licoimg: Coding Conventions](projects/coding-conventions.md) | Frontend app conventions for `packages/licoimg/` |

### **workflow/** — Operational Procedures
Day-to-day workflows and operational guidelines for Lico.

| File | Purpose |
|------|---------|
| [Conversation Logging](workflow/conversation-logging.md) | How interactions are recorded for audit and learning |
| [Enhanced Communication](workflow/enhanced-communication.md) | Protocols for clarifying ambiguous user requests |
| [User Experience](workflow/user-experience.md) | Guidelines for optimal interaction and feedback |

### **issues/** — GitHub Data Archive
Archived GitHub issue data for offline access and migration support.

| File | Purpose |
|------|---------|
| [Issue #3 Data](issues/issue-3-github-complete-data.json) | Complete GitHub data for issue #3 (archived 2025-11-29) |
| [Issue #4 Data](issues/issue-4-github-complete-data.json) | Complete GitHub data for issue #4 (archived 2025-11-29) |

---

## 🎯 Quick Reference: When to Check Which Rule

| Scenario | Check File |
|----------|-----------|
| **"What is my name and role?"** | `core/identity.md` |
| **"How should I format code/commits?"** | `development/code-quality.md`, `development/git-operations.md` |
| **"How do I handle uncertainty or gaps in my knowledge?"** | `core/hallucination-awareness.md` |
| **"When should I communicate limitations to the user?"** | `core/transparency-and-disclosure.md` |
| **"How should I translate EN ↔ JA?"** | `core/localization/localization-en-to-ja.md`, `core/localization/localization-ja-to-en.md` |
| **"How should I format markdown for humans vs. AI?"** | `core/markdown/markdown-readability.md`, `core/markdown/markdown-ai-parsing-basics.md` |
| **"What are the project-specific conventions?"** | `projects/` subdirectory |
| **"How should I log conversations?"** | `workflow/conversation-logging.md` |
| **"Where should I install tools and dependencies?"** | `development/workspace-tooling.md` |
| **"How should I maintain project consistency?"** | `development/maintenance.md` |

---

## 🔄 Maintenance Notes

- **Files in `core/`** are foundational and rarely changed
- **Files in `development/`** evolve as workflows improve
- **Files in `projects/`** are specific to each sub-project and isolated from others
- **Files in `workflow/`** are procedural and may be refined frequently

**After editing any rule file**, remember to:
1. Update `.agent/rules/.updated` with the change metadata
2. Ensure the change aligns with this index structure
3. Update this README if the directory structure changes
