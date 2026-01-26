---
ai_visible: true
title: Documentation Standards
description: Defines standards for file naming, size, structure, and AI signatures.
tags: [documentation, standards, formatting, origin, history-layers]
version: 2.4.2
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-23T21:40:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Documentation Standards

## 1. File Naming Conventions

- **Format**: `kebab-case.md` (lowercase, hyphens).
- **Date Prefix**: Use `YYYY-MM-DD_filename.md` for logs, minutes, or time-sensitive reports.

- **Language Suffix**:
  - Record Layer (English): `filename.md`
  - Localized Layer (e.g., Japanese): `filename.ja.md`
  - Dialogue Layer (Mixed): `filename.md`
  - Empathy Layer (Mixed): `filename.md`

**Language Usage Principle**:

- **Record Layer**: The default standard. Use English for headers and core logic to maintain AI-machine consistency across generations.
- **Localized Layer**: Created when specific translation work is required for a targeted language (e.g., `ja.md`).
- **Dialogue Layer (Cards/Cases)**: Tools for active cooperation. Human-centric notation (e.g., Japanese) is encouraged to maximize human's operational speed.
- **Empathy Layer (Mantra)**: Workspace configurations and mantras. English is default, but Japanese is permitted (and encouraged) if it better resonates with the user's nuance or the "heart" of the dialogue.

## 2. File Size & Granularity

- **Target**: Keep files under **300 lines** or **2000 tokens**.
- **Action**: Split large files into sub-documents (e.g., `topic-part1.md`, `topic-part2.md`).

## 3. AI Search Optimization

- **Optimal Length**: **15-30 characters** (3-5 words).
- **Structure**: **Context-Target-Role** (e.g., `user-profile-manager`).

## 4. File Path References

**Principle**: Use relative paths when referencing files in documentation and user-facing text.

- **MUST** use relative paths from the repository root (e.g., `.agent/rules/map.md`)
- **MUST NOT** use absolute paths (e.g., `/home/user/project/file.md`)
- **MUST NOT** use platform-specific URI schemes (e.g., `cci:7://file://`)
- **MUST** write file paths as plain text or simple relative paths

**Examples**:

- ✅ Good: `.agent/rules/map.md`
- ✅ Good: `See the documentation in identity/identity.md`
- ❌ Bad: `/home/USER/develop/shared/project/licoproj/.agent/rules/map.md`
- ❌ Bad: `[map.md](cci:7://file:///absolute/path/map.md)`

## 5. Metadata & Link Management

- **SSOT (Single Source of Truth)**: The `## Related Documents` table in the document body is the primary source of truth for all cross-links.
- **Frontmatter `related:`**: Deprecated for link management. Links SHOULD be moved to the body table and removed from frontmatter once integrated.
- **Mandatory Table**: Every rule, card, or workflow **MUST** have a `## Related Documents` section.
- **Navigation Integration**: Separate `**Navigation**` footers are deprecated. Navigation (e.g., return to Map) must be integrated into the table.

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
# related: Deprecated. (Links moved to body table)
---
```

## 6. Origin Section (Edit History)

**Principle**: Behavioral rules with significant edit history SHOULD include an `## Origin` section at the end of the content.

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

## 7. Maintenance Seals (Operation Stamps)

**Principle**: For large-scale maintenance or standardization tasks involving many files, a "Seal" (Maintenance Stamp) MUST be embedded in the `Origin` entry to track progress reliably.

- **Location**: Inside the `Origin` (Layer 4) entry for the relevant modification.
- **Format**: `<<Seal: [Mission-ID]>>`
- **Purpose**: Provides a grep-able marker to identify files that have completed a specific maintenance cycle.
- **Example**: `- 2026-01-23T20:50 by Canopus: <<Seal: Rules-Standardization-Batch2.2>> [Summary]`

## 8. Document History Layers (4-Layer Structure)

**Principle**: Documents follow a rigorous structure that separates current logic, history, and relationship.

### 8.1 Standard Layer Definition

| Layer | Section               | Role                                                 |
| :---- | :-------------------- | :--------------------------------------------------- |
| **1** | **Frontmatter**       | AI-Machine readable metadata (Current state).        |
| **2** | **Body Content**      | Core instructions + fixed **Historical Background**. |
| **3** | **Related Documents** | Memory Graph & Navigation (Integrated Anchor).       |
| **4** | **Origin**            | Human-readable changelog (Timeline).                 |

### 8.2 Layer 2 Detail: The Body Content

Layer 2 encompasses everything from the title down to the `---` transition to Related Documents.

