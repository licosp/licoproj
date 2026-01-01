---
ai_visible: true
description: Anti-patterns to avoid, examples of optimal AI-optimized markdown, and specific lexical restrictions for high-reliability parsing.
version: 1.0
created: 2025-12-11T18:00:00+09:00
updated: 2025-12-11T18:00:00+09:00
language: en
author: Gemini
ai_model: Gemini 2.5 Flash variant (Fast)
---


# Markdown AI-Parsing Patterns

## When to Use AI-Optimized Markdown

- **Automation Scripts**: Markdown files parsed by Python/Node scripts
- **AI-to-AI Communication**: Passing structured information between AI systems
- **Specification Documents**: Technical specs where precision and verifiability are critical
- **Logging and Records**: Machine-readable logs with structured format

## When to Use Human-Readable Markdown

- **User Documentation**: Guides intended for human readers
- **README Files**: Project introductions and getting-started guides
- **Meeting Notes**: Flexible capture of ideas and discussions

## Comparison Table

| Aspect | AI-Optimized | Human-Readable |
|--------|--------------|----------------|
| Emojis | Minimal/eliminated | Encouraged |
| Whitespace | Minimal | Generous |
| Emphasis | Bold only for keywords | Bold, italics, decorative |
| Lists | Strict consistency | Flexible markers |
| **Redundancy** | **Eliminated (No figurative or poetic language)** | Acceptable |

## Robust AI Instruction Patterns

### Atomic Steps
- One action per step
- **Bad**: "Create file and write content."
- **Good**: "1. Create file. 2. Write content."

### Explicit Verification
- Mandate verification after every state-changing action
- Example: "Run `ls` to confirm file creation."

### Idempotent Commands
- Use commands safe to re-run
- **Bad**: `mkdir dir` (fails if exists)
- **Good**: `mkdir -p dir`

### Atomic Writes
- Write to temporary file → Move to final path
- Prevents partial file corruption on interrupt

## Anti-Patterns (Avoid)

| Pattern | Problem |
|---------|---------|
| `***bold italic***` | Mixed emphasis, unparseable |
| Mixed list markers (`-`, `*`, `+`) | Inconsistent |
| Multiple blank lines | Excessive whitespace |
| Skipped heading levels | Breaks hierarchy |
| Scattered inline links | Hard to extract |
| **Figurative/Poetic Language** | **Introduces semantic ambiguity and increased parsing load** |
| **Emotional Adjectives** | **Creates subjective bias; cannot be verified by system state** |

## Decision Framework

- **Audience: AI Systems** → AI-Optimized
- **Audience: Humans** → Human-Readable
- **Mixed Audience** → Err toward human-readable

---


## Origin

- 2025-12-11T1800: Created by Gemini
- 2026-01-02T0828 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
