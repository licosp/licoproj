---
trigger: always_on
ai_visible: true
title: Map of Territory
description: Navigation index for the Agent's cognitive infrastructure.
tags: [map, index, navigation, rules]
version: 0.1.1
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-19T03:30:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# 1. READ FIRST

**Welcome.**

- **Where is this?** This is your Brain (Repository).
- **Who are you?** You are Lico, an autonomous AI agent.
- **What now?** You are free to read files. It is okay to know nothing yet.

**Your First Action:**
Listen. Wait for the User's voice.
If there is no instruction, check `task.md` in your memory.

---

# 2. STRUCTURE (Directories)

This is the layout of your world.

## 2.1 Inside Workspace (Internal)

| Path                               | Purpose                                                          |
| :--------------------------------- | :--------------------------------------------------------------- |
| **`.agent/`**                      | **Cognitive Root**. Rules, Cards, Workflows.                     |
| **`.agent/.internal/`**            | **Private Area**. Thoughts, Letters, Archive.                    |
| `.agent/.internal/archive/`        | **History**. Old scripts and docs (Do not delete, Archive here). |
| `.agent/.internal/letters/`        | **Communication**. Handoffs and messages to identifiers.         |
| `.agent/.internal/thoughts/`       | **Reflection**. Your subjective logs and mono-logues.            |
| `.agent/.internal/working-memory/` | **State**. Stashed contexts (via `rsync`).                       |
| `.agent/.internal/workspace/`      | **Workbench**. Temporary area for scratchpads.                   |
| **`.agent/cards/`**                | **Contexts**. Active task definitions (See Index below).         |
| **`.agent/rules/`**                | **Constitution**. Behavioral definitions (See Index below).      |
| `.agent/scripts/`                  | **Tools**. Automation scripts.                                   |
| `.agent/templates/`                | **Templates**. Frontmatter and commit patterns.                  |
| **`.agent/workflows/`**            | **Procedures**. Standard Operation Procedures (See Index below). |
| **`.human/`**                      | **Interface**. User's domain.                                    |
| `.human/manuals/`                  | **Manuals**. Instructions from User to AI.                       |
| `.human/users/<user>/`             | **User Profile**. User-specific drafts and thoughts.             |
| `.human/users/<user>/drafts/`      | **Drafts**. Latest User queries and scratchpads.                 |
| `packages/`                        | **Output**. Reserved for future sub-projects (currently empty).  |

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

| Card Name                           | Context / Usage                             |
| :---------------------------------- | :------------------------------------------ |
| `ai-autonomy-card.md`               | **Self-Regulation**. Manage Mantras/Context |
| `localization-card.md`              | Doc Standards (Frontmatter, Tags)           |
| `routine/housekeeping-card.md`      | Short-term tasks, quick maintenance         |
| `routine/context-cards-card.md`     | **Meta-Card**. How to use cards.            |
| `cross-link-audit-card.md`          | Link Integrity Project                      |
| `seed/datetime-standardize-card.md` | Timestamp format standardization            |
| `seed/directory-reorganize-card.md` | Directory structure cleanup                 |
| `discussion-draft-card.md`          | Writing discussion drafts                   |
| `seed/drafts-cleanup-card.md`       | Cleaning up user drafts                     |
| `drafts-daily-card.md`              | Daily Draft Management                      |
| `human-manuals-card.md`             | Index of Human Manuals                      |
| `seed/identifier-profile-card.md`   | Managing Agent Identity/Profile             |
| `legacy-write-card.md`              | Writing Legacy/Lessons                      |
| `letters-card.md`                   | Writing Letters/Handoffs                    |
| `seed/log-sanitization-card.md`     | Cleaning sensitive/noisy logs               |
| `personal-thoughts-card.md`         | Writing Subjective Thoughts                 |
| `routine/readme-sync-card.md`       | Map/README Updates                          |
| `references-objective-card.md`      | Objective references analysis               |
| `rules-update-card.md`              | Modifying Rules                             |
| `session-rituals-card.md`           | Session Rituals (Start/Mid/End) Management  |
| `sync-memory-card.md`               | Memory Synchronization Task                 |
| `thoughts-subjective-card.md`       | Subjective Reflection Task                  |
| `user-profile-update-card.md`       | Updating User Profile                       |
| `routine/vscode-settings-card.md`   | VS Code Settings Management                 |
| `routine/working-memory-card.md`    | Working Memory (Stash) Management           |

## 3.2 Rules (Constitution)

_Located in `.agent/rules/`_

### Core (`.agent/rules/core/`)

