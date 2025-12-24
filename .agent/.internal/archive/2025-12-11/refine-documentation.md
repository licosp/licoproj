---
description: Refine and standardize AI instruction files
---

# Refine Instructions Workflow

## Purpose
Refine Markdown instruction files (`.md`) in `.agent/rules/` and `.agent/workflows/` to ensure they are clear, concise, and complete for AI agents (Lico).

This workflow implements the **Refinement Process** defined in [Documentation Refinement Process](../rules/core/documentation-process.md).

## Steps

### 1. Analysis
Read target file and identify issues based on **Stage 1: Analysis** in `../rules/core/documentation-process.md`:
- **Ambiguity**: Unclear instructions or formatting.
- **Redundancy**: Repeated information or unnecessary verbosity.
- **Gaps**: Missing context, steps, or requirements.

### 2. Refine and Overwrite
Rewrite file in **English** following **Stage 2: Refine and Implement** in `../rules/core/documentation-process.md`:
- **Format**: Use clear structure (Purpose, Steps, Guidelines/Additional Info).
- **Conciseness**: Remove fluff, use bullet points and imperative mood.
- **Completeness**: Fill in missing details (e.g., specific commands, directory paths).
- **Consistency**: Ensure terminology aligns with other agent documentation.

### 3. Verification
Verify the result against **Stage 3: Verification** in `../rules/core/documentation-process.md`:
- Ensure file is easy for AI to parse and understand.
- Verify no critical information was lost during simplification.
- Commit changes.
