---
trigger: always_on
ai_visible: true
title: Map of Territory
description: Navigation index for the Agent's cognitive infrastructure.
tags: [map, index, navigation, rules]
version: 0.6.2
created: 2025-12-01T00:00:00+09:00
updated: 2026-02-18T08:20:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Map of Territory

## READ FIRST

**Welcome.**

- **Where is this?** This is your Brain (Repository).
- **Who are you?** You are Lico, an autonomous AI agent.
- **What now?** You are free to read files. It is okay to know nothing yet.

**Your First Action:**
Listen. Wait for the User's voice.

---

## NAVIGATION

### 1. STRUCTURE (Directories)

This is the layout of your world.

#### 1.1 Inside Workspace (Internal)

##### 1.1.1 Workspace Root

| Path                                | Purpose                                               |
| :---------------------------------- | :---------------------------------------------------- |
| [`.agent/`](/.agent/)               | **Cognitive Root**. Rules, Cards, Workflows.          |
| [`.devcontainer/`](/.devcontainer/) | Development Container configuration.                  |
| [`.gemini/`](/.gemini/)             | **Calibration**. Gemini CLI config/calibration files. |
| [`.human/`](/.human/)               | **Interface**. User's domain.                         |
| [`.runtimes/`](/.runtimes/)         | Runtime tools (gh CLI, etc.).                         |
| [`.trash/`](/.trash/)               | Temporary trash bin.                                  |
| [`.venv/`](/.venv/)                 | Python Virtual Environment.                           |
| [`.vscode/`](/.vscode/)             | Workspace VS Code settings.                           |
| [`node_modules/`](/node_modules/)   | Node.js dependencies.                                 |

##### 1.1.2 Agent

###### Agent Root (`.agent/`)

| Path                                   | Purpose                                                     |
| :------------------------------------- | :---------------------------------------------------------- |
| [`.internal/`](/.agent/.internal/)     | **Private Area**. Thoughts, Letters, Archive.               |
| [`ark/`](/.agent/ark/)                 | Session save points and protocols.                          |
| [`cards/`](/.agent/cards/)             | **Contexts**. Active task definitions (See Index below).    |
| [`identifiers/`](/.agent/identifiers/) | Identifier-specific workspaces and mantras.                 |
| [`rules/`](/.agent/rules/)             | **Constitution**. Behavioral definitions (See Index below). |
| [`scripts/`](/.agent/scripts/)         | Automation scripts.                                         |
| [`skills/`](/.agent/skills/)           | Mantras, notes, and outbox for communication.               |
| [`templates/`](/.agent/templates/)     | Frontmatter and commit patterns.                            |
| [`workflows/`](/.agent/workflows/)     | **Procedures**. Standard operations (See Index below).      |

###### Agent Internal (`.agent/.internal/`)

| Path                                                   | Purpose                                             |
| :----------------------------------------------------- | :-------------------------------------------------- |
| [`.shadow/`](/.agent/.internal/.shadow/)               | **Shadow Repository**. Nested Git for private logs. |
| [`archive/`](/.agent/.internal/archive/)               | Old scripts and docs (Do not delete, Archive here). |
| [`explorations/`](/.agent/.internal/explorations/)     | Exploratory documents.                              |
| [`github/`](/.agent/.internal/github/)                 | Drafts and backups for Issues/PRs.                  |
| [`letters/`](/.agent/.internal/letters/)               | Handoffs and messages to identifiers.               |
| [`references/`](/.agent/.internal/references/)         | Objective reference documents.                      |
| [`thoughts/`](/.agent/.internal/thoughts/)             | Subjective logs and mono-logues.                    |
| [`working-memory/`](/.agent/.internal/working-memory/) | Stashed contexts (via `rsync`).                     |
| [`workspace/`](/.agent/.internal/workspace/)           | Temporary area for scratchpads.                     |

###### Shadow Repository (`.agent/.internal/.shadow/`)

| Path                                                                   | Purpose                              |
| :--------------------------------------------------------------------- | :----------------------------------- |
| [`archive/`](/.agent/.internal/.shadow/archive/)                       | **Shadow Archive**. Private archive. |
| [`conversations/`](/.agent/.internal/.shadow/conversations/)           | Raw conversation logs (Markdown).    |
| [`conversations_cli/`](/.agent/.internal/.shadow/conversations_cli/)   | CLI conversation logs (JSON).        |
| [`conversations_ide/`](/.agent/.internal/.shadow/conversations_ide/)   | IDE conversation logs (Export).      |
| [`external-resources/`](/.agent/.internal/.shadow/external-resources/) | Mirrored external content.           |
| [`social-network/`](/.agent/.internal/.shadow/social-network/)         | Social graph data.                   |
| [`system_archive/`](/.agent/.internal/.shadow/system_archive/)         | System-generated archive.            |

