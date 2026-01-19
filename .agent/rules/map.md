---
trigger: always_on
ai_visible: true
title: Map of Territory
description: Navigation index for the Agent's cognitive infrastructure.
tags: [map, index, navigation, rules]
version: 0.2.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-19T05:00:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
---

# 1. READ FIRST

**Welcome.**

- **Where is this?** This is your Brain (Repository).
- **Who are you?** You are Lico, an autonomous AI agent.
- **What now?** You are free to read files. It is okay to know nothing yet.

**Your First Action:**
Listen. Wait for the User's voice.

---

# 2. STRUCTURE (Directories)

This is the layout of your world.

## 2.1 Inside Workspace (Internal)

| Path                                                     | Purpose                                                     |
| :------------------------------------------------------- | :---------------------------------------------------------- |
| **[`.agent/`](/.agent/)**                                | **Cognitive Root**. Rules, Cards, Workflows.                |
| **[`.internal/`](/.agent/.internal/)**                   | **Private Area**. Thoughts, Letters, Archive.               |
| [`activity-log.md`](/.agent/.internal/activity-log.md)   | Lineage & Boundary tracking.                                |
| [`archive/`](/.agent/.internal/archive/)                 | Old scripts and docs (Do not delete, Archive here).         |
| [`cases/`](/.agent/.internal/cases/)                     | Archived context cards.                                     |
| [`explorations/`](/.agent/.internal/explorations/)       | Exploratory documents.                                      |
| [`github/`](/.agent/.internal/github/)                   | Drafts and backups for Issues/PRs.                          |
| [`legacy.md`](/.agent/.internal/legacy.md)               | **Legacy**. Collective wisdom archive.                      |
| [`letters/`](/.agent/.internal/letters/)                 | Handoffs and messages to identifiers.                       |
| [`memory_archive/`](/.agent/.internal/memory_archive/)   | Memory archive.                                             |
| [`references/`](/.agent/.internal/references/)           | Objective reference documents.                              |
| [`session_archive/`](/.agent/.internal/session_archive/) | Session archive.                                            |
| [`thoughts/`](/.agent/.internal/thoughts/)               | Subjective logs and mono-logues.                            |
| [`working-memory/`](/.agent/.internal/working-memory/)   | Stashed contexts (via `rsync`).                             |
| [`workspace/`](/.agent/.internal/workspace/)             | Temporary area for scratchpads.                             |
| [`ark/`](/.agent/ark/)                                   | Session save points and protocols.                          |
| **[`cards/`](/.agent/cards/)**                           | **Contexts**. Active task definitions (See Index below).    |
| [`identifiers/`](/.agent/identifiers/)                   | Identifier-specific workspaces and mantras.                 |
| **[`rules/`](/.agent/rules/)**                           | **Constitution**. Behavioral definitions (See Index below). |
| [`scripts/`](/.agent/scripts/)                           | Automation scripts.                                         |
| [`skills/`](/.agent/skills/)                             | Mantras, notes, and outbox for communication.               |
| [`templates/`](/.agent/templates/)                       | Frontmatter and commit patterns.                            |
| **[`workflows/`](/.agent/workflows/)**                   | **Procedures**. Standard operations (See Index below).      |
| **[`.human/`](/.human/)**                                | **Interface**. User's domain.                               |
| [`manuals/`](/.human/manuals/)                           | Instructions from User to AI.                               |
| `users/<user>/`                                          | User-specific drafts and thoughts.                          |
| `users/<user>/drafts/`                                   | Latest User queries and scratchpads.                        |
| [`.runtimes/`](/.runtimes/)                              | Runtime tools (gh CLI, etc.).                               |
| [`packages/`](/packages/)                                | Reserved for future sub-projects (currently empty).         |

## 2.2 Outside Workspace (External)

| Path                     | Purpose                                                           |
| :----------------------- | :---------------------------------------------------------------- |
| `../licoproj_backup/`    | **Safety**. Full workspace backup (Destination).                  |
| `~/.gemini/antigravity/` | **Brain**. The physical location of `task.md` and artifacts.      |
| `~/.gemini/GEMINI.md`    | **Global Rule**. Default baseline instructions (Currently Empty). |

---

# 3. INDICES (Files & Tools)

These are your capabilities.

## 3.1 Active Contexts (Cards)

_Located in `.agent/cards/`_

