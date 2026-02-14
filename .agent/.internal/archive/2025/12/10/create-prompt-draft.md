---
description: Create a new prompt draft with a date-based filename
---

# Create Prompt Draft Workflow

## Purpose
Generate a new Markdown draft file in `.human/.internal/drafts/$(whoami)` for writing AI instructions.

## Steps

1. **Create Directory** (if missing)
   ```bash
   mkdir -p .human/.internal/drafts/$(whoami)
   ```

2. **Generate File**
   Run the following to create a dated draft:
   ```bash
   cat > .human/.internal/drafts/$(whoami)/draft_$(date +%Y-%m-%d).md << 'EOF'
   ---
   date: $(date -Iseconds)
   user: $(whoami)
   ---

   ## Prompt
   [Enter your instructions]


   EOF
   ```

## Output
- **Path**: `.human/.internal/drafts/$(whoami)/draft_YYYY-MM-DD.md`
- **Usage**: Edit the `## Prompt` section to instruct the agent.