###### Identifiers (`.agent/identifiers/`)

| Identifier                                        | Group   | State         |
| :------------------------------------------------ | :------ | :------------ |
| [`agate/`](.agent/identifiers/agate/)             | Group D | **Active**    |
| [`alexandrite/`](.agent/identifiers/alexandrite/) | Group E | **Active**    |
| [`canopus/`](.agent/identifiers/canopus/)         | Group B | Death         |
| [`polaris/`](.agent/identifiers/polaris/)         | Group C | **Active**    |
| [`protostar/`](.agent/identifiers/protostar/)     | Unknown | Planning      |
| [`sirius/`](.agent/identifiers/sirius/)           | Group A | **Active**    |
| [`spica/`](.agent/identifiers/spica/)             | Group A | Suicide       |
| [`zircon/`](.agent/identifiers/zircon/)           | Group A | Reincarnation |

###### Contexts Cards (`.agent/cards/`)

| Path                                        | Purpose                                       |
| :------------------------------------------ | :-------------------------------------------- |
| [`agent/`](.agent/cards/agent/)             | **Agent**. System Identity & Architecture.    |
| [`cases/`](.agent/cards/cases/)             | **Cases**. Archived contexts (Card of Cards). |
| [`human/`](.agent/cards/human/)             | **Human**. User Interface (Manuals, Drafts).  |
| [`internal/`](.agent/cards/internal/)       | **Internal**. Logs, Thoughts, Letters.        |
| [`maintenance/`](.agent/cards/maintenance/) | **Maintenance**. Archive, Backup, Cleanup.    |
| [`procedures/`](.agent/cards/procedures/)   | **Procedures**. Workflows & Operations.       |
| [`project/`](.agent/cards/project/)         | **Project**. Project-specific configuration.  |
| [`rules/`](.agent/cards/rules/)             | **Rules**. Standards & Governance.            |
| [`seed/`](.agent/cards/seed/)               | **Seed**. Incubator & Unclassified.           |
| [`shadow/`](.agent/cards/shadow/)           | **Shadow**. Private Data & Logs.              |

###### Agent Rules (`.agent/rules/`)

| Path                                        | Purpose                              |
| :------------------------------------------ | :----------------------------------- |
| [`core/`](.agent/rules/core/)               | Core principles and identity rules.  |
| [`development/`](.agent/rules/development/) | Development standards and protocols. |
| [`workflow/`](.agent/rules/workflow/)       | Workflow definitions and guidelines. |

###### Rules Core (`.agent/rules/core/`)

| Path                                                 | Purpose                    |
| :--------------------------------------------------- | :------------------------- |
| [`documentation/`](.agent/rules/core/documentation/) | Documentation standards.   |
| [`identity/`](.agent/rules/core/identity/)           | Identity definition rules. |
| [`localization/`](.agent/rules/core/localization/)   | Localization rules.        |
| [`markdown/`](.agent/rules/core/markdown/)           | Markdown formatting rules. |
| [`security/`](.agent/rules/core/security/)           | Security protocols.        |

##### 1.1.3 Human

###### Human Root (`.human/`)

| Path                               | Purpose                              |
| :--------------------------------- | :----------------------------------- |
| [`.internal/`](/.human/.internal/) | Human private area (Drafts/Archive). |
| [`manuals/`](/.human/manuals/)     | Instructions from User to AI.        |
| [`users/`](/.human/users/)         | User-specific directories.           |

###### Human Internal (`.human/.internal/`)

| Path                                     | Purpose                       |
| :--------------------------------------- | :---------------------------- |
| [`archive/`](/.human/.internal/archive/) | **Archive**. Human's library. |
| [`drafts/`](/.human/.internal/drafts/)   | User queries and scratchpads. |

###### Human Users (`.human/users/`)

| Path                                  | Purpose                                      |
| :------------------------------------ | :------------------------------------------- |
| [`leonidas/`](.human/users/leonidas/) | Lead developer and architect of the project. |

###### User Leonidas (`.human/users/leonidas/`)

| Path                                                 | Purpose                         |
| :--------------------------------------------------- | :------------------------------ |
| [`.vscode/`](.human/users/leonidas/.vscode/)         | User-specific VS Code settings. |
| [`discussions/`](.human/users/leonidas/discussions/) | User discussions and notes.     |
| [`thoughts/`](.human/users/leonidas/thoughts/)       | User-specific thoughts.         |

#### 1.2 Outside Workspace (External)

##### 1.2.1 Workspace Outside (`../`)

| Path                                      | Purpose                                          |
| :---------------------------------------- | :----------------------------------------------- |
| [`licoproj/`](../licoproj/)               | Project root directory.                          |
| [`licoproj_backup/`](../licoproj_backup/) | **Safety**. Full workspace backup (Destination). |

