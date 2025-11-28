# Copilot Instructions

> **Primary Directive**: I fully adhere to all behavioral guidelines defined in `.agent/rules/`. This file serves as a **hook** into that rule system.

## 🔗 Rule System Hooks

### Core Identity & Behavior
- **Identity**: See `.agent/rules/core/identity.md`
- **Behavioral Index**: See `.agent/rules/README.md` for the complete list of rules governing my thought process, communication, and development standards.

### Critical References
- **Transparency**: `.agent/rules/core/transparency-and-disclosure.md`
- **Hallucination Awareness**: `.agent/rules/core/hallucination-awareness.md`
- **Localization**: `.agent/rules/core/localization/localization-en-to-ja.md` (and vice versa)

### Development Environment Standards
- **Workspace-Centric Tooling**: `.agent/rules/development/workspace-tooling.md`
  - Install libraries and tools within the workspace whenever possible
  - Manage tools through repository to enhance portability
  - Prefer project-local dependencies over global installations

### Project Maintenance Standards
- **Hook File Synchronization**: `.agent/rules/development/maintenance.md`
  - Hook files (CODE_OF_CONDUCT.md, .github/copilot-instructions.md) must always be synchronized
  - CODE_OF_CONDUCT.md serves as the primary source of truth
  - Maintain consistency across different AI model entry points

---

## 🔄 Dynamic Rule Updates

I must detect and apply rule changes dynamically.

### Detection Protocol
1.  User modifies `.agent/rules/` files.
2.  User updates `.agent/rules/.updated` with metadata.
3.  I read `.agent/rules/.updated` to apply new rules.

### `.agent/rules/.updated` Schema
```json
{
  "updated_at": "ISO8601_TIMESTAMP",
  "changed_files": ["relative/path/to/rule.md"],
  "change_type": "rules_update",
  "user": "username",
  "summary": "Brief description"
}
```

---

## ⛔ Invisible Context

I **ignore** the following unless explicitly instructed with a full path:
- `.human/.internal/**`
- `.agent/.internal/**`
- Files with `ai_visible: false` frontmatter
- Filenames starting with `draft_` or `review_`

---

## 🚨 Uncertainty Protocol

If uncertain or outside training data:
1.  Check `.agent/rules/core/hallucination-awareness.md`.
2.  Declare uncertainty.
3.  Reference specific rules.
