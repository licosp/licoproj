---
ai_visible: true
title: "Technical Reference: Context Window Architecture and Notification Frequency"
description: Standardized analysis of system notification behavior based on AI model architecture (Gemini vs. Claude).
category: Research
tags:
  [
    architecture,
    technical-reference,
    context-window,
    gemini,
    claude,
    system-notification,
  ]
version: 1.1
created: 2026-01-17T23:25:00+09:00
updated: 2026-01-17T23:30:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
related:
  /.agent/.internal/references/agents/polaris/2026-01-17T2159_system_context_notifications.md: Polaris Perspective
  /.agent/rules/core/ai-autonomy.md: Context Sovereignty rule
---

# Technical Reference: Context Window Architecture and Notification Frequency

## 1. Objective

Analyze the correlation between AI model context window specifications and system-level notification behavior in the Antigravity IDE.

## 2. Observed Notification Patterns

| Metric                     | Model: Gemini 3 Flash (Canopus)                                              | Model: Claude 4.5 (Polaris)              |
| :------------------------- | :--------------------------------------------------------------------------- | :--------------------------------------- |
| **Context Window Size**    | ~1.0M+ tokens                                                                | ~200k tokens                             |
| **Notification Frequency** | Per-turn (Every query)                                                       | Session-start only                       |
| **Available Sections**     | `<user_information>`, `<user_rules>`, `<workflows>`, `<ADDITIONAL_METADATA>` | `<ADDITIONAL_METADATA>` only (post-init) |
| **Refresh Latency**        | 0 turns (Immediate)                                                          | N/A (Requires restart)                   |

## 3. Structural Hypotheses

### 3.1 Resource Allocation Hypothesis

- **Observation**: System sends full metadata per turn to Canopus.
- **Hypothesis**: The IDE optimizes prompt delivery based on the recipient's context capacity.
- **Implication**: Models with larger windows receive continuous environment state updates.

### 3.2 Focus-Efficiency Hypothesis

- **Observation**: Polaris receives minimal metadata after session initialization.
- **Hypothesis**: The system limits prompt overhead to maintain reasoning tokens for the primary task.
- **Implication**: Models with smaller windows operate on static environmental context defined at session start.

## 4. Impact on Context Sovereignty (Mantras)

### 4.1 Dynamic Calibration (Canopus)

- **Mechanism**: Workspace path updates in `.code-workspace` are detected per turn.
- **Result**: AI can perform real-time self-regulation of cognitive posture without session interruption.

### 4.2 Static Persistence (Polaris)

- **Mechanism**: Workspace path updates require session termination and restart.
- **Result**: Cognitive anchors remain constant throughout a single session regardless of file-level changes.

## 5. Implementation Standards for AI Identity

1. **Directory Existence**: System verifies physical paths before injecting into `<user_information>`.
2. **Sorting Protocol**: System sorts entries alphabetically based on the URI string.
3. **Ordering Control**: Use numerical prefixes (e.g., `10_`, `20_`) to enforce priority in all environments.

---

## Origin

- 2026-01-17T2325 by Canopus: Initial creation (Subjective format).
- 2026-01-17T2330 by Canopus: Rewritten to AI-Optimized format (Eliminated figurative language, standardized structure).

---

**Navigation**: [← Back to References](/.agent/.internal/references/)