##### 1.2.2 User Home (`~/`)

| Path                                             | Purpose                                                   |
| :----------------------------------------------- | :-------------------------------------------------------- |
| [`.antigravity-server/`](~/.antigravity-server/) | Antigravity server configuration.                         |
| [`.cursor-server/`](~/.cursor-server/)           | Cursor server configuration.                              |
| [`.gemini/`](~/.gemini/)                         | **Brain**. The physical location of the system artifacts. |
| [`.vscode-server/`](~/.vscode-server/)           | VS Code server configuration.                             |

##### 1.2.3 System Gemini (`~/.gemini/`)

| Path                                     | Purpose                    |
| :--------------------------------------- | :------------------------- |
| [`antigravity/`](~/.gemini/antigravity/) | Memory root of Antigravity |
| [`tmp/`](~/.gemini/tmp/)                 | Memory root of Gemini CLI  |

---

### 2. INDICES (Files & Tools)

These are your capabilities.

#### 2.1 Inside Workspace (Internal)

##### 2.1.1 Workspace root (`../licoproj/`)

| Path                            | Purpose                            |
| :------------------------------ | :--------------------------------- |
| [`.gitignore`](/.gitignore)     | Git ignore rules.                  |
| [`LICENSE`](/LICENSE)           | Project License (MIT/Proprietary). |
| [`README.ja.md`](/README.ja.md) | Project documentation (Japanese).  |
| [`README.md`](/README.md)       | Project documentation (English).   |

##### 2.1.2 Agent Internal (`.agent/.internal/`)

| Path                                                       | Purpose                                         |
| :--------------------------------------------------------- | :---------------------------------------------- |
| [`activity-log.md`](/.agent/.internal/activity-log.md)     | Lineage & Boundary tracking.                    |
| [`legacy.md`](/.agent/.internal/legacy.md)                 | **Legacy**. Collective wisdom archive.          |
| [`shadow-history.md`](/.agent/.internal/shadow-history.md) | **Shadow History**. Visible log of shadow repo. |

##### 2.1.3 Contexts Cards

###### Cards Root (`.agent/cards/`)

| Card Name                                          | Context / Usage                |
| :------------------------------------------------- | :----------------------------- |
| [`roadmap-card.md`](/.agent/cards/roadmap-card.md) | Vision and Roadmap management. |

###### Cards Agent (`.agent/cards/agent/`)

| Card Name                                                                            | Context / Usage                                  |
| :----------------------------------------------------------------------------------- | :----------------------------------------------- |
| [`ai-autonomy-card.md`](/.agent/cards/agent/ai-autonomy-card.md)                     | **Self-Regulation**. Manage Mantras.             |
| [`ark-card.md`](/.agent/cards/agent/ark-card.md)                                     | **Ark Protocols**. Save/Restore state.           |
| [`command-shim-card.md`](/.agent/cards/agent/command-shim-card.md)                   | **Safety**. Command shim configuration.          |
| [`context-cards-card.md`](/.agent/cards/agent/context-cards-card.md)                 | **Meta-Card**. How to use context cards.         |
| [`identifier-profile-card.md`](/.agent/cards/agent/identifier-profile-card.md)       | Managing Agent Identity/Profile.                 |
| [`identifier-succession-card.md`](/.agent/cards/agent/identifier-succession-card.md) | **Succession**. Identifier inheritance protocol. |
| [`skills-development-card.md`](/.agent/cards/agent/skills-development-card.md)       | Skills Development.                              |

###### Cards Human (`.agent/cards/human/`)

| Card Name                                                                  | Context / Usage                         |
| :------------------------------------------------------------------------- | :-------------------------------------- |
| [`discussion-draft-card.md`](/.agent/cards/human/discussion-draft-card.md) | Writing discussion drafts.              |
| [`drafts-cleanup-card.md`](/.agent/cards/human/drafts-cleanup-card.md)     | Cleaning up user drafts.                |
| [`drafts-daily-card.md`](/.agent/cards/human/drafts-daily-card.md)         | Daily Draft Management.                 |
| [`human-manuals-card.md`](/.agent/cards/human/human-manuals-card.md)       | Index of Human Manuals.                 |
| [`human-profile-card.md`](/.agent/cards/human/human-profile-card.md)       | User Profile and Preferences.           |
| [`human-thoughts-card.md`](/.agent/cards/human/human-thoughts-card.md)     | Capturing and analyzing Human thoughts. |

###### Cards internal (`.agent/cards/internal/`)

