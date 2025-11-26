---
description: Initialize the commit process with robust error handling and idempotency.
---

# Initialize Commit Process (Robust)

This workflow automates the "Initialize" phase of the Issue-Driven Development flow, ensuring robustness against common failures.

## 1. Pre-flight Checks
Ensure the environment is ready.

```bash
# Check if gh is installed
if ! command -v gh &> /dev/null; then
    echo "Error: GitHub CLI (gh) is not installed."
    exit 1
fi

# Check if gh is authenticated
if ! gh auth status &> /dev/null; then
    echo "Error: GitHub CLI is not authenticated. Please run 'gh auth login'."
    exit 1
fi

# Check if inside a git repository
if ! git rev-parse --is-inside-work-tree &> /dev/null; then
    echo "Error: Not inside a git repository."
    exit 1
fi
```

## 2. Investigate Changes
Analyze repository status.

```bash
git status
git diff --stat
```
*If no changes are found, abort the process.*

## 3. Generate Issue Details
Synthesize the following based on the investigation:
- **Title**: `[Type]: [Short Description]`
- **Body**: Summary, Changes, Purpose.
- **Tags**: `refactor`, `feat`, `fix`, etc.
- **Branch Name**: Derived from title (kebab-case).

## 4. Create Issue & Branch (Idempotent)
Execute safely, handling existing resources.

```bash
# Variables (Replace these)
ISSUE_TITLE="<TITLE>"
ISSUE_BODY="<BODY>"
ISSUE_LABELS="<TAGS>"
BRANCH_NAME="<BRANCH_NAME>"

# 4-1. Create Issue
# Check if a similar issue already exists (optional, but good for idempotency)
# For now, we assume a new issue is always desired for a new task.
echo "Creating issue..."
ISSUE_URL=$(gh issue create --title "$ISSUE_TITLE" --body "$ISSUE_BODY" --label "$ISSUE_LABELS")
ISSUE_NUMBER=$(echo $ISSUE_URL | awk -F'/' '{print $NF}')

if [ -z "$ISSUE_NUMBER" ]; then
    echo "Error: Failed to create issue."
    exit 1
fi
echo "Created Issue #$ISSUE_NUMBER"

# 4-2. Create/Checkout Branch
if git show-ref --verify --quiet "refs/heads/$BRANCH_NAME"; then
    echo "Branch '$BRANCH_NAME' already exists. Checking out..."
    git checkout "$BRANCH_NAME"
else
    echo "Creating and linking branch..."
    gh issue develop "$ISSUE_NUMBER" --name "$BRANCH_NAME" --checkout
fi
```

## 5. Finalize
```bash
git fetch origin
echo "Initialization complete. On branch: $(git branch --show-current)"
```
