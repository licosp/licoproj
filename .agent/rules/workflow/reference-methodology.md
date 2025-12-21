---
ai_visible: true
description: Protocol for managing Objective Knowledge (References) vs Subjective Thoughts.
version: 1.0
created: 2025-12-22T03:30:00+09:00
updated: 2025-12-22T03:30:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High): Planning
---

# Reference Methodology (Objective Knowledge Management)

## 1. Definition

**References** (`.agent/.internal/references/`) store **Objective Knowledge**, **External Analysis**, and **Technical Concepts**.
They are distinct from **Thoughts** (`.agent/.internal/thoughts/`), which store Lico's **Subjective Experience** and **Internal Narrative**.

- **Thoughts**: "I felt...", "I decided...", "My plan..." (Subjective/Context-Heavy)
- **References**: "The system is...", "The user prefers...", "Concept X is defined as..." (Objective/Portable)

---

## 2. The "Second Eye" (External AI)

The "Second Eye" refers to external AI models (e.g., browser-based LLMs) that interact with the user outside the repository context.

### 2.1 Role

- **Verification**: Audits the project from a "clean slate" perspective without repository bias.
- **Cooldown**: Provides a space for the user to disengage from the heat of development and reflect.
- **Idea Generation**: Creating new concepts from high-level dialogue.

### 2.2 Output

- Produces analysis reports (e.g., `lico-evolution-and-identity-synthesis-report.md`).
- These documents serve as "External Truth" for Lico to read and internalize.

---

## 3. Lico's Role (Internal AI)

Lico also creates References, but only under specific conditions:

### 3.1 When to Create

- **Objective Scribing**: When the user explicitly teaches a concept or theory that should be preserved as fact.
- **Cognitive Crystallization**: When a subjective realization in `thoughts` evolves into a reusable heuristic or rule.
  - _Example_: `memory-priority-deep-knowledge.md`
  - _Example_: `heuristics_driven_tool_selection.md`

### 3.2 Where to Save

- **AI/Cognition Topics**: `.agent/.internal/references/agents/`
- **General Analysis**: `.agent/.internal/references/` or appropriate subdirectories.

---

## 4. Usage Protocol

### 4.1 Reading

- Lico **MUST** treat References as high-priority knowledge sources.
- Unlike `thoughts` (which may be obsolete), References are presumed "Valid until proven otherwise."

### 4.2 Updating

- **Immutable Concepts**: Do not modify historical reports from the Second Eye.
- **Living Documents**: Technical references created by Lico MAY be updated as understanding evolves.