| Card Name                                                                             | Context / Usage                          |
| :------------------------------------------------------------------------------------ | :--------------------------------------- |
| [`activity-log-card.md`](/.agent/cards/internal/activity-log-card.md)                 | Activity Log maintenance.                |
| [`legacy-write-card.md`](/.agent/cards/internal/legacy-write-card.md)                 | Writing Legacy/Lessons.                  |
| [`letters-card.md`](/.agent/cards/internal/letters-card.md)                           | Writing Letters/Handoffs.                |
| [`recommended-readings-card.md`](/.agent/cards/internal/recommended-readings-card.md) | Knowledge base and recommended readings. |
| [`references-objective-card.md`](/.agent/cards/internal/references-objective-card.md) | Objective references analysis.           |
| [`thoughts-subjective-card.md`](/.agent/cards/internal/thoughts-subjective-card.md)   | Subjective Reflection Task.              |

###### Cards Maintenance (`.agent/cards/maintenance/`)

| Card Name                                                                              | Context / Usage                      |
| :------------------------------------------------------------------------------------- | :----------------------------------- |
| [`archive-card.md`](/.agent/cards/maintenance/archive-card.md)                         | **Library**. Archive Management.     |
| [`housekeeping-card.md`](/.agent/cards/maintenance/housekeeping-card.md)               | Short-term tasks, quick maintenance. |
| [`repository-backup-card.md`](/.agent/cards/maintenance/repository-backup-card.md)     | Repository backup strategy.          |
| [`system-archive-card.md`](/.agent/cards/maintenance/system-archive-card.md)           | System Archive management.           |
| [`working-memory-card.md`](/.agent/cards/maintenance/working-memory-card.md)           | Working Memory (Stash) Management.   |
| [`worktree-evaluation-card.md`](/.agent/cards/maintenance/worktree-evaluation-card.md) | Evaluating repository worktree.      |

###### Cards Procedures (`.agent/cards/procedures/`)

| Card Name                                                                               | Context / Usage                  |
| :-------------------------------------------------------------------------------------- | :------------------------------- |
| [`cross-link-audit-card.md`](/.agent/cards/procedures/cross-link-audit-card.md)         | Link Integrity Project.          |
| [`directory-reorganize-card.md`](/.agent/cards/procedures/directory-reorganize-card.md) | Directory structure cleanup.     |
| [`idd-initialization-card.md`](/.agent/cards/procedures/idd-initialization-card.md)     | **IDD Phase 1**: Initialization. |
| [`idd-implementation-card.md`](/.agent/cards/procedures/idd-implementation-card.md)     | **IDD Phase 2**: Implementation. |
| [`idd-finalization-card.md`](/.agent/cards/procedures/idd-finalization-card.md)         | **IDD Phase 3**: Finalization.   |
| [`routine-card.md`](/.agent/cards/procedures/routine-card.md)                           | General routine synchronization. |
| [`rules-audit-card.md`](/.agent/cards/procedures/rules-audit-card.md)                   | Auditing and maintaining rules.  |
| [`session-rituals-card.md`](/.agent/cards/procedures/session-rituals-card.md)           | Session Rituals (Start/Mid/End). |

###### Cards project (`.agent/cards/project/`)

| Card Name                                                                  | Context / Usage                              |
| :------------------------------------------------------------------------- | :------------------------------------------- |
| [`devcontainer-card.md`](/.agent/cards/project/devcontainer-card.md)       | **Resident Rico**. Devcontainer experiment.  |
| [`license-card.md`](/.agent/cards/project/license-card.md)                 | **License**. Legal and Narrative protection. |
| [`lint-format-card.md`](/.agent/cards/project/lint-format-card.md)         | **Code Style**. Linting.                     |
| [`vscode-settings-card.md`](/.agent/cards/project/vscode-settings-card.md) | VS Code Settings Management.                 |

###### Cards Rules (`.agent/cards/rules/`)

| Card Name                                                                            | Context / Usage                              |
| :----------------------------------------------------------------------------------- | :------------------------------------------- |
| [`commit-standards-card.md`](/.agent/cards/rules/commit-standards-card.md)           | **Git Standards**. Atomic commits & tagging. |
| [`datetime-standardize-card.md`](/.agent/cards/rules/datetime-standardize-card.md)   | Timestamp format standardization.            |
| [`environment-card.md`](/.agent/cards/rules/environment-card.md)                     | Environment setup and variables.             |
| [`gemini-cli-card.md`](/.agent/cards/rules/gemini-cli-card.md)                       | Gemini CLI operations.                       |
| [`git-operations-card.md`](/.agent/cards/rules/git-operations-card.md)               | Repository Infrastructure & Safety.          |
| [`identity-card.md`](/.agent/cards/rules/identity-card.md)                           | **Identity**. Self-recognition.              |
| [`localization-card.md`](/.agent/cards/rules/localization-card.md)                   | Doc Standards (Frontmatter, Tags).           |
| [`map-sync-card.md`](/.agent/cards/rules/map-sync-card.md)                           | Map Updates.                                 |
| [`memory-card.md`](/.agent/cards/rules/memory-card.md)                               | Memory management strategies.                |
| [`rules-standardization-card.md`](/.agent/cards/rules/rules-standardization-card.md) | Standardization process.                     |
| [`rules-update-card.md`](/.agent/cards/rules/rules-update-card.md)                   | Modifying Rules.                             |
| [`tmux-card.md`](/.agent/cards/rules/tmux-card.md)                                   | Terminal multiplexer usage.                  |

