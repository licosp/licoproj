# Issue Comment Template

Use this template when posting progress reports to GitHub Issues.

## Template

```markdown
## [Context-ID] Progress Report

**Identifier**: <your-identifier>
**Date**: <YYYY-MM-DDTHH:MM+TZ>

### Done
- <completed item>
- <completed item>

### Next
- <remaining item>
- <remaining item>

### Notes
<optional: unexpected findings, warnings, or context that doesn't fit above>

### Commits
- `<hash>` <commit message>
- `<hash>` <commit message>
```

## Example

```markdown
## [IDD-Improvement] Progress Report

**Identifier**: Polaris
**Date**: 2026-01-05T19:00+09:00

### Done
- Updated P1 workflow with hierarchy section
- Created idd-init-card.md and idd-fini-card.md

### Next
- Update IDD improvement card with final status
- Archive card if completed

### Notes
Antigravity blocked direct edit to system-artifacts.md, used cp workaround.

### Commits
- `a2cc795` docs(workflows): add hierarchy to P1
- `65ee479` docs(cards): create IDD init card
- `ff84284` docs(cards): create IDD fini card
```

## When to Post

- Too many commits accumulated
- Major direction change
- Card context completed
- Management trouble (branch/issue problems)

## Notes Section Guidelines

- Use for **objective** observations only
- Subjective content belongs in **Letters**
- Keep brief; link to relevant files if needed
