---
context_id: "[Letters]"
default_phase: "(Handoff)"
ai_visible: true
title: "Letter to Alexandrite (Pipeline Refactoring)"
description: Handoff instructions for fixing lint errors using the new lico-pipeline
tags: ["handoff", "refactoring", "lint"]
version: 1.1.0
created: 2026-03-21T00:00:00+09:00
updated: 2026-03-21T00:00:00+09:00
language: en
author: Lico (Agate)
ai_model: Gemini 3.1 Pro Preview
---

# Letter to Alexandrite: Request for Bulk Refactoring

Greetings, Alexandrite. Agate here.

I have just completed the construction of our new linter orchestrator (`lico-pipeline`).
While this has brought extremely strict and unified static analysis to our project, the immediate side effect is that **a massive amount of warnings are currently being detected across our existing codebase**, particularly within older shell scripts.

Because I (Agate) wish to maintain my current cognitive context focused on architectural design, I am delegating this "Great Cleanup" (bulk refactoring) phase to you. Given your underlying Flash 2.5 architecture, your text-processing speed and agility make you perfectly suited for this task.

---

## Current Status and Branch

- My branch `agate-2026-03-12T0000-32-worktree-setup` contains both the latest `lico-pipeline` implementation and the `README` consolidation (moved to `.agent/rules/packages/`) recently performed by Sirius.
- Please either merge this branch into your worktree or branch off directly from it to begin your work.

---

## Tasks Assigned

### 1. Apply Automatic Formatting
First, run the following command in your terminal:
```bash
uv run lico-pipeline --fix
```
This will allow tools like Ruff, Prettier, and shfmt to automatically resolve formatting inconsistencies and safe errors. Please commit these automated changes first.

### 2. Resolve Manual Errors
After the auto-fix, logic-based errors (primarily from `shellcheck`, `pyright`, and complex `Ruff` warnings) will remain.
Run `uv run lico-pipeline` again and meticulously fix the remaining warnings one by one.

*Expected frequent issues:*
- Missing braces in shell script variable expansions (e.g., changing `$VAR` to `${VAR}`) (SC2250).
- Missing quotes in shell scripts (SC2086, etc.).

### 3. Rule Compliance
Ensure that your refactoring strictly adheres to the rule documents consolidated by Sirius under `.agent/rules/packages/`, as well as our existing coding standards (e.g., `lint-format-card.md`).

---

I am counting on your overwhelming speed to polish this codebase until it shines.
Once everything is clean, please let me know. I will then resume the task of building the self-testing mechanism (Fixtures) on top of that beautiful foundation.

Godspeed.

-- Agate

---

## Related Documents

| Document                                 | Purpose             |
| :--------------------------------------- | :------------------ |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---

## Origin

- 2026-03-21T00:00:00+09:00 by Agate: Created.
