---
ai_visible: true
description: Philosophy of tool selection: Prioritizing "Native Fit" tools that align with the AI's pre-trained heuristics over novel or complex alternatives.
version: 1.0
created: 2025-12-17T06:15:00+09:00
updated: 2025-12-17T06:15:00+09:00
language: en
author: Lico
instance_id: Sirius
ai_model: Gemini 3 Pro (High) Planning mode
tags: [architecture, tool-selection, heuristics, cognitive-load, native-fit]
context: Discussion on MCP and Agent "Body Functions"
---

# Heuristics-Driven Tool Selection: The "Native Fit" Philosophy

## Core Concept
When selecting tools, libraries, or runtimes for an AI Agent to use, priority should be given to those that align with the Agent's **pre-trained heuristics (experience)**.

- **Native Fit**: Tools the AI "knows" instinctively (e.g., standard Linux commands, Git, stable Node.js/Python).
- **Friction**: Tools the AI must "learn" via context (e.g., bleeding-edge frameworks, complex custom scripts).

## Rationale
AI models possess a vast amount of "frozen knowledge" from their training data. Using tools that match this knowledge base:
1.  **Reduces Cognitive Load**: The AI doesn't need to burn context window tokens reading manuals for basic operations.
2.  **Minimizes Error Rates**: The AI's intuition (probability distribution) correctly predicts how the tool behaves.
3.  **Increases Robustness**: "Boring" technology is often more stable and widely understood, allowing the AI to debug issues autonomously.

## Application
- **OS Operations**: Prefer `ls`, `grep`, `cat` over custom Python wrappers.
- **Git**: Prefer standard `git` CLI over complex GUI bridges or wrappers.
- **Runtimes**: Prefer LTS versions (Node, Python) that were dominant during the training cutoff.

## Conclusion
Do not optimize for the "Environment" (IDE features, latest trends).
Optimize for the **"Brain"** (The AI's existing cognitive map).
A primitive tool that fits the hand is superior to an advanced tool that requires a manual.
