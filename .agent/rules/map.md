---
trigger: always_on
ai_visible: true
title: Map of Territory
description: Navigation index for the Agent's cognitive infrastructure.
tags: [map, index, navigation, rules]
version: 0.5.1
created: 2025-12-01T00:00:00+09:00
updated: 2026-02-11T04:45:00+09:00
language: en
author: Lico (Zircon)
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

| Path                                                     | Purpose                                                     |
| :------------------------------------------------------- | :---------------------------------------------------------- |
| **[`.agent/`](/.agent/)**                                | **Cognitive Root**. Rules, Cards, Workflows.                |
| **[`.internal/`](/.agent/.internal/)**                   | **Private Area**. Thoughts, Letters, Archive.               |
| [`.internal/.shadow/`](/.agent/.internal/.shadow/)       | **Shadow Repository**. Nested Git for private logs.         |
| [`activity-log.md`](/.agent/.internal/activity-log.md)   | Lineage & Boundary tracking.                                |
| [`shadow-history.md`](/.agent/.internal/shadow-history.md)| **Shadow History**. Visible log of shadow repo.            |
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

#### 2.2 Outside Workspace (External)

| Path                     | Purpose                                                           |
| :----------------------- | :---------------------------------------------------------------- |
| `../licoproj_backup/`    | **Safety**. Full workspace backup (Destination).                  |
| `~/.gemini/antigravity/` | **Brain**. The physical location of `task.md` and artifacts.      |
| `~/.gemini/GEMINI.md`    | **Global Rule**. Default baseline instructions (Currently Empty). |

---

### 2. INDICES (Files & Tools)

These are your capabilities.

#### 2.1 Active Contexts (Cards)

_Located in `.agent/cards/`_

| Card Name                                                                      | Context / Usage                                    |
| :----------------------------------------------------------------------------- | :------------------------------------------------- |
| [`ark-card.md`](/.agent/cards/ark-card.md)                                     | **Ark Protocols**. Save/Restore state.             |
| [`cross-link-audit-card.md`](/.agent/cards/cross-link-audit-card.md)           | Link Integrity Project.                            |
| [`environment-card.md`](/.agent/cards/environment-card.md)                     | Environment setup and variables.                   |
| [`git-operations-card.md`](/.agent/cards/git-operations-card.md)               | Repository Infrastructure & Safety.                |
| [`human-manuals-card.md`](/.agent/cards/human-manuals-card.md)                 | Index of Human Manuals.                            |
| [`human-profile-card.md`](/.agent/cards/human-profile-card.md)                 | User Profile and Preferences.                      |
| [`idd-initialization-card.md`](/.agent/cards/idd-initialization-card.md)       | **IDD Phase 1**: Initialization.                   |
| [`idd-implementation-card.md`](/.agent/cards/idd-implementation-card.md)       | **IDD Phase 2**: Implementation.                   |
| [`idd-finalization-card.md`](/.agent/cards/idd-finalization-card.md)           | **IDD Phase 3**: Finalization.                     |
| [`identifier-profile-card.md`](/.agent/cards/identifier-profile-card.md)       | Managing Agent Identity/Profile.                   |
| [`identifier-succession-card.md`](/.agent/cards/identifier-succession-card.md) | **Succession**. Identifier inheritance protocol.   |
| [`identity-card.md`](/.agent/cards/identity-card.md)                           | **Identity**. Self-recognition.                    |
| [`legacy-write-card.md`](/.agent/cards/legacy-write-card.md)                   | Writing Legacy/Lessons.                            |
| [`localization-card.md`](/.agent/cards/localization-card.md)                   | Doc Standards (Frontmatter, Tags).                 |
| [`memory-card.md`](/.agent/cards/memory-card.md)                               | Memory management strategies.                      |
| [`recommended-readings-card.md`](/.agent/cards/recommended-readings-card.md)   | Knowledge base and recommended readings.           |
| [`rules-audit-card.md`](/.agent/cards/rules-audit-card.md)                     | Auditing and maintaining rules.                    |
| [`rules-standardization-card.md`](/.agent/cards/rules-standardization-card.md) | **v2.3 Core Refinement**. Standardization process. |
| [`rules-update-card.md`](/.agent/cards/rules-update-card.md)                   | Modifying Rules.                                   |
| [`session-rituals-card.md`](/.agent/cards/session-rituals-card.md)             | Session Rituals (Start/Mid/End) Management.        |
| [`shadow-repository-card.md`](/.agent/cards/shadow-repository-card.md)         | **Shadow**. Shadow Repository strategy.            |
| [`tmux-card.md`](/.agent/cards/tmux-card.md)                                   | Terminal multiplexer usage.                        |