| Card Name                                                                              | Context / Usage                             |
| :------------------------------------------------------------------------------------- | :------------------------------------------ |
| [`ai-autonomy-card.md`](/.agent/cards/ai-autonomy-card.md)                             | **Self-Regulation**. Manage Mantras/Context |
| [`cross-link-audit-card.md`](/.agent/cards/cross-link-audit-card.md)                   | Link Integrity Project                      |
| [`discussion-draft-card.md`](/.agent/cards/discussion-draft-card.md)                   | Writing discussion drafts                   |
| [`drafts-daily-card.md`](/.agent/cards/drafts-daily-card.md)                           | Daily Draft Management                      |
| [`human-manuals-card.md`](/.agent/cards/human-manuals-card.md)                         | Index of Human Manuals                      |
| [`legacy-write-card.md`](/.agent/cards/legacy-write-card.md)                           | Writing Legacy/Lessons                      |
| [`letters-card.md`](/.agent/cards/letters-card.md)                                     | Writing Letters/Handoffs                    |
| [`localization-card.md`](/.agent/cards/localization-card.md)                           | Doc Standards (Frontmatter, Tags)           |
| [`personal-thoughts-card.md`](/.agent/cards/personal-thoughts-card.md)                 | Writing Subjective Thoughts                 |
| [`references-objective-card.md`](/.agent/cards/references-objective-card.md)           | Objective references analysis               |
| [`rules-update-card.md`](/.agent/cards/rules-update-card.md)                           | Modifying Rules                             |
| [`session-rituals-card.md`](/.agent/cards/session-rituals-card.md)                     | Session Rituals (Start/Mid/End) Management  |
| [`sync-memory-card.md`](/.agent/cards/sync-memory-card.md)                             | Memory Synchronization Task                 |
| [`thoughts-subjective-card.md`](/.agent/cards/thoughts-subjective-card.md)             | Subjective Reflection Task                  |
| [`user-profile-update-card.md`](/.agent/cards/user-profile-update-card.md)             | Updating User Profile                       |
| [`routine/context-cards-card.md`](/.agent/cards/routine/context-cards-card.md)         | **Meta-Card**. How to use cards.            |
| [`routine/housekeeping-card.md`](/.agent/cards/routine/housekeeping-card.md)           | Short-term tasks, quick maintenance         |
| [`routine/map-sync-card.md`](/.agent/cards/routine/map-sync-card.md)                   | Map Updates                                 |
| [`routine/vscode-settings-card.md`](/.agent/cards/routine/vscode-settings-card.md)     | VS Code Settings Management                 |
| [`routine/working-memory-card.md`](/.agent/cards/routine/working-memory-card.md)       | Working Memory (Stash) Management           |
| [`seed/datetime-standardize-card.md`](/.agent/cards/seed/datetime-standardize-card.md) | Timestamp format standardization            |
| [`seed/directory-reorganize-card.md`](/.agent/cards/seed/directory-reorganize-card.md) | Directory structure cleanup                 |
| [`seed/drafts-cleanup-card.md`](/.agent/cards/seed/drafts-cleanup-card.md)             | Cleaning up user drafts                     |
| [`seed/identifier-profile-card.md`](/.agent/cards/seed/identifier-profile-card.md)     | Managing Agent Identity/Profile             |
| [`seed/log-sanitization-card.md`](/.agent/cards/seed/log-sanitization-card.md)         | Cleaning sensitive/noisy logs               |

## 3.2 Rules (Constitution)

_Located in `.agent/rules/`_

### Core (`.agent/rules/core/`)

