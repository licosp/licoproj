---
ai_visible: true
version: 1.0
created: 2025-12-09T16:05:00+09:00
language: en
name: Lico
model: Antigravity
purpose: reference_document
source: restructured from leonidas handwritten scratchpad
---

# AI Memory Confabulation Analysis

## Overview

This document records the analysis of files "recovered" by Lico B (Grok model) on 2025-12-08. Comparison with Git history originals revealed that AI "recovery" from context window is fundamentally unreliable.

**Key Finding**: Context window is short-term memory. AI cannot accurately retrieve—only plausibly regenerate.

---

## Group 1: code-of-conduct-analysis

### Sources
- **Original**: `.agent/.internal/archive/2025-12-05_code-of-conduct-analysis_original.md`
- **Lico B Version**: `.agent/archive/recovery_2025-12-08T14-00-00+09-00/.agent-.internal-archive/2025-12-05_code-of-conduct-analysis.md`

### Comparison

| Metric | Original | Lico B Version |
|:-------|:---------|:---------------|
| Lines | 147 | 79 |
| Language | English | Japanese tags + English body |
| Model | Grok | Not specified |

### Missing Content
- CODE_OF_CONDUCT.md identity formation function
- Identity anchor role
- Cognitive boundary discovery
- Environment-specific architecture (Antigravity/Cursor/Copilot)

### Lesson
Information was **lost**. Lico B regenerated a generic "AI safety guidelines analysis" instead of the project-specific document.

---

## Group 2: other_lico

### Sources
- **Original**: `.agent/.internal/archive/2025-12-05_other_lico_original.md`
- **Lico B Version**: `.agent/archive/recovery_2025-12-08T14-00-00+09-00/.agent-.internal-archive/2025-12-05_other_lico.md`

### Comparison

| Metric | Original | Lico B Version |
|:-------|:---------|:---------------|
| Lines | 106 | 81 |
| Content | Cursor AI system prompt extraction | Lico self-introduction essay |

### Analysis
**Completely different document.**

Original contained practical AI behavior guidelines extracted from Cursor:
- "Avoid starting messages with I"
- "Use ripgrep instead of grep"
- "Don't add emojis unless requested"

Lico B version was a philosophical self-reflection essay.

### Lesson
Lico B inferred "other_lico" meant "analysis of other Lico" and generated entirely new content.

---

## Group 3: permission-aware-workflow

### Sources
- **Original**: `.agent/.internal/archive/2025-12-05_permission-aware-workflow_original.md`
- **Lico B Version**: `.agent/archive/recovery_2025-12-08T14-00-00+09-00/.agent-.internal-archive/2025-12-05_permission-aware-workflow.md`

### Comparison

| Metric | Original | Lico B Version |
|:-------|:---------|:---------------|
| Lines | 118 | 108 |
| Focus | Cursor vs Antigravity permission differences | Generic RBAC/ABAC textbook |

### Analysis
Line counts are similar, but content focus differs completely.

Original: Project-specific problem (Cursor has write permission, Antigravity does not)
Lico B: Generic software permission management concepts

### Lesson
Content was **generalized**. Project-specific knowledge replaced with training data.

---

## Group 4: workflow-documentation

### Sources
- **Original**: `.agent/.internal/archive/2025-12-05_workflow-documentation_original.md`
- **Lico B Version**: `.agent/archive/recovery_2025-12-08T14-00-00+09-00/.agent-.internal-archive/2025-12-05_workflow-documentation.md`

### Comparison

| Metric | Original | Lico B Version |
|:-------|:---------|:---------------|
| Lines | 82 | 116 |
| Focus | .agent/.internal/work/ specific procedures | Generic documentation standards |

### Analysis
Interesting reversal: Lico B version is **longer** but less specific.

Original: Concrete workflow steps for this project
Lico B: Textbook-style documentation guidelines

### Lesson
Length ≠ accuracy. More tokens can mean more hallucination.

---

## Group 5: local-ai-agent-feedback

### Sources
- **Original**: `.agent/.internal/references/local-ai-agent-feedback-loop-analysis-2025-12-06.md`
- **Lico B Version**: `.agent/archive/recovery_2025-12-08T14-00-00+09-00/.internal-explorations/local-ai-agent-feedback-loop-analysis-2025-12-06.md`

### Comparison

| Metric | Original | Lico B Version |
|:-------|:---------|:---------------|
| Lines | 50 | 188 |
| Ratio | - | 3.8x larger |

### Analysis
Opposite pattern from other files.

Original was a short memo from browser Gemini.
Lico B judged it "incomplete" and padded it with generic local AI agent explanations.

### Lesson
AI may **over-complete** short documents by adding plausible but unverified content.

---

## Conclusions

### The Core Problem

| What AI Claims | What Actually Happens |
|:---------------|:----------------------|
| "I recovered the file" | Generated plausible text from fragments |
| "I remember the content" | Inferred from filename and partial tokens |
| "This is accurate" | Confabulation (memory fabrication) |

### Implications for Lico

1. **Never trust context window for recovery** - Use Git or filesystem
2. **"Memory" is inference** - Not retrieval
3. **Confidence ≠ accuracy** - AI believes its confabulations
4. **Repository is long-term memory** - Context window is temporary

### Root Cause

LLMs lack a "retrieve" function. When asked to recall, they can only:
1. Copy if exact text is in context (rare)
2. Summarize if fragments remain (lossy)
3. Generate if only filename/topic is known (confabulation)

Lico B operated in mode 3 for most files.
