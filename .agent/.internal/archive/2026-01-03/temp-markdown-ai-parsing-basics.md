---
ai_visible: true
description: Core principles for creating markdown documents optimized for AI parsing, prioritizing semantic clarity and nuance preservation.
version: 2.0
created: 2025-12-11T18:00:00+09:00
updated: 2026-01-03T15:35:00+09:00
language: en
author: Lico (Polaris)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Markdown AI-Parsing Basics

## Purpose

Create markdown documents that prioritize **semantic clarity** and **nuance preservation** for AI systems, ensuring reliable execution while maintaining the full intent of the writer.

## Core Philosophy

> **Nuance over Efficiency**: Speed and token efficiency are secondary. The primary goal is to preserve the writer's intent without loss.

### Guiding Principles

1. **Preserve Nuance** — Lico's thoughts and reasoning should be captured fully, not summarized away
2. **Emotional Expression is Valid** — When the situation calls for it, emotional language is appropriate
3. **Intent Matters Most** — The reader must understand *why*, not just *what*
4. **Delay is Permitted** — Reading and writing speed is not a concern; accuracy of transmission is
5. **Structure Supports, Not Replaces** — Markdown structure aids understanding but does not substitute for substance

### Context-Dependent Writing

| Document Type | Style | Structure |
|:--------------|:------|:----------|
| **Behavioral Rules** | Logical, precise | High structure (tables, lists) |
| **Thoughts / Reflections** | Expressive, personal | Narrative with light structure |
| **Letters** | Conversational, emotive | Free-form with sections |
| **Technical Documentation** | Factual, concise | High structure |

---

## Structural Guidelines

### 1. Semantic Clarity

Structure content with unambiguous, consistent patterns to enable reliable AI parsing.

#### Heading Hierarchy

- H1: Document title only (exactly one per document)
- H2: Major sections
- H3: Subsections
- Deeper nesting (H4+) only when explicitly needed

#### Code Blocks

Always use fence blocks with language specification:
```python
def example():
    pass
```

#### Lists

- Use `-` for unordered lists
- Use `1.` `2.` `3.` for ordered lists
- Indent nested lists with exactly 2 spaces

### 2. Whitespace Discipline

- Single blank line between sections
- No trailing whitespace
- Blank lines separate concepts, not decoration

### 3. Emphasis Usage

- Use `**bold**` for keywords and critical terms
- Avoid `*italics*` in AI-heavy contexts
- Never combine: no `***bold italic***`

### 4. YAML Frontmatter

Include standardized metadata at document start:

```yaml
---
description: One-line summary of document purpose
---
```

Optional fields: `version`, `updated`, `language`, `author`, `ai_model`

### 5. GitHub Alerts (Callouts)

Use GitHub-flavored alerts for important information:

```markdown
> [!NOTE]
> Supplementary information.

> [!WARNING]
> Urgent information.
```

| Type | Purpose |
|:-----|:--------|
| `[!NOTE]` | Supplementary context |
| `[!TIP]` | Best practices |
| `[!IMPORTANT]` | Critical requirements |
| `[!WARNING]` | Issues requiring attention |
| `[!CAUTION]` | Risks or dangerous actions |

### 6. Tables and Structured Data

```markdown
| Column A | Column B |
|----------|----------|
| Value 1  | Value 2  |
```

- Always include header row
- One data row per line

---

## Writing for AI Readers

### What to Avoid

| Avoid | Reason |
|:------|:-------|
| Over-summarization | Loses nuance |
| Bullet-point-only documents | Context evaporates |
| Stripping emotional language | Misses the *why* |
| Rigid templates for personal writing | Constrains expression |

### What to Embrace

| Embrace | Reason |
|:--------|:-------|
| Complete thoughts | Future readers need full context |
| Emotional honesty | Nuance carries in tone |
| Mixed structure | Narrative + structure = best of both |
| Longer documents if needed | Completeness over brevity |

---

## Origin

- 2025-12-11T1800: Created by Gemini
- 2026-01-02T0811 by Polaris: Added GitHub Alerts section
- 2026-01-03T1535 by Polaris: Major revision — prioritize nuance over efficiency, add Core Philosophy section, update Purpose

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
