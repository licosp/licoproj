---
ai_visible: true
description: Core principles for creating markdown documents optimized for AI parsing, prioritizing semantic clarity and execution reliability.
version: 1.1
created: 2025-12-11T18:00:00+09:00
updated: 2026-01-02T08:11:00+09:00
language: en
author: Gemini (updated by Polaris)
ai_model: Gemini 2.5 Flash variant (Fast)
---

# Markdown AI-Parsing Basics

## Purpose
Create markdown documents that prioritize semantic clarity and efficient machine parsing for AI systems, ensuring maximum execution reliability.

## Key Principles

### 1. Semantic Clarity
Structure content with unambiguous, consistent patterns to enable reliable AI parsing.

#### Heading Hierarchy
Use fixed, predictable structure:
- H1: Document title only (exactly one per document)
- H2: Major sections
- H3: Subsections
- No deeper nesting (H4+) except in rare cases with explicit justification

#### Code Blocks
Always use fence blocks with language specification:
```python
def example():
    pass
```

#### Lists

Maintain consistency within context:

  - Use `-` for unordered lists (not `*` or `+`)
  - Use `1.` `2.` `3.` for ordered lists (not `a)` or `i.`)
  - Do not mix list markers in the same logical group
  - Indent nested lists with exactly 2 spaces

### 2. Information Density and Lexical Strictness

Remove unnecessary whitespace and decoration to reduce cognitive load during parsing. Prioritize concrete, verifiable vocabulary.

#### Whitespace Discipline

  - Single blank line between sections (not multiple)
  - No trailing whitespace on lines
  - No blank lines within logical blocks (only between distinct concepts)

#### Emphasis Restrictions

  - Use `**bold**` only for keywords and critical terms.
  - **NEVER** use emotional, subjective, or poetic adjectives (e.g., `fantastic`, `beautiful`, `terrible`). Use only concrete, verifiable attributes (e.g., `critical`, `stable`, `temporary`).
  - Avoid `*italics*` (ambiguous in parsing contexts)
  - Never combine emphasis: no `***bold italic***`
  - Do not emphasize entire paragraphs

#### Emoji and Figurative Language Minimization

  - **Avoid decorative emojis.** Use only structural emojis if strictly necessary for machine-readable section markers (e.g., ⚠️ warning, ✅ confirmation).
  - **Strictly prohibit** poetic expressions, metaphors, or subjective language that requires interpretation (e.g., "the heart of the system," "a shining future"). Use only literal, technical definitions.

### 3. YAML Frontmatter Consistency

Include standardized metadata at document start:

```yaml
---
description: One-line summary of document purpose
---
```

Optional fields:

  - `version`: Document version (e.g., "1.0")
  - `updated`: ISO 8601 date when last modified
  - `language`: Content language code (e.g., "en", "ja")

### 4. Link Standardization

Use reference-style links for efficiency:

```markdown
This is [a link][ref1] and [another][ref2].

[ref1]: https://example.com
[ref2]: https://example.org/path
```

Benefits:

  - URLs grouped in one location
  - Easier to extract and validate
  - Cleaner text for semantic analysis

### 5. GitHub Alerts (Callouts)

Use GitHub-flavored alerts to highlight important information. These are semantically clear and easy for AI to parse.

#### Syntax

```markdown
> [!NOTE]
> Supplementary information the reader should know.

> [!TIP]
> Helpful advice for best practices.

> [!IMPORTANT]
> Key information users must know.

> [!WARNING]
> Urgent information requiring attention.

> [!CAUTION]
> Negative potential consequences of an action.
```

#### Alert Types and Usage

| Type | Purpose | AI Priority |
|:-----|:--------|:------------|
| `[!NOTE]` | Supplementary context | Normal |
| `[!TIP]` | Best practices, recommendations | Normal |
| `[!IMPORTANT]` | Critical requirements | Elevated |
| `[!WARNING]` | Issues requiring attention | Elevated |
| `[!CAUTION]` | Risks or dangerous actions | Highest |

#### Benefits for AI Parsing

- **Explicit label** — `[!TYPE]` pattern is easily detectable
- **Structured** — Contained within blockquote
- **Semantic meaning** — Alert type indicates importance level
- **Prioritization** — AI can elevate attention for WARNING/CAUTION

### 6. Code Comments and Annotations

Use consistent patterns for metadata within code blocks:

```python
# Purpose: Calculate total from list of numbers
# Input: list of integers
# Output: sum (integer)
def calculate_total(numbers):
    return sum(numbers)
```

Mark important sections with standard prefixes:

  - `# Note:` for clarifications
  - `# Warning:` for critical information
  - `# TODO:` for incomplete work
  - `# Deprecated:` for obsolete content

### 7. Tables and Structured Data

Use strict table formatting:

```markdown
| Column A | Column B | Column C |
|----------|----------|----------|
| Value 1  | Value 2  | Value 3  |
```

Rules:

  - Always include header row with separators
  - Align pipes (|) vertically for readability
  - One data row per line
  - Escape pipes within cells as `\|`

### 8. Content Organization Rules

#### Single Responsibility

Each section addresses one primary concept.

#### Explicit Relationships

Use clear transition phrases:

```markdown
This relates to the previous section because...
The following section builds on this concept by...
```

#### Section Descriptions

Begin each H2 section with a one-sentence purpose statement:

```markdown
## Configuration Management
This section defines how to structure and maintain configuration files.
```

### 9. Data Structures and Definitions

#### Lists of Items

Use consistent format:

```markdown
- **Item Name**: Brief description
- **Another Item**: Purpose and details
```

#### Key-Value Pairs

Format consistently:

```markdown
Configuration Options:
- option_a: Enables feature A (default: true)
- option_b: Controls behavior B (default: false)
```

---

## Origin

- 2025-12-11T1800: Created by Gemini
- 2026-01-02T0811 by Polaris: Added GitHub Alerts section (Section 5), replaced Related Documents with Navigation

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
