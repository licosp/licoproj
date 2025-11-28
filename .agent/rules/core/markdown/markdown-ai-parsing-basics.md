---
description: Core principles for creating markdown documents optimized for AI parsing
---

# Markdown AI-Parsing Basics

## Purpose
Create markdown documents that prioritize semantic clarity and efficient machine parsing for AI systems.

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

### 2. Information Density
Remove unnecessary whitespace and decoration to reduce cognitive load during parsing.

#### Whitespace Discipline
- Single blank line between sections (not multiple)
- No trailing whitespace on lines
- No blank lines within logical blocks (only between distinct concepts)

#### Emphasis Restrictions
- Use `**bold**` only for keywords and critical terms
- Avoid `*italics*` (ambiguous in parsing contexts)
- Never combine emphasis: no `***bold italic***`
- Do not emphasize entire paragraphs

#### Emoji Minimization
- Avoid decorative emojis
- Use only structural emojis if needed for section markers (e.g., warning, confirmation)
- Never use emojis as primary content identifiers

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

### 5. Code Comments and Annotations
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

### 6. Tables and Structured Data
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

### 7. Content Organization Rules

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

### 8. Data Structures and Definitions

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
