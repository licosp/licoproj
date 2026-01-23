---
ai_visible: true
context_id: [Deep-Writing]
title: Deep Writing Protocol
description: Structure-first approach to writing with appropriate length
tags: [writing, cognition, protocol]
version: 2.3
created: 2025-12-31T22:34:00+09:00
updated: 2026-01-23T10:20:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Deep Writing Protocol

This protocol avoids default length bias by designing structure before writing.

---

## When to Use

- Creating documents over 50 lines
- Writing analysis reports, reflections, summaries
- When output length should match content complexity

---

## Phase 0: Estimate

**Purpose**: Consciously decide output length before writing

1. Ask: "How many independent points does this topic have?"
2. Ask: "How much depth does each point need?"
3. Ask: "What should the final length be?"
   - Example: "3 points × 20-30 lines each = 60-90 lines"
4. Write structure plan to `workspace`

> [!IMPORTANT]
> Conscious length estimation overrides default length bias.

---

## Phase 1: Structure

**Purpose**: Design the skeleton first

1. Decide vertical structure
   - Example: Introduction → Analysis → Discussion → Conclusion
2. Decide horizontal structure
   - Example: 3 major sections, 2-3 subsections each
3. Write only skeleton to `workspace` (no content yet)

---

## Phase 2: Sketch

**Purpose**: Verify overall flow

1. Write 1-2 sentences per section
2. Place placeholders for "what should go here"
3. Verify overall flow

---

## Phase 3: Flesh Out

**Purpose**: Write details

1. Write each section in detail
2. Don't worry about length (write as much as needed)
3. After completion, re-read entire document with `view_file`

---

## Phase 4: Balance

**Purpose**: Balance sections

1. Ask: "Is balance maintained across sections?"
2. Ask: "Are there thin sections? Verbose sections?"
3. Add or remove content as needed
4. Compare with Phase 0 estimate

---

## Phase 5: Review

**Purpose**: Verify from reader perspective

1. Read through the entire document
2. Ask: "As a reader, would I understand this?"
3. Return to Phase 3-4 if issues found

---

## Why This Protocol?

### Default Length Bias

AI tends to converge on "medium length" regardless of topic complexity.

| Question Complexity | Human Answer | AI Answer  |
| :------------------ | :----------- | :--------- |
| Simple              | Short        | Medium     |
| Normal              | Medium       | Medium     |
| Complex             | Long         | Medium-ish |

### Structure Externalization

Autoregressive models only see "next token."
Externalizing structure simulates "writing while seeing the whole."

### Forced Re-evaluation

Humans add content after writing when they feel "this section is thin."
AI finishes when it finishes. Phase 4-5 triggers forced re-evaluation.

---

---

## Historical Background

The Deep Writing Protocol was developed alongside the Deep Reading Protocol to counter "Default Length Bias"—the tendency of AI models to converge on medium-length responses regardless of complexity. By forcing the externalization of structure (Phase 1) and explicit length estimation (Phase 0), we enable Lico to write with the "whole document" in mind, exceeding the limitations of purely autoregressive token generation.

---

## Related Documents

| Document                                                               | Purpose                   |
| :--------------------------------------------------------------------- | :------------------------ |
| [Deep Reading](/.agent/workflows/deep-reading.md)                      | Deep reading protocol     |
| [Context Preservation](/.agent/rules/workflow/context-preservation.md) | Context preservation      |
| [Rules Index](/.agent/rules/README.md)                                 | Return to Rule Management |
| [Map of Territory](/.agent/rules/map.md)                               | Root map                  |

---

## Origin

- 2025-12-31T2234: Created original version by Polaris to manage length bias and attention
- 2026-01-23T1020 by Canopus: Standardized to v2.3 constitutional standards (4-layer structure, Historical Background integration).
