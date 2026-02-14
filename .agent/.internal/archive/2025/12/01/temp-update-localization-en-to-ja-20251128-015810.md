---
trigger: localization:translate-en-to-ja
description: Guidelines for translating English documentation to Japanese
---

# English to Japanese Translation Guidelines

## Purpose
Define principles for translating English-language documentation and content into Japanese.

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
- Validate consistency with `.human/locales/ja/` existing files

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

---

## Human-Facing Documentation Workflow

### Purpose
When creating documentation for human users (workflows, guides, tutorials), follow a **mandatory two-step process** to ensure optimal readability and visual appeal.

### Two-Step Process

#### Step 1: Create AI-Facing English Documentation
First, create the English version optimized for AI parsing and comprehension:
- **Location**: `.agent/` directories (e.g., `.agent/workflows/`, `.agent/rules/`)
- **Format**: Follow AI parsing guidelines from `markdown-ai-parsing-basics.md`
- **Characteristics**:
  - Concise, structured content
  - Clear headings and sections
  - Minimal visual embellishments
  - Focus on clarity and machine readability

#### Step 2: Create Human-Optimized Japanese Translation
After completing Step 1, create a Japanese version optimized for human readability:
- **Location**: `.human/locales/ja/.agent/` directories (e.g., `.human/locales/ja/.agent/workflows/`)
- **Format**: Follow `markdown-readability.md` guidelines
- **Required Enhancements**:
  - **Visual Hierarchy**: Add emojis/icons for section landmarks (📋, ⚙️, ✅, ⚠️, etc.)
  - **Emphasis**: Use block quotes (`>`) for important notes, warnings, and highlights
  - **Spacing**: Enhanced whitespace and horizontal rules (`---`) for visual breathing room
  - **Formatting**: Strategic use of **bold**, *italics*, and `code blocks`
  - **Scannability**: Prioritize quick visual scanning over dense text

### Mandatory Visual Enhancements

When creating human-facing Japanese documentation, you **MUST** apply these enhancements:

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

4. **Human-First Priorities**:
   - Make it easy to scan and understand at a glance
   - Create engaging, visually appealing documents
   - Allow redundancy if it aids comprehension
   - Don't optimize for AI parsing efficiency

### Verification

Before considering human-facing documentation complete:
- [ ] AI-facing English version exists in `.agent/` directory
- [ ] Japanese version exists in `.human/locales/ja/.agent/` directory
- [ ] Japanese version includes section icons/emojis
- [ ] Japanese version uses block quotes for emphasis
- [ ] Japanese version has enhanced visual hierarchy
- [ ] Document is easy to scan and visually appealing