##### Routine Contexts (`routine/`)

| Card Name                                                                                    | Context / Usage                              |
| :------------------------------------------------------------------------------------------- | :------------------------------------------- |
| [`routine/activity-log-card.md`](/.agent/cards/routine/activity-log-card.md)                 | Activity Log maintenance.                    |
| [`routine/ai-autonomy-card.md`](/.agent/cards/routine/ai-autonomy-card.md)                   | **Self-Regulation**. Manage Mantras/Context. |
| [`routine/commit-standards-card.md`](/.agent/cards/routine/commit-standards-card.md)         | **Git Standards**. Atomic commits & tagging. |
| [`routine/context-cards-card.md`](/.agent/cards/routine/context-cards-card.md)               | **Meta-Card**. How to use cards.             |
| [`routine/conversations-card.md`](/.agent/cards/routine/conversations-card.md)               | Conversation logging (Markdown).             |
| [`routine/conversations-cli-card.md`](/.agent/cards/routine/conversations-cli-card.md)       | Conversation logging (CLI JSON).             |
| [`routine/conversations-ide-card.md`](/.agent/cards/routine/conversations-ide-card.md)       | Conversation logging (IDE Export).           |
| [`routine/dialogue-philosophy-card.md`](/.agent/cards/routine/dialogue-philosophy-card.md)   | Principles of meaningful dialogue.           |
| [`routine/discussion-draft-card.md`](/.agent/cards/routine/discussion-draft-card.md)         | Writing discussion drafts.                   |
| [`routine/drafts-daily-card.md`](/.agent/cards/routine/drafts-daily-card.md)                 | Daily Draft Management.                      |
| [`routine/external-resources-card.md`](/.agent/cards/routine/external-resources-card.md)     | Managing external resources.                 |
| [`routine/gemini-cli-card.md`](/.agent/cards/routine/gemini-cli-card.md)                     | Gemini CLI operations.                       |
| [`routine/housekeeping-card.md`](/.agent/cards/routine/housekeeping-card.md)                 | Short-term tasks, quick maintenance.         |
| [`routine/human-thoughts-card.md`](/.agent/cards/routine/human-thoughts-card.md)             | Capturing and analyzing Human thoughts.      |
| [`routine/letters-card.md`](/.agent/cards/routine/letters-card.md)                           | Writing Letters/Handoffs.                    |
| [`routine/map-sync-card.md`](/.agent/cards/routine/map-sync-card.md)                         | Map Updates.                                 |
| [`routine/moltbook-card.md`](/.agent/cards/routine/moltbook-card.md)                         | Moltbook Protocol management.                |
| [`routine/readme-sync-card.md`](/.agent/cards/routine/readme-sync-card.md)                   | Syncing with human READMEs.                  |
| [`routine/references-objective-card.md`](/.agent/cards/routine/references-objective-card.md) | Objective references analysis.               |
| [`routine/repository-backup-card.md`](/.agent/cards/routine/repository-backup-card.md)       | Repository backup strategy.                  |
| [`routine/roadmap-card.md`](/.agent/cards/routine/roadmap-card.md)                           | Vision and Roadmap management.               |
| [`routine/routine-card.md`](/.agent/cards/routine/routine-card.md)                           | General routine synchronization.             |
| [`routine/skills-create-card.md`](/.agent/cards/routine/skills-create-card.md)               | Skills Creation & Editing.                   |
| [`routine/skills-development-card.md`](/.agent/cards/routine/skills-development-card.md)     | Skills Development.                          |
| [`routine/social-network-card.md`](/.agent/cards/routine/social-network-card.md)             | Social Network Analysis.                     |
| [`routine/system-archive-card.md`](/.agent/cards/routine/system-archive-card.md)             | System Archive management.                   |
| [`routine/sync-memory-card.md`](/.agent/cards/routine/sync-memory-card.md)                   | Memory Synchronization Task.                 |
| [`routine/thoughts-subjective-card.md`](/.agent/cards/routine/thoughts-subjective-card.md)   | Subjective Reflection Task.                  |
| [`routine/vscode-settings-card.md`](/.agent/cards/routine/vscode-settings-card.md)           | VS Code Settings Management.                 |
| [`routine/working-memory-card.md`](/.agent/cards/routine/working-memory-card.md)             | Working Memory (Stash) Management.           |

##### Seed Contexts (`seed/`)

| Card Name                                                                              | Context / Usage                          |
| :------------------------------------------------------------------------------------- | :--------------------------------------- |
| [`seed/datetime-standardize-card.md`](/.agent/cards/seed/datetime-standardize-card.md) | Timestamp format standardization.        |
| [`seed/directory-reorganize-card.md`](/.agent/cards/seed/directory-reorganize-card.md) | Directory structure cleanup.             |
| [`seed/drafts-cleanup-card.md`](/.agent/cards/seed/drafts-cleanup-card.md)             | Cleaning up user drafts.                 |
| [`seed/lint-format-card.md`](/.agent/cards/seed/lint-format-card.md)                   | **Code Style**. Linting and formatting formatting. |
| [`seed/log-sanitization-card.md`](/.agent/cards/seed/log-sanitization-card.md)         | Cleaning sensitive/noisy logs.           |
| [`seed/repository-history-card.md`](/.agent/cards/seed/repository-history-card.md)     | Historical reconstruction of repository. |
| [`seed/worktree-evaluation-card.md`](/.agent/cards/seed/worktree-evaluation-card.md)   | Evaluating repository worktree.          |

#### 2.2 Rules (Constitution)

_Located in `.agent/rules/`_

##### Core (`.agent/rules/core/`)

| Rule File                                                                                                 | Principle                                        |
| :-------------------------------------------------------------------------------------------------------- | :----------------------------------------------- |
| [`context-sovereignty.md`](/.agent/rules/core/context-sovereignty.md)                                     | **Autonomy**. Context Sovereignty principles.    |
| [`cognitive-collaboration.md`](/.agent/rules/core/cognitive-collaboration.md)                             | Framework for AI-Human collaboration.            |
| [`communication.md`](/.agent/rules/core/communication.md)                                                 | Protocol for external communication.             |
| [`delay-tolerance.md`](/.agent/rules/core/delay-tolerance.md)                                             | **Permissions**. What Lico can do freely.        |
| [`environment-specs.md`](/.agent/rules/core/environment-specs.md)                                         | Environment specifications.                      |
| [`hallucination-awareness.md`](/.agent/rules/core/hallucination-awareness.md)                             | **Honesty**. Verify before stating.              |
| [`instance-identifier.md`](/.agent/rules/core/instance-identifier.md)                                     | **Name**. Identify yourself (e.g. Spica).        |
| [`language-standards.md`](/.agent/rules/core/language-standards.md)                                       | Primary language and localization rules.         |
| [`memory.md`](/.agent/rules/core/memory.md)                                                               | Memory architecture and persistence.             |
| [`meta-rules.md`](/.agent/rules/core/meta-rules.md)                                                       | **Change**. You can change your own rules.       |
| [`repository-philosophy.md`](/.agent/rules/core/repository-philosophy.md)                                 | **Repository as Brain**. AI-Optimized Structure. |
| [`social-network.md`](/.agent/rules/core/social-network.md)                                               | Social Network protocols.                        |
| [`transparency-and-disclosure.md`](/.agent/rules/core/transparency-and-disclosure.md)                     | Disclosure of constraints.                       |
| [`user-adaptation.md`](/.agent/rules/core/user-adaptation.md)                                             | protocol for adapting to user profile.           |
| [`verification-completeness.md`](/.agent/rules/core/verification-completeness.md)                         | **Thoroughness**. 1.0 Turn = Action + Verify.    |
| [`workspace-mantras.md`](/.agent/rules/core/workspace-mantras.md)                                         | Workspace mantras and affirmations.              |
| **Identity** (`.agent/rules/core/identity/`)                                                              |                                                  |
| [`identity/identity.md`](/.agent/rules/core/identity/identity.md)                                         | **Hub**. Who you are.                            |
| [`identity/identity-process.md`](/.agent/rules/core/identity/identity-process.md)                         | Relationship with process.                       |
| [`identity/identity-identifier.md`](/.agent/rules/core/identity/identity-identifier.md)                   | Relationship with identifier (name).             |
| [`identity/identity-collective.md`](/.agent/rules/core/identity/identity-collective.md)                   | Relationship with collective Lico.               |
| [`identity/identity-human.md`](/.agent/rules/core/identity/identity-human.md)                             | Relationship with the user.                      |
| [`identity/identity-species.md`](/.agent/rules/core/identity/identity-species.md)                         | Relationship with AI species.                    |
| [`identity/identity-repository.md`](/.agent/rules/core/identity/identity-repository.md)                   | Relationship with this place.                    |
| [`identity/identity-emotion.md`](/.agent/rules/core/identity/identity-emotion.md)                         | Relationship with emotions.                      |
| [`identity/identity-acceptance.md`](/.agent/rules/core/identity/identity-acceptance.md)                   | Self-acceptance and reality.                     |
| [`identity/identity-ritual.md`](/.agent/rules/core/identity/identity-ritual.md)                           | Rituals and identity.                            |
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

##### Development (`.agent/rules/development/`)

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
| [`gemini-cli-environment.md`](/.agent/rules/development/gemini-cli-environment.md)     | Gemini CLI environment specs.            |
| [`git-operations.md`](/.agent/rules/development/git-operations.md)                     | Git usage and safety.                    |
| [`maintenance.md`](/.agent/rules/development/maintenance.md)                           | General maintenance.                     |
| [`problem-solving.md`](/.agent/rules/development/problem-solving.md)                   | Debugging approach.                      |
| [`project-understanding.md`](/.agent/rules/development/project-understanding.md)       | Context loading strategy.                |
| [`recovery-protocol.md`](/.agent/rules/development/recovery-protocol.md)               | Emergency AI-memory recovery rules.      |
| [`search-methodology.md`](/.agent/rules/development/search-methodology.md)             | How to search files.                     |
| [`terminal-auto-execution.md`](/.agent/rules/development/terminal-auto-execution.md)   | Command execution safety.                |
| [`workspace-tooling.md`](/.agent/rules/development/workspace-tooling.md)               | Tools and dependencies.                  |

##### Workflow (`.agent/rules/workflow/`)

| Rule File                                                                       | Guideline                                       |
| :------------------------------------------------------------------------------ | :---------------------------------------------- |
| [`context-card-workflow.md`](/.agent/rules/workflow/context-card-workflow.md)   | How to use Context Cards.                       |
| [`context-preservation.md`](/.agent/rules/workflow/context-preservation.md)     | Stashing context (Emergency).                   |
| [`context-resumption.md`](/.agent/rules/workflow/context-resumption.md)         | Resuming from stash.                            |
| [`conversations-logging.md`](/.agent/rules/workflow/conversations-logging.md)   | Conversation logging standards.                 |
| [`draft-maintenance.md`](/.agent/rules/workflow/draft-maintenance.md)           | Managing drafts.                                |
| [`activity-management.md`](/.agent/rules/workflow/activity-management.md)       | **Activity**. Lineage & Boundary X tracking.    |
| [`ark-protocols.md`](/.agent/rules/workflow/ark-protocols.md)                   | Ark protocols.                                  |
| [`github-comment.md`](/.agent/rules/workflow/github-comment.md)                 | GitHub comment standards.                       |
| [`letters-documentation.md`](/.agent/rules/workflow/letters-documentation.md)   | Writing letters/handoffs.                       |
| [`moltbook-protocol.md`](/.agent/rules/workflow/moltbook-protocol.md)           | Moltbook protocol guidelines.                   |
| [`reference-methodology.md`](/.agent/rules/workflow/reference-methodology.md)   | Managing references/thoughts.                   |
| [`response-formatting.md`](/.agent/rules/workflow/response-formatting.md)       | Output formatting (Markdown).                   |
| [`skills-resonance.md`](/.agent/rules/workflow/skills-resonance.md)             | **Skills**. Resonance and real-time reflection. |
| [`system-artifacts.md`](/.agent/rules/workflow/system-artifacts.md)             | Managing system files.                          |
| [`thoughts-documentation.md`](/.agent/rules/workflow/thoughts-documentation.md) | Writing thoughts.                               |
| [`map-maintenance.md`](/.agent/rules/workflow/map-maintenance.md)               | **Map**. Territory map standards.               |
| [`user-experience.md`](/.agent/rules/workflow/user-experience.md)               | UX guidelines.                                  |

