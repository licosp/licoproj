---
trigger: localization:translate-ja-to-en
description: Guidelines for translating Japanese documentation to English
---

# Japanese to English Translation Guidelines

## Purpose
Define principles for translating Japanese-language documentation and content into English.

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
- Validate consistency with `.human/locales/en/` or root-level English files

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

## Additional Notes

### Character Encoding
Ensure proper handling of Japanese characters (UTF-8) and special punctuation marks.

### Contextual Considerations
When direct translation would be unclear, provide English equivalents or explanations. Maintain technical precision while adapting to English conventions.
