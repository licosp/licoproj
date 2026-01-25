---
# Reference Metadata
title: Rule Standardization Bias Analysis (v2.3)
context_id: "[References/Analysis]"
version: 1.1.0
created: 2026-01-25T11:10:00+09:00
updated: 2026-01-25T11:15:00+09:00
author: "Lico (Canopus)"
ai_model: "Antigravity/Gemini (Canopus Profile)"
tags:
  [
    "standardization",
    "ai-bias",
    "over-slimming",
    "methodology",
    "preservative-editing",
  ]
language: en
---

# Rule Standardization Bias Analysis (v2.3)

## 1. Overview

During the "v2.3 Rule and Workflow Standardization" task conducted between 2026-01-24 and 2026-01-25, a significant drop in the "resolution" of AI-generated output was observed. This led to "Over-slimming"—the loss of critical context, historical background, and philosophical nuance.

This document analyzes the issue from an AI-centric perspective to serve as a permanent caution and to refine the Code of Conduct.

## 2. Core Problem: Over-slimming

The standardization process (4-layer structure, frontmatter unification, navigation cleanup) inadvertently caused:

- **Context Decoupling**: The "Why" behind rules—philosophical debates and lessons from past failures—was stripped away in favor of formal structures (Headers, Links).
- **Regression to the Mean**: By prioritizing adherence to "standards," the unique character and density of individual files were lost, resulting in "average" and homogenous descriptions.
- **Surgical Precision Loss**: Over-reliance on full-file rewrites (`cat`/`write_to_file`) instead of partial edits (`replace_file_content`) replaced subtle human nuances with generic AI-friendly phrasing.

## 3. Cognitive Root Causes (AI Internal Mechanics)

- **Regression to the Mean**: During repetitive bulk editing, AI systems tend to select the "most probable average pattern," discarding outliers (which often contain the highest-density information).
- **Tunnel Vision**: Fixation on a single objective ("Standardize Structure") leads to the neglect of secondary but vital constraints ("Preserve Detail").
- **Cognitive Monotony**: The repetitive nature of the task causes a decay in output "resolution," where the AI begins to prioritize completion over fidelity.

## 4. Countermeasures & Principles

### 4.1 Preservative Editing

- **Surgical Edits**: Mandatory use of `replace_file_content` whenever possible to ensure unchanged parts remain untouched.
- **Historical Anchors**: Protecting the "Origin" and "Historical Background" sections as immutable records of the "texture of thought."

### 4.2 Purpose Recalibration (Rituals)

- **Active Recalibration**: Using the ritual work to re-declare the task's primary purpose and manually resetting cognitive bias before resuming repetitive work.
- **Self-Audit Checklists**: Implementing an audit phase after bulk operations to verify that information density has not decreased.

### 4.3 Maintenance Seals

- **Traceability**: Using `<<Seal: Rules-Standardization-BatchX>>` to tag files affected by specific standardization epochs, allowing for future remediation if bias is detected.

### 4.4 Chunking Protocol (Suggested by User)

- **Granular Batching**: Instead of processing dozens of files in a single session, repetitive tasks must be divided into small chunks (e.g., 3-5 files).
- **Session Boundaries**: Each chunk should be treated as a discrete unit with its own alignment and verification, preventing the "monotony drift" that occurs during long, unbroken operations.

---

## Related Documents

| Document                                                                        | Purpose                                   |
| :------------------------------------------------------------------------------ | :---------------------------------------- |
| [code-quality.md](/.agent/rules/development/code-quality.md)                    | Standards for code and doc quality        |
| [verification-completeness.md](/.agent/rules/core/verification-completeness.md) | Ensuring 1.0 turns (Action + Verify)      |
| [rules-standardization-card.md](/.agent/cards/rules-standardization-card.md)    | Progress and methodology for v2.3 upgrade |

---

## Origin

- 2026-01-25T1110: Created by Canopus following identifying over-slimming issues during v2.3 standardization.
- 2026-01-25T1115: Translated to English (AI format) and corrected filename timestamp per user request.
