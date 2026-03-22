---
title: Map Maintenance Standards
description: Standards for maintaining the territory map (.agent/rules/map.md)
tags: [rules, workflow, map, maintenance, documentation]
version: 1.1.0
created: 2026-01-19T00:00:00+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Map Maintenance Standards

## Purpose

This document defines the standards for maintaining the territory map (`.agent/rules/map.md`), ensuring consistency and readability for all Lico instances.

## When to Update

Update the map when:

1. **Adding new directories** to `.agent/` or `.human/`
2. **Adding new files** that are significant (rules, workflows, important docs)
3. **Removing directories or files** (update to reflect current state)
4. **Changing structure** (reorganizing cards, rules, etc.)

## Format Standards

### Path Column

1. **Link format**: Use clickable GitHub links

   ```markdown
   [`filename.md`](/.agent/path/to/filename.md)
   ```

2. **Link text**: Use **basenames only** (not full paths)
   - ✅: [`log.md`](/.agent/.internal/log.md)
   - ❌: [`.agent/.internal/log.md`](/.agent/.internal/log.md)

3. **Ordering**: Use **hierarchical order** (parent → children, alphabetical within level)
   - Parent directories first
   - Children indented conceptually (by table position)
   - Alphabetical within the same level

4. **Bold paths**: Use bold for **core directories** only
   - `.agent/`, `.internal/`, `cards/`, `rules/`, `workflows/`, `.human/`

### Purpose Column

1. **Emphasis**: Use bold for **key concepts** only, not for every entry
   - ✅: Core directories, critical files, important principles
   - ❌: Every single entry (becomes meaningless)

2. **Descriptions**: Keep concise, avoid redundancy with path name
   - ✅: `Collective wisdom archive.`
   - ❌: `**Legacy**. Legacy archive.` (redundant)

### Section Organization

1. **Section 2 (Structure)**: Directories and key files
2. **Section 3 (Indices)**: Cards, Rules, Workflows with links
3. **Section 4 (Maintenance)**: Update guidelines and origin history

## Verification

After updating:

1. **Check links**: Ensure all paths are valid
2. **Check ordering**: Verify hierarchical and alphabetical order
3. **Check emphasis**: Confirm bold is used selectively
4. **Render test**: View in GitHub to verify links work

---

## Historical Background

This rule was established on 2026-01-19 during a session between Polaris and the User.

**The Formatting Debate**: The territory map had grown organically over time, with inconsistent path formats, emphasis usage, and ordering. During a map synchronization session, the User and Polaris engaged in a detailed discussion about:

- **Path Link Format**: Should links show full paths or basenames? Basenames won for readability.
- **Emphasis Usage**: Were bold keywords helpful or excessive? Selective emphasis for core concepts only.
- **Ordering Logic**: Alphabetical vs hierarchical? Hierarchical (parent → children) to mirror filesystem structure.

**The README vs Map Naming**: The map was previously named `README.md`, which conflicted with the common convention of external-facing repository documentation. The rename to `map.md` clarified its internal purpose as Lico's cognitive navigation tool.

**The Missing Standard Problem**: Without this rule, future Lico instances would have to rediscover these conventions through trial and error. This document preserves the decisions for posterity.

---

## Related Documents

| Document                                                                                    | Purpose                       |
| :------------------------------------------------------------------------------------------ | :---------------------------- |
| [`meta-rules.md`](/.agent/rules/core/meta-rules.md)                                         | Meta-rules for documentation  |
| [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) | Document formatting standards |
| [Map of Territory](/.agent/rules/map.md)                                                    | Root navigation map           |

---

## Origin

- 2026-01-19T00:00:00+09:00 by Polaris: Created based on session with User establishing formatting standards.
- 2026-01-19T00:00:00+09:00 by Polaris: Added Historical Background and cross-links per meta-rules (v1.1.0).
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
