---
description: Identify and consolidate repository changes into logical atomic commits, supporting partial staging.
---

# Robust Commit Workflow

This workflow is designed for medium-to-large scale changes, ensuring atomic commits through iterative analysis and staging.

## 1. Analyze Changes
Understand the scope of work before committing.

```bash
git status
git diff --stat
```
*Agent Action*: Categorize changes (e.g., Config, Refactor, Feat, Docs). Determine if a single commit is sufficient or if splitting is required.

## 2. Commit Loop
Repeat the following steps until `git status` shows no relevant changes to commit.

### 2-1. Select & Stage
Choose a logical unit of work.

- **Option A: File-level Staging**
  ```bash
  git add <path/to/file_or_dir>
  ```
- **Option B: Partial Staging (Patch)**
  Use this when a single file contains multiple logical changes (e.g., a fix and a refactor).
  ```bash
  git add -p <path/to/file>
  ```
  *Agent Note*: Since `git add -p` is interactive, you may need to use `git diff` to identify line ranges and use `git apply` or careful `git add` if interactivity is limited, or ask the user to stage complex patches. **For this workflow, prefer precise `git add` or asking user assistance for complex patches.**

**Option C: Stop/Pause**
If you wish to stop the iteration (e.g., to review current progress or take a break), simply stop the loop. The current state (staged/unstaged) will be preserved.

### 2-2. Verify Staged Content
**CRITICAL**: Always check what is about to be committed.
```bash
git diff --cached --stat
git diff --cached
```
*Agent Action*: Ensure *only* the intended changes are staged. If unrelated files are staged, use `git restore --staged <file>` to unstage them.

### 2-3. Commit
Create the commit with a clear, descriptive message.

```bash
git commit -m "<Type>: <Subject>" -m "<Body (Optional)>"
```
- **Types**: `feat`, `fix`, `docs`, `style`, `refactor`, `test`, `chore`
- **Subject**: Imperative, present tense (e.g., "Add login page" not "Added...").

## 3. Review and Push
Once all changes are committed:

```bash
git log --oneline -n 5
git push origin <current_branch>
```
