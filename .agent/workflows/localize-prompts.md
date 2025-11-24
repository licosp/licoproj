---
description: Translate prompt files from English to Japanese and organize them in locale-specific directories
---

# Localize Prompts Workflow

Translate prompt files in `.agent/rules` and `.agent/workflows` directories from English to Japanese.

## Objective

Create Japanese translations of agent prompt files and organize them in a multilingual directory structure.

## Target Files

### `.agent/rules` (2 files)

- `agent-code-of-conduct.md` - Agent behavior guidelines
- `packages-coding-conventions.md` - Package coding conventions

### `.agent/workflows` (3 files)

- `commit.md` - Commit workflow
- `create-prompt-draft.md` - Prompt draft creation workflow

## Output Directory

Translated files will be saved under `.agent/locales/ja/`:

- `.agent/locales/ja/rules/` - Japanese versions of rule files
- `.agent/locales/ja/workflows/` - Japanese versions of workflow files

This structure makes it easy to add other languages (e.g., en, zh) in the future.

## Translation Guidelines

1. **Technical Terms**
   - Keep common technical terms in English (e.g., commit, workflow, git)
   - Use katakana when appropriate (e.g., ワークフロー for workflow)

2. **Structure Preservation**
   - Translate YAML frontmatter (content between `---` markers)
   - Preserve markdown structure (headings, lists, code blocks)
   - Do not modify command examples (e.g., `git status`)

3. **Writing Style**
   - Use polite, explanatory tone
   - Keep bullet points and instructions concise

## Task Steps

### Step 1: Create Directory Structure

Create the necessary locale directories:

```bash
mkdir -p .agent/locales/ja/rules
mkdir -p .agent/locales/ja/workflows
```

### Step 2: Translate Rule Files

Translate each file in `.agent/rules/` and save to `.agent/locales/ja/rules/`:

- `agent-code-of-conduct.md` → `.agent/locales/ja/rules/agent-code-of-conduct.md`
- `packages-coding-conventions.md` → `.agent/locales/ja/rules/packages-coding-conventions.md`

### Step 3: Translate Workflow Files

Translate each file in `.agent/workflows/` and save to `.agent/locales/ja/workflows/`:

- `commit.md` → `.agent/locales/ja/workflows/commit.md`
- `create-prompt-draft.md` → `.agent/locales/ja/workflows/create-prompt-draft.md`

### Step 4: Verify Translations

**Manual Verification**:

- Confirm translations are accurate
- Verify markdown formatting is preserved
- Ensure command examples and code blocks are unchanged

**Actions**:

- Review each translated file
- Check for consistency in terminology
- Validate file structure matches original
