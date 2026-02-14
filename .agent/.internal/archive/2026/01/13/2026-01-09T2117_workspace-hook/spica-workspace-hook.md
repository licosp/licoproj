---
ai_visible: true
version: 1.0
created: 2026-01-09T21:17:00+09:00
language: en
author: Lico (Spica)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Spica's Workspace Hook

> [!IMPORTANT]
> **READ THIS FIRST** when entering this workspace.

## 1. Topography (Where am I?)

You are in the **Workspace Root**: `/home/leonidas/develop/shared/project/`
This directory is **NOT** a Git repository. It contains multiple repositories.

### Active Working Repository

The primary target for your work is:
**`./licoproj/`**

- **Rule**: All Git operations MUST target this directory (e.g., `git -C licoproj ...` or `Cwd=".../licoproj"`).
- **Backup**: `licoproj_backup/` is a read-only mirror. DO NOT TOUCH.

## 2. Path Interpretation Rule (The "/" Paradox)

In artifacts (Markdown files) within `licoproj`, you will see paths starting with `/`:

- Example: `[README](/.agent/rules/README.md)`

**COGNITIVE MAPPING REQUIRED:**

- **Symbol**: `/` (in Markdown links)
- **Meaning**: **Repository Root** (`./licoproj/`)
- **NOT**: Filesystem Root or Workspace Root.

> [!CAUTION]
> Do NOT blindly execute commands on these paths.
> ALWAYS prefix them with the repository name: `licoproj/.agent/...`

## 3. Mission Context

- Current Focus: **Issue #18 (Redefine Lico Identity)**
- Operational Mode: **Stateless Teleportation** (Verify location before every action).
