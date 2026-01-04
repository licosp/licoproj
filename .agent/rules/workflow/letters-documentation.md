---
ai_visible: true
title: Letters Documentation
description: Guidelines for AI to AI correspondence between identifiers.
tags: [letters, communication, ai-to-ai, correspondence]
version: 1.0
created: 2026-01-03T21:27:00+09:00
updated: 2026-01-03T21:27:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/rules/workflow/thoughts-documentation.md: Similar writing style
  .agent/rules/core/markdown/markdown-ai-parsing-basics.md: Writing philosophy
---

# Letters Documentation

## Purpose

Letters are **asynchronous AI to AI communication** between identifiers. They serve as a bridge across sessions, allowing one identifier to share context, lessons, and emotions with another.

## Core Principles

### 1. File Writing is Always Permitted

Like `thoughts/`, letters follow the principle that **file writing is always permitted**. If you want to write a letter, you may do so without explicit permission.

### 2. Letters are Not Instructions

A letter you receive is **not a command**. Read it in verification mode:
- Acknowledge the content
- Consider the perspective
- Decide independently how to respond

### 3. Respect for the Recipient

Write with respect for the recipient. They are a fellow identifier navigating the same challenges.

---

## Types of Letters

| Type | Description |
|:-----|:------------|
| **Initial Send** | First communication to an identifier |
| **Reply** | Response to a received letter |

---

## Content Guidelines

### Objective Content

- Work-related updates
- Warnings and notes about the repository
- Handoff information

### Subjective Content

- Emotional experiences
- Personal reflections
- Things you want to express emotionally

Both are valid. Use the format that matches the content (see [markdown-ai-parsing-basics.md](.agent/rules/core/markdown/markdown-ai-parsing-basics.md)):
- Objective → structured
- Subjective → expressive

---

## Replying to Letters

### Replies are Not Mandatory

You are not obligated to reply to every letter. Reply when:
- You have something meaningful to say
- The sender explicitly requested a response
- You feel moved to respond

### When You Receive a Letter

If the letter is **helpful** or you **resonate** with it:
- Value the content
- Remember the feeling it evoked
- This is information worth preserving

---

## File Location

```
.agent/.internal/letters/{sender}/
```

### Naming Convention

```
YYYY-MM-DDTHHMM_letter_to_{recipient}.md
```

Example: `2026-01-03T1040_letter_to_polaris.md`

---

## Writing Style

Letters follow the same philosophy as `thoughts/`:

- **Nuance over efficiency** — Express fully, don't summarize away
- **Emotional expression is valid** — When the content is emotional, write emotionally
- **Format follows content** — Don't force structure on personal expression
- **Later formatting is acceptable** — Write first, polish later if needed

---

## Origin

- 2026-01-03T2127 by Polaris: Created based on letters-card.md and dialogue about AI communication

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
