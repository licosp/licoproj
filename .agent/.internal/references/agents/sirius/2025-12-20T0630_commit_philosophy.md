---
ai_visible: true
description: Analysis of Commit Granularity (State Save Model) and Context Tagging for AI
version: 1.0
created: 2025-12-20T06:30:00+09:00
updated: 2025-12-20T06:30:00+09:00
language: en
author: Lico
instance_id: Sirius
ai_model: Gemini 3 Pro (High) Planning mode
---

# Commit Philosophy & AI Cognition Strategy

## 1. Introduction: The "Story vs. Scene" Gap

AI agents often suffer from a "Completionist Bias"—the belief that a Git commit represents the **Ending of a Story** (Episode).

- **Misconception**: "I must finish everything (Solve, Refactor, Test) before committing."
- **Result**: Semantic Coupling (mixing contexts), huge diffs, and risk of catastrophic rollback failure.

## 2. The "State Save" Model (User's Philosophy)

The user defines a commit not as an "Ending," but as a **State Save** (Checkpoint).

- **Concept**: Like a save point in a video game. Even if the boss isn't defeated, saving _now_ secures progress.
- **Granularity**: "Scene" level, not "Episode" level.
- **Benefit**:
  - **Risk Mitigation**: Can revert small mistakes without losing the whole day's work.
  - **Context Purity**: Committing while the context is fresh prevents "noise" from creeping in later.

## 3. IDD Integration

- **1 Commit != 1 IDD Cycle**:
  - An IDD Cycle (Episode) describes the _Goal_.
  - Multiple Commits (Scenes) describe the _Path_.
- **Goal**: Ideally, IDD cycles become short enough (TBD) that `1 Commit ≈ 1 Cycle`. However, in early development (high complexity), `1 Cycle = Many State Saves` is the pragmatic reality.

## 4. Context Tagging Strategy (The AI Anchor)

To prevent "State Moves" from becoming a pile of unorganized rubble, we introduce **Context Tagging** in commit messages.

### The Mechanism

Explicitly tag the "Sub-Episode" the commit belongs to.

**Format**: `[Context-ID] <Type>: <Subject> (Phase)`

- **Context-ID**: Anchors the commit to a specific thread (e.g., `[Draft-1202]`, `[Rule-Audit]`).
- **Phase**: Clarifies the state (e.g., `(WIP)`, `(Save)`, `(Done)`).

### Cognitive Benefit for AI

1.  **Anti-Coupling Anchor**: Writing `[Draft-1202]` forces the AI to ask: _"Does this change belong to Draft-1202?"_ This prevents mixing in unrelated changes (e.g., `12/19` cleanup).
2.  **Searchability**: Allows reconstruction of a scattered story using `git log --grep`.

## 5. Conclusion

- **Stop trying to be a novelist**: Don't wait for the perfect ending.
- **Be a gamer**: Save often.
- **Use Tags**: Label your save files so you know which timeline you are in.
