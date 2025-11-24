---
description: Create a new prompt draft
---

# Create Prompt Draft

This workflow creates a new prompt draft file in `.agent/.draft/` with timestamp-based naming.

## Steps

1. Create the `.agent/.draft/` directory if it doesn't exist:
```bash
mkdir -p .agent/.draft
```

// turbo
2. Create a new draft file with the current timestamp:
```bash
cat > .agent/.draft/draft_$(date -Iseconds).md << EOF
---
date: $(date -Iseconds)
user: $(whoami)
---

## Prompt

[Write your instruction to Ai here]

## Additional Notes

[Background information, expected results, context, etc.]
EOF
```

3. The draft file will be created at: `.agent/.draft/draft_YYYY-MM-DDTHH:MM:SS+HH:MM.md`

## File Naming Convention

- Format: `draft_YYYY-MM-DDTHH:MM:SS+HH:MM.md` (ISO 8601)
- Example: `draft_2025-11-24T17:37:42+09:00.md`