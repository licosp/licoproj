---
description: Translate files between English and Japanese
---

# Localize Workflow

## Purpose
Translate documentation files (`.md`) between English and Japanese, following the standards defined in `.agent/rules/core/localization.md`.

## Translation Directions

### English to Japanese (EN → JA)

**Source**: `.agent/rules/**/*.md` and `.agent/workflows/*.md`  
**Destination**: `.agent/locales/ja/` (preserving directory structure)

#### Steps
1. **Create Directories**
   ```bash
   mkdir -p .agent/locales/ja/rules
   mkdir -p .agent/locales/ja/workflows
   ```

2. **Translate & Save**
   - **Rules**: `.agent/rules/**/*.md` → `.agent/locales/ja/rules/**/*.md`
   - **Workflows**: `.agent/workflows/*.md` → `.agent/locales/ja/workflows/*.md`

3. **Verify & Commit**
   - Check translation accuracy and Markdown formatting
   - Commit and push changes

---

### Japanese to English (JA → EN)

**Source**: `.agent/locales/ja/`  
**Destination**: `.agent/rules/**/*.md` and `.agent/workflows/*.md`

> [!WARNING]
> This overwrites existing English files. Commit changes before running.

#### Steps
1. **Translate & Overwrite**
   - **Rules**: `.agent/locales/ja/rules/**/*.md` → `.agent/rules/**/*.md`
   - **Workflows**: `.agent/locales/ja/workflows/*.md` → `.agent/workflows/*.md`

2. **Verify & Commit**
   - Ensure accurate translation and correct formatting
   - Commit and push changes

## Guidelines
Refer to `.agent/rules/core/localization.md` for detailed translation standards.
