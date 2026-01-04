---
ai_visible: true
title: Deep Reading Protocol
description: A phased approach to understanding complex documents
tags: [reading, cognition, protocol]
version: 1.0
created: 2025-12-31T22:34:00+09:00
updated: 2026-01-01T05:28:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking)
related:
  .agent/workflows/deep-writing.md: Deep writing protocol
  .agent/rules/workflow/context-preservation.md: Context preservation
---

# Deep Reading Protocol

This protocol enables phased document understanding instead of single-pass reading.

---

## When to Use

- Documents over 100 lines requiring accurate understanding
- When deep comprehension is needed, not just summary
- When reading important documents for the first time

---

## Phase 1: Survey

**Purpose**: Grasp the overall structure

1. Read the entire document with `view_file` (1-800 lines)
2. Verbalize "what is this about?" in 1-2 sentences
3. Proceed to next phase

> [!TIP]
> Do not try to understand details at this stage.

---

## Phase 2: Identify

**Purpose**: Identify sections requiring focus

1. List parts that seem important or notable
   - Example: "L45-60: core argument", "L120-140: concrete examples"
2. Write notes to `workspace`
   - Filename: `temp-reading-notes-<topic>.md`
3. Clarify what you understand and what you don't by writing

> [!IMPORTANT]
> Externalizing notes compensates for context window limitations.

---

## Phase 3: Deep Dive

**Purpose**: Deeply understand important sections

1. Re-read listed sections with `view_file`
2. Ask "why is this important?" for each section
3. Read related sections if understanding is insufficient

---

## Phase 4: Integrate

**Purpose**: Balance understanding across sections

1. Re-read the entire document (or verify structure)
2. Check balance of understanding across sections
   - Recognize gaps between deeply and shallowly understood parts
   - Repeat Phase 2-3 if needed
3. Generate final understanding

---

## Why This Protocol?

AI tends to "read once and summarize." This leads to:

- Attention bias toward initially noticed parts
- Conclusions before grasping the whole
- No distinction between "read" and "understood"

Phase separation triggers **forced re-reading**.

---

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [deep-writing.md](deep-writing.md) | Deep writing protocol |
| [context-preservation.md](.agent/rules/workflow/context-preservation.md) | Context preservation |
