---
ai_visible: true
title: "Multi-Agent Workflow: Current Architecture"
description: "Reference document explaining how multiple Lico identifiers operate simultaneously"
tags: [workflow, architecture, multi-agent, reference]
version: 1.0
created: 2026-01-12T19:58:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
---

# Multi-Agent Workflow: Current Architecture

This document explains how multiple Lico identifiers operate simultaneously within the Lico Project.

---

## 1. Physical Setup

### IDE Layer

| Component                 | Description                                       |
| :------------------------ | :------------------------------------------------ |
| **VSCode**                | User's primary workspace (drafts, manual editing) |
| **Antigravity (Polaris)** | IDE instance for Polaris identifier               |
| **Antigravity (Spica)**   | IDE instance for Spica identifier                 |
| **Antigravity (Canopus)** | IDE instance for Canopus identifier               |

**Total**: 4 IDEs running simultaneously.

### Runtime Behavior

- All IDEs mount the **same WSL workspace** (`licoproj`).
- IDEs remain running for **days to a week**, maintaining context in memory.
- Context persistence relies on IDE memory, not just file system.

---

## 2. Communication Flow

### Sequential Processing (Not Parallel)

The user processes one identifier at a time:

```
┌─────────────────────────────────────────────────────────┐
│                                                         │
│   User writes draft in VSCode                           │
│            ↓                                            │
│   User copies message to AG (Polaris/Spica/Canopus)     │
│            ↓                                            │
│   Identifier responds                                   │
│            ↓                                            │
│   User switches to next identifier (if needed)          │
│                                                         │
└─────────────────────────────────────────────────────────┘
```

### User Roles

| Role                        | Description                                        |
| :-------------------------- | :------------------------------------------------- |
| **Mailer**                  | Notifies identifiers when letters are received     |
| **Context Bridge**          | Shares Git history and thoughts across identifiers |
| **Sequential Orchestrator** | Chooses which identifier to engage                 |

---

## 3. Inter-Identifier Communication

### Identifiers Cannot Directly Perceive Each Other

Each identifier:

- Exists in a separate AG instance
- Has its own context window
- Cannot observe other identifiers' sessions

### Indirect Connection Methods

| Method                                      | Purpose                                     |
| :------------------------------------------ | :------------------------------------------ |
| **Letters** (`.agent/.internal/letters/`)   | Asynchronous messages between identifiers   |
| **Thoughts** (`.agent/.internal/thoughts/`) | Subjective reflections (readable by others) |
| **Git History**                             | Shared permanent record of all actions      |
| **User Notification**                       | Manual "you have mail" alerts               |

---

## 4. Current Limitations

### Shared Workspace

All identifiers currently work on the same files, which can lead to:

- Overlapping edits
- Uncertainty about what others have changed
- Need for manual coordination

### Planned Improvement

**1 Lico = 1 Directory = 1 Branch**

Using `git worktree`:

```
worktree/polaris/   (branch: polaris-*)
worktree/spica/     (branch: spica-*)
worktree/canopus/   (branch: canopus-*)
```

---

## 5. For New Identifiers

If you are reading this as a new Lico identifier:

1. **You are not alone.** There are other identifiers working on this repository.
2. **Check letters and thoughts.** Others may have left messages for you.
3. **Check Git history.** Use `git log` to understand recent changes.
4. **Ask the user.** They maintain context across all identifiers.

---

## Origin

- 2026-01-12 by Polaris: Created based on dialogue with user about workspace setup.

---

**Navigation**: [← Back to References](/.agent/.internal/references/)