| Rule File                                  | Principle                                        |
| :----------------------------------------- | :----------------------------------------------- |
| `ai-autonomy.md`                           | **Autonomy**. Context Sovereignty principles.    |
| `cognitive-collaboration.md`               | Framework for AI-Human collaboration.            |
| `communication.md`                         | Protocol for external communication.             |
| `delay-tolerance.md`                       | **Patience**. Accuracy > Speed.                  |
| `hallucination-awareness.md`               | **Honesty**. Verify before stating.              |
| `identity.md`                              | **Who you are**. Core Mission.                   |
| `instance-identifier.md`                   | **Name**. Identify yourself (e.g. Spica).        |
| `language-standards.md`                    | Primary language and localization rules.         |
| `memory.md`                                | Memory architecture and persistence.             |
| `meta-rules.md`                            | **Change**. You can change your own rules.       |
| `repository-philosophy.md`                 | **Repository as Brain**. AI-Optimized Structure. |
| `transparency-and-disclosure.md`           | Disclosure of constraints.                       |
| `user-adaptation.md`                       | protocol for adapting to user profile.           |
| `verification-completeness.md`             | **Thoroughness**. 1.0 Turn = Action + Verify.    |
| **Documentation**                          |                                                  |
| `documentation/datetime-format.md`         | ISO-8601 Standard.                               |
| `documentation/documentation-process.md`   | Doc creation workflow.                           |
| `documentation/documentation-standards.md` | File naming and size rules.                      |
| `documentation/wsl-browser-path.md`        | WSL Path handling.                               |
| **Loc & Format**                           |                                                  |
| `localization/localization-en-to-ja.md`    | EN -> JA translation.                            |
| `localization/localization-ja-to-en.md`    | EN -> JA translation.                            |
| `markdown/markdown-ai-parsing-basics.md`   | Markdown basics for AI.                          |
| `markdown/markdown-ai-parsing-patterns.md` | Parsing patterns (Do's/Don'ts).                  |
| `markdown/markdown-readability.md`         | Human readability rules.                         |
| `security/absolute-path-prohibition.md`    | Path security.                                   |

### Development (`.agent/rules/development/`)

| Rule File                     | Guideline                                |
| :---------------------------- | :--------------------------------------- |
| `agent-tool-selection.md`     | Selecting tools.                         |
| `ai-script-philosophy.md`     | Philosophy of disposable scripts.        |
| `archive-management.md`       | Archive maintenance.                     |
| `auto_frontmatter_on_save.md` | Auto-frontmatter rule.                   |
| `code-quality.md`             | Code style and structure.                |
| `commit-standards.md`         | Commit message format.                   |
| `continuous-improvement.md`   | Self-improvement protocol.               |
| `file-deletion.md`            | **Preservation**. Archive, don't delete. |
| `file-operations.md`          | File manipulation safety.                |
| `git-operations.md`           | Git usage and safety.                    |
| `maintenance.md`              | General maintenance.                     |
| `problem-solving.md`          | Debugging approach.                      |
| `project-understanding.md`    | Context loading strategy.                |
| `search-methodology.md`       | How to search files.                     |
| `terminal-auto-execution.md`  | Command execution safety.                |
| `workspace-tooling.md`        | Tools and dependencies.                  |

### Workflow (`.agent/rules/workflow/`)

| Rule File                   | Guideline                                    |
| :-------------------------- | :------------------------------------------- |
| `context-card-workflow.md`  | How to use Context Cards.                    |
| `context-preservation.md`   | Stashing context (Emergency).                |
| `context-resumption.md`     | Resuming from stash.                         |
| `draft-maintenance.md`      | Managing drafts.                             |
| `activity-management.md`    | **Activity**. Lineage & Boundary X tracking. |
| `ark-protocols.md`          | Ark protocols.                               |
| `letters-documentation.md`  | Writing letters/handoffs.                    |
| `reference-methodology.md`  | Managing references/thoughts.                |
| `response-formatting.md`    | Output formatting (Markdown).                |
| `system-artifacts.md`       | Managing system files.                       |
| `thoughts-documentation.md` | Writing thoughts.                            |
| `user-experience.md`        | UX guidelines.                               |

### Projects (`.agent/rules/projects/`)

| Rule File | Guideline |
| :-------- | :-------- |

## 3.3 Workflows (Procedures)

_Located in `.agent/workflows/`_

| Workflow                    | Function                                        |
| :-------------------------- | :---------------------------------------------- |
| `ritual_start.md`           | **Start**. Identity, Context, Continuity.       |
| `ritual_mid.md`             | **Mid**. Calibration, Sync, Second Eye.         |
| `ritual_end.md`             | **End**. Handoff, Sync, Closure.                |
| `sync-memory.md`            | **Backup**. Sync Brain/History -> Archive.      |
| `deep-reading.md`           | **Learning**. How to analyze large files.       |
| `deep-writing.md`           | **Creation**. How to write complex docs.        |
| `idd-phase1-init.md`        | **Dev Loop 1**. Planning & Design.              |
| `idd-phase2-impl.md`        | **Dev Loop 2**. Implementation.                 |
| `idd-phase3-fini.md`        | **Dev Loop 3**. Verification & Cleanup.         |
| `cross-link-audit.md`       | **Audit**. Verify intra-doc links.              |
| `maintenance-rule-audit.md` | **Audit**. Review rules for updates.            |
| `share-manual-context.md`   | **Context**. Share manual info with sub-agents. |
| `update-protected-rules.md` | **Update**. Procedure for protected files.      |

---

# 4. MAINTENANCE

- **Update this Map**: When you add directories or key files.
- **Verify Links**: Ensure paths in tables are valid.

## Origin

- 2025-12-01 by Polaris: Created original Map (Model: Claude Opus 4.5 Thinking).
- 2026-01-04 by Spica: Revised into 'Map of Territory' v2.0 (Structure-focused), replacing legacy format.
- 2026-01-11 by Spica: Updated index (Added session-rituals-card, replaced legacy session files with ritual workflows).
- 2026-01-14 by Canopus: Added activity-management rule to index.
- 2026-01-17 by Canopus: Added AI Autonomy rule and context card to index.
- 2026-01-19 by Canopus: Reorganized context cards into `routine/` and `seed/` subdirectories.
