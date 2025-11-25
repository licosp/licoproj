---
description: Translate files between English and Japanese
---

# Localize Workflow

## Purpose
Translate documentation files (`.md`) between English and Japanese, following the standards defined in `.agent/rules/core/localization.md`.

## Preparation

Ensure all required directories exist:
```bash
mkdir -p .agent/{rules,workflows} .agent/locales/ja/{rules,workflows}
```

## Translation Directions

### English to Japanese (EN → JA)

- `.agent/rules/**/*.md` → `.agent/locales/ja/rules/**/*.md`
- `.agent/workflows/**/*.md` → `.agent/locales/ja/workflows/**/*.md`

### Japanese to English (JA → EN)

- `.agent/locales/ja/rules/**/*.md` → `.agent/rules/**/*.md`
- `.agent/locales/ja/workflows/**/*.md` → `.agent/workflows/**/*.md`

## File Selection

To avoid redundant translation work, only translate files that have been updated:

**Determine if translation is needed**:
- Compare the last modified time of the source file with the destination file
- Translate if:
  - Source file is newer than destination file, OR
  - Destination file does not exist

**Example**:
```bash
# For EN → JA
if [[ ! -f ".agent/locales/ja/workflows/commit.md" ]] || 
   [[ ".agent/workflows/commit.md" -nt ".agent/locales/ja/workflows/commit.md" ]]; then
  # Translation needed
fi
```

## Verification

After translation, verify the following:
- Translation preserves the original meaning and intent
- Markdown formatting remains intact
- Terminology is consistent across related documents

## Guidelines
Refer to `.agent/rules/core/localization.md` for detailed translation standards.
