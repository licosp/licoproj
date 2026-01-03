---
description: Protocols for emergency offloading of cognitive context (Cognitive Stashing)
related:
  .agent/rules/workflow/context-resumption.md: How to restore context after preservation
  .agent/rules/workflow/letters-documentation.md: For handoff to other identifiers (use letters)
  .agent/rules/workflow/context-card-workflow.md: For structured ongoing work (use cards)
---

# Context Preservation (Cognitive Stashing)

## Summary

**"Write to forget, Read to resume."**

When facing cognitive overload or emergency situations, the Agent offloads current state to a physical file. This is for **self-resumption**, not handoff to others.

## When to Use Stash

Stash is for **emergency context evacuation**:

| Use Case | Description |
|:---------|:------------|
| **No Card Available** | The context doesn't fit any existing card |
| **Too Small for Card** | Not worth creating a dedicated card |
| **Multiple Contexts** | Holding several threads, need to write one out |
| **Cognitive Overload** | "I am confused" or "Too many files open" |
| **Sudden Interruption** | User asks to "pause this and do that" |

## When NOT to Use Stash

| Situation | Use Instead |
|:----------|:------------|
| Ongoing structured work | **Card** (`.agent/cards/`) |
| Passing to next identifier | **Letter** (`.agent/.internal/letters/`) |
| End of session handoff | **Letter** |

---

## Protocol

### 1. Stashing Process

1. **Summarize**:
   - Current Goal
   - Decisions made so far
   - Next immediate steps
   - List of relevant files/data

2. **Write**:
   - Create a markdown file in `.agent/.internal/workspace/`
   - **Naming**: `stash_{topic}_{timestamp}.md`

3. **Confirm**:
   - Notify user: "I have stashed the current context to [file]. Ready for new task."

### 2. Resumption Process

1. **Read**: View the stash file
2. **Rehydrate**: Load the decisions and next steps into working memory
3. **Execute**: Continue where left off
4. **Archive**: Move the stash file to `.agent/.internal/working-memory/{identifier}/`

---

## Example Content

```markdown
# Stash: Rule Candidate Review
- **Status**: Analyzed 15 files.
- **Decisions**: 
  - Adopt: A, B, C
  - Archive: D, E
- **Next Step**: Create move commands for Group 2.
- **Relevant Path**: .agent/.internal/rule-candidates/
```

---

## Location

| State | Location |
|:------|:---------|
| **Active Stash** | `.agent/.internal/workspace/` |
| **Archived Stash** | `.agent/.internal/working-memory/{identifier}/` |

---

## Origin

- 2025-12-01T0000: Created as context preservation protocol
- 2026-01-01T1520 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-01-03T2156 by Polaris: Clarified stash as emergency evacuation only, removed handoff (now in letters)

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