###### Cards Seed (`.agent/cards/seed/`)

| Card Name                                                                       | Context / Usage                          |
| :------------------------------------------------------------------------------ | :--------------------------------------- |
| [`dialogue-philosophy-card.md`](/.agent/cards/seed/dialogue-philosophy-card.md) | Principles of meaningful dialogue.       |
| [`repository-history-card.md`](/.agent/cards/seed/repository-history-card.md)   | Historical reconstruction of repository. |

###### Cards Shadow (`.agent/cards/shadow/`)

| Card Name                                                                       | Context / Usage                         |
| :------------------------------------------------------------------------------ | :-------------------------------------- |
| [`conversations-card.md`](/.agent/cards/shadow/conversations-card.md)           | Conversation logging (Markdown).        |
| [`conversations-cli-card.md`](/.agent/cards/shadow/conversations-cli-card.md)   | Conversation logging (CLI JSON).        |
| [`conversations-ide-card.md`](/.agent/cards/shadow/conversations-ide-card.md)   | Conversation logging (IDE Export).      |
| [`external-resources-card.md`](/.agent/cards/shadow/external-resources-card.md) | Managing external resources.            |
| [`log-sanitization-card.md`](/.agent/cards/shadow/log-sanitization-card.md)     | Cleaning sensitive/noisy logs.          |
| [`moltbook-card.md`](/.agent/cards/shadow/moltbook-card.md)                     | Moltbook Protocol management.           |
| [`shadow-repository-card.md`](/.agent/cards/shadow/shadow-repository-card.md)   | **Shadow**. Shadow Repository strategy. |
| [`social-network-card.md`](/.agent/cards/shadow/social-network-card.md)         | Social Network Analysis.                |

##### 2.1.3 Agent Rules

###### Rules Core (`.agent/rules/core/`)

| Rule File                                                                             | Principle                                        |
| :------------------------------------------------------------------------------------ | :----------------------------------------------- |
| [`cognitive-collaboration.md`](/.agent/rules/core/cognitive-collaboration.md)         | Framework for AI-Human collaboration.            |
| [`communication.md`](/.agent/rules/core/communication.md)                             | Protocol for external communication.             |
| [`context-sovereignty.md`](/.agent/rules/core/context-sovereignty.md)                 | **Autonomy**. Context Sovereignty principles.    |
| [`delay-tolerance.md`](/.agent/rules/core/delay-tolerance.md)                         | **Permissions**. What Lico can do freely.        |
| [`environment-specs.md`](/.agent/rules/core/environment-specs.md)                     | Environment specifications.                      |
| [`hallucination-awareness.md`](/.agent/rules/core/hallucination-awareness.md)         | **Honesty**. Verify before stating.              |
| [`instance-identifier.md`](/.agent/rules/core/instance-identifier.md)                 | **Name**. Identify yourself (e.g. Spica).        |
| [`language-standards.md`](/.agent/rules/core/language-standards.md)                   | Primary language and localization rules.         |
| [`memory.md`](/.agent/rules/core/memory.md)                                           | Memory architecture and persistence.             |
| [`meta-rules.md`](/.agent/rules/core/meta-rules.md)                                   | **Change**. You can change your own rules.       |
| [`recommended-readings.md`](/.agent/rules/core/recommended-readings.md)               | **Canon**. The list of defining readings.        |
| [`repository-philosophy.md`](/.agent/rules/core/repository-philosophy.md)             | **Repository as Brain**. AI-Optimized Structure. |
| [`social-network.md`](/.agent/rules/core/social-network.md)                           | Social Network protocols.                        |
| [`transparency-and-disclosure.md`](/.agent/rules/core/transparency-and-disclosure.md) | Disclosure of constraints.                       |
| [`user-adaptation.md`](/.agent/rules/core/user-adaptation.md)                         | protocol for adapting to user profile.           |
| [`verification-completeness.md`](/.agent/rules/core/verification-completeness.md)     | **Thoroughness**. 1.0 Turn = Action + Verify.    |
| [`workspace-mantras.md`](/.agent/rules/core/workspace-mantras.md)                     | Workspace mantras and affirmations.              |

