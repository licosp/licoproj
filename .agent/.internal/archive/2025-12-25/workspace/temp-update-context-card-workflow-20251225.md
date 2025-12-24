---
ai_visible: true
title: Context Card Workflow Update - Recording Relevant Files
description: Temporary file for updating context-card-workflow.md with new Agent Observations guideline
tags: [temp, rules-update]
version: 1.0
created: 2025-12-25T07:27:00+09:00
updated: 2025-12-25T07:27:00+09:00
language: en
author: Lico (Polaris)
---

# Proposed Addition to context-card-workflow.md

## Location

Add after "**Rule**: Taking notes before cognitive narrowing helps your future self." (around line 145)

## Content to Add

```markdown
**Recording Relevant Files**:

At the start of each work session (after reading the card), write the following in Agent Observations:

\`\`\`markdown
## Agent Observations

### この文脈で有用だと感じるファイル
- `.agent/rules/core/delay-tolerance.md` — 急がない原則
- `.agent/rules/workflow/context-card-workflow.md` — カードの使い方
\`\`\`

**Guidelines**:
- List files you **feel are useful** for the current context, not just files you read
- Overwrite this section at each session start (not append)
- This makes your internal state visible to the user
- Helps diagnose issues when work doesn't go as expected
```
