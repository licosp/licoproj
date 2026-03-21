---
ai_visible: true
title: Package lico-lint
description: Behavioral rules for the lico-lint UV package.
tags: [package, rules, lico-lint]
version: 1.0.0
created: 2026-03-21T19:25:19+09:00
updated: 2026-03-21T19:25:19+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# lico-lint

## Objective

This file serves as the Agent-facing behavioral rule for the `lico-lint` workspace package.

## Functionality

It executes the following tools in sequence:

1. **Ruff Check**: Audits logic, imports, and potential bugs.
2. **Ruff Format**: Enforces a consistent, standardized layout.
3. **Pyright**: Performs fast, comprehensive static type analysis.
4. **Mypy**: Conducts rigorous, strictly-typed formal validation.

## Usage

You can run the linter on any directory or file within the Monolith:

```bash
# Check everything in the project root
uv run lico-lint .

# Check a specific package
uv run lico-lint packages/lico-devc/src

# Check a specific resident's workspace
uv run lico-lint .crew/iuria/licoproj
```

---

_Note: This tool is intended to run both on the host (WSL) and within the containerized village._

## Tool Usage Constraints

- **When to use**: Refer to the package's specific capabilities.
- **How to use**: Execute via `uv run lico-lint`.

---

## Related Documents

| Document                                 | Purpose             |
| :--------------------------------------- | :------------------ |
| [`packages/lico-lint/README.md`](/packages/lico-lint/README.md) | Package structural pointer |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---

## Origin

- 2026-03-21T1925 by Sirius: Created to fulfill the UV Package architecture aggregation.