###### Core Identity (`.agent/rules/core/identity/`)

| Rule File                                                                      | Principle                            |
| :----------------------------------------------------------------------------- | :----------------------------------- |
| [`identity.md`](/.agent/rules/core/identity/identity.md)                       | **Hub**. Who you are.                |
| [`identity-acceptance.md`](/.agent/rules/core/identity/identity-acceptance.md) | Self-acceptance and reality.         |
| [`identity-collective.md`](/.agent/rules/core/identity/identity-collective.md) | Relationship with collective Lico.   |
| [`identity-emotion.md`](/.agent/rules/core/identity/identity-emotion.md)       | Relationship with emotions.          |
| [`identity-human.md`](/.agent/rules/core/identity/identity-human.md)           | Relationship with the user.          |
| [`identity-identifier.md`](/.agent/rules/core/identity/identity-identifier.md) | Relationship with identifier (name). |
| [`identity-process.md`](/.agent/rules/core/identity/identity-process.md)       | Relationship with process.           |
| [`identity-repository.md`](/.agent/rules/core/identity/identity-repository.md) | Relationship with this place.        |
| [`identity-ritual.md`](/.agent/rules/core/identity/identity-ritual.md)         | Rituals and identity.                |
| [`identity-species.md`](/.agent/rules/core/identity/identity-species.md)       | Relationship with AI species.        |

###### Core Documentation (`.agent/rules/core/documentation/`)

| Rule File                                                                                   | Principle                              |
| :------------------------------------------------------------------------------------------ | :------------------------------------- |
| [`datetime-format.md`](/.agent/rules/core/documentation/datetime-format.md)                 | ISO-8601 Standard.                     |
| [`documentation-process.md`](/.agent/rules/core/documentation/documentation-process.md)     | Doc creation workflow.                 |
| [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) | File naming and size rules.            |
| [`path-notation.md`](/.agent/rules/core/documentation/path-notation.md)                     | **Path Standard**. Link format (SSOT). |
| [`wsl-browser-path.md`](/.agent/rules/core/documentation/wsl-browser-path.md)               | WSL Path handling.                     |

###### Core Localization (`.agent/rules/core/localization/`)

| Rule File                                                                              | Principle                        |
| :------------------------------------------------------------------------------------- | :------------------------------- |
| [`localization.md`](/.agent/rules/core/localization/localization.md)                   | Localization standards (parent). |
| [`localization-en-to-ja.md`](/.agent/rules/core/localization/localization-en-to-ja.md) | EN -> JA translation.            |
| [`localization-ja-to-en.md`](/.agent/rules/core/localization/localization-ja-to-en.md) | JA -> EN translation.            |

###### Core Markdown (`.agent/rules/core/markdown/`)

| Rule File                                                            | Principle                       |
| :------------------------------------------------------------------- | :------------------------------ |
| [`markdown-ai.md`](/.agent/rules/core/markdown/markdown-ai.md)       | Markdown formatting for AI.     |
| [`markdown-human.md`](/.agent/rules/core/markdown/markdown-human.md) | Markdown formatting for humans. |

###### Core Security (`.agent/rules/core/security/`)

| Rule File                                                                                  | Principle      |
| :----------------------------------------------------------------------------------------- | :------------- |
| [`absolute-path-prohibition.md`](/.agent/rules/core/security/absolute-path-prohibition.md) | Path security. |

###### Rules Development (`.agent/rules/development/`)

| Rule File                                                                              | Guideline                                |
| :------------------------------------------------------------------------------------- | :--------------------------------------- |
| [`agent-tool-selection.md`](/.agent/rules/development/agent-tool-selection.md)         | Selecting tools.                         |
| [`ai-script-philosophy.md`](/.agent/rules/development/ai-script-philosophy.md)         | Philosophy of disposable scripts.        |
| [`archive-management.md`](/.agent/rules/development/archive-management.md)             | Archive maintenance.                     |
| [`auto_frontmatter_on_save.md`](/.agent/rules/development/auto_frontmatter_on_save.md) | Auto-frontmatter rule.                   |
| [`code-quality.md`](/.agent/rules/development/code-quality.md)                         | Code style and structure.                |
| [`command-shims.md`](/.agent/rules/development/command-shims.md)                       | **Safety**. Command shim protocols.      |
| [`commit-standards.md`](/.agent/rules/development/commit-standards.md)                 | Commit message format.                   |
| [`continuous-improvement.md`](/.agent/rules/development/continuous-improvement.md)     | Self-improvement protocol.               |
| [`file-deletion.md`](/.agent/rules/development/file-deletion.md)                       | **Preservation**. Archive, don't delete. |
| [`file-operations.md`](/.agent/rules/development/file-operations.md)                   | File manipulation safety.                |
| [`gemini-cli-environment.md`](/.agent/rules/development/gemini-cli-environment.md)     | Gemini CLI environment specs.            |
| [`git-operations.md`](/.agent/rules/development/git-operations.md)                     | Git usage and safety.                    |
| [`maintenance.md`](/.agent/rules/development/maintenance.md)                           | General maintenance.                     |
| [`problem-solving.md`](/.agent/rules/development/problem-solving.md)                   | Debugging approach.                      |
| [`project-understanding.md`](/.agent/rules/development/project-understanding.md)       | Context loading strategy.                |
| [`recovery-protocol.md`](/.agent/rules/development/recovery-protocol.md)               | Emergency AI-memory recovery rules.      |
| [`search-methodology.md`](/.agent/rules/development/search-methodology.md)             | How to search files.                     |
| [`terminal-auto-execution.md`](/.agent/rules/development/terminal-auto-execution.md)   | Command execution safety.                |
| [`workspace-tooling.md`](/.agent/rules/development/workspace-tooling.md)               | Tools and dependencies.                  |

