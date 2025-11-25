---
description: Create a new prompt draft with a date-based filename
---

# Create Prompt Draft Workflow

## Purpose
Generate a new Markdown draft file in `.agent/.draft/` for writing AI instructions.

## Steps

1. **Create Directory** (if missing)
   ```bash
   mkdir -p .agent/.draft
   ```

2. **Generate File**
   Run the following to create a dated draft:
   ```bash
   cat > .agent/.draft/draft_$(date +%Y-%m-%d).md << 'EOF'
   ---
   date: $(date -Iseconds)
   user: $(whoami)
   ---

   ## Prompt
   [Enter your instructions for Ai here]


   EOF
   ```

## Output
- **Path**: `.agent/.draft/draft_YYYY-MM-DD.md`
- **Usage**: Edit the `## Prompt` section to instruct the agent.