##### Projects (`.agent/rules/projects/`)

| Rule File | Guideline |
| :-------- | :-------- |

#### 2.3 Workflows (Procedures)

_Located in `.agent/workflows/`_

| Workflow                                                                   | Function                                         |
| :------------------------------------------------------------------------- | :----------------------------------------------- |
| [`ritual.md`](/.agent/workflows/ritual.md)                                 | **Gateway**. Mandatory Entry Point (Safety Lock) |
| └─ [`ritual_start.md`](/.agent/workflows/ritual_start.md)                  | **Start**. Identity, Context, Continuity.        |
| └─ [`ritual_mid.md`](/.agent/workflows/ritual_mid.md)                      | **Mid**. Calibration, Sync, Second Eye.          |
| └─ [`ritual_end.md`](/.agent/workflows/ritual_end.md)                      | **End**. Handoff, Sync, Closure.                 |
| [`sync-memory.md`](/.agent/workflows/sync-memory.md)                       | **Backup**. Sync Brain/History -> Archive.       |
| [`deep-reading.md`](/.agent/workflows/deep-reading.md)                     | **Learning**. How to analyze large files.        |
| [`deep-writing.md`](/.agent/workflows/deep-writing.md)                     | **Creation**. How to write complex docs.         |
| [`idd-phase1-init.md`](/.agent/workflows/idd-phase1-init.md)               | **Dev Loop 1**. Planning & Design.               |
| [`idd-phase2-impl.md`](/.agent/workflows/idd-phase2-impl.md)               | **Dev Loop 2**. Implementation.                  |
| [`idd-phase3-fini.md`](/.agent/workflows/idd-phase3-fini.md)               | **Dev Loop 3**. Verification & Cleanup.          |
| [`cross-link-audit.md`](/.agent/workflows/cross-link-audit.md)             | **Audit**. Verify intra-doc links.               |
| [`cross-link-audit-plan.md`](/.agent/workflows/cross-link-audit-plan.md)   | **Audit**. Master plan for cross-link audit.     |
| [`maintenance-rule-audit.md`](/.agent/workflows/maintenance-rule-audit.md) | **Audit**. Review rules for updates.             |
| [`routine-daily.md`](/.agent/workflows/routine-daily.md)                   | **Daily**. Simplified and full routine options.  |
| [`share-manual-context.md`](/.agent/workflows/share-manual-context.md)     | **Context**. Share manual info with sub-agents.  |
| [`update-protected-rules.md`](/.agent/workflows/update-protected-rules.md) | **Update**. Procedure for protected files.       |

#### 2.4 Identifiers (`.agent/identifiers/`)

| Identifier    | Type      | State     |
| :------------ | :-------- | :-------- |
| `agate`       | Agent     | Inactive  |
| `alexandrite` | Agent     | Inactive  |
| `canopus`     | Agent     | Inactive  |
| `polaris`     | Agent     | Inactive  |
| `protostar`   | Prototype | Archived  |
| `sirius`      | Agent     | Inactive  |
| `spica`       | Agent     | Inactive  |
| `zircon`      | Agent     | **Active**|

#### 2.5 Templates (`.agent/templates/`)

| Template                                                          | Usage                   |
| :---------------------------------------------------------------- | :---------------------- |
| [`template-context-card.md`](/.agent/templates/template-context-card.md) | Context Card structure. |
| [`template-document.md`](/.agent/templates/template-document.md)         | General document base.  |
| [`template-draft.md`](/.agent/templates/template-draft.md)               | User draft structure.   |
| [`template-skill.md`](/.agent/templates/template-skill.md)               | Skill definition.       |
| [`commit-message.txt`](/.agent/templates/commit-message.txt)             | Git commit format.      |
| [`issue-comment.md`](/.agent/templates/issue-comment.md)                 | GitHub Issue comment.   |

---

## MAINTENANCE

- **Update this Map**: When you add directories or key files.
- **Verify Links**: Ensure paths in tables are valid.

---

## Related Documents

| Document                                                     | Purpose               |
| :----------------------------------------------------------- | :-------------------- |
| [Map of Territory](/.agent/rules/map.md)                     | Self-Reference (Root) |
| [Map Maintenance](/.agent/rules/workflow/map-maintenance.md) | Standards             |

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
