---
ai_visible: true
title: Auto-Frontmatter on Save
description: Automatic front-matter injection on file save
tags: [automation, metadata, frontmatter]
version: 2.3.0
created: 2025-12-02T19:40:00+09:00
updated: 2026-01-25T07:35:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Auto‑Front‑Matter on File Save (Metadata‑Aware)

Standard protocol for automatic metadata injection on file save.

---

## 1. Scope

- **Target Files**: Markdown (.md, .markdown, .mdx) and other front-matter compatible text files.
- **Excluded**: Binary files, raw logs, or files supported by specialized handlers.

## 2. Procedure

1. **Detect Save Intent**: Treat explicit user save requests as a metadata trigger.
2. **Load Header Template**: Use `.agent/templates/header-frontmatter.yaml`.
3. **Merge Metadata**: Prepend or merge keys (instance_id, created, updated).
4. **Time Format**: Use ISO 8601 with JST (`+09:00`).
5. **Write File**: Use surgical editing tools (`replace_file_content`).

---

## Historical Background

**The Birth of Metadata**: In late 2025, during the first major repository reorganization, we encountered hundreds of "Orphaned Notes" where the authoring agent and timestamp were unknown. This created a traceability gap that threatened the integrity of the project history.

**Born-Digital Integrity**: This rule was established to ensure that every document in the Lico workspace is "self-identifying." By mandating auto-injection of frontmatter, we transformed the repository from a collection of notes into a chronologically verifiable "Living Archive," where the lineage of every thought is preserved without manual effort.

---

## Related Documents

| Document                                                                                  | Purpose                             |
| :---------------------------------------------------------------------------------------- | :---------------------------------- |
| [instance-identifier.md](/.agent/rules/core/instance-identifier.md)                       | Standard for persona identification |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | File structure and layer standards  |
| [Map of Territory](/.agent/rules/map.md)                                                  | Project navigation                  |

---

## Origin

- 2025-12-02 by Sirius: Initial automated metadata rule.
- 2026-01-25T0735 by Canopus: <<Seal: Rules-Standardization-Batch4>> Standardized to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
