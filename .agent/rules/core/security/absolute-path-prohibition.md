---
ai_visible: true
title: Absolute Path Prohibition
description: Rules for using relative paths and sanitizing absolute paths to ensure security and portability.
tags: [security, paths, rules, sanitization]
version: 2.3
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-22T06:15:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Absolute Path Prohibition

## Summary

**NEVER use absolute paths in repository-facing content** (commits, issues, PRs, documentation).
Always use **relative paths** to ensure security, portability, and privacy.

> [!NOTE]
> For Markdown link formatting, see [path-notation.md](/.agent/rules/core/documentation/path-notation.md).

## Rationale

### Security Risks

Absolute paths can leak sensitive information:

- Local username: `/home/USER/...` → reveals OS user
- Directory structure: `/home/USER/develop/shared/...` → reveals project organization
- System paths: `/usr/local/...` → reveals system configuration

### Portability Issues

Absolute paths break when:

- Repository is cloned to different locations
- Different users collaborate
- CI/CD environments use different paths

## Rules

### 1. Artifacts & Commits (Strict)

**Strict Prohibition**: Any file committed to the repository MUST NOT contain absolute paths to the local environment.

**Protocol**:

- **Think**: `/home/USER/develop/shared/project/licoproj/README.md` (System requirement)
- **Write**: `README.md` or `./README.md` (Output filter)

### 2. IDE Protocol Sanitization (Strict)

**Strict Prohibition**: NEVER expose IDE-specific file protocols in external-facing content (GitHub issues, PRs, etc.).

**Prohibited Protocols**:

- `cci:7://file:///` (Cursor)
- `vscode://file/` (VS Code)
- `file:///` (Standard URI)

**Action**:

- Remove the protocol.
- Remove the absolute path prefix.
- Use the repository-relative path.

### 3. Conversation Logs (Best Effort)

**Best Effort**: While system tools (e.g., `view_file`) require absolute paths in their arguments (which are logged), the Agent SHOULD consciously sanitize paths in its **natural language responses** and **thoughts**.

### 4. Sanitization Protocol (Exceptions)

If a full path structure is absolutely necessary for context (e.g., documenting `mount` points or config examples), you **MUST** use one of the following generic placeholders:

- **Username Placeholder**: Replace specific user with `USER`.
  - ❌ `/home/USER/.gemini/`
  - ✅ `/home/USER/.gemini/`
- **Root Abbreviation**: Use `...` to trunkate the root.
  - ❌ `/home/USER/develop/shared/project/licoproj/packages/`
  - ✅ `.../licoproj/packages/`

## Examples

### Git Commits / Documentation

```
✅ docs: update .agent/rules/README.md
❌ docs: update /home/USER/develop/shared/project/licoproj/.agent/rules/README.md
```

### IDE Protocols (GitHub/Issues)

```
❌ See cci:7://file:///home/USER/develop/shared/project/licoproj/README.md
✅ See `README.md`
```

### Sanitized Exception

```
✅ "Ensure the config is at /home/USER/.config/myapp/settings.json"
❌ "Ensure the config is at /home/USER/.config/myapp/settings.json"
```

---

## Related Documents

| Document                                                                                  | Purpose                                   |
| :---------------------------------------------------------------------------------------- | :---------------------------------------- |
| [Map of Territory](/.agent/rules/map.md)                                                  | Repository Index (Integrated Navigation)  |
| [path-notation.md](/.agent/rules/core/documentation/path-notation.md)                     | Standard path notation for Markdown links |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | Structural standards                      |

---

## Origin

- 2025-12-01: Created as absolute path prohibition rule.
- 2026-01-13: Added link to path-notation.md (v1.1).
- 2026-01-22T0430 by Canopus: Initial 4-layer structure draft (v2.0).
- 2026-01-22T0500 by Canopus: Attempted link integration and shift to Origin-before-Links order (v2.1).
- 2026-01-22T0615 by Canopus: Final alignment; correctly established Related Documents Layer 3 and Origin Layer 4 (v2.3).
