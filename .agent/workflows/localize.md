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

**Source**: `.agent/rules/**/*.md` and `.agent/workflows/*.md`  
**Destination**: `.agent/locales/ja/` (preserving directory structure)

---

### Japanese to English (JA → EN)

**Source**: `.agent/locales/ja/`  
**Destination**: `.agent/rules/**/*.md` and `.agent/workflows/*.md`

## Verification

After translation, verify the following:
- Translation preserves the original meaning and intent
- Markdown formatting remains intact
- Terminology is consistent across related documents

## Guidelines
Refer to `.agent/rules/core/localization.md` for detailed translation standards.
