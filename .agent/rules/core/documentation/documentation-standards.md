---
ai_visible: true
title: Documentation Standards
description: Defines standards for file naming, size, structure, and AI signatures.
tags: [documentation, standards, formatting, origin]
version: 1.2
created: 2025-12-01T00:00:00+09:00
updated: 2025-12-28T09:40:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/rules/core/meta-rules.md: Rules for creating rules
  .agent/templates/header-frontmatter.yaml: Frontmatter template
  .agent/rules/core/documentation/datetime-format.md: Datetime format standard
---

# Documentation Standards

## 1. File Naming Conventions

- **Format**: `kebab-case.md` (lowercase, hyphens).
- **Date Prefix**: Use `YYYY-MM-DD_filename.md` for logs, minutes, or time-sensitive reports.
- **Language Suffix**:
  - English (Default): `filename.md`
  - Japanese: `filename.ja.md`

## 2. Directory Organization

- **Core Rules**: `.agent/rules/core/`
- **Workflows**: `.agent/workflows/`
- **Memory/Logs**: `.agent/.internal/conversations/`
- **Ideas/Drafts**: `.agent/.internal/ideas/`

## 3. File Size & Granularity

- **Target**: Keep files under **300 lines** or **2000 tokens**.
- **Reason**: To ensure fit within LLM context windows and improve retrieval accuracy.
- **Action**: Split large files into sub-documents (e.g., `topic-part1.md`, `topic-part2.md`).

## 4. AI Search Optimization

- **Optimal Length**: **15-30 characters** (3-5 words).
- **Structure**: **Context-Target-Role** (e.g., `user-profile-manager`).
- **Rationale**:
  - **Breadth-First Search (BFS) Friendly**: Enables Lico to identify relevance from `list_dir` output without opening the file.
  - **Information Density**: Provides sufficient context to filter irrelevant paths (pruning) while keeping token usage low.

## 5. File Path References

**Principle**: Use relative paths when referencing files in documentation and user-facing text.

**Requirements**:

- **MUST** use relative paths from the repository root (e.g., `.agent/rules/README.md`)
- **MUST NOT** use absolute paths (e.g., `/home/user/project/file.md`)
- **MUST NOT** use platform-specific URI schemes (e.g., `cci:7://file://`)
- **MUST** write file paths as plain text or simple relative paths

**Rationale**:

- Relative paths are portable across different systems and users
- Absolute paths and URI schemes are unreadable and non-functional for humans
- Plain text paths are universally understood

**Examples**:

- ✅ Good: `.agent/rules/README.md`
- ✅ Good: `See the documentation in core/identity.md`
- ❌ Bad: `/home/USER/develop/shared/project/licoproj/.agent/rules/README.md`
- ❌ Bad: `[README.md](cci:7://file:///absolute/path/README.md)`

## 6. Frontmatter Template Usage

**Principle**: All files in `.agent/rules/` and `.agent/workflows/` MUST use the standard frontmatter template.

**Template Location**: `.agent/templates/header-frontmatter.yaml`

**Requirements**:

- **MUST** include the full frontmatter template when creating or updating rules/workflows
- **MUST** populate all required fields: `ai_visible`, `title`, `description`, `version`, `created`, `updated`, `language`, `author`, `ai_model`
- **MUST** include `related` field with cross-links per meta-rules cross-linking standards
- **MUST** include footer Related Documents table

**Rationale**:

- Ensures consistency across all behavioral documents
- Enables AI to reliably parse metadata
- Provides traceability (author, model, timestamps)
- Supports cross-linking and discoverability

**Example**:

```yaml
---
ai_visible: true
title: Example Rule
description: One-line summary
tags: [example, rule]
version: 1.0
created: 2025-12-23T00:00:00+09:00
updated: 2025-12-23T00:00:00+09:00
language: en
author: Lico (Instance-ID)
ai_model: Model Name
related:
  .agent/rules/core/meta-rules.md: Cross-linking standards
---
```

## 7. Origin Section (Edit History)

**Principle**: Behavioral rules with significant edit history SHOULD include an `## Origin` section at the end, before `## Related Documents`.

**Purpose**:

- Provides at-a-glance visibility into file history
- Records context for changes (not just what, but why)
- Preserves instance identifiers across generations

**Format**:

```markdown
## Origin

- YYYY-MM-DDTHHMM: Created [context/purpose]
- YYYY-MM-DDTHHMM by <Instance-ID>: [summary of change]
```

**Requirements**:

- **Date format**: `YYYY-MM-DDTHHMM` (per datetime-format.md standard)
- **Instance-ID**: Include when available (e.g., `Polaris`, `Sirius`)
- **Change summary**: Brief description of what changed and why

**Example**:

```markdown
## Origin

- 2025-12-09T0000: Created based on session learnings
- 2025-12-25T0800 by Polaris: Transformed into ritual format
- 2025-12-28T0940 by Polaris: Added legacy consideration steps
```

**Note**: This is OPTIONAL for minor updates. Use judgment on whether the change is significant enough to warrant recording.

---


## Origin

- 2025-12-01T0000: Created as documentation standards
- 2026-01-02T0828 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
