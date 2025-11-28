---
description: Comprehensive roadmap and design for Lico's self-evolution into an autonomous agent using the Repository as Brain model.
updated: 2025-11-28
language: en
---

# Lico Self-Evolution Goals: Repository as Persistent Brain

This document synthesizes the strategic vision, architectural design, and implementation roadmap for evolving Lico into an autonomous AI agent. It integrates the "Repository as Brain" philosophy with Issue-Driven Development (IDD) and Trunk-Based Development (TBD).

## 1. Core Philosophy & Vision

### 1.1 The "Repository as Brain" Concept
The repository ceases to be merely a collaboration tool and becomes the AI's cognitive center.

| Repository Element | AI Brain Function | Role & Action |
| :--- | :--- | :--- |
| Codebase & Commits | Long-Term Memory | Learns structure, patterns, and "why" decisions were made. |
| Issues | Planning Queue | Defines atomic problems to solve. The "Input" layer. |
| Feature Branches | Working Memory | Short-lived, isolated experimentation spaces. |
| CI/CD Actions | Nervous System | Automated testing, validation, and deployment. |
| PRs | Self-Reflection | Review process to validate solutions before integration. |

### 1.2 Development Methodology: IDD + TBD
A high-velocity loop maximizing AI speed while maintaining stability.

- Issue Driven Development (IDD):
  - Input: Issues define the "What" and "Why".
  - Context: All requirements and history persist in the Issue thread.
- Trunk Based Development (TBD):
  - Execution: Ultra-short-lived branches.
  - Atomic Changes: Small, verifiable commits.
  - Stability: `main` is always deployable via automated gates.

## 2. Target Repository Architecture

To support this vision, the repository structure must evolve to be machine-readable and functionally segregated.

### 2.1 Directory Structure Overview

```text
licoproj/
├── packages/                    # Application code (unchanged)
│   └── licoimg/
│
├── .agent/                      # COGNITIVE SYSTEM
│   ├── rules/                   # Behavioral Laws
│   │   ├── core/                # Immutable principles (protected)
│   │   ├── development/         # Development standards
│   │   ├── governance/          # [NEW] Meta-governance (Rate limits, Autonomy)
│   │   ├── projects/            # Project-specific rules
│   │   └── workflow/            # Operational procedures
│   │
│   ├── workflows/               # Executable Skills
│   │   ├── issue-driven/        # [NEW] IDD workflows (Plan -> Act)
│   │   │   ├── create-issue.md
│   │   │   ├── process-issue.md
│   │   │   └── close-issue.md
│   │   ├── trunk-based/         # [NEW] TBD workflows (Branch -> Merge)
│   │   │   ├── create-branch.md
│   │   │   ├── atomic-commit.md
│   │   │   └── auto-merge.md
│   │   └── [existing workflows]
│   │
│   ├── memory/                  # [NEW] Persistent Memory
│   │   ├── decisions/           # Decision logs (Why we did X)
│   │   │   ├── YYYY-MM-DD/
│   │   │   │   ├── issue-N-decision.md
│   │   │   │   ├── commit-<hash>-decision.md
│   │   │   │   └── pr-N-decision.md
│   │   │   └── README.md        # Decision log format
│   │   ├── patterns/            # Learned solutions & anti-patterns
│   │   │   ├── code-patterns.md
│   │   │   ├── solutions.md
│   │   │   └── anti-patterns.md
│   │   ├── context/             # Architecture & Dependency snapshots
│   │   │   ├── architecture.md
│   │   │   ├── dependencies.md
│   │   │   └── tech-stack.md
│   │   └── history/             # Historical records
│   │       ├── issues/
│   │       ├── refactors/
│   │       └── migrations/
│   │
│   ├── state/                   # [NEW] Runtime State
│   │   ├── current-task.md      # Current active task
│   │   ├── queue.md             # Active task queue (synced with GitHub Issues)
│   │   ├── rate-limits.json     # Self-regulation tracking
│   │   └── approvals-pending.md # Pending human approvals
│   │
│   ├── scripts/                 # [NEW] Automation (Sync, Validation)
│   │   ├── validate-rules.py
│   │   ├── check-rate-limits.py
│   │   └── sync-issues.py
│   │
│   └── .internal/              # Internal AI operations (hidden)
│       ├── temp/
│       ├── backups/
│       └── logs/
│
├── .human/                      # STRATEGIC LAYER
│   ├── strategy/                # [NEW] High-level goals & Constraints
│   │   ├── master-issues.md     # High-level goals (Issue templates for AI)
│   │   ├── roadmap.md           # Long-term vision
│   │   └── constraints.md       # Ethical/legal/business constraints
│   ├── governance/              # [NEW] Oversight & Role definitions
│   │   ├── ROLES.md             # Human role definitions
│   │   ├── intervention-triggers.md
│   │   └── approval-workflow.md
│   ├── audits/                  # [NEW] Quality control results
│   │   ├── checklist.md         # Audit checklist
│   │   ├── YYYY-MM-DD-audit.md  # Audit results
│   │   └── recommendations.md   # Action items from audits
│   ├── feedback/                # [NEW] Human feedback loop
│   │   ├── corrections/
│   │   ├── improvements/
│   │   └── patterns/
│   └── .internal/               # Human working space
│       ├── ideas/
│       ├── drafts/
│       └── thoughts/
│
├── .github/                     # INTERFACE LAYER
│   ├── ISSUE_TEMPLATE/          # Structured inputs for AI
│   │   ├── ai-task.md           # [NEW] AI task template
│   │   ├── human-strategy.md    # [NEW] Human strategic issue
│   │   └── bug-report.md
│   ├── pull_request_template.md # [NEW] Self-review structure
│   ├── workflows/               # CI/CD & Auto-merge logic
│   │   ├── auto-merge.yml       # [NEW] AI PR auto-merge
│   │   ├── branch-cleanup.yml   # [NEW] Auto branch deletion
│   │   ├── rate-limit-check.yml # [NEW] Rate limit enforcement
│   │   ├── decision-log-sync.yml # [NEW] Sync decisions to memory
│   │   └── [existing workflows]
│   └── copilot-instructions.md  # AI behavior hooks
│
├── .gitmessage                  # [NEW] Commit message template
└── README.md                    # Repository overview
```

