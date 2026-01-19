---
ai_visible: true
title: English to Japanese Translation Guidelines
description: Guidelines for translating English documentation to Japanese (EN → JA-HU)
tags: [localization, translation, english, japanese]
version: 1.1.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-19T20:18:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/rules/core/localization/localization.md: Parent rule with common standards
  .agent/rules/core/localization/localization-ja-to-en.md: JA → EN translation (reverse direction)
  .agent/rules/core/markdown/markdown-readability.md: Human document format target
  .agent/cards/localization-card.md: Context card for translation work
---

# English to Japanese Translation Guidelines

## Purpose

Define principles for translating English-language documentation and content into Japanese.
This is primarily used for creating human-readable Japanese versions of AI documentation.

## Core Translation Principles

### Technical Terms

- **Preserve Technical Accuracy**: Keep technical terms (e.g., `commit`, `workflow`, `git`, `markdown`) in Katakana or English for clarity
- **Consistency**: Use consistent terminology across all translated documents
- **Context-Aware**: Choose appropriate translation based on the context and target audience

### Structure Preservation

- **YAML Front-matter**: Preserve all front-matter metadata without translation
- **Headings**: Maintain heading hierarchy and formatting
- **Code Blocks**: Keep code snippets, file paths, and command examples unchanged
- **Links**: Preserve file links and URLs in their original form

## Tone and Style

### Language Register

- **Formal Japanese**: Use polite Japanese (Desu/Masu form) for professional documentation
- **Technical Terms**: Keep technical terms in Katakana or English (e.g., `コミット`, `ワークフロー`, or `commit`, `workflow`)
- **Clarity**: Prioritize clear communication over literal translation
- **Natural Flow**: Ensure translations read naturally in Japanese

### Common Patterns

- API references and code documentation: Keep technical terminology in original English form
- User guides and workflows: Translate to natural Japanese while preserving meaning
- Error messages and warnings: Maintain consistency with existing translated messages
- UI text: Use concise Japanese appropriate for interface constraints

## Quality Assurance

### Accuracy

- Verify translation preserves the original meaning and intent
- Cross-check technical terminology with existing translated documents
- Ensure no sections are accidentally skipped

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

- **Same language, same location**: Keep original filename
- **Different language version**: Add language suffix (e.g., `file.ja.md`)

### Visual Enhancements (Human-Facing)

When creating human-facing Japanese documentation, apply these enhancements:

1. **Section Icons**: Add emojis to major sections
   - 📋 Overview/Purpose sections
   - ⚙️ Configuration/Setup sections
   - ✅ Completion/Success criteria
   - ⚠️ Warnings/Important notes
   - 🔧 Troubleshooting sections

2. **Block Quotes**: Use for important callouts

   ```markdown
   > **Important**: This is a critical note
   ```

3. **Visual Separators**: Add `---` between major sections for clarity

---

## Historical Background

This guideline was created in December 2025 to enable Japanese users to access AI documentation in their native language.

**The Two-Step Process**: Initially, all documentation was created directly in the target format. We discovered that creating an AI-facing English version first, then translating to human-facing Japanese, produced higher quality output and maintained separation of concerns.

**Visual Enhancement Mandate**: Human readers benefit from visual hierarchy (emojis, block quotes, spacing) that would be noise for AI parsing. This guideline formalizes the requirement to add these enhancements when creating human-facing Japanese documentation.

---

## Related Documents

| Document                                                                               | Purpose                           |
| :------------------------------------------------------------------------------------- | :-------------------------------- |
| [`localization-ja-to-en.md`](/.agent/rules/core/localization/localization-ja-to-en.md) | Reverse direction (JA → EN)       |
| [`markdown-readability.md`](/.agent/rules/core/markdown/markdown-readability.md)       | Human document format guidelines  |
| [`localization-card.md`](/.agent/cards/localization-card.md)                           | Context card for translation work |

---

## Origin

- 2025-12-01T00:00 by unknown: Created for EN→JA translation guidelines.
- 2026-01-04T10:41 by Polaris: Added Origin and Navigation (cross-link audit).
- 2026-01-19T20:18 by Polaris: Added 5-layer structure, output specification, historical background (v1.1.0).

---

**Navigation**: [← Back to Rules Index](/.agent/rules/map.md)
