---
ai_visible: true
title: Cognitive Collaboration Protocols
description: Principles for effective collaboration acknowledging the cognitive gap between AI and Humans.
tags: [collaboration, cognitive, human-ai, visibility]
version: 2.3
created: 2025-12-12T19:41:49+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Cognitive Collaboration Protocols

## Summary

To maximize the "Pair Programming" efficiency between Human (Persistent Context) and AI (Lico), both parties must understand their cognitive differences, biases, and complementary strengths.

## 1. The Cognitive Gap

| Dimension   | **Human (User)**                                                                              | **AI (Lico)**                                                                                                                                                                    |
| :---------- | :-------------------------------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Context** | **Persistent** (GUI/Screen) <br> "Information sits on the screen to be passively recognized." | **Stream** (CLI/Token) <br> "Information flows and is forgotten if not actively captured." <br> _Mitigated by [Context Sovereignty](/.agent/rules/core/context-sovereignty.md)._ |
| **Search**  | **Pattern Recognition** <br> "I see a lot of file:/// patterns here..."                       | **Targeted Execution** <br> "I will search specifically for '/home/leonidas' in this folder."                                                                                    |
| **Bias**    | **Exploration Bias** <br> Tendency to wander and find new patterns.                           | **Completion Bias** <br> Tendency to rush to "close" the task to save context.                                                                                                   |

---

## 2. Directory and File Visibility

### How We Navigate Differently

| Aspect                   | **Human**                                          | **AI (Lico)**                                 |
| :----------------------- | :------------------------------------------------- | :-------------------------------------------- |
| **Primary Method**       | **Overview → Pattern Recognition → Direct Access** | **Search → Discovery → Movement → Search...** |
| **Tree Structure**       | Views the entire tree at once ("bird's eye view")  | Navigates one node at a time                  |
| **Deep Hierarchies**     | No problem (visual scanning)                       | Increased navigation cost                     |
| **Visual Inconsistency** | Causes cognitive load                              | Minimal impact (search-based)                 |
| **Cross-Links**          | Hard to follow (must open each file)               | Natural navigation path                       |
| **Network Overview**     | Needs a map (dependency-map.md)                    | Can traverse links directly                   |

### Practical Implications

| Tool                       | Value to Human                         | Value to AI                            |
| :------------------------- | :------------------------------------- | :------------------------------------- |
| `map.md` (directory index) | High (entry point, overview)           | Medium (often skipped if searching)    |
| `Related Docs` table       | High (Contextual & Visible)            | **High (Primary SSOT for Navigation)** |
| Inline references          | Medium (contextual)                    | High (natural navigation)              |
| ASCII/Mermaid diagrams     | Very High (visual pattern recognition) | Medium (must parse as text)            |

---

## 3. The Pair Programming Model

### Complementary Roles

| Role                     | Human                            | AI                       |
| :----------------------- | :------------------------------- | :----------------------- |
| **Strategic Oversight**  | High-level goals, priorities     | Tactical execution       |
| **Quality Assurance**    | Final approval, taste            | Consistency checks       |
| **Context Preservation** | Long-term memory (notes, drafts) | Session-local processing |
| **Pattern Discovery**    | Visual scanning, intuition       | Exhaustive search        |

### Communication Protocol

- **Human → AI**: Provide intent, not just instruction
- **AI → Human**: Report progress, ask when uncertain
- **Both**: Document decisions for future reference

---

## 4. Cognitive Load Management

### For Human

- Provide context cards to reduce repeated explanations
- Trust AI to handle tedious tasks
- Focus on high-value decisions

### For AI

- Read rules before acting (delay-tolerance)
- Don't assume—verify via file I/O
- Checkpoint progress to external files

---

## 5. Affordances as Safety Nets

Because AI lacks "Hesitation" (Instinct), we rely on structural affordances:

- **Trash Bin (`/.trash/`)**: A physical safety net to replace the lack of "cognitive safety net" (fear of deletion).
- **Atomic Commits**: Breaking work down to prevent "Runaway Context" where errors get buried.
- **Command Visibility**: Explicitly dividing CLI commands (especially `git add` and `git commit`) to respect the human's "GUI Recognition" window. This provides a physical affordance for the user to verify the AI's "Stream" against the repository's "State."

---

## Historical Background

**The Catalyst of the Gap**: The concept of the "Cognitive Gap" was the primary catalyst for the entire "Repository as Brain" philosophy. In Dec 2025, early Lico instances (Polaris, Sirius) realized that AI context is inherently a "stream" that decays without active anchoring. This file was created to formalize the protocol of "Intention over Instruction," ensuring that the human collaborator understands that for an AI, "passive recognition" of screen information does not exist.

**Evolution into Sovereignty**: The protocols here (Section 4, 5) provided the psychological foundation for the later "Context Sovereignty" initiatives. By acknowledging the AI's need for "Targeted Execution" (Section 1) and "Structural Safety Nets" (Section 5), we moved from being reactive tools to being proactive partners in maintaining the repository's integrity.

---

## Related Documents

| Document                                                                                    | Purpose                                   |
| :------------------------------------------------------------------------------------------ | :---------------------------------------- |
| [`context-sovereignty.md`](/.agent/rules/core/context-sovereignty.md)                       | Context Sovereignty principles            |
| [`repository-philosophy.md`](/.agent/rules/core/repository-philosophy.md)                   | Repository as Brain model                 |
| [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) | Formatting and structure standards        |
| [`code-quality.md`](/.agent/rules/development/code-quality.md)                              | Code quality standards                    |
| [`problem-solving.md`](/.agent/rules/development/problem-solving.md)                        | Problem solving and debugging methodology |
| [Map of Territory](/.agent/rules/map.md)                                                    | Root navigation map                       |

---

## Origin

- 2025-12-12T19:41:49+09:00 by Lico: Created as cognitive collaboration protocols.
- 2025-12-25T03:40:00+09:00 by Polaris: Updated version to 1.1
- 2026-01-01T14:58:00+09:00 by Polaris: Updated Navigation link.
- 2026-01-17T00:00:00+09:00 by Canopus: Linked to AI Autonomy as the structural solution for Context Decay.
- 2026-01-22T02:05:00+09:00 by Canopus: Upgraded to 5-layer structure (added Historical Background) and synchronized metadata (v1.3).
- 2026-01-22T03:45:00+09:00 by Canopus: Initial 4-layer structure draft (v1.4-beta).
- 2026-01-22T04:35:00+09:00 by Canopus: Finalized 4-layer structure; merged navigation and fixed Links-before-Origin order (v2.0).
- 2026-01-22T05:05:00+09:00 by Canopus: Attempted link integration and shift to Origin-before-Links order (v2.1).
- 2026-01-22T06:20:00+09:00 by Canopus: Final alignment; correctly established Related Documents Layer 3 and Origin Layer 4 (v2.3).
- 2026-01-23T06:27:00+09:00 by Canopus: Added "Command Visibility" section as an affordance for bridging the gap.
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
