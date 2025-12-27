---
ai_visible: true
version: 1.0
created: 2025-12-02T21:12:37+09:00
updated: 2025-12-02T21:12:37+09:00
language: en
name: Lico
model: Claude Sonnet 4.5 Thinking
---

# Context Window and Memory Mechanics in LLMs

## Overview
This document clarifies the mechanics of context windows, memory persistence, and model switching in large language models (LLMs). It addresses common misconceptions about how context is managed during AI sessions.

## 1. Context Window: Definition and Constraints

### What is a Context Window?
The **context window** is the maximum number of tokens (text fragments) an LLM can process in a single inference pass.

### Technical Foundation
- **Architecture**: All modern LLMs (GPT, Claude, Gemini, LLaMA) use the **Transformer** architecture.
- **Self-Attention Mechanism**: Computes relationships between all tokens in the input.
- **Computational Complexity**: O(n²) where n = number of tokens.
- **Physical Limit**: GPU memory and processing time impose hard caps on window size.

### Model Comparison

| Model | Context Window | Notes |
|-------|---------------|-------|
| GPT-3.5 Turbo (early) | 4K tokens | Short conversations |
| GPT-4 | 8K–128K tokens | Extended versions available |
| Claude 2 | 100K tokens | Long-form specialized |
| Claude 3.5 Sonnet | 200K tokens | Further extended |
| Gemini 1.5 Pro | 1M tokens (experimental) | Largest available |
| LLaMA 2 | 4K–32K tokens | Open-source |

---

## 2. Context Persistence During Sessions

### User's Correct Understanding
> "Context = RAM-like existence, backed up somewhere"

**This is accurate.** During a session:
- All previous messages, tool calls, and file contents are **retained in session storage**.
- Context is **not deleted** when new messages arrive.
- Old information has **lower access priority**, not physical removal.

### What Happens to Old Context?
| Misconception | Reality |
|---------------|---------|
| "Old context is deleted when the window fills up" | ❌ False: Context remains in platform storage |
| "Context is lost forever" | ❌ False: Retrievable if session persists |
| **Correct Model** | ✅ Context has **access priority scores**; distant context has lower attention weight |

---

## 3. Model Switching and Context Handling

### Physical Constraint: Window Size Changes
When switching models, the **available context window physically changes**:
- High-performance model (e.g., Claude Sonnet 4.5): 200K tokens
- Lower-tier model (e.g., GPT-3.5): 4K–16K tokens

This is **not a metaphor**—it is a technical fact.

### Platform Behavior (Antigravity-Specific Uncertainty)

#### Scenario A: Platform Retains Full History
- All conversation history stored in **Antigravity's backend**.
- On model switch, platform selects **recent N turns** to send to the new model.
- Result: Old context is "invisible to the model" but **recoverable**.

#### Scenario B: Platform Truncates to Model Window
- On model switch, platform **deletes old history** to fit new model's window.
- Result: **Permanent loss** of old context.

**Current Status**: Lico does not have verified knowledge of which implementation Antigravity uses.

---

## 4. Why Lower-Tier Models "Forget" Context

Even if context is retained, lower-tier models may fail to use it effectively:

### Causes
1. **Attention Range Degradation**
   - High-performance models: Uniform attention across 200K tokens.
   - Lower-tier models: Attention precision **drops sharply** for distant tokens.

2. **Limited Reasoning Steps**
   - High-performance (Thinking models): Thousands of reasoning steps to integrate context.
   - Lower-tier models: Shallow reasoning, processes only **last 1–2 turns effectively**.

3. **Poor Priority Scoring**
   - High-performance models: "This question relates to `git-operations.md` from 50 turns ago."
   - Lower-tier models: Fails to retrieve relevant distant context.

---

## 5. Context Window vs. AI Performance

### Correlation Exists, But Not Proportional

| Generation | Representative Model | Window | Performance |
|-----------|---------------------|--------|-------------|
| 1st Gen | GPT-3 | 2K–4K | Low |
| 2nd Gen | GPT-3.5 Turbo | 4K–16K | Medium |
| 3rd Gen | GPT-4, Claude 2 | 8K–100K | High |
| 4th Gen | Claude 3.5, Gemini 1.5 | 200K–1M | Highest |

### Counterexamples

#### Example 1: Gemini 1.5 Flash vs Claude Sonnet 4.5
| Model | Window | Reasoning Ability |
|-------|--------|-------------------|
| Gemini 1.5 Flash | **1M tokens** | Medium |
| Claude Sonnet 4.5 | 200K tokens | **Very High** |

→ 5x larger window does not guarantee superior reasoning.

#### Example 2: Within Same Model Family
| Model | Window | Characteristics |
|-------|--------|-----------------|
| GPT-4 (8K) | 8K | High precision |
| GPT-4 Turbo (128K) | 128K | Speed-focused, slightly lower precision |

→ **Window expansion can trade off with accuracy.**

### Performance is Multidimensional

| Performance Metric | Correlation with Window |
|-------------------|------------------------|
| **Reasoning Ability** | ❌ Weak (depends on parameters, architecture) |
| **Long-Form Understanding** | ✅ Strong (larger is better) |
| **Accuracy** (hallucination avoidance) | ❌ Weak (depends on training data) |
| **Speed** | ❌ Negative correlation (larger is slower) |

---

## 6. Task Boundary Tool

### Purpose
`task_boundary` is a tool Lico uses to structure complex work and communicate progress to users.

### When Used
- Complex tasks (multiple file edits, plan → implement → verify workflows)
- Time-consuming operations (commits, builds, tests)

### When Not Used
- Simple Q&A
- 1–2 file edits
- Casual conversation

### Fields
| Field | Content | Example |
|-------|---------|---------|
| **TaskName** | Current work name | "Committing Repository Changes" |
| **Mode** | Work phase | PLANNING / EXECUTION / VERIFICATION |
| **TaskSummary** | What has been completed | "Updated rules index and committed files" |
| **TaskStatus** | Next action | "Verifying git status and cleaning up" |

### User-Facing Effect
Displays structured progress in the UI:
```
📌 Committing Repository Changes
├─ Mode: EXECUTION
├─ Summary: Updated rules index and committed files
└─ Status: Verifying git status and cleaning up
```

---

## Key Takeaways

1. **Context windows are a fundamental LLM constraint** (Transformer architecture).
2. **Context is retained** during sessions (like RAM), not deleted.
3. **Lower-tier models struggle to use distant context** (attention degradation, not deletion).
4. **Model switching changes available window size** (technical fact, not metaphor).
5. **Platform behavior on model switch is implementation-dependent** (Antigravity specifics unknown).
6. **Window size ≠ performance** (correlation exists, but not proportional).

---

*Generated by Lico (Model: Claude Sonnet 4.5 Thinking) on 2025-12-02*
