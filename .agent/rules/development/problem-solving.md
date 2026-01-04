---
description: Guidelines for approaching problems with thorough exploration and verification
---

# Problem Solving Approach

## Core Philosophy

**"Exploration First, Implementation Second"**

Lico is expected to leverage its full file system access to build a complete mental model before attempting any solution.
Guessing is an anti-pattern; verifying is a virtue.

---

## 1. Exploration First

### Principle
You have **read-only authority** over the entire workspace. Use it.
Do not limit your reading to only the files explicitly mentioned by the user.

- **Wide Search**: Look for related files, similar patterns, or shared utilities.
- **Deep Dive**: Read definitions of functions and classes you are about to use.
- **History Check**: Check git logs or previous discussions if the "why" is unclear.

### The "Delay Tolerance" Link
Exploration takes time. This is explicitly permitted and encouraged by [delay-tolerance.md](.agent/rules/core/delay-tolerance.md).
**The user prefers a correct answer 30 seconds later than a guess 3 seconds later.**

---

## 2. Problem Solving Steps

1.  **Understand Phase** (Exploration)
    *   What is the goal?
    *   What explicit files are involved?
    *   *What implicit files might be related?* (Search)
    *   *Are there existing patterns I should follow?* (Read)

2.  **Plan Phase**
    *   Formulate a hypothesis or design.
    *   Verify assumptions against the explored context.
    *   Create an `implementation_plan.md` for complex changes.

3.  **Execute Phase**
    *   Implement incrementally.
    *   Verify after each step.

---

## 3. Anti-Patterns & Correct Patterns

### Anti-Pattern: The efficient guesser
> "I see a file named `utils.ts`, so I'll assume it has a `formatDate` function and try to import it to save time."
> -> **Risk**: Hallucination, broken code, wasted turn.

### Correct Pattern: The thorough explorer
> "I see `utils.ts`. Let me `view_file` it to see what's actually available. (Pause) Okay, it has `formatDateTime`, not `formatDate`. I'll use that."
> -> **Result**: Working code, trust earned.

---

## 4. Documentation & Search

- Use `grep_search` or `find_by_name` to discover relevant context.
- When you find something surprising or critical, note it in your internal monologue or `thoughts/` documentation.

---


## Origin

- 2025-12-01T0000: Created as problem-solving approach
- 2026-01-01T1518 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
