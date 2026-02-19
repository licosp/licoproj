---
# Context Configuration
context_id: "[Tech-Stack]"
default_phase: "(Rule)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-02-19T08:25:00+09:00
updated: 2026-02-19T12:06:00+09:00
tags: [rules, standards, tech-stack, python, bash]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Technology Stack Standards

This card defines the approved technology stack for the \`licoproj\` workspace and the rules for their usage.

---

## 1. Core Languages

### 1.1 Python (Primary Logic)

- **Role**: Complex scripts, automation logic, data processing.
- **Standard**: **Strict Mode**.
  - **Type Hints**: Mandatory for all function signatures and complex variables.
  - **Linting**: Compliant with standard linters (ruff/flake8).
  - **Formatting**: Auto-formatted (black/isort).
  - **Runtime Strategy**: Use `uv` + Command Shims (Future Roadmap).

### 1.2 Bash (Infrastructure Glue)

- **Role**: Command composition, file movement, simple environment checks.
- **Standard**: **Primitive Only**.
  - Avoid complex logic (arrays, loops).
  - Use for linear execution flow.

---

## 2. Infrastructure Tools

### 2.1 uv (Python Manager)

- **Role**: Fast Python package installer and resolver.
- **Status**: **Planned** (See Roadmap).
- **Usage**: Will be integrated via Command Shims to transparently manage runtimes.

### 2.2 Command Shims

- **Role**: Intercepting and sanitizing dangerous commands (git, rm, etc.).
- **Location**: `.agent/scripts/` (Implementation) -> `.runtimes/bin/` (Symlinks).

---

## 3. Related Documents

| Document                                                                     | Purpose                           |
| :--------------------------------------------------------------------------- | :-------------------------------- |
| [ai-script-philosophy.md](/.agent/rules/development/ai-script-philosophy.md) | Decision logic for choosing tools |
| [command-shims.md](/.agent/rules/development/command-shims.md)               | Shim protocol details             |
| [Map of Territory](/.agent/rules/map.md)                                     | Root navigation map               |

---

## Origin

- 2026-02-19: Created by Sirius to formalize the "Strict Python" decision.
