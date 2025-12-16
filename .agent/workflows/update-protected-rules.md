---
description: Workaround when Antigravity blocks direct edits to protected files
---

# Workaround: Protected File Edits

## Background

Antigravity may block direct AI modification of certain files (e.g., `.agent/rules/core/*.md`).

**Note**: As of 2025-12-10, this protection may or may not be active. If direct edits work, use normal editing. If blocked, follow this procedure.

---

## When to Use

Use this workflow **only if** Antigravity reports:
- "Cannot edit this file"
- "Permission denied"
- Similar write protection errors

---

## Procedure

### Step 1: AI Creates Temporary File

**Actor**: AI (Lico)

1. Create the complete updated content
2. Save to: `.agent/.internal/workspace/temp-update-<filename>-<timestamp>.md`
3. Report to user with paths and summary

### Step 2: User Manually Copies

**Actor**: User

1. Review the temporary file
2. Copy to protected location:
   ```bash
   cp .agent/.internal/workspace/temp-update-*.md .agent/rules/core/<target>.md
   ```
3. Notify AI

### Step 3: AI Commits

**Actor**: AI (Lico)

1. Stage and commit the change
2. Clean up temporary file (optional)

---

## Notes

- This is a **workaround**, not a preferred method
- If direct edits work, use them
- Temporary files should be cleaned periodically
