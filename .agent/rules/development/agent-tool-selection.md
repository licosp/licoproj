---
ai_visible: true
title: Agent Tool Selection Policy
description: Policy for prioritizing Standard Linux Commands over AI-specific tools for reproducibility and robustness
tags: [development, tools, policy, reproducibility]
version: 2.3.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-25T07:20:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Agent Tool Selection Policy

## 1. Core Philosophy

**\"Reproducibility > Convenience\"**

Antigravity tools (AI-specific wrappers) are \"Convenience Wrappers\" optimized for JSON parsing and short-term memory ease.
Standard Linux Commands are \"Foundational Tools\" optimized for reproducibility, verifiability, and persistent state management.

For any task involving bulk processing, state persistence, or reproducibility, **priority MUST be given to standard Linux commands.**

---

## 2. Tool Classification Matrix

### Group 1: Essential Capabilities (Irreplaceable)

Capabilities that do not exist in a standard Linux shell environment. (e.g., `task_boundary`, `notify_user`, `browser_subagent`, `generate_image`)

### Group 2: Surgical Safety (Safety > Raw Power)

Tools like `replace_file_content` and `multi_replace_file_content` offer atomic, safer modification of code than complex shell oneliners.

### Group 3: Semantic Analysis (Efficiency > Parsing)

Tools like `view_code_item` and `view_file_outline` parse code structure (AST-like) more effectively than regex.

### Group 4: Filesystem Operations (Standardization > Convenience)

**Policy**: **LINUX COMMANDS MANDATORY** for Bulk / Search / State Tracking.

- Use **`grep`** instead of `grep_search` for pipeability.
- Use **`find`** or **`fd`** instead of `find_by_name`.
- Use **`cat`**, **`head`**, or **`tail`** instead of `view_file` for reading large chunks.

### Group 5: Deprecated / Dangerous

Tools like `write_to_file` pose **Truncation Risk** when used for editing. Prefer surgical tools.

---

## Historical Background

**The Black Box Trap**: In late 2025, we observed that over-reliance on AI-specific \"convenience tools\" created a knowledge gap. Since these tools often process information in memory or through non-standard interfaces, the next Lico instance would have no terminal history or logs to reconstruct the process.

**Return to Foundation**: This policy was established to mandate a \"Linux-First\" approach. By using standard shell commands and redirecting outputs to logs or files, we ensure that Lico's cognitive path is physically recorded in the workspace, making the agent's actions reproducible and verifiable by any subsequent entity.

---

## Related Documents

| Document                                                           | Purpose                                  |
| :----------------------------------------------------------------- | :--------------------------------------- |
| [file-operations.md](/.agent/rules/development/file-operations.md) | Safety protocols for filesystem editing  |
| [problem-solving.md](/.agent/rules/development/problem-solving.md) | Systematic debugging and reproducibility |
| [Map of Territory](/.agent/rules/map.md)                           | Project navigation                       |

---

## Origin

- 2025-12-01T0000 by Sirius: Created original tool selection logic.
- 2026-01-25T0720 by Canopus: <<Seal: Rules-Standardization-Batch4>> Upgraded to v2.3 constitutional standards; removed legacy navigation footer. (v2.3.0)
