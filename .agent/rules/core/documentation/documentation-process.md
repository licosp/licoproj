---
description: Decision framework and refinement workflow for documentation
---
# Documentation Refinement Process

## Decision Framework

### When to Split a File
1. File exceeds 150 lines
2. File contains multiple distinct responsibilities
3. Independent sections are frequently referenced separately

### When to Merge Files
1. Related files are always referenced together
2. Total combined size is less than 80 lines
3. Conceptual overlap is high

### When to Create a Subdirectory
1. Directory contains 10+ files
2. Clear subcategories emerge (e.g., `testing/`, `deployment/`)
3. Files share a common prefix (e.g., `git-commit.md`, `git-push.md` → `git/commit.md`, `git/push.md`)

### When to Flatten Directory Structure
1. Subdirectory contains only 1-2 files
2. Deep nesting (4+ levels) without clear benefit
3. Directory names are redundant with parent context

---

## Current Structure Reference

The behavioral rules hierarchy is organized as:

```
.agent/rules/
├── README.md (index)
├── core/ (behavioral standards)
├── development/ (development practices)
├── projects/ (project-specific rules)
└── workflow/ (operational procedures)
```

**Depth**: 2 levels ✓ (adheres to standards)

---

## Refinement Process

### Stage 1: Analysis
When reviewing documentation files, identify:
- **Ambiguity**: Unclear instructions or formatting
- **Redundancy**: Repeated information across multiple files
- **Gaps**: Missing context, incomplete steps, or undefined requirements

### Stage 2: Refine and Implement
Rewrite documentation with these goals:
- **Format**: Use clear, consistent structure (Purpose, Content Sections, Decision Criteria)
- **Conciseness**: Remove fluff, use bullet points and imperative language
- **Completeness**: Fill in missing details; avoid hardcoded paths or file-specific references
- **Consistency**: Ensure terminology and tone align across all documentation

### Stage 3: Verification
- Ensure the refined content is easy for AI agents to parse and apply
- Verify no critical information was lost during refinement
- Confirm the file adheres to granularity standards (size, naming, depth)
- Document changes in version control

---

## Application Workflow

### Maintenance Cycle
1. **Monitor**: Track documentation quality and identify files needing refinement
2. **Analyze**: Apply Stage 1 analysis to target files
3. **Refine**: Apply Stage 2 refinement principles
4. **Verify**: Complete Stage 3 verification
5. **Commit**: Record changes with clear commit messages

### When to Apply Refinement
- New documentation is created
- Documentation becomes outdated or difficult to understand
- File size exceeds 150 lines
- Multiple files contain overlapping content
- AI comprehension issues are identified
