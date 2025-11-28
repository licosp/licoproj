---
description: Standards for file size, naming, and directory organization
---
# Documentation Standards

## Purpose
Define optimal file and directory structure standards to maximize AI comprehension and maintain clarity in documentation.

## 1. File Size

### Recommended Range
- **Ideal**: 20-80 lines per file
- **Warning threshold**: 100+ lines
- **Split required**: 150+ lines

### Rationale
- Single concept coverage: Each file should comprehensively explain one concept
- Cognitive load: Entire content visible at a glance
- AI efficiency: Optimal context window utilization

### Decision Criteria
- ✅ Does the file have a single, clear responsibility?
- ✅ Can it be understood independently?
- ❌ Does it contain multiple unrelated concepts?

**Action**: Split files exceeding 150 lines into logical components.

---

## 2. File Naming

### Recommended Length
- **Preferred**: 10-25 characters (including `.md`)
- **Minimum acceptable**: 8 characters (e.g., `push.md`)
- **Maximum acceptable**: 30 characters

### Naming Patterns

#### Single Word (8-15 characters)
Use when directory context provides clarity:
- `identity.md`
- `commit.md`
- `localization.md`

#### Hyphenated 2-3 Words (16-30 characters)
Use when specificity is needed:
- `code-quality.md`
- `language-standards.md`
- `conversation-logging.md`

### Avoid
- **Abbreviations**: `conv-log.md`, `cont-imp.md` (unclear)
- **Redundancy**: `continuous-improvement-and-learning-guidelines.md` (too verbose)

### Decision Criteria
- ✅ Is the content clear from the filename?
- ✅ Is it readable at a glance?
- ✅ Does the directory path + filename provide full context?

---

## 3. Directory File Count

### Recommended Range
- **Ideal**: 3-7 files per directory
- **Warning threshold**: 10+ files
- **Reorganization needed**: 12+ files

### Rationale
- **Miller's Law**: Human short-term memory holds 7±2 items
- Long lists increase cognitive load
- Categorization improves understanding

### Decision Criteria
- ✅ Are files logically grouped?
- ✅ Should a subdirectory be created for better organization?
- ❌ Are unrelated files mixed together?

**Action**: Create subdirectories when file count exceeds 10.

---

## 4. Directory Tree Depth

### Recommended Depth
- **Ideal**: 2-3 levels
- **Maximum acceptable**: 4 levels

### Examples

#### Optimal (2 levels)
```
.agent/rules/core/identity.md
```

#### Acceptable (3 levels)
```
.agent/rules/development/testing/unit-tests.md
```

#### Warning (4 levels)
```
.agent/rules/workflow/communication/logging/format.md
```

#### Avoid (5+ levels)
Deep nesting makes navigation difficult and increases cognitive load.

### Rationale
- **Too deep**: Navigation becomes cumbersome, complexity increases
- **Too shallow**: Files scatter, poor organization
- **2-3 levels**: Balanced structure, clear hierarchy

### Decision Criteria
- ✅ Is the role clear from the path?
- ✅ Does each level represent a meaningful classification?
- ❌ Is the structure over-engineered?

---

## 5. Human Review Materials

### Requirement
Materials requiring human review **MUST** be:
1.  Created in a **human-readable format** (e.g., Markdown optimized for reading, not parsing).
2.  Saved in the **optimal directory** within the workspace (e.g., `.human/locales/ja/` for Japanese users).
3.  Given an **optimal name** that clearly describes the content to a human.

### Rationale
- **Respect for User Time**: Humans read differently than machines; formatting should prioritize human cognition.
- **Contextual Relevance**: Files should reside where humans expect to find them.
- **Clarity**: Filenames should be descriptive and intuitive.
