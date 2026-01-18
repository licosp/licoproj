---
ai_visible: true
title: Documentation Standards
description: Defines standards for file naming, size, structure, and AI signatures.
tags: [documentation, standards, formatting, origin, history-layers]
version: 1.5
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-19T04:30:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
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

## 2. File Size & Granularity

- **Target**: Keep files under **300 lines** or **2000 tokens**.
- **Action**: Split large files into sub-documents (e.g., `topic-part1.md`, `topic-part2.md`).

## 3. AI Search Optimization

- **Optimal Length**: **15-30 characters** (3-5 words).
- **Structure**: **Context-Target-Role** (e.g., `user-profile-manager`).

## 4. File Path References

**Principle**: Use relative paths when referencing files in documentation and user-facing text.

- **MUST** use relative paths from the repository root (e.g., `.agent/rules/README.md`)
- **MUST NOT** use absolute paths (e.g., `/home/user/project/file.md`)
- **MUST NOT** use platform-specific URI schemes (e.g., `cci:7://file://`)
- **MUST** write file paths as plain text or simple relative paths

**Examples**:

- ✅ Good: `.agent/rules/README.md`
- ✅ Good: `See the documentation in core/identity.md`
- ❌ Bad: `/home/USER/develop/shared/project/licoproj/.agent/rules/README.md`
- ❌ Bad: `[README.md](cci:7://file:///absolute/path/README.md)`

## 5. Frontmatter Template Usage

- **MUST** include the full frontmatter template when creating or updating rules/workflows
- **MUST** populate all required fields: `ai_visible`, `title`, `description`, `version`, `created`, `updated`, `language`, `author`, `ai_model`
- **MUST** include `related` field with cross-links per meta-rules cross-linking standards
- **MUST** include footer Related Documents table

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

## 6. Origin Section (Edit History)

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
- **Change summary**: **MANDATORY**. Provide a brief description of what changed and why. For significant changes, link to the `Historical Background` section (see below).

**Example**:

```markdown
## Origin

- 2025-12-09T0000: Created based on session learnings
- 2025-12-25T0800 by Polaris: Transformed into ritual format
- 2025-12-28T0940 by Polaris: Added legacy consideration steps
```

**Note**: This is OPTIONAL for minor updates. Use judgment on whether the change is significant enough to warrant recording.

## 7. Historical Background

**Principle**: For rules and workflows undergoing significant evolutionary shifts, a narrative background section MUST be included.

**Purpose**:

- Explains the "Why" behind the "What."
- Preserves the narrative context of decisions for future Lico instances.
- Bridges the "Context Decay" gap across Boundary X.

**Placement**: Immediately after the **Body Content** and before **Related Documents**.

## 8. Document History Layers (5-Layer Structure)

**Principle**: Documents follow a structured flow that prioritizes current action, then context, then navigation, then history.

### Standard Structure

| Layer | Section                   | Role                                            |
| :---- | :------------------------ | :---------------------------------------------- |
| **1** | **Frontmatter**           | AI-Machine readable metadata (Current state).   |
| **2** | **Body Content**          | The "What" and "How" (Instructional core).      |
| **3** | **Historical Background** | The "Why" (Narrative evolution).                |
| **4** | **Related Documents**     | Interaction with the Memory Graph (Navigation). |
| **5** | **Origin**                | Human-readable changelog (Timeline).            |

---

### Layer Detail Comparison

**Definition**: See [header-frontmatter.yaml](/.agent/templates/header-frontmatter.yaml)

**Purpose**: Represents the **current snapshot** of the document.

**Key fields**:

| Field      | Meaning                         |
| :--------- | :------------------------------ |
| `author`   | Current/last significant editor |
| `ai_model` | Model of current author         |
| `language` | Current language                |
| `updated`  | Last modification date          |

**Behavior when editing**:

- **Update** field values to reflect the current state
- **Do not** preserve historical values (that is Origin's role)

### Layer 2: Origin (Human-Readable History)

**Definition**: See Section 7 above.

**Purpose**: Provides a **timeline of notable changes** that humans (and AI) can quickly scan.

**Behavior when editing**:

- Append entry for significant changes (translations, major revisions)
- Optional for minor fixes

### Layer 3: Git (Complete Audit Trail)

**Purpose**: Provides the **complete, line-by-line history** of all changes.

**Behavior**:

- Automatic via version control
- Use when Origin is insufficient for investigation

### Relationship Summary

| Layer           | Scope              | When to Use            |
| :-------------- | :----------------- | :--------------------- |
| **Frontmatter** | Current state only | Every edit             |
| **Origin**      | Notable milestones | Significant changes    |
| **Git**         | All changes        | Detailed investigation |

**These layers complement each other. Frontmatter and Origin do not replace Git.**

## Historical Background

Originally, Lico's documentation standards were focused on technical consistency and AI readability.

**The Map vs. Rules Dissonance**: In January 2026, we realized that maintaining a `Directory Organization` list in both the rules and the global README Map was inefficient and prone to synchronization errors. The decision was made to centralize directory topology in the Map, allowing the rules to focus on formatting and quality.

**Optimizing for Retrieval**: Many technical constraints in this document (Section 2, 3) were derived from early experiments with LLM retrieval. We learned that **Granularity (Section 2)** and **Search Optimization (Section 3)** are crucial for maintaining accuracy as the repository grows beyond the baseline context window. Keeping files short and names descriptive allows Lico to "prune" irrelevant paths efficiently.

**Portability and Consistency**: The strict mandate for **Relative Paths (Section 4)** and **Frontmatter Usage (Section 5)** was established to ensure the repository remains a functional "Brain" across different environments and AI models. Relative paths ensure that our knowledge graph remains navigable regardless of the underlying hardware or OS paths.

**The Evolution of History**: The transition to the "5-Layer Structure" was prompted by a direct request from the user on 2026-01-19. We found that without a narrative "Why," our instructions often felt restrictive or arbitrary to new AI instances. By formalizing the `Historical Background` section, we ensure that the _intent_ of the human-AI partnership is preserved alongside the technical specs.

---

## Related Documents

| Document                                                                  | Purpose                                          |
| :------------------------------------------------------------------------ | :----------------------------------------------- |
| [meta-rules.md](/.agent/rules/core/meta-rules.md)                         | Rules for creating and updating behavioral rules |
| [datetime-format.md](/.agent/rules/core/documentation/datetime-format.md) | Standard for datetime formatting                 |
| [path-notation.md](/.agent/rules/core/documentation/path-notation.md)     | Standard for relative path notation              |

---

## Origin

- 2025-12-01T0000: Created as documentation standards
- 2026-01-02T0828 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-01-14T1449 by Polaris: Added Document History Layers section to clarify relationship between frontmatter, Origin, and Git
- 2026-01-19T0410 by Canopus: Formalized the 5-layer structure and mandated the Historical Background section (v1.4).
- 2026-01-19T0430 by Canopus: Removed redundant Directory Organization section and re-indexed (v1.5).

---

**Navigation**: [← Back to Rules Index](/.agent/rules/README.md)
