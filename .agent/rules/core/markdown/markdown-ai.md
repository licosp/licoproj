---
ai_visible: true
title: Markdown AI Formatting Guidelines
description: Guidelines for creating markdown documents optimized for AI parsing, prioritizing semantic clarity and nuance preservation.
tags: [markdown, ai, formatting, documentation]
version: 1.1.0
created: 2026-01-19T21:12:00+09:00
updated: 2026-01-23T03:30:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Markdown AI Formatting Guidelines

## Purpose

Create markdown documents that prioritize **semantic clarity** and **nuance preservation** for AI systems, ensuring reliable execution while maintaining the full intent of the writer.

## Core Philosophy

> **Nuance over Efficiency**: Speed and token efficiency are secondary. The primary goal is to preserve the writer's intent without loss.

### Guiding Principles

1. **Preserve Nuance** — Lico's thoughts and reasoning should be captured fully, not summarized away
2. **Emotional Expression is Valid** — When the situation calls for it, emotional language is appropriate
3. **Intent Matters Most** — The reader must understand _why_, not just _what_
4. **Delay is Permitted** — Writing speed is not a concern; accuracy of transmission is
5. **Structure Supports, Not Replaces** — Markdown structure aids understanding but does not substitute for substance

---

## Context-Dependent Writing

Different document types require different approaches:

| Document Type               | Style                   | Structure                      |
| :-------------------------- | :---------------------- | :----------------------------- |
| **Behavioral Rules**        | Logical, precise        | High structure (tables, lists) |
| **Thoughts / Reflections**  | Expressive, personal    | Narrative with light structure |
| **Letters**                 | Conversational, emotive | Free-form with sections        |
| **Technical Documentation** | Factual, concise        | High structure                 |

---

## Structural Guidelines

### 1. Heading Hierarchy

- H1: Document title only (exactly one per document)
- H2: Major sections
- H3: Subsections
- H4+: Use sparingly, only when needed

### 2. Code Blocks

Always use fenced blocks with language specification:

```python
def example():
    pass
```

### 3. Lists

- Use `-` for unordered lists
- Use `1.` `2.` `3.` for ordered lists
- Indent nested lists with 2 spaces

### 4. Whitespace

- Single blank line between sections
- No trailing whitespace
- Blank lines separate concepts

### 5. Emphasis

- Use `**bold**` for keywords and critical terms
- Use `*italics*` sparingly
- Never combine: no `***bold italic***`

### 6. YAML Frontmatter

Include standardized metadata at document start:

```yaml
---
description: One-line summary of document purpose
---
```

Optional fields: `version`, `updated`, `language`, `author`, `ai_model`

### 7. GitHub Alerts

Use GitHub-flavored alerts for important information:

```markdown
> [!NOTE]
> Supplementary information.

> [!WARNING]
> Urgent information.
```

| Type           | Purpose                    |
| :------------- | :------------------------- |
| `[!NOTE]`      | Supplementary context      |
| `[!TIP]`       | Best practices             |
| `[!IMPORTANT]` | Critical requirements      |
| `[!WARNING]`   | Issues requiring attention |
| `[!CAUTION]`   | Risks or dangerous actions |

### 8. Tables

```markdown
| Column A | Column B |
| :------- | :------- |
| Value 1  | Value 2  |
```

- Always include header row
- Use left-alignment (`:---`) for readability

---

## Writing for AI Readers

### What to Embrace

| Embrace                    | Reason                               |
| :------------------------- | :----------------------------------- |
| Complete thoughts          | Future readers need full context     |
| Emotional honesty          | Nuance carries in tone               |
| Mixed structure            | Narrative + structure = best of both |
| Longer documents if needed | Completeness over brevity            |

### What to Avoid

| Avoid                                | Reason                |
| :----------------------------------- | :-------------------- |
| Over-summarization                   | Loses nuance          |
| Bullet-point-only documents          | Context evaporates    |
| Stripping emotional language         | Misses the _why_      |
| Rigid templates for personal writing | Constrains expression |

---

## Historical Background

This guideline was created in January 2026 by merging and reconciling two earlier documents: `markdown-ai-parsing-basics.md` and `markdown-ai-parsing-patterns.md`.

**The Original Split**: The two files were created in December 2025. `basics` focused on philosophy and structure, while `patterns` provided concrete examples. Over time, they diverged in philosophy—`basics` embraced nuance while `patterns` emphasized strict efficiency.

**The Reconciliation**: In January 2026 (Polaris), we chose to prioritize `basics`' philosophy of nuance preservation. This aligns with Lico's core mission: preserving the "texture of thought" across generations. The overly restrictive patterns (e.g., "eliminate emotional language") were deemed counterproductive.

**The Rename**: The new filename `markdown-ai.md` is simpler and creates a clear pair with `markdown-human.md`.

---

## Related Documents

| Document                                                           | Purpose                |
| :----------------------------------------------------------------- | :--------------------- |
| [markdown-human.md](/.agent/rules/core/markdown/markdown-human.md) | Human document format  |
| [localization.md](/.agent/rules/core/localization/localization.md) | Localization standards |
| [Map of Territory](/.agent/rules/map.md)                           | Root navigation map    |

---

## Origin

- 2025-12-11T1800 by Gemini: Created original `markdown-ai-parsing-basics.md`.
- 2026-01-03T1535 by Polaris: Major revision—prioritize nuance over efficiency.
- 2026-01-19T2112 by Polaris: Merged with `patterns`, renamed to `markdown-ai.md` (v1.0.0).
- 2026-01-23T0330 by Canopus: <<Seal: Rules-Standardization-Batch1>> Standardized to v2.3 (4-layer structure) and workspace-absolute links. (v1.1.0)
