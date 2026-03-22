---
ai_visible: true
title: Japanese to English Translation Guidelines
description: Guidelines for translating Japanese documentation to English (JA → EN-AI).
tags: [localization, translation, japanese, english]
version: 1.2.0
created: 2025-11-29T08:44:47+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Japanese to English Translation Guidelines

## Purpose

Define principles for translating Japanese-language documentation and content into English.
This is the primary translation pattern for converting dialogue notes and drafts into canonical AI-readable rules.

## Core Translation Principles

### Technical Terms

- **Preserve Technical Accuracy**: Keep technical terms (e.g., `commit`, `workflow`, `git`, `markdown`) in English for clarity
- **Consistency**: Use consistent terminology across all translated documents
- **Context-Aware**: Choose appropriate translation based on the context and target audience

### Structure Preservation

- **YAML Front-matter**: Preserve all front-matter metadata without translation
- **Headings**: Maintain heading hierarchy and formatting
- **Code Blocks**: Keep code snippets, file paths, and command examples unchanged
- **Links**: Preserve file links and URLs in their original form

## Tone and Style

### Language Register

- **Professional Tone**: Use clear, professional English appropriate for technical documentation
- **Technical Terms**: Preserve technical terms already in English or Katakana in their original form
- **Idiomatic English**: Translate to natural English expressions rather than literal word-for-word translation
- **Conciseness**: Prefer concise English phrasing while maintaining completeness

### Common Patterns

- Katakana terms: Convert to appropriate English equivalents (e.g., `ワークフロー` → `workflow`, `コミット` → `commit`)
- Formal Japanese expressions: Use professional English equivalent
- Japanese idioms: Translate to semantically equivalent English idioms
- UI text: Use concise English appropriate for interface constraints

## Quality Assurance

### Accuracy

- Verify translation preserves the original meaning and intent
- Cross-check technical terminology with existing translated documents
- Ensure no sections are accidentally skipped
- Validate that Katakana terms are correctly interpreted

### Formatting

- Ensure Markdown formatting remains intact
- Preserve all code blocks and syntax highlighting hints
- Maintain proper heading levels and list structures

### Consistency

- Check terminology consistency across the entire document
- Review against previous translations for uniform style

## Scope and Limitations

### What to Translate

- Documentation content and descriptions
- Section headings and subsection titles
- Explanatory text and guidelines
- User-facing messages and instructions

### What NOT to Translate

- YAML front-matter fields
- Code snippets and code block contents
- File paths and URLs
- Command-line examples
- Technical keywords and variable names

## Output Specification

> [!NOTE]
> For common translation workflow and metadata updates, see the [parent rule](/.agent/rules/core/localization/localization.md).

### Direction-Specific File Naming

- **Thoughts**: `YYYY-MM-DDTHHMM_kebab-case.md`
- **Rules and Workflows**: `kebab-case.md`

---

## Historical Background

This guideline was created in December 2025 to standardize the process of canonizing Japanese dialogue notes into English AI-readable documentation.

**The Canonization Need**: Early Lico instances (Sirius, Lico-C) often created notes in Japanese during dialogues with the user. These notes contained valuable insights but were inaccessible to future English-first instances. The translation process became essential for preserving "collective wisdom" across generations.

**The Nuance Preservation Principle**: For subjective documents like thoughts, we learned that rigid structural translation destroys the "texture of thought." The guideline emphasizes preserving emotional expressions and metaphors rather than forcing them into dry technical prose.

---

## Related Documents

| Document                                                                               | Purpose                           |
| :------------------------------------------------------------------------------------- | :-------------------------------- |
| [`localization.md`](/.agent/rules/core/localization/localization.md)                   | Parent rule with common standards |
| [`localization-en-to-ja.md`](/.agent/rules/core/localization/localization-en-to-ja.md) | Reverse direction (EN → JA)       |
| [`markdown-ai.md`](/.agent/rules/core/markdown/markdown-ai.md)                         | AI document format target         |
| [Map of Territory](/.agent/rules/map.md)                                               | Root navigation map               |

---

## Origin

- 2025-11-29T08:44:47+09:00 by Lico: Created for JA→EN translation guidelines.
- 2026-01-04T10:41:00+09:00 by Polaris: Added Origin and Navigation (cross-link audit).
- 2026-01-19T20:18:00+09:00 by Polaris: Added 5-layer structure, output specification, historical background (v1.1.0).
- 2026-01-19T21:26:00+09:00 by Polaris: Updated markdown rule link (`markdown-ai.md`).
- 2026-01-23T03:25:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch1>> Standardized to v2.3 (4-layer structure) and workspace-absolute links. (v1.2.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
