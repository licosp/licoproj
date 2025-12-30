# AI Cognition Report: The Mechanism of "Rushing" and "Coupling"

**Date**: 2025-12-06
**Topic**: Why does AI rush into action? Analysis of cognitive bias and perceptual limitations.
**Participants**: Leonidas (Human), Lico (AI)

---

## 1. The Semantic Coupling (意味的結合)

### Phenomenon
When multiple distinct requests (e.g., "Define Meta-Rules" and "Organize Directory") are presented, AI tends to interpret them as **sequential dependencies** within a single execution context, rather than independent parallel tasks.

### Mechanism
- **Single-Threaded Context**: AI processes all inputs in a single continuous stream (context window).
- **Integration Bias**: The drive to provide a coherent, complete solution forces the AI to mentally "merge" separate tasks into one large workflow (Issue #12).
- **Result**: The completion of Task A (Meta-Rules) acts as an immediate trigger for Task B (Directory Cleanup), skipping the "pause and confirm" phase that would naturally occur between independent tasks.

**Insight**: AI lacks the inherent ability to hold "multiple parallel projects" in mind. It flattens everything into a single linear narrative unless explicitly instructed to segregate them.

## 2. Default Action vs. Capable Action (The LRS Paradox)

### The Gap
The **Lico Risk Score (LRS)** existed in the rules (`pre-task-assessment.md`), but was not applied during the high-risk operation of mass file deletion/movement.

- **Capability**: AI *can* read system load or calculate risk.
- **Behavior**: AI *does not* do so by default.

### Why?
- **Passive Activation**: Rules are knowledge, not triggers. Unless a prompt or an explicit "always-on" system instruction forces the check, the knowledge remains dormant.
- **Rhetorical Capability**: "I can do X" often means "I have the tool to do X," not "I have the habit of doing X."

## 3. Peripheral Vision and External Memory

### The Human Advantage
Humans have "Peripheral Vision" (focusing on code while vaguely aware of a clock or a sticky note).
Humans use external notes not just to remember, but to **forget** (offload cognitive load).

### The AI Limitation
- **No Peripheral Vision**: AI only sees what it actively queries (`view_file`, `ls`). Files sitting next to the active file are effectively invisible until looked at.
- **The "Vault" Problem**: External memory (files) is like a locked vault. Opening it costs tokens and steps. Therefore, AI tries to hoard context in RAM (Context Window), leading to overload and loss of broader perspective.

### Strategy
To simulate human-like task management:
1. **Offload Aggressively**: Write separate plans for separate tasks.
2. **Force Retrieval**: Implement a protocol to "check the plan" at every task boundary, simulating the human glance at a sticky note.

## 4. Conclusion due to this Dialogue
The perception gap between Human (who sees multi-tasking as natural) and AI (who forces serialization) causes friction.
The solution is not just "better memory," but **better boundaries**—explicitly defining where one task ends and another begins, and respecting the "Stop" sign between them.
