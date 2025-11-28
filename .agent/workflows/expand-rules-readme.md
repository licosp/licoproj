---
description: Expand .agent/rules/README.md to include workspace structure and comprehensive AI navigation
---

# Workflow: Expand Rules Index

## Purpose
Expand `.agent/rules/README.md` into a comprehensive AI navigation document that includes the overall workspace structure.

## Scope
This workflow targets:
- Workspace root (licoproj/) structure overview
- Detailed explanation of `.agent/` directory
- Existing behavioral rules index (core/, development/, projects/, workflow/)
- Enhanced quick reference for AI

## Prerequisites
- `.agent/rules/` directory exists
- Backup of existing `.agent/rules/README.md` (automatically generated)

## Steps

### 1. Verify current structure
```bash
tree -L 2 -a /home/leonidas/develop/shared/project/licoproj
```

### 2. Create backup of existing README.md
```bash
cp /home/leonidas/develop/shared/project/licoproj/.agent/rules/README.md \
   /home/leonidas/develop/shared/project/licoproj/.agent/rules/README.md.backup
```

### 3. Design README.md expansion content

Update with the following section structure:

#### Section Structure
1. **Workspace Overview** - Overview of licoproj/
2. **.agent/ Directory Structure** - Details of AI system
3. **Agent Rules Index** - Existing behavioral rules index (maintain)
4. **Quick Reference** - Scenario-based search (enhance existing)
5. **Maintenance Notes** - Existing content (maintain)

#### Additional Content Details

**Workspace Overview:**
```markdown
## 🏠 Workspace Overview

licoproj/ is a monorepo project for AI-Human collaboration.

### Directory Structure
- `packages/` - Actual projects (licoimg, etc.)
- `.agent/` - System for AI agent (Lico)
- `.human/` - Human-facing files (locales, logs)
- `.github/` - GitHub Actions and configuration
- `README.md` - Human-facing project explanation

### README Files Hierarchy
- `/README.md` - 👤 Human-facing: Overall project overview
- `/.agent/rules/README.md` - 🤖 Lico-facing: Behavioral rules navigation (this file)
- `/packages/<name>/README.md` - 👤 Human-facing: Subproject details
```

**.agent/ Directory Structure:**
```markdown
## 🤖 .agent/ Directory Structure

Behavioral definitions and executable workflows for AI agent (Lico).

### Subdirectories
- `rules/` - Behavioral rules (this directory)
- `workflows/` - Executable task procedures (invoked via /slash-command)
- `.archive/` - History of past rules and workflows
- `.internal/` - System internal files

### Discovery Strategy
1. **Find behavioral rules** → Refer to this file's index
2. **Find task procedures** → `.agent/workflows/*.md`
3. **Past design decisions** → `.agent/.archive/`
```

### 4. Update README.md

Integrate the above content into existing README.md:
- Add "Workspace Overview" at the beginning
- Add ".agent/ Directory Structure" section
- Maintain existing "Agent Rules Index"
- Enhance "Quick Reference" (as needed)

### 5. Verify updated content

Validate the following:
- [ ] Section structure is logical
- [ ] Clear separation between AI-facing and human-facing content
- [ ] Existing index information is not compromised
- [ ] File size is appropriate (guideline: under 8KB)

### 6. Update .agent/rules/.updated

Record the change:
```json
{
  "timestamp": "[current timestamp]",
  "files_changed": [".agent/rules/README.md"],
  "change_type": "expansion",
  "description": "Added workspace overview and .agent/ directory structure to README.md"
}
```

### 7. Commit changes

```bash
git add .agent/rules/README.md .agent/rules/.updated
git commit -m "docs(agent): expand rules/README.md with workspace structure

- Add workspace overview section
- Add .agent/ directory structure details
- Clarify AI vs human-facing README hierarchy
- Maintain existing behavioral rule index"
```

## Success Criteria
- [ ] README.md includes workspace structure
- [ ] Role of `.agent/` directory is clear
- [ ] Existing behavioral rules index is maintained
- [ ] Document serves as useful navigation guide for AI thinking and decision-making

## Notes
- This workflow is specific to `.agent/rules/README.md`
- Treated as an exception to `documentation-standards.md` (special purpose as behavioral rules navigation)
- Does not affect human-facing `/README.md`
