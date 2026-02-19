---
context_id: "[Dependencies]"
default_phase: "(Maintenance)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-02-20T07:10:00+09:00
updated: 2026-02-20T07:10:00+09:00
tags: ["python", "node", "uv", "yarn", "packages"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Context Whiteboard: Dependency Management

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- プロジェクトの言語依存関係（パッケージ）を管理します。
- **Python**: `uv` (`pyproject.toml`, `uv.lock`)
- **Node.js**: `yarn` (`package.json`, `yarn.lock`)

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- **Update**: `uv sync`, `yarn install`, `yarn upgrade`
- **Add**: `uv add`, `yarn add`
- **Lockfiles**: Always commit lockfiles to ensure reproducible builds.
- **Cleanup**: Remove conflicting lockfiles (e.g., `package-lock.json` when using `yarn`).

---

## Agent Observations

### Sirius (2026-02-20)

- **Initialization**: Created this card to separate "Dependency State" from "Tech Stack Philosophy".
- **Tech Stack**:
  - Python: Managed by `uv`.
  - Node: Managed by `yarn`.

---

## Related Documents

| Document                                                       | Purpose                       |
| :------------------------------------------------------------- | :---------------------------- |
| [tech-stack-card.md](/.agent/cards/rules/tech-stack-card.md)   | Language selection philosophy |
| [environment-card.md](/.agent/cards/rules/environment-card.md) | OS/Container definitions      |
| [Map of Territory](/.agent/rules/map.md)                       | Root navigation map           |

---

## Origin

- 2026-02-20T07:10:00+09:00 by Sirius: Created for dependency management commits.
