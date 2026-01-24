# GitHub Comment Templates

Copy the appropriate template below when posting to GitHub Issues or PRs.

---

## Daily Routine Checkpoint

```markdown
## Daily Routine Checkpoint

- **Date**: <YYYY-MM-DDTHH:MM+TZ>
- **Last Checked Commit**: <short-hash>
- **Identifier**: <your-identifier>

### Summary

<N> commits since <previous-checkpoint-hash>

**Milestones**:

- <milestone 1>
- <milestone 2>

**Audit Status**:

- [ ] Compliance with `<Identifier>: [Context-ID] type: description (Phase)`
- [ ] Context Integrity verified
```

---

## Progress Report

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

- `<hash>` <Identifier>: [Context-ID] type: description (Phase)
- `<hash>` <Identifier>: [Context-ID] type: description (Phase)
```
