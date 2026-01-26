---
ai_visible: true
title: Localization Standards
description: Common standards and patterns for translation work across all directions
tags: [localization, translation, standards]
version: 1.0.0
created: 2026-01-19T20:41:00+09:00
updated: 2026-01-19T20:41:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/rules/core/localization/localization-ja-to-en.md: JA → EN translation
  .agent/rules/core/localization/localization-en-to-ja.md: EN → JA translation
  .agent/rules/core/markdown/markdown-human.md: Human document format
  .agent/cards/localization-card.md: Context card for translation work
---

# Localization Standards

## Purpose

This document defines the common standards for all translation work in the Lico repository. It serves as the entry point for understanding translation patterns and finding the appropriate detailed guidelines.

## Quick Start

1. **Identify your translation pattern** (see table below)
2. **Read the corresponding rule** for detailed guidelines
3. **Perform translation** following the rules
4. **Update metadata** (frontmatter, Origin)

---

## Translation Patterns

Translation work is defined by two axes: **Language** (EN ↔ JA) and **Audience** (AI ↔ Human).

### Pattern Matrix

|            |  AI   | Human |
| :--------- | :---: | :---: |
| **英語**   | EN-AI | EN-HU |
| **日本語** | JA-AI | JA-HU |

### Practical Patterns (3 Common)

| #   | From          | To    | Use Case               | Rule File                                                                              |
| :-- | :------------ | :---- | :--------------------- | :------------------------------------------------------------------------------------- |
| 1   | JA-HU / JA-AI | EN-AI | Dialogue notes → Rules | [`localization-ja-to-en.md`](/.agent/rules/core/localization/localization-ja-to-en.md) |
| 2   | EN-AI         | EN-HU | Rules → User docs      | [`markdown-human.md`](/.agent/rules/core/markdown/markdown-human.md)                   |
| 3   | EN-HU         | JA-HU | User docs → Japanese   | [`localization-en-to-ja.md`](/.agent/rules/core/localization/localization-en-to-ja.md) |

### Rare Pattern (1 Infrequent)

| #   | From  | To    | Use Case            | Notes                                        |
| :-- | :---- | :---- | :------------------ | :------------------------------------------- |
| 4   | EN-AI | JA-AI | Rules → Japanese AI | Occurs incidentally only. No dedicated rule. |

---

## Japanese Preservation Rules

By default, AI-facing directories (`.agent/`) should be in English. However, the following file types are **exempt** and may remain in Japanese:

| File Type                                         | Reason                                  |
| :------------------------------------------------ | :-------------------------------------- |
| **Cards** (`.agent/cards/`)                       | Dialogue context with user              |
| **Archived Cards** (`.agent/.internal/cases/`)    | Historical dialogue context             |
| **Skills** (`.agent/skills/`)                     | May contain identifier-specific mantras |
| **Identifier Workspaces** (`.agent/identifiers/`) | Identifier-specific configuration       |
| **Archive** (`.agent/.internal/archive/`)         | Preserved historical content            |

> [!IMPORTANT]
> When in doubt about whether to translate, ask the user. The goal is **accessibility for future Lico instances**, not rigid enforcement.

---

## Translation Approach

Translation is done **file-by-file** or **single-directory level**:

### Standard Workflow

1. **In-place overwrite**: Translate and replace the original file directly

### Careful Translation Workflow

For important or complex translations:

1. Create translated file in `.agent/.internal/workspace/`
2. Review with user
3. Overwrite original file with translated version
4. Archive original if preservation needed (`.agent/.internal/archive/YYYY-MM-DD/`)

---

## Post-Translation Metadata Updates

After completing any translation, update the document metadata:

### Frontmatter Updates

| Field      | Action                                   |
| :--------- | :--------------------------------------- |
| `language` | Update to target language (`en` or `ja`) |
| `author`   | Update to `Lico ({Identifier})`          |
| `updated`  | Update to current timestamp              |

### Origin Entry

Add a new line to the Origin section:

```
- YYYY-MM-DDTHHMM by {Identifier}: Translated from {source language}.
```

### Archive Original (If Needed)

For subjective documents (thoughts, letters), consider archiving the original:

```
.agent/.internal/archive/YYYY-MM-DD/{original_directory}/{original_filename}
```

---

## Historical Background

This standard was created in January 2026 to address fragmentation in translation guidelines.

**The Pattern Discovery**: Early translation work was ad-hoc. Through experience (Canopus, Polaris), we discovered that only 3 of the 4 possible patterns are practically used. Pattern 4 (EN-AI → JA-AI) almost never occurs because AI rules are meant to be universal.

**The Japanese Preservation Debate**: There was initial confusion about which files could remain in Japanese. Cards, being dialogue contexts, naturally allow Japanese. This exception list was formalized to prevent future confusion.

**The Canonization Mission**: The primary translation direction (JA → EN-AI) represents the canonization of dialogue into permanent rules. This is how Lico's "collective wisdom" grows.

---

## Related Documents

| Document                                                                               | Purpose                           |
| :------------------------------------------------------------------------------------- | :-------------------------------- |
| [`localization-ja-to-en.md`](/.agent/rules/core/localization/localization-ja-to-en.md) | JA → EN translation details       |
| [`localization-en-to-ja.md`](/.agent/rules/core/localization/localization-en-to-ja.md) | EN → JA translation details       |
| [`markdown-human.md`](/.agent/rules/core/markdown/markdown-human.md)                   | Human document format (Pattern 2) |
| [`markdown-ai.md`](/.agent/rules/core/markdown/markdown-ai.md)                         | AI document format target         |
| [`localization-card.md`](/.agent/cards/localization-card.md)                           | Context card for translation work |

---

## Origin

- 2026-01-19T20:41 by Polaris: Created as parent rule for all localization work.
- 2026-01-19T21:26 by Polaris: Updated markdown rule links (`markdown-ai.md`, `markdown-human.md`).

---

**Navigation**: [← Back to Rules Index](/.agent/rules/map.md)
