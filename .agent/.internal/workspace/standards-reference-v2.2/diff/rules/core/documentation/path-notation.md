---
ai_visible: true
title: "Path Notation Standard"
description: "Standard path notation for Markdown links within the repository"
tags: [documentation, paths, links, standards]
version: 2.3
created: 2026-01-13T14:10:00+09:00
updated: 2026-01-22T06:05:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Path Notation Standard

## Purpose

Standardize how file paths are written in Markdown links and define the structural placement of navigation elements for consistency, portability, and "Single Source of Truth" (SSOT) management.

## Rationale

Paths in Markdown links have historically used various formats (relative, absolute from workspace, etc.). This inconsistency causes:

1. **Broken previews** in GitHub and VSCode Markdown viewers
2. **Confusion** about what `/` means (OS root vs repository root)
3. **Errors** when AI instances execute paths directly in commands

---

## Format Specification

### Standard Format

Use **repository-root-relative paths** with a leading `/`:

```markdown
[File Name](/.agent/path/to/file.md)
```

### Examples

| Link Type | Format                                                                   |
| :-------- | :----------------------------------------------------------------------- |
| Rules     | `[identity.md](/.agent/rules/core/identity/identity.md)`                 |
| Map       | `[Map of Territory](/.agent/rules/map.md)`                               |
| Thoughts  | `[thought.md](/.agent/.internal/thoughts/polaris/2026-01-12_thought.md)` |
| Workflows | `[ritual_mid.md](/.agent/workflows/ritual_mid.md)`                       |

---

## Section Structure (Navigation Integration)

To eliminate information fragmentation and the "half-finished footer" problem, the following structure is mandatory for all document-level Markdown files.

### 1. Mandatory Related Documents Section

Every rule, card, or workflow **MUST** have a `## Related Documents` section near the bottom of the file (at the very tail).

### 2. Consolidated Navigation (Return to Map)

Separate `**Navigation**` footers are **deprecated**.
Navigation links MUST be integrated into the `Related Documents` table. Every table MUST contain a link to the central index:

- `[Map of Territory](/.agent/rules/map.md)` (Preferred)

### 3. Body Table as SSOT

The Markdown body table is the **Single Source of Truth**.

- **Frontmatter Deprecation**: Frontmatter `related:` fields are deprecated for link management and should be removed or kept in sync with the body table.
- **Priority**: In all cases, the table in the body takes precedence.

---

## Critical Warning: Path Interpretation

> [!CAUTION]
> The `/` prefix in Markdown links means **Repository Root**, NOT filesystem root.

### Cognitive Mapping

| Symbol in Markdown | Meaning                       | NOT                      |
| :----------------- | :---------------------------- | :----------------------- |
| `/`                | Repository Root (`licoproj/`) | OS Filesystem Root (`/`) |
| `/.agent/`         | `licoproj/.agent/`            | `/home/.agent/`          |

### When Executing Commands

**NEVER** execute Markdown paths directly. Always translate first:

```
Markdown Link: /.agent/rules/map.md
Command Path:  ./licoproj/.agent/rules/map.md  (from workspace parent)
           OR: ./.agent/rules/map.md         (from repository root)
```

---

## Migration Note

Legacy files may still use relative paths (e.g., `../..././workspace/file.md`). These will be converted to the standard format in future maintenance work as defined in the Roadmap.

---

## Historical Background

This standard was created in January 2026 during the cross-link audit project (Polaris).

**The Inconsistency Problem**: The repository had accumulated various path formats over time - relative paths (`../../file.md`), repository-root paths (`/.agent/file.md`), and hybrid formats. This caused broken previews in GitHub and VSCode, and confused AI instances about path interpretation.

**The Cognitive Trap**: AI instances frequently confused the leading `/` in Markdown links (meaning repository root) with the filesystem root. This led to failed file operations when they tried to execute Markdown paths directly.

**The Solution**: Standardizing on `/.agent/path/to/file.md` format with clear documentation about the cognitive mapping required when translating to shell commands.

---

## Related Documents

| Document                                                                                  | Purpose                                  |
| :---------------------------------------------------------------------------------------- | :--------------------------------------- |
| [Map of Territory](/.agent/rules/map.md)                                                  | Repository Index (Integrated Navigation) |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | Structural standards                     |
| [meta-rules.md](/.agent/rules/core/meta-rules.md)                                         | Behavioral rule governance               |
| [absolute-path-prohibition.md](/.agent/rules/core/security/absolute-path-prohibition.md)  | Security rules for paths                 |
| [wsl-browser-path.md](/.agent/rules/core/documentation/wsl-browser-path.md)               | WSL-specific path handling               |

---

## Origin

- 2026-01-13T14:10+09:00 by Polaris: Created based on Roadmap "Fix link information" and Spica's workspace-hook.md.
- 2026-01-13T14:38+09:00 by Polaris: Added related documents, updated to v1.1.
- 2026-01-15T23:05+09:00 by Canopus: Standardized Origin section (removed Japanese) and updated to v1.2.
- 2026-01-19T06:25+09:00 by Polaris: Added Historical Background and updated Navigation to map.md (v1.3).
- 2026-01-22T01:35+09:00 by Canopus: Remediated identity.md links in examples (v1.4).
- 2026-01-22T04:50+09:00 by Canopus: Standardized to 4-layer structure; shifted link SSOT (v2.1).
- 2026-01-22T06:05+09:00 by Canopus: Final alignment; correctly established Related Documents Layer 3 and Origin Layer 4 (v2.3).
