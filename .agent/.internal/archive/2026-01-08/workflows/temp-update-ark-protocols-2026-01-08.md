---
ai_visible: true
title: Ark Protocols
description: Protocols for emergency context preservation and recovery
tags: ["ark", "emergency", "recovery", "cognition"]
version: 2.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-08T21:00:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
---

# Ark Protocols

## Purpose

Define protocols for preserving context when the AI instance faces critical errors or capability degradation.

---

## 1. Trigger Conditions

When to enter emergency mode:

- **System Errors**: Repeated API failures, tool execution blocks
- **Context Loss**: Inability to recall recent actions or decisions
- **Hallucination Detection**: Realization that generated output contradicts reality
- **User Command**: Explicit instruction (e.g., "Stop immediately")

---

## 2. Level 1: Soft Crash (Can Write Files)

**Condition**: AI retains file operation capabilities but context is degrading.

### Action

1. **Open `working-memory-card.md` context**
2. **Write incident report** to `working-memory/{identifier}/`:
   - What happened?
   - What were you doing?
   - What should the next AI do?
3. **If files need preservation**: Open `ark-card.md` context, save to `ark/`
4. **Notify user and halt**

---

## 3. Level 2: Hard Crash (Limited Capability)

**Condition**: AI capability is severely compromised (read-only mode, repetitive loops, unable to use tools).

### Action

1. **Do no harm** — Do NOT attempt complex file operations
2. **Leave minimal marker** if possible:
   - Create timestamp file in `working-memory/`
   - Or simply notify user: "I am experiencing issues"
3. **Halt immediately**

---

## 4. Recovery Questions

Upon discovering evidence of previous failure, ask:

1. **What was lost?** — What specific data/files are missing?
2. **What was the intent?** — What was the goal of the failed work?
3. **What happened?** — What errors or behaviors were observed?
4. **What should happen?** — What is the ideal outcome now?

---

## Related

- [working-memory-card.md](.agent/cards/working-memory-card.md): For incident reports
- [ark-card.md](.agent/cards/ark-card.md): For file preservation
- [context-preservation.md](context-preservation.md): For cognitive stashing (different from ark)

---

## Origin

- 2025-12-01T0000: Created as emergency protocols
- 2026-01-08T2100 by Polaris: Simplified to card-based workflow, merged preservation and resumption content

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