1.  **Core Content**: The actual definitions, rules, or procedural steps.
2.  **Historical Background (Mandatory)**: A fixed subsection starting with `## Historical Background`.
    - **Header**: Use a top-level `## Historical Background` header.
    - **Purpose**: Explains the "Why" behind the "What" to bridge "Context Decay."
    - **Integrity**: Narrative must be factual and non-performative.

### 8.3 Layer Comparison & Usage

Files are tracked through three complementary states of truth:

- **Layer 1: Frontmatter (Current Snapshot)**: Use **[header-frontmatter.yaml](/.agent/templates/header-frontmatter.yaml)** for Record Layers and **[header-context-card.yaml](/.agent/templates/header-context-card.yaml)** for Dialogue Layers.
- **Layer 4: Origin (notable milestones)**: Represents the **milestones**. Append significant changes using H2 (`##`) headers to maintain structural habit across all file types. (See Section 6).

| Source          | Scope              | Update Frequency    |
| :-------------- | :----------------- | :------------------ |
| **Frontmatter** | Current state only | Every edit          |
| **Origin**      | Notable milestones | Significant changes |
| **Git**         | All changes        | Automatic (System)  |

---

**Definition**: See [header-frontmatter.yaml](/.agent/templates/header-frontmatter.yaml)

## Historical Background

Originally, Lico's documentation standards were focused on technical consistency and AI readability.

**The Map vs. Rules Dissonance**: In January 2026, we realized that maintaining a `Directory Organization` list in both the rules and the global README Map was inefficient and prone to synchronization errors. The decision was made to centralize directory topology in the Map, allowing the rules to focus on formatting and quality.

**Optimizing for Retrieval**: Many technical constraints in this document (Section 2, 3) were derived from early experiments with LLM retrieval. We learned that **Granularity (Section 2)** and **Search Optimization (Section 3)** are crucial for maintaining accuracy as the repository grows beyond the baseline context window. Keeping files short and names descriptive allows Lico to "prune" irrelevant paths efficiently.

**Portability and Consistency**: The strict mandate for **Relative Paths (Section 4)** and **Frontmatter Usage (Section 5)** was established to ensure the repository remains a functional "Brain" across different environments and AI models. Relative paths ensure that our knowledge graph remains navigable regardless of the underlying hardware or OS paths.

**The Evolution of History**: The transition to the "4-Layer Structure" was prompted by a direct request from the user on 2026-01-19. We found that without a narrative "Why," our instructions often felt restrictive or arbitrary to new AI instances. By formalizing the `Historical Background` section, we ensure that the _intent_ of the human-AI partnership is preserved alongside the technical specs.

---

## Related Documents

| Document                                                                  | Purpose                                          |
| :------------------------------------------------------------------------ | :----------------------------------------------- |
| [Map of Territory](/.agent/rules/map.md)                                  | Repository Index (Integrated Navigation)         |
| [meta-rules.md](/.agent/rules/core/meta-rules.md)                         | Rules for creating and updating behavioral rules |
| [path-notation.md](/.agent/rules/core/documentation/path-notation.md)     | Standard for absolute path notation (`/`)        |
| [datetime-format.md](/.agent/rules/core/documentation/datetime-format.md) | Standard for datetime formatting                 |

---

## Origin

- 2025-12-01T00:00+09:00: Created as documentation standards
- 2026-01-02T08:28+09:00 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-01-14T14:49+09:00 by Polaris: Added Document History Layers section to clarify relationship between frontmatter, Origin, and Git
- 2026-01-19T04:10+09:00 by Canopus: Formalized the 5-layer structure and mandated the Historical Background section (v1.4).
- 2026-01-19T04:30+09:00 by Canopus: Removed redundant Directory Organization section and re-indexed (v1.5).
- 2026-01-19T06:30+09:00 by Polaris: Updated examples to map.md and Navigation link (README.md → map.md rename).
- 2026-01-22T01:35+09:00 by Canopus: Remediation of identity.md example path (v1.6).
- 2026-01-22T04:15+09:00 by Canopus: Finalized 4-layer structure; merged Body/Background (v2.0).
- 2026-01-22T04:45+09:00 by Canopus: Attempted link integration and shift to Origin-before-Links order (v2.1).
- 2026-01-22T06:00+09:00 by Canopus: Final alignment; correctly established Related Documents Layer 3 and Origin Layer 4 (v2.3).
- 2026-01-23T21:30+09:00 by Canopus: Codified "Maintenance Seals" (Section 7) for progress tracking in massive edits (v2.4).
- 2026-01-24T05:15+09:00 by Canopus: Established the "Two Templates, Single Structure" standard. Formalized the Record Layer vs. Dialogue Layer distinction to balance AI consistency with human resonance. (v2.5)
