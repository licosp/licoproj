---
description: Workflow for auditing and standardizing cross-links between rule files (The Gardening Protocol)
related:
  rules/development/search-methodology.md: Implements the Search methodology defined here
  rules/core/meta-rules.md: Enforces cross-linking mandates
---

# Maintenance: Rule Audit & Cross-Linking

## Purpose
Systematically review behavioral rules to ensure they are properly interconnected, ensuring Lico can navigate the "Memory Graph" without dead ends.

## Trigger
- **Routine**: Once per IDD Cycle or Monthly.
- **Specific**: After adding a new core rule (e.g., `emergency-protocols.md`) to retroactively link it from existing files.

## Methodology
This workflow strictly follows **[search-methodology.md](.agent/rules/development/search-methodology.md)**.
- **Do not assume scalar results**.
- **Detect and report Overflow**.
- **Seek help if stuck**.

## Procedure

### Phase 1: Scope Definition
1.  **Define Target**: Decide which directory or concept to audit.
    - Example: "All files in `rules/core/`"
    - Example: "All files referencing 'memory'"

### Phase 2: Discovery & Filter (The Search Loop)
1.  **Query**: Run `find_by_name` or `grep_search`.
2.  **Overflow Check**:
    - If output is truncated -> **Refine Query** immediately.
    - **Anti-Pattern**: Using truncated list as "All files".
3.  **Filter**: Select high-priority targets.

### Phase 3: Diagnosis (The Double-Check)
For each target file:
1.  **Read Header**: Check YAML Frontmatter.
    - *Is there a `related:` key?*
    - *Are the paths mapped to descriptions?*
2.  **Read Footer**: Check "Related Documents" section.
    - *Does it match the Frontmatter?*
3.  **Conflict Check (The Union Rule)**:
    - **Path Mismatch**: If Header and Footer have different paths -> **Union** (Keep Both sources).
    - **Description Mismatch**: If description for the same path differs -> **Header Wins** (Source of Truth).
4.  **Concept Check**:
    - scan content for keywords (e.g., "stashing", "handoff").
    - *Are these concepts linked to their definitions?*

### Phase 4: Act (The Double-Entry Fix)
If links are missing, broken, or conflicting, apply the **Double-Entry Strategy**:

**Constraint**: All paths MUST be **Workspace-Relative** (e.g., `.agent/rules/core/memory.md`).

1.  **Update Footer (For Humans)**:
    ```markdown
    ## Related Documents
    | Document | Purpose |
    |:---------|:--------|
    | [.agent/dir/foo.md](.agent/dir/foo.md) | Explanation of Foo |
    ```

2.  **Update Frontmatter (For AI)**:
    ```yaml
    related:
      .agent/dir/foo.md: Explanation of Foo
    ```

**Rationale**:
- Frontmatter guarantees Machine Readability.
- Footer guarantees Human Readability.
- Root-Relative paths guarantee Robustness.

### Phase 5: Verification & Report
1.  **Verify**: Check that paths are valid (no 404s).
2.  **Report**: Summarize changes.
    - "Linked `memory.md` to `project-understanding.md`."
