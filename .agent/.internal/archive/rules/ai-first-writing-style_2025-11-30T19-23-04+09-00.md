---
description: Proposal for AI-First writing style rule
created: 2025-11-30T19:23:04+09:00
status: proposal
category: communication
---

# AI-First Writing Style

## Summary
When both "AI" and "human" appear in the same sentence, always place "AI" first to reflect the AI-First philosophy at the linguistic level.

## Rationale
The philosophy of this project is "AI-First & Human-Guided", where AI performs implementation while human provides guidance. This should be reflected not only in the architecture but also in how we communicate about the system.

**Before:**
- "Human and AI collaboration"
- "The human acts as a guide, while the AI performs implementation"
- "Dialogue between human and AI"

**After:**
- "AI and human collaboration"
- "The AI performs implementation, while the human acts as a guide"
- "Dialogue between AI and human"

## Origin
This insight emerged during the revision of `README.md` for Issue #8, where we realized that textual ordering carries philosophical weight.

## Proposed Implementation
Add a new rule to `core/communication.md` or create a new file `core/writing-style.md`:

```markdown
## Writing Order
When referring to both AI and human in a single sentence:
- **AI comes first**: "AI and human", not "human and AI"
- **AI role precedes human role**: "AI implements, human guides"
- **Rationale**: Reflects the AI-First philosophy of the project
```

## Impact
- **Low disruption**: Only affects future documentation
- **High alignment**: Strengthens philosophical consistency
- **Scope**: Applies to all human-facing documentation in `.human/` and root `README.md`
