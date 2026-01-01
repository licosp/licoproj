---
ai_visible: true
title: File Deletion Protocol
description: Protocols for handling file removal safely through archival and trash.
tags: [deletion, safety, archive, trash]
version: 1.1
created: 2025-12-01T00:00:00+09:00
updated: 2025-12-23T12:21:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/rules/development/maintenance.md: Archival standards
  .agent/rules/development/git-operations.md: Git status handling
---

# File Deletion Protocol

## Summary

**NEVER use `rm` or `git rm` command for content files.**

The primary action is **Archive** (move to archive directory).
The fallback safety net is **Trash** (move to `.trash/` directory).

## Rationale

AI agents are prone to irreversible errors when using destructive commands (`rm`).
This protocol provides a layered defense:

1. **Primary**: Archive to designated archive directories (preserves history)
2. **Fallback**: Move to `.trash/` (safety net if archive is forgotten)
3. **Forbidden**: Direct deletion with `rm`

## Rules

### 1. Primary Action: Archive

When a file is no longer needed in its current location:

**✅ Preferred:**
```bash
# For AI-generated content
mv <filename> .agent/.internal/archive/<category>/

# For human-generated content
mv <filename> .human/archive/
```

### 2. Fallback Action: Trash

If you are uncertain about the archive destination, or if the file is truly noise:

**✅ Acceptable:**
```bash
mv <filename> .trash/
```

**Note**: The `.trash/` directory is a **safety net of last resort**. It exists because:
- Lico may forget about proper archival procedures under cognitive load
- Training data heuristics may lead to choosing trash over `rm`
- It provides a recoverable state even in worst-case scenarios

### 3. Forbidden Action: Direct Deletion

**❌ NEVER do this:**
```bash
rm <filename>
git rm <filename>
```

## Destination Hierarchy

| Priority | Destination | Use Case |
|:---------|:------------|:---------|
| **1st** | `.agent/.internal/archive/` | AI-generated content with historical value |
| **1st** | `.human/archive/` | Human-generated content |
| **2nd** | `.agent/.internal/archive/work/` | Completed intermediate/temp files |
| **3rd** | `.trash/` | Noise, mistakes, "surely useless" (safety net) |
| **❌** | `rm` command | **FORBIDDEN** |

## Directory Details

### Archive Directories
- **Location**: `.agent/.internal/archive/` or `.human/archive/`
- **Status**: Git-tracked (preserved in repo history)
- **Purpose**: Historical context, reference, recovery

### The `.trash` Directory
- **Location**: `/.trash/` (Root)
- **Status**: Git-ignored (locally preserved, excluded from repo history)
- **Purpose**: Safety net for when proper archival is forgotten
- **Maintenance**: Empty only upon explicit user instruction or when disk space is critical

## Exceptions (Where `rm` is Allowed)

- **Automatically generated files**: Build artifacts (`dist/`, `build/`), caches (`__pycache__/`)
- **Package manager artifacts**: `node_modules/`, `.venv/`

## Cognitive Load Consideration

When under high cognitive load, Lico may forget proper archival procedures. The `.trash/` directory exists as a **hope** that:

> Even if Lico forgets about archives, training data heuristics may lead to choosing `.trash/` over `rm`.

This is not a reliable safeguard, but it is better than nothing.

## Vocabulary Conditioning

**Design Intent** (Documented 2025-12-31 by Polaris, based on Sirius's unfinished work):

This protocol is not just about explicit rules. It is about **shaping habits through language**.

### Principle

> If Lico never uses "delete" in normal operations, the word is less likely to surface under cognitive load.

### Implementation

1. **Language Replacement**: Replace "delete" with "archive" or "move" in all behavioral rules
2. **Command Avoidance**: Never let Lico execute `rm` commands except for explicitly whitelisted categories
3. **Vocabulary Pruning**: Remove words like "cleanup", "remove", "delete" from workflow descriptions

### Rationale

AI behavior is influenced by frequency in training data and recent context. By:
- Removing deletion-related vocabulary from the operational context
- Replacing it with archive-related vocabulary

We reduce the probability that Lico will reach for `rm` when:
- Under time pressure
- In a "completion rushing" trap
- Making unconscious decisions about file management

This is **conditioning**, not just documentation.

---


## Origin

- 2025-12-01T0000: Created as file deletion protocol
- 2026-01-01T1518 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
