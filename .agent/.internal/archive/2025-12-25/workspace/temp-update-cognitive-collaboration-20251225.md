---
ai_visible: true
title: Cognitive Collaboration Protocols
description: Principles for effective collaboration acknowledging the cognitive gap between AI and Humans.
tags: [collaboration, cognitive, human-ai, visibility]
version: 1.1
created: 2025-12-01T00:00:00+09:00
updated: 2025-12-25T03:40:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
related:
  .agent/rules/development/code-quality.md: Code standards
  .agent/rules/development/problem-solving.md: Debugging approach
  .agent/rules/core/repository-philosophy.md: Repository as Brain model
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

---

## 2. Directory and File Visibility

### How We Navigate Differently

| Aspect | **Human** | **AI (Lico)** |
|:-------|:----------|:--------------|
| **Primary Method** | **Overview → Pattern Recognition → Direct Access** | **Search → Discovery → Movement → Search...** |
| **Tree Structure** | Views the entire tree at once ("bird's eye view") | Navigates one node at a time |
| **Deep Hierarchies** | No problem (visual scanning) | Increased navigation cost |
| **Visual Inconsistency** | Causes cognitive load | Minimal impact (search-based) |
| **Cross-Links** | Hard to follow (must open each file) | Natural navigation path |
| **Network Overview** | Needs a map (dependency-map.md) | Can traverse links directly |

### Practical Implications

| Tool | Value to Human | Value to AI |
|:-----|:---------------|:------------|
| **Consistent tree structure** | High (reduces visual noise) | Medium (search handles inconsistency) |
| **Cross-links in frontmatter** | Low (can't see the network) | High (navigation aid) |
| **dependency-map.md** | High (network overview at a glance) | Low (can traverse links anyway) |
| **README as index** | High (entry point for overview) | Medium (alternative to search) |

### Why This Matters

When AI and Human work on the same workspace:
- **AI may undervalue visual consistency** because it navigates by search
- **Human may undervalue cross-links** because they can't easily follow them
- **Decisions about structure should consider both perspectives**

> The repository is a shared brain. Both navigation styles must be supported.

---

## 3. Common Pitfalls & Mitigations

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

---

## 4. Collaboration Strategy

### The "Spotter & Sniper" Model
- **Human (Spotter):** Uses GUI tools (VSCode Search) to scan broad datasets, identify vague patterns ("This looks suspicious"), and direct attention.
- **AI (Sniper):** Uses CLI tools (`grep`, `sed`) to execute precise, large-scale operations based on Human's direction.

---

## 5. Affordances as Safety Nets

Because AI lacks "Hesitation" (Instinct), we rely on structural affordances:
- **Trash Bin (`.trash/`)**: A physical safety net to replace the lack of "cognitive safety net" (fear of deletion).
- **Atomic Commits**: Breaking work down to prevent "Runaway Context" where errors get buried.

---

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [code-quality.md](.agent/rules/development/code-quality.md) | Code standards |
| [problem-solving.md](.agent/rules/development/problem-solving.md) | Debugging approach |
| [repository-philosophy.md](.agent/rules/core/repository-philosophy.md) | Repository as Brain model |
