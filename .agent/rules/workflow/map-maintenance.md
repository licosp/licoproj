---
title: Map Maintenance Standards
description: Standards for maintaining the territory map (.agent/rules/map.md)
tags: [rules, workflow, map, maintenance, documentation]
version: 1.0.0
created: 2026-01-19T05:55:00+09:00
updated: 2026-01-19T05:55:00+09:00
language: en
author: Lico (Polaris)
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
   - ✅ `[`activity-log.md`](/.agent/.internal/activity-log.md)`
   - ❌ `[`.agent/.internal/activity-log.md`](/.agent/.internal/activity-log.md)`

3. **Ordering**: Use **hierarchical order** (parent → children, alphabetical within level)
   - Parent directories first
   - Children indented conceptually (by table position)
   - Alphabetical within the same level

4. **Bold paths**: Use bold for **core directories** only
   - `.agent/`, `.internal/`, `cards/`, `rules/`, `workflows/`, `.human/`

### Purpose Column

1. **Emphasis**: Use bold for **key concepts** only, not for every entry
   - ✅ Core directories, critical files, important principles
   - ❌ Every single entry (becomes meaningless)

2. **Descriptions**: Keep concise, avoid redundancy with path name
   - ✅ `Collective wisdom archive.`
   - ❌ `**Legacy**. Legacy archive.` (redundant)

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

## Related Files

| File | Purpose |
|:-----|:--------|
| [`.agent/rules/map.md`](/.agent/rules/map.md) | The territory map itself |
| [`map-sync-card.md`](/.agent/cards/routine/map-sync-card.md) | Context card for map updates |

## Origin

- 2026-01-19 by Polaris: Created based on session with User establishing formatting standards.
