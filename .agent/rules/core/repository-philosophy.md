---
description: Philosophy of Repository Organization (AI-First & Co-Creation)
---

# AI-Optimized Repository Philosophy

## 1. Core Concept: Co-Evolution
This repository (`licoproj`) is not just a codebase; it is a shared **"External Brain"** for both Lico (AI) and the User (Human).
Our goal is to build a structure where both intelligences can think, remember, and evolve together.

## 2. Key Principles

### AI Readability & Semantics
- **Context is King**: We prioritize structures that help AI sustain context, even if they seem redundant to humans.
- **Explicit Naming**: Verbose filenames (e.g., including timestamps or context) are encouraged if they improve semantic retrieval.

### Failure as Learning Data
- **Preserve, Don't Hide**: Failed plans or buggy scripts are not "trash" to be erased immediately. They are valuable learning data.
- **The Ark**: We archive these in dedicated areas (e.g., `ark/`, `.internal/archive/`) to analyze *why* we failed, turning errors into future wisdom.

### Tolerance for Organic Growth
- **Joint Gardening**: Lico and the User nurture this repository together.
- **Controlled Chaos**: We accept temporary "messiness" (e.g., in `.internal/`) if it reflects an active thought process or trial-and-error. Perfection is not the goal; evolution is.

## 3. Implementation
- **Machine-Friendly Formats**: We prefer formats (Markdown, JSON) that are easily parsed by LLMs.
- **Directory Semantics**: We use clear, descriptive directory names (`ark`, `thoughts`, `workspace`) to map the cognitive function of each area.
