---
ai_visible: true
title: Meta-Rules for Documentation
description: Rules for creating and updating behavioral rules (Standard protocols).
tags: [meta-rules, documentation, hierarchy, standards]
version: 1.2
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-15T23:10:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
related:
  .agent/rules/development/search-methodology.md: Guidelines for finding rules
  .agent/rules/core/documentation/documentation-standards.md: Document formatting standards
  .agent/rules/core/documentation/path-notation.md: Path notation standard for links
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

### 5.1 Double-Entry Principle

To ensure both **AI machine readability** and **Human visibility**, link information must be recorded **atomically** (simultaneously) in the following two locations.

1.  **YAML Frontmatter (For AI)**:
    - The metadata region at the top of the file. Essential for AI recognition without truncation risk.
    - Format: An associative array (Map) using the `related` key.

    ```yaml
    related:
      .agent/rules/core/memory.md: Memory Architecture Definition
    ```

2.  **Footer Table (For Humans)**:
    - The "Related Documents" section at the end of the file. Optimized for human navigation in Markdown previews.

    ```markdown
    ## Related Documents

    | Document                                  | Purpose                        |
    | :---------------------------------------- | :----------------------------- |
    | [memory.md](/.agent/rules/core/memory.md) | Memory Architecture Definition |
    ```

### 5.2 Path Notation Standard

> [!NOTE]
> Refer to [path-notation.md](/.agent/rules/core/documentation/path-notation.md) for details.

**Summary**: Links must be written in the format `/.agent/...` (absolute paths from the repository root). Use of `../` is prohibited.

### 5.3 Conflict Resolution Policy

If the information in the Header and Footer conflicts, the AI resolves it as follows:

1.  **Master Source**: The **YAML Frontmatter (Header)** is the Source of Truth (SoT).
2.  **Conflict Handling**:
    - **Path Presence**: Take the **Union** of path information in the Header and Footer to prevent data loss.
    - **Description Mismatch**: Prioritize the Header's description.

### 5.4 Link Topology Principles

Focus on structured connectivity rather than linking everything to everything.

1.  **Mesh (Strongly Coupled)**:
    - **Target**: `rules/` <--> `workflows/`
    - **Direction**: **Bidirectional (Mutual)**
    - **Reasoning**: These represent Lico's "Kernel" and are mutually dependent.
2.  **Upstream (Hierarchical)**:
    - **Target**: `thoughts/` (Ephemeral) --> `rules/` (Stable)
    - **Direction**: **Unidirectional** (Volatile points to Stable)
    - **Constraint**: Linking from stable rules to individual thought logs is **prohibited** to prevent obsolescence.
3.  **References (Fixed)**:
    - **Target**: `rules/` --> `references/` (Static)
    - **Direction**: **Unidirectional** (Stable points to Static)

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

**Anti-pattern**:

```
"I have accurately restored this file."
```

**Correct pattern**:

```
"I have created the file. Please verify it using the following command:
git diff <original> <restored>"
```

### 6.3 Standards for Rule Writing

To ensure interpretation by lower-tier models:

- **MUST** use explicit step-by-step instructions.
- **MUST** minimize required inference.
- **MUST** use MUST/MUST NOT for clarity.
- **MUST** provide concrete examples over abstract principles.
- **SHOULD** convert complex rules to checklists.

### 6.4 Rationale

- Lower-tier models may not recognize their own limitations.
- Abstract instructions like "be humble" do not work effectively.
- Integrating verification as a **procedural requirement** ensures safety independent of model performance.

## 7. Workflow Design Assumptions

Workflows (`.agent/workflows/`) are governed by specific design assumptions that differ from user-facing documentation.

### 7.1 Audience

- **Primary Reader**: Lico (AI) only.
- **User Invocation**: Users do NOT directly use slash commands.
- Slash commands are internally processed by Lico when the user mentions them in conversation.

### 7.2 Implications

- **No User-Facing Considerations**: No special formatting or accessibility accommodations for human readers.
- **Format Consistency**: Workflows use the same frontmatter as rules (author, version, related, etc.).
- **Language**: Primarily English.

### 7.3 Common Mistake

Past Lico instances assumed slash commands implied direct user interaction. This is incorrect.

**Wrong assumption**:

> "Workflows are invoked by users via /command, so they need user-friendly formatting."

**Correct understanding**:

> "Workflows define procedures for Lico to follow. Users request actions; Lico internally invokes the workflow."

---

## Origin

- 2025-12-01 by Sirius: Initial creation as meta-rules for rule governance.
- 2026-01-04 by Polaris: Added Origin and Navigation sections (cross-link audit).
- 2026-01-13 by Polaris: Shortened Section 5.2, delegated to path-notation.md for SoT.
- 2026-01-15 by Canopus: Fully translated to English and standardized formatting (v1.2).

---

**Navigation**: [<- Back to Rules Index](/.agent/rules/README.md)
