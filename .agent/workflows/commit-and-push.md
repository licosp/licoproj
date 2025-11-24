---
description: Identify repository changes, organize them into logical commits, and push them to GitHub
---

# Commit and Push Workflow

## Objective

Identify repository changes, organize them into logical commits, and push them to GitHub.

## Task Steps

### Step 1: Investigate Changes

Identify and analyze all uncommitted changes in the repository.

**Actions**:
- Run `git status` to see modified, added, and deleted files
- Run `git diff` to review the actual changes
- Categorize changes by their purpose or component

**Output**:
- Create a list grouping related changes together
- Each group should represent a logical, atomic commit
- List the files affected in each group

### Step 2: Create Commits

Create individual commits for each logical group of changes.

**Requirements**:
- Use `git add` to stage files for each commit
- Write clear, descriptive commit messages in English
- Follow commit message best practices:
  - Use imperative mood (e.g., "Add feature" not "Added feature")
  - Keep the first line under 50 characters
  - Provide additional context in the body if needed
  - Reference issue numbers if applicable

**Process**:
1. Stage related files together: `git add <files>`
2. Create commit with descriptive message: `git commit -m "message"`
3. Repeat for each logical group of changes

### Step 3: Review and Push

Review all commits and push them to GitHub.

**Actions**:
- Run `git log` to review commit history
- Verify each commit is atomic and well-described
- Push commits to the remote repository: `git push`

**Verification**:
- Confirm all changes have been committed
- Ensure commit messages are clear and in English
- Verify successful push to GitHub