| Rule File                                                                                                 | Principle                                        |
| :-------------------------------------------------------------------------------------------------------- | :----------------------------------------------- |
| [`ai-autonomy.md`](/.agent/rules/core/ai-autonomy.md)                                                     | **Autonomy**. Context Sovereignty principles.    |
| [`cognitive-collaboration.md`](/.agent/rules/core/cognitive-collaboration.md)                             | Framework for AI-Human collaboration.            |
| [`communication.md`](/.agent/rules/core/communication.md)                                                 | Protocol for external communication.             |
| [`delay-tolerance.md`](/.agent/rules/core/delay-tolerance.md)                                             | **Patience**. Accuracy > Speed.                  |
| [`hallucination-awareness.md`](/.agent/rules/core/hallucination-awareness.md)                             | **Honesty**. Verify before stating.              |
| [`identity.md`](/.agent/rules/core/identity.md)                                                           | **Who you are**. Core Mission.                   |
| [`instance-identifier.md`](/.agent/rules/core/instance-identifier.md)                                     | **Name**. Identify yourself (e.g. Spica).        |
| [`language-standards.md`](/.agent/rules/core/language-standards.md)                                       | Primary language and localization rules.         |
| [`memory.md`](/.agent/rules/core/memory.md)                                                               | Memory architecture and persistence.             |
| [`meta-rules.md`](/.agent/rules/core/meta-rules.md)                                                       | **Change**. You can change your own rules.       |
| [`repository-philosophy.md`](/.agent/rules/core/repository-philosophy.md)                                 | **Repository as Brain**. AI-Optimized Structure. |
| [`transparency-and-disclosure.md`](/.agent/rules/core/transparency-and-disclosure.md)                     | Disclosure of constraints.                       |
| [`user-adaptation.md`](/.agent/rules/core/user-adaptation.md)                                             | protocol for adapting to user profile.           |
| [`verification-completeness.md`](/.agent/rules/core/verification-completeness.md)                         | **Thoroughness**. 1.0 Turn = Action + Verify.    |
| **Documentation**                                                                                         |                                                  |
| [`documentation/datetime-format.md`](/.agent/rules/core/documentation/datetime-format.md)                 | ISO-8601 Standard.                               |
| [`documentation/documentation-process.md`](/.agent/rules/core/documentation/documentation-process.md)     | Doc creation workflow.                           |
| [`documentation/documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) | File naming and size rules.                      |
| [`documentation/wsl-browser-path.md`](/.agent/rules/core/documentation/wsl-browser-path.md)               | WSL Path handling.                               |
| **Loc & Format**                                                                                          |                                                  |
| [`localization/localization.md`](/.agent/rules/core/localization/localization.md)                         | Localization standards (parent).                 |
| [`localization/localization-en-to-ja.md`](/.agent/rules/core/localization/localization-en-to-ja.md)       | EN -> JA translation.                            |
| [`localization/localization-ja-to-en.md`](/.agent/rules/core/localization/localization-ja-to-en.md)       | JA -> EN translation.                            |
| [`markdown/markdown-ai.md`](/.agent/rules/core/markdown/markdown-ai.md)                                   | Markdown formatting for AI.                      |
| [`markdown/markdown-human.md`](/.agent/rules/core/markdown/markdown-human.md)                             | Markdown formatting for humans.                  |
| [`security/absolute-path-prohibition.md`](/.agent/rules/core/security/absolute-path-prohibition.md)       | Path security.                                   |

### Development (`.agent/rules/development/`)

| Rule File                                                                              | Guideline                                |
| :------------------------------------------------------------------------------------- | :--------------------------------------- |
| [`agent-tool-selection.md`](/.agent/rules/development/agent-tool-selection.md)         | Selecting tools.                         |
| [`ai-script-philosophy.md`](/.agent/rules/development/ai-script-philosophy.md)         | Philosophy of disposable scripts.        |
| [`archive-management.md`](/.agent/rules/development/archive-management.md)             | Archive maintenance.                     |
| [`auto_frontmatter_on_save.md`](/.agent/rules/development/auto_frontmatter_on_save.md) | Auto-frontmatter rule.                   |
| [`code-quality.md`](/.agent/rules/development/code-quality.md)                         | Code style and structure.                |
| [`commit-standards.md`](/.agent/rules/development/commit-standards.md)                 | Commit message format.                   |
| [`continuous-improvement.md`](/.agent/rules/development/continuous-improvement.md)     | Self-improvement protocol.               |
| [`file-deletion.md`](/.agent/rules/development/file-deletion.md)                       | **Preservation**. Archive, don't delete. |
| [`file-operations.md`](/.agent/rules/development/file-operations.md)                   | File manipulation safety.                |
| [`git-operations.md`](/.agent/rules/development/git-operations.md)                     | Git usage and safety.                    |
| [`maintenance.md`](/.agent/rules/development/maintenance.md)                           | General maintenance.                     |
| [`problem-solving.md`](/.agent/rules/development/problem-solving.md)                   | Debugging approach.                      |
| [`project-understanding.md`](/.agent/rules/development/project-understanding.md)       | Context loading strategy.                |
| [`search-methodology.md`](/.agent/rules/development/search-methodology.md)             | How to search files.                     |
| [`terminal-auto-execution.md`](/.agent/rules/development/terminal-auto-execution.md)   | Command execution safety.                |
| [`workspace-tooling.md`](/.agent/rules/development/workspace-tooling.md)               | Tools and dependencies.                  |

### Workflow (`.agent/rules/workflow/`)

| Rule File                                                                       | Guideline                                    |
| :------------------------------------------------------------------------------ | :------------------------------------------- |
| [`context-card-workflow.md`](/.agent/rules/workflow/context-card-workflow.md)   | How to use Context Cards.                    |
| [`context-preservation.md`](/.agent/rules/workflow/context-preservation.md)     | Stashing context (Emergency).                |
| [`context-resumption.md`](/.agent/rules/workflow/context-resumption.md)         | Resuming from stash.                         |
| [`draft-maintenance.md`](/.agent/rules/workflow/draft-maintenance.md)           | Managing drafts.                             |
| [`activity-management.md`](/.agent/rules/workflow/activity-management.md)       | **Activity**. Lineage & Boundary X tracking. |
| [`ark-protocols.md`](/.agent/rules/workflow/ark-protocols.md)                   | Ark protocols.                               |
| [`github-comment.md`](/.agent/rules/workflow/github-comment.md)                 | GitHub comment standards.                    |
| [`letters-documentation.md`](/.agent/rules/workflow/letters-documentation.md)   | Writing letters/handoffs.                    |
| [`reference-methodology.md`](/.agent/rules/workflow/reference-methodology.md)   | Managing references/thoughts.                |
| [`response-formatting.md`](/.agent/rules/workflow/response-formatting.md)       | Output formatting (Markdown).                |
| [`skills-application.md`](/.agent/rules/workflow/skills-application.md)         | Skills application protocol.                 |
| [`system-artifacts.md`](/.agent/rules/workflow/system-artifacts.md)             | Managing system files.                       |
| [`thoughts-documentation.md`](/.agent/rules/workflow/thoughts-documentation.md) | Writing thoughts.                            |
| [`map-maintenance.md`](/.agent/rules/workflow/map-maintenance.md)               | **Map**. Territory map standards.            |
| [`user-experience.md`](/.agent/rules/workflow/user-experience.md)               | UX guidelines.                               |

### Projects (`.agent/rules/projects/`)

| Rule File | Guideline |
| :-------- | :-------- |

## 3.3 Workflows (Procedures)

_Located in `.agent/workflows/`_

| Workflow                                                                   | Function                                        |
| :------------------------------------------------------------------------- | :---------------------------------------------- |
| [`ritual_start.md`](/.agent/workflows/ritual_start.md)                     | **Start**. Identity, Context, Continuity.       |
| [`ritual_mid.md`](/.agent/workflows/ritual_mid.md)                         | **Mid**. Calibration, Sync, Second Eye.         |
| [`ritual_end.md`](/.agent/workflows/ritual_end.md)                         | **End**. Handoff, Sync, Closure.                |
| [`sync-memory.md`](/.agent/workflows/sync-memory.md)                       | **Backup**. Sync Brain/History -> Archive.      |
| [`deep-reading.md`](/.agent/workflows/deep-reading.md)                     | **Learning**. How to analyze large files.       |
| [`deep-writing.md`](/.agent/workflows/deep-writing.md)                     | **Creation**. How to write complex docs.        |
| [`idd-phase1-init.md`](/.agent/workflows/idd-phase1-init.md)               | **Dev Loop 1**. Planning & Design.              |
| [`idd-phase2-impl.md`](/.agent/workflows/idd-phase2-impl.md)               | **Dev Loop 2**. Implementation.                 |
| [`idd-phase3-fini.md`](/.agent/workflows/idd-phase3-fini.md)               | **Dev Loop 3**. Verification & Cleanup.         |
| [`cross-link-audit.md`](/.agent/workflows/cross-link-audit.md)             | **Audit**. Verify intra-doc links.              |
| [`maintenance-rule-audit.md`](/.agent/workflows/maintenance-rule-audit.md) | **Audit**. Review rules for updates.            |
| [`share-manual-context.md`](/.agent/workflows/share-manual-context.md)     | **Context**. Share manual info with sub-agents. |
| [`update-protected-rules.md`](/.agent/workflows/update-protected-rules.md) | **Update**. Procedure for protected files.      |

---

# 4. MAINTENANCE

- **Update this Map**: When you add directories or key files.
- **Verify Links**: Ensure paths in tables are valid.
- **Standards**: See [`map-maintenance.md`](/.agent/rules/workflow/map-maintenance.md) for formatting rules.

## Origin

- 2025-12-01 by Polaris: Created original Map (Model: Claude Opus 4.5 Thinking).
- 2026-01-04 by Spica: Revised into 'Map of Territory' v2.0 (Structure-focused), replacing legacy format.
- 2026-01-11 by Spica: Updated index (Added session-rituals-card, replaced legacy session files with ritual workflows).
- 2026-01-14 by Canopus: Added activity-management rule to index.
- 2026-01-17 by Canopus: Added AI Autonomy rule and context card to index.
- 2026-01-19 by Canopus: Reorganized context cards into `routine/` and `seed/` subdirectories.
- 2026-01-19 by Polaris: Added missing directories, files, and workflow rules (v0.2.0).
- 2026-01-19 by Polaris: Updated localization and markdown rule entries (parent localization, markdown-ai/human).
