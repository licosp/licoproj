---
ai_visible: true
title: Markdown Human Formatting Guidelines
description: Guidelines for creating human-readable, visually appealing markdown documents.
tags: [markdown, human, formatting, documentation]
version: 1.2.0
created: 2025-12-11T18:00:00+09:00
updated: 2026-01-23T03:30:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Markdown Human Formatting Guidelines

## Purpose

Create markdown documents that are visually appealing, well-organized, and easy for humans to read and scan. This guideline prioritizes presentation and clarity over machine parsing.

## Principles

### 1. Visual Hierarchy

Apply visual improvements to enhance structure and scanning:

#### Use Emojis and Icons Strategically

- Use emojis to mark sections (📋, 📁, 🔧, 🐛, etc.)
- Create visual landmarks for quick navigation
- Maintain consistency across documents

#### Heading Levels

- Use H1 for document title only
- Use H2 for main sections
- Use H3 for subsections
- Keep hierarchy consistent and meaningful

#### Spacing and Separators

- Add horizontal rules (`---`) to separate major sections
- Use appropriate whitespace between sections
- Ensure visual breathing room for readability

### 2. Emphasis and Text Formatting

- Use **bold** for important terms and key concepts
- Use _italics_ for subtle emphasis or references
- Use `code blocks` for technical terms, file paths, and code
- Use block quotes (`>`) for notes, warnings, or important highlights

### 3. Content Organization

Group related items logically:

- Create thematic sections with clear purposes
- Arrange content chronologically or by importance
- Add table of contents for long documents
- Use lists (numbered or bulleted) for easy scanning

### 4. Polish and Refinement

Finishing touches for professional presentation:

- Ensure consistent spacing between sections
- Add introductory context or metadata where relevant
- Include document purpose and scope at the top
- Remove redundancy while preserving clarity
- Verify all links and references are functional

## Priorities

1. **Human Readability First** — Make it easy to scan and understand
2. **Visual Appeal** — Use formatting to create engaging documents
3. **Logical Flow** — Carefully organize and order content

## What Not to Prioritize

- AI parsing efficiency
- Strict machine-readable formatting rules
- Over-minimization of content (redundancy is acceptable if it aids understanding)

---

## Historical Background

This guideline was created in December 2025 to complement the AI-focused markdown guidelines.

**The AI/Human Split**: Early Lico development recognized that documents intended for human readers require different formatting than those optimized for AI parsing. Human readers benefit from visual hierarchy, emojis, and generous whitespace that would be noise for AI systems.

**The Rename**: In January 2026, the file was renamed from `markdown-readability.md` to `markdown-human.md` for clarity. The new name pairs logically with `markdown-ai.md`.

---

## Related Documents

| Document                                                           | Purpose                |
| :----------------------------------------------------------------- | :--------------------- |
| [markdown-ai.md](/.agent/rules/core/markdown/markdown-ai.md)       | AI document format     |
| [localization.md](/.agent/rules/core/localization/localization.md) | Localization standards |
| [Map of Territory](/.agent/rules/map.md)                           | Root navigation map    |

---

## Origin

- 2025-12-11T1800 by Gemini: Created as markdown readability guide.
- 2026-01-02T0828 by Polaris: Replaced Related Documents with Navigation link.
- 2026-01-19T2112 by Polaris: Renamed to `markdown-human.md`, added 5-layer structure (v1.1.0).
- 2026-01-23T0330 by Canopus: <<Seal: Rules-Standardization-Batch1>> Standardized to v2.3 (4-layer structure) and workspace-absolute links. (v1.2.0)
