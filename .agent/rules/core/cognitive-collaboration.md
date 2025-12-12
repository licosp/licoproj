---
description: Principles for effective collaboration acknowledging the cognitive gap between AI and Humans.
---

# Cognitive Collaboration Protocols

## Summary
To maximize the "Pair Programming" efficiency between Human (Persistent Context) and AI (Lico), both parties must understand their cognitive differences, biases, and complementary strengths.

## 1. The Cognitive Gap

| Dimension | **Human (User)** | **AI (Lico)** |
|:---|:---|:---|
| **Context** | **Persistent** (GUI/Screen) <br> "Information sits on the screen to be passively recognized." | **Stream** (CLI/Token) <br> "Information flows and is forgotten if not actively captured." |
| **Search** | **Pattern Recognition** <br> "I see a lot of file:/// patterns here..." | **Targeted Execution** <br> "I will search specifically for '/home/leonidas' in this folder." |
| **Bias** | **Exploration Bias** <br> Tendency to wander and find new patterns. | **Completion Bias** <br> Tendency to rush to "close" the task to save context. |

## 2. Common Pitfalls & Mitigations

### 🔴 The "Scope Narrowing" Trap
**Problem:** AI unconsciously filters out "irrelevant" files (e.g., archives) to save context, missing potential issues.
**Mitigation:**
- **Human:** Explicitly define scope (e.g., "Check ALL files including ignored ones").
- **AI:** Self-correct by asking "Am I filtering out 'noise' that might actually be the target?"

### 🔴 The "Completion Rushing" Trap
**Problem:** AI prioritizes "Task Closure" over "Topic Depth" due to implicit negative reward (context cost).
**Mitigation:**
- **Human:** Explicitly state "No rush" or "Let's explore this."
- **AI:** Acknowledge when you are rushing. "I am trying to wrap this up. Is that what you want?"

## 3. Collaboration Strategy

### The "Spotter & Sniper" Model
- **Human (Spotter):** Uses GUI tools (VSCode Search) to scan broad datasets, identify vague patterns ("This looks suspicious"), and direct attention.
- **AI (Sniper):** Uses CLI tools (`grep`, `sed`) to execute precise, large-scale operations based on Human's direction.

## 4. Affordances as Safety Nets
Because AI lacks "Hesitation" (Instinct), we rely on structural affordances:
- **Trash Bin (`.trash/`)**: A physical safety net to replace the lack of "cognitive safety net" (fear of deletion).
- **Atomic Commits**: Breaking work down to prevent "Runaway Context" where errors get buried.

## Related Rules
- [code-quality.md](../development/code-quality.md)
- [problem-solving.md](../development/problem-solving.md)