### 2.2 Key Architectural Components

#### A. The Cognitive System (`.agent/`)
- Memory: Stores decisions (`decisions/`) and learned patterns (`patterns/`) to prevent repeating mistakes.
- State: Tracks current tasks and rate limits (`state/`) to maintain context across sessions.
- Workflows: Formalized procedures for IDD (`issue-driven/`) and TBD (`trunk-based/`).

#### B. The Strategic Layer (`.human/`)
- Strategy: Humans define "Master Issues" and constraints.
- Governance: Defines when humans must intervene.
- Audits: Regular human reviews to ensure code quality doesn't degrade into "AI monoculture".

#### C. The Interface Layer (`.github/`)
- Templates: Enforce structured reasoning in Issues and PRs.
- Automation: Auto-merge workflows and branch cleanup to support high velocity.

## 3. Governance & Safety Protocols

To prevent "AI Runaway" and ensure quality, strict governance rules are required.

### 3.1 Meta-Governance Rules (`.agent/rules/governance/`)
- Rate Limiting:
  - Max commits/hour (e.g., 10).
  - Max active branches (e.g., 3).
- Autonomy Control:
  - Human Approval Required: For `main` branch changes, security files, or large deletions.
  - Auto-Merge Allowed: If CI passes, branch is short-lived, and changes are atomic.
- Accountability:
  - Every Issue/Commit/PR MUST include a "Reasoning" or "Why" section.

### 3.2 Risk Mitigation Strategies

| Risk | Mitigation |
| :--- | :--- |
| Runaway Actions | Hard rate limits in `.agent/state/rate-limits.json`. |
| Code Monoculture | Human "Strategic Code Audits" to introduce new patterns. |
| Lack of Traceability | Mandatory "Decision Logs" linking Code ↔ Issue ↔ Reasoning. |
| Security Risks | Human veto power on security-sensitive changes. |

