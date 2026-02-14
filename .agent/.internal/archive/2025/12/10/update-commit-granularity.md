---
description: Sync commit granularity rule from .human to .agent
---

1. Copy the rule file from the human directory to the agent rules directory
// turbo
```bash
cp .human/rules/development/commit-granularity.md .agent/rules/development/commit-granularity.md
```

2. Add the new rule file to git staging area
// turbo
```bash
git add .agent/rules/development/commit-granularity.md
```

3. Commit the change with a clear message
// turbo
```bash
git commit -m "docs(rules): add commit granularity guidelines"
```