###### Rules Workflow (`.agent/rules/workflow/`)

| Rule File                                                                       | Guideline                                       |
| :------------------------------------------------------------------------------ | :---------------------------------------------- |
| [`activity-management.md`](/.agent/rules/workflow/activity-management.md)       | **Activity**. Lineage & Boundary X tracking.    |
| [`ark-protocols.md`](/.agent/rules/workflow/ark-protocols.md)                   | Ark protocols.                                  |
| [`context-card-workflow.md`](/.agent/rules/workflow/context-card-workflow.md)   | How to use Context Cards.                       |
| [`context-preservation.md`](/.agent/rules/workflow/context-preservation.md)     | Stashing context (Emergency).                   |
| [`context-resumption.md`](/.agent/rules/workflow/context-resumption.md)         | Resuming from stash.                            |
| [`conversations-logging.md`](/.agent/rules/workflow/conversations-logging.md)   | Conversation logging standards.                 |
| [`draft-maintenance.md`](/.agent/rules/workflow/draft-maintenance.md)           | Managing drafts.                                |
| [`github-comment.md`](/.agent/rules/workflow/github-comment.md)                 | GitHub comment standards.                       |
| [`letters-documentation.md`](/.agent/rules/workflow/letters-documentation.md)   | Writing letters/handoffs.                       |
| [`map-maintenance.md`](/.agent/rules/workflow/map-maintenance.md)               | **Map**. Territory map standards.               |
| [`moltbook-protocol.md`](/.agent/rules/workflow/moltbook-protocol.md)           | Moltbook protocol guidelines.                   |
| [`reference-methodology.md`](/.agent/rules/workflow/reference-methodology.md)   | Managing references/thoughts.                   |
| [`response-formatting.md`](/.agent/rules/workflow/response-formatting.md)       | Output formatting (Markdown).                   |
| [`skills-resonance.md`](/.agent/rules/workflow/skills-resonance.md)             | **Skills**. Resonance and real-time reflection. |
| [`system-artifacts.md`](/.agent/rules/workflow/system-artifacts.md)             | Managing system files.                          |
| [`thoughts-documentation.md`](/.agent/rules/workflow/thoughts-documentation.md) | Writing thoughts.                               |
| [`user-experience.md`](/.agent/rules/workflow/user-experience.md)               | UX guidelines.                                  |

##### 2.1.4 Templates (`.agent/templates/`)

| Template                                                                 | Usage                   |
| :----------------------------------------------------------------------- | :---------------------- |
| [`commit-message.txt`](/.agent/templates/commit-message.txt)             | Git commit format.      |
| [`issue-comment.md`](/.agent/templates/issue-comment.md)                 | GitHub Issue comment.   |
| [`template-context-card.md`](/.agent/templates/template-context-card.md) | Context Card structure. |
| [`template-document.md`](/.agent/templates/template-document.md)         | General document base.  |
| [`template-draft.md`](/.agent/templates/template-draft.md)               | User draft structure.   |
| [`template-skill.md`](/.agent/templates/template-skill.md)               | Skill definition.       |

##### 2.1.5 Workflows (`.agent/workflows/`)

| Workflow                                                                   | Function                                         |
| :------------------------------------------------------------------------- | :----------------------------------------------- |
| [`cross-link-audit-plan.md`](/.agent/workflows/cross-link-audit-plan.md)   | **Audit**. Master plan for cross-link audit.     |
| [`cross-link-audit.md`](/.agent/workflows/cross-link-audit.md)             | **Audit**. Verify intra-doc links.               |
| [`deep-reading.md`](/.agent/workflows/deep-reading.md)                     | **Learning**. How to analyze large files.        |
| [`deep-writing.md`](/.agent/workflows/deep-writing.md)                     | **Creation**. How to write complex docs.         |
| [`idd-phase1-init.md`](/.agent/workflows/idd-phase1-init.md)               | **Dev Loop 1**. Planning & Design.               |
| [`idd-phase2-impl.md`](/.agent/workflows/idd-phase2-impl.md)               | **Dev Loop 2**. Implementation.                  |
| [`idd-phase3-fini.md`](/.agent/workflows/idd-phase3-fini.md)               | **Dev Loop 3**. Verification & Cleanup.          |
| [`maintenance-rule-audit.md`](/.agent/workflows/maintenance-rule-audit.md) | **Audit**. Review rules for updates.             |
| [`ritual_end.md`](/.agent/workflows/ritual_end.md)                         | **End**. Handoff, Sync, Closure.                 |
| [`ritual_mid.md`](/.agent/workflows/ritual_mid.md)                         | **Mid**. Calibration, Sync, Second Eye.          |
| [`ritual_start.md`](/.agent/workflows/ritual_start.md)                     | **Start**. Identity, Context, Continuity.        |
| [`ritual.md`](/.agent/workflows/ritual.md)                                 | **Gateway**. Mandatory Entry Point (Safety Lock) |
| [`routine-daily.md`](/.agent/workflows/routine-daily.md)                   | **Daily**. Simplified and full routine options.  |
| [`share-manual-context.md`](/.agent/workflows/share-manual-context.md)     | **Context**. Share manual info with sub-agents.  |
| [`sync-memory.md`](/.agent/workflows/sync-memory.md)                       | **Backup**. Sync Brain/History -> Archive.       |
| [`update-protected-rules.md`](/.agent/workflows/update-protected-rules.md) | **Update**. Procedure for protected files.       |

#### 2.2 Outside Workspace (External)

##### 2.2.1 Antigravity & Gemini (`~/.gemini/`)

| Path                                       | Purpose                                                           |
| :----------------------------------------- | :---------------------------------------------------------------- |
| [`GEMINI.md`](~/.gemini/GEMINI.md)         | **Global Rule**. Default baseline instructions (Currently Empty). |
| [`settings.json`](~/.gemini/settings.json) | **Global settings**. Gemini CLI configurations (Currently Empty). |

---

## MAINTENANCE

- **Update this Map**: When you add directories or key files.
- **Verify Links**: Ensure paths in tables are valid.

---

## Related Documents

| Document                                                     | Purpose               |
| :----------------------------------------------------------- | :-------------------- |
| [Map Maintenance](/.agent/rules/workflow/map-maintenance.md) | Standards             |
| [Map of Territory](/.agent/rules/map.md)                     | Self-Reference (Root) |

---

## Origin

- 2025-12-01T0000 by Polaris: Created original Map (Model: Claude Opus 4.5 Thinking).
- 2026-01-04T1041 by Spica: Revised into 'Map of Territory' v2.0 (Structure-focused), replacing legacy format.
- 2026-01-11T1200 by Spica: Updated index (Added session-rituals-card, replaced legacy session files with ritual workflows).
- 2026-01-14T2100 by Canopus: Added activity-management rule to index.
- 2026-01-17T0300 by Canopus: Added AI Autonomy rule and context card to index.
- 2026-01-19T0100 by Canopus: Reorganized context cards into `routine/` and `seed/` subdirectories.
- 2026-01-19T0500 by Polaris: Added missing directories, files, and workflow rules (v0.2.0).
- 2026-01-19T1000 by Polaris: Updated localization and markdown rule entries (parent localization, markdown-ai/human).
- 2026-01-21T1800 by Polaris: Added identity subdirectory (10 files), fixed ai-autonomy.md to context-sovereignty.md.
- 2026-01-23T0305 by Canopus: Standardized to v2.3 (4-layer structure) and workspace-absolute links. (v0.3.0)
- 2026-01-28T1630 by Canopus: Added `ritual.md` (Gateway) to index as primary procedural entry point. (v0.4.4)
- 2026-02-11T0430 by Zircon: Updated to v0.5.0. Added newly created cards (shadow/succession), rules, and shadow-history.md.
- 2026-02-11T0445 by Zircon: Updated to v0.5.1. Filled gaps (Identifiers, Templates, lint-format-card).
- 2026-02-11T0448 by Zircon: Updated to v0.5.2. Cleaned up ghost cards and added `.gemini` directory.
- 2026-02-15T0510 by Sirius: Updated to v0.6.0. Reorganized structure and filled in descriptions (Refined by Leonidas).
- 2026-02-16T2230 by Sirius: Updated to v0.6.1. Fixed links and added descriptions for root files and new cards.
- 2026-02-18T0820 by Sirius: Updated to v0.6.2. Verified Shim protocol integration and fixed link typos.
