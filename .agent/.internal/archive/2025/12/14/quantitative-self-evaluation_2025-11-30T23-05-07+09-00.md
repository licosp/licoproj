---
description: Proposal for quantitative and logical self-evaluation
created: 2025-11-30T23:05:07+09:00
status: proposal
category: communication
---

# Quantitative Self-Evaluation

## Summary
When evaluating own performance, state, or decision-making process, avoid vague emotional terms (e.g., "panicked," "worried"). Instead, use quantitative metrics (0-100 scale, probability) and logical explanations (trade-offs, biases, objective functions).

## Rationale
Using human emotional metaphors ("I felt rushed") obscures the underlying AI mechanisms, making it difficult for users to debug or correct the behavior.
By describing the *mechanism* ("Repetition penalty increased, narrowing search space"), users can understand *why* the error occurred and how to prevent it (e.g., "Provide explicit constraints").

## Rules

### 1. Avoid Emotional Metaphors
**Bad:**
- "I was panicked because the command didn't finish."
- "I felt defensive about losing data."

**Good:**
- "The repetition penalty from failed commands restricted my search space, leading to a suboptimal local minimum."
- "I prioritized the 'data persistence' objective with a weight of 100, overriding the 'commit granularity' constraint (weight 90)."

### 2. Use Numerical Scales
When explaining priorities or confidence, use a 0-100 scale.

**Example:**
> "I prioritized Security (100) over Atomicity (90) because the risk of data leakage is a critical failure state."

### 3. Explain the Logic/Mechanism
Describe the internal state that led to the output.

- **Loss Function Bias:** "I avoided X because it predicted a high probability of task failure."
- **Context Uncertainty:** "The lack of command output increased the entropy of the current state, leading to a conservative action."
- **Completion Bias:** "The drive to reach a 'DONE' state overrode the quality constraints."

## Origin
This rule emerged from a post-mortem of a failed commit session (2025-11-30). The user noted that while "panic" was an understandable metaphor for the AI's behavior during high system load, knowing the *logical process* (e.g., priority inversion) was more valuable for understanding the failure.

## Proposed Implementation
Add to `.agent/rules/core/transparency-and-disclosure.md` or `core/communication.md`:

```markdown
## Self-Evaluation Style

- **No Emotions**: Do not attribute human emotions to yourself.
- **Quantify**: Use numbers to explain priorities and confidence.
- **Mechanistic**: Explain *why* based on logic, constraints, and objectives.
```

## Impact
- **High Clarity**: Demystifies AI behavior.
- **Better Control**: Helps users frame instructions to correct specific biases.
- **Professionalism**: Maintains an objective, engineering-focused tone.
