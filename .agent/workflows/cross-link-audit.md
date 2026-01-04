---
ai_visible: true
title: Cross-Link Audit Workflow
description: Audit and fix cross-links in rules and workflows
tags: [maintenance, cross-link, audit]
version: 1.1
created: 2026-01-01T12:26:00+09:00
updated: 2026-01-04T11:24:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking)
related:
  .agent/rules/core/meta-rules.md: Section 5 - Cross-linking standards
  .agent/rules/core/markdown/markdown-ai-parsing-basics.md: AI markdown format
  .agent/rules/core/documentation/documentation-standards.md: Documentation standards
---

# Cross-Link Audit Workflow

Audit and fix cross-links in rules and workflows to ensure consistency and maintainability.

---

## When to Use

- Periodic maintenance (monthly or after major restructuring)
- After moving or renaming files
- When creating new rules or workflows

---

## Scope

> [!IMPORTANT]
> Execute this workflow on **one directory at a time** (e.g., `.agent/rules/`).
> Complete all phases for one directory before moving to the next.

---


## Link Design Policy

### Link Placement

| Location | Content | Reader |
|:---------|:--------|:-------|
| **frontmatter `related:`** | Complete list of related files | Lico (AI) |
| **Inline references** | Context-dependent refs (specific to paragraph) | Lico (AI) |
| **Footer** | README link only | Human |

### Rules

- **Generic related docs** → Move to frontmatter, not in body
- **Context-dependent refs** → Keep in body, may also be in frontmatter
- **frontmatter is the complete related list**
- **README link is NOT in frontmatter** (navigation vs. relation)

---

## Phase 1: Preparation

**1-1. Identify Scope**

Determine which directories to audit:
```bash
# List all rule and workflow files
find .agent/rules -name "*.md" -type f
find .agent/workflows -name "*.md" -type f
```

**1-2. Extract Current Links**

Extract all links from files:
```bash
# Extract frontmatter related links
grep -r "^  \." .agent/rules --include="*.md" | head -50

# Extract footer table links
grep -r "^\|.*\](.*\.md)" .agent/rules --include="*.md" | head -50

# Extract inline markdown links
grep -rE "\[.*\]\(.*\.md\)" .agent/rules --include="*.md" | head -50
```

---

## Phase 2: Link Validation

**2-1. Check for Broken Links**

```bash
# Find all .md links and verify they exist
grep -rohE "\[.*\]\([^)]+\.md[^)]*\)" .agent/rules | \
  grep -oE "\([^)]+\)" | tr -d '()' | sort -u | \
  while read path; do
    [ ! -f "$path" ] && echo "BROKEN: $path"
  done
```

**2-2. Check Path Format**

All paths should be workspace-root relative (`.agent/...`), not file-relative (`../...`).

```bash
# Find relative paths (../...)
grep -rE "\.\./.*\.md" .agent/rules --include="*.md"
```

**2-3. Convert Relative Paths to Workspace Root**

For each file with `../` paths, convert to workspace-root format:

```bash
# Example: Convert ../core/foo.md to .agent/rules/core/foo.md
sed -i 's|\.\./core/|.agent/rules/core/|g' <file>
sed -i 's|\.\./\.\./|.agent/|g' <file>
```

> [!TIP]
> Paths in documentation examples (showing what NOT to do) should remain unchanged.

> [!CAUTION]
> Do NOT delete broken links immediately. The file may have moved. Search first.

---

## Phase 3: Footer Simplification

**3-1. Identify Files with Related Documents Tables**

```bash
# Find files with Related Documents section
grep -l "## Related Documents" .agent/rules/**/*.md
```

**3-2. Replace with README Link**

For each file, replace the Related Documents table with:

```markdown
---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
```

> [!NOTE]
> Move any useful links from the table to frontmatter `related:` before deleting.

---

## Phase 4: Frontmatter Consolidation

**4-1. Identify Missing Related Links**

For each file, compare:
- Inline references in body
- Frontmatter `related:` section

**4-2. Add Missing Links to Frontmatter**

Format:
```yaml
related:
  .agent/rules/core/memory.md: Memory architecture
  .agent/rules/development/git-operations.md: Git standards
```

---

## Phase 5: Orphan Detection

**5-1. Find Orphaned Files**

Files not linked from anywhere:
```bash
# Get all .md files
find .agent/rules -name "*.md" > /tmp/all-files.txt

# Get all linked files
grep -rohE "\[.*\]\([^)]+\.md[^)]*\)" .agent/rules | \
  grep -oE "\([^)]+\)" | tr -d '()' | sort -u > /tmp/linked-files.txt

# Find orphans
comm -23 <(sort /tmp/all-files.txt) <(sort /tmp/linked-files.txt)
```

**5-2. Decision**

For each orphan:
- Add link from README.md or parent document
- Or document why it should remain unlinked

---

## Phase 6: Cycle Detection

**6-1. Check for Meaningless Cycles**

A→B→C→A is acceptable if each link adds value.

```bash
# Extract all bidirectional link pairs
# For each file, list what it links to
for f in $(find .agent/rules -name "*.md"); do
  basename="$(basename $f)"
  grep -oE "\[.*\]\([^)]+\.md[^)]*\)" "$f" 2>/dev/null | \
    grep -oE "\([^)]+\)" | tr -d '()' | \
    while read target; do
      echo "$basename -> $(basename $target)"
    done
done | sort
```

**6-2. Review Bidirectional Links**

For each A↔B pair, ask:
- Does A→B make sense from A's context?
- Does B→A make sense from B's context?

If both directions add value, keep them. Otherwise, remove one direction.

---

## Phase 7: Commit

**7-1. Stage Changes**
```bash
git add .agent/rules/ .agent/workflows/
git status --short
```

**7-2. Commit**
```bash
git commit -m "docs(rules): audit and fix cross-links

- Simplified footers to README link only
- Consolidated related links in frontmatter
- Fixed broken links
- Unified path format to workspace-root relative

[16-cross-link-methods] (Maintenance)"
```

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