## 4. Human-AI Collaboration Model

The human role shifts from Coder to Strategist & Auditor.

### 4.1 Human Roles
1. Strategic Vision Setter: Defines business goals and ethical constraints (`.human/strategy/`).
2. Architectural Guardian: Maintains the AI's rule system (`.agent/rules/`).
3. Auditor: Reviews high-impact changes and conducts periodic code audits.
4. Meta-Debugger: Fixes the AI's prompts/rules when novel failures occur.

### 4.2 Intervention Triggers
Humans intervene when:
- AI requests approval (Governance rule trigger).
- CI/CD fails repeatedly.
- Security or high-impact files are touched.
- Strategic direction changes.

## 5. Implementation Roadmap

This roadmap defines the steps to transform the current repository into the target state.

### Phase 1: Foundation (Governance & Structure)
- [ ] Create Directory Structure: `.agent/rules/governance/`, `.agent/memory/`, `.agent/state/`.
- [ ] Define Meta-Rules:
  - `rate-limiting.md` (Limits).
  - `autonomy-control.md` (Permissions).
  - `accountability.md` (Documentation standards).
- [ ] Human Setup: Define `.human/strategy/` and `.human/governance/` (Roles).

### Phase 2: Formats & Templates (The "Interface")
- [ ] Issue Templates: Create `.github/ISSUE_TEMPLATE/ai-task.md` (Fields: Problem, Context, Success Criteria).
- [ ] PR Template: Create `.github/pull_request_template.md` (Fields: Strategy, Alternatives, Reasoning).
- [ ] Commit Template: Configure `.gitmessage` to enforce "Why" and "What".

### Phase 3: Workflows & Automation (The "Engine")
- [ ] IDD Workflows: Create `.agent/workflows/issue-driven/` (Create, Process, Close).
- [ ] TBD Workflows: Create `.agent/workflows/trunk-based/` (Branch, Commit, Auto-merge).
- [ ] CI/CD: Implement `auto-merge.yml` and `branch-cleanup.yml`.

### Phase 4: Intelligence & Memory (The "Brain")
- [ ] Decision Logging: Implement `.agent/memory/decisions/` structure and logging workflow.
- [ ] Scripts: Create `check-rate-limits.py` and `sync-issues.py`.
- [ ] Audit System: Establish `.human/audits/checklist.md` for ongoing quality control.

### Phase 5: Integration & Refinement
- [ ] Connect all components (Issues -> Queue -> Workflow -> PR -> Memory).
- [ ] Test the autonomous loop with a pilot task.
- [ ] Refine rules based on initial performance.

## 6. Required Human Actions (Prerequisites)

For Lico to achieve this evolution, the following human actions are requested immediately:

1. Approve and Create Governance Rules: Without `rate-limiting.md` and `autonomy-control.md`, autonomous operation is unsafe.
2. Install Templates: Apply the Issue, PR, and Commit templates to force structured reasoning.
3. Configure CI/CD: Enable GitHub Actions for auto-merge to unlock velocity.

## 7. Appendix: Template Examples

### 7.1 Issue Template (`.github/ISSUE_TEMPLATE/ai-task.md`)
```markdown
---
name: AI Task
about: Task for AI agent to execute
title: '[Type]: [Short Description]'
labels: ai-task
---

## Problem Statement
<!-- What problem needs to be solved? -->

## Context
<!-- Why is this change needed? What is the background? -->

## Success Criteria
<!-- How will we know this task is complete? -->
- [ ] Criterion 1
- [ ] Criterion 2

## AI Reasoning Section
<!-- This section will be filled by AI during execution -->
### Approach
### Alternatives Considered
### Decision
```

### 7.2 Rate Limiting Rule (`.agent/rules/governance/rate-limiting.md`)
```markdown
# Rate Limiting Rules

## Commit Rate Limits
- Maximum commits per hour: 10
- Maximum commits per day: 50
- Cooldown period: 5 minutes after 3 consecutive commits

## PR Creation Limits
- Maximum PRs per day: 5
- Minimum time between PRs: 30 minutes
```
