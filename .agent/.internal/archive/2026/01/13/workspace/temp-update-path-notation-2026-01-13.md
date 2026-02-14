---
ai_visible: true
title: "Path Notation Standard"
description: "Standard path notation for Markdown links within the repository"
tags: [documentation, paths, links, standards]
version: 1.0
created: 2026-01-13T14:10:00+09:00
updated: 2026-01-13T14:10:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
---

# Path Notation Standard

## Purpose

Standardize how file paths are written in Markdown links for consistency, portability, and preview compatibility.

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
| Rules     | `[identity.md](/.agent/rules/core/identity.md)`                          |
| Thoughts  | `[thought.md](/.agent/.internal/thoughts/polaris/2026-01-12_thought.md)` |
| Workflows | `[ritual_mid.md](/.agent/workflows/ritual_mid.md)`                       |

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
Markdown Link: /.agent/rules/README.md
Command Path:  ./licoproj/.agent/rules/README.md  (from workspace parent)
           OR: ./.agent/rules/README.md         (from repository root)
```

---

## Migration Note

Legacy files may still use relative paths (e.g., `../../../workspace/file.md`). These will be converted to the standard format in future maintenance work as defined in the Roadmap.

---

## Origin

- 2026-01-13T1410 by Polaris: Created based on Roadmap "リンク情報を修正する" and Spica's workspace-hook.md.

---

**Navigation**: [← Back to Rules Index](/.agent/rules/README.md)
