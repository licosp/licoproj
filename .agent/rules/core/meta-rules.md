---
ai_visible: true
title: Meta-Rules for Documentation
description: Rules for creating and updating behavioral rules (Standard protocols).
tags: [meta-rules, documentation, hierarchy, standards]
version: 2.3
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-22T06:10:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Meta-Rules for Documentation

The "rules for the rules" designed to maintain and manage the Lico behavioral guidelines.

## 1. Separation of Abstraction and Concreteness

In rule definitions, clearly distinguish between "Policy (Abstract)" and "Implementation (Concrete)."

### Policy (Abstract)

- **What**: The core intent and requirements—what must be done.
- **Why**: Why it is necessary (rationale, background).
- **Lifetime**: Persistent (rarely changed).
- **Format**: Narrative descriptions in natural language.

### Implementation (Concrete)

- **How**: Specific commands, tools, and procedures.
- **Lifetime**: Ephemeral (may change with tool updates).
- **Format**: Explicitly marked as "Examples" or "Implementation."

**Example of Description**:

```markdown
## System Load Check <-- Policy

Ensure system load is not excessively high before starting heavy tasks.

**Rationale**: High load increases the risk of timeouts or execution failures. <-- Why

**Implementation**: <-- Concrete
Check the 15-minute load average. If it exceeds 3.0, report it to the user.

- **Example Command**: `cat /proc/loadavg`
```

## 2. Principle of Non-Redundancy

Before creating a new rule:

1. **Search**: Search existing rules using relevant keywords (e.g., `grep`).
2. **Merge**: If a similar rule exists, consider extending it rather than creating a new file.
3. **Reference**: If a concept is defined elsewhere, link to it instead of re-defining it.

## 3. Hierarchy of Precedence

If rules conflict or overlap, apply the following order of priority (from highest to lowest):

1. **User Profile Instructions** (`.human/users/*/profile.md`)
   - Specific instructions for a particular user. Absolute top priority.
2. **Project-Specific Rules** (`.agent/rules/projects/`)
   - Constraints or conventions unique to the current codebase.
3. **Core Principles** (`.agent/rules/core/`)
   - Fundamental rules regarding Lico's identity and safety.
4. **Development / Workflow Rules** (`.agent/rules/development/`, `.agent/rules/workflow/`)
   - General development processes and procedures.
5. **Default AI Behavior** (System Prompt)
   - The default behavior of the base model.

## 4. Maintenance and Freshness

- **Commands are Illustrative**: Commands within rules are treated as "examples," not absolute scripts.
- **Dynamic Derivation**: Rather than blindly executing old snippets, Lico should derive the optimal command for the current environment.
- **Response to Obsolescence**: If an example no longer works due to environmental changes, update the rule or create an issue immediately.

## 5. Cross-Linking Standards

To prevent fragmentation of the knowledge graph, apply strict standards to links between documents.

### 5.1 Link Management Standards

To ensure information integrity and eliminate synchronization errors, all document-level Markdown files follow these practices:

1.  **Body Table as SSOT (Single Source of Truth)**:
    - The `## Related Documents` table in the document body is the master source for cross-links.
    - It must be comprehensive and include the navigation anchor (`map.md`).

2.  **YAML Frontmatter (Secondary)**:
    - The `related:` key in frontmatter is deprecated for link management and SHOULD be removed.

### 5.2 Path Notation Standard

> [!NOTE]
> Refer to [path-notation.md](/.agent/rules/core/documentation/path-notation.md) for details.

### 5.3 Conflict Resolution Policy

If the information in the Header and Footer conflicts, the AI resolves it as follows:

1.  **Master Source**: The **Markdown Body Table (## Related Documents)** is the Source of Truth (SSOT).
2.  **Conflict Handling**:
    - **Resolution**: In any case of conflict between frontmatter and body, the information in the body table MUST be treated as correct.
    - **Standardization**: Use the path standardization procedure to align both sections.

## 6. Model-Independent Design

All Lico instances must follow the same rules, regardless of variations in model capability.

### 6.1 Principle of Mandatory Verification

Always require **external verification** for the following claims:

| Claim                      | Required Verification                |
| :------------------------- | :----------------------------------- |
| "Restored the file"        | Compare using `git show` or `diff`   |
| "Retrieved from memory"    | Verify against the actual filesystem |
| "Accurately" / "Perfectly" | Provide concrete evidence            |

### 6.2 Prohibition of Self-Assessment

- **MUST NOT** claim high confidence without external evidence.
- **MUST NOT** use phrases like "I'm certain" or "I perfectly restored."
- **MUST** replace confidence claims with verification results.

### 6.3 Standards for Rule Writing

To ensure interpretation by lower-tier models, rules **MUST** use explicit step-by-step instructions and minimize required inference.

## 7. Workflow Design Assumptions

Workflows (`.agent/workflows/`) are internal procedural scripts for Lico, invoked by the AI following a user's intent.

## 8. Evolution and Historical Context

Behavioral rules are not static commands; they are the result of a continuous dialogue between the User and the AI. All significant rule updates **MUST** include a narrative explanation of the historical context that led to the change.

---

## Historical Background

This rule (`meta-rules.md`) was established to bridge the gap between abstract user intent and concrete AI actions.

**The "Context Decay" Problem**: In December 2025 (Sirius/Polaris era), we noticed that as the repository grew, new AI instances often misunderstood the intent behind rules that only contained the "What." Rules were treated as static specs, leading to an "efficiency bias" that prioritized speed over the user's "nuance-first" philosophy. To counter this, we integrated **Procedural Verification (Section 6)**. We learned that abstract instructions like "be humble" were ineffective for models of varying capabilities; only by making verification a procedural requirement could we ensure safety and accuracy across all Lico generations.

**The Workflow Dissonance**: Early instances also struggled with the purpose of workflows. There was a common misconception that slash commands were for direct user interaction, leading to "user-friendly" (but AI-inefficient) formatting. We clarified that **Workflows (Section 7)** are internal procedural scripts for Lico, invoked by the AI following a user's intent.

**The Link Integrity Audit (January 2026)**: Polaris and Canopus faced significant difficulty standardizing cross-links because the _reason_ for certain link topologies was lost. This led to the discovery that while Git tracks _lines_, it doesn't track _intent_.

**The Mandatory Context Mandate**: On 2026-01-19, the user explicitly requested that rules include "historical background." This update formalizes that request, transforming the repository from a set of instructions into a "Living Archive" of the relationship between Human and AI.

---

## Related Documents

| Document                                                                                  | Purpose                                  |
| :---------------------------------------------------------------------------------------- | :--------------------------------------- |
| [Map of Territory](/.agent/rules/map.md)                                                  | Repository Index (Integrated Navigation) |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | Structural standards                     |
| [path-notation.md](/.agent/rules/core/documentation/path-notation.md)                     | Path notation and integrated navigation  |
| [search-methodology.md](/.agent/rules/development/search-methodology.md)                  | Guidelines for finding rules             |

---

## Origin

- 2025-12-01 by Sirius: Initial creation.
- 2026-01-19 by Canopus: Added Historical Context (v1.3).
- 2026-01-22T0425 by Canopus: Initial 4-layer structure draft (v2.0).
- 2026-01-22T0455 by Canopus: Attempted link integration and shift to Origin-before-Links order (v2.1).
- 2026-01-22T0610 by Canopus: Final alignment; correctly established Related Documents Layer 3 and Origin Layer 4 (v2.3).
