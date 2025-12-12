---
description: Proposal for absolute path prohibition in repository-facing content
created: 2025-11-30T19:58:07+09:00
status: proposal
category: security-and-portability
---

# Absolute Path Prohibition

## Summary
NEVER use absolute paths in repository-facing content (commits, issues, PRs, documentation). Always use relative paths to ensure security, portability, and privacy.

## Rationale

### Security Risks
Absolute paths can leak sensitive information:
- Local username: `/home/leonidas/...` → reveals OS user
- Directory structure: `/home/leonidas/develop/shared/...` → reveals project organization
- System paths: `/usr/local/...` → reveals system configuration

### Portability Issues
Absolute paths break when:
- Repository is cloned to different locations
- Different users collaborate (different home directories)
- CI/CD environments use different paths
- Repository is migrated to different machines

### Privacy Concerns
GitHub issues, PRs, and commits are public. Absolute paths expose:
- User identity
- File system structure
- Development environment details

## Rules

### ✅ Use Relative Paths

**In Git commits:**
```
✅ docs: update .agent/rules/README.md
❌ docs: update /home/leonidas/develop/shared/project/licoproj/.agent/rules/README.md
```

**In issue comments:**
```
✅ See `.agent/workflows/prepare-commit.md` for details
❌ See `/home/leonidas/develop/shared/project/licoproj/.agent/workflows/prepare-commit.md`
```

**In PR descriptions:**
```
✅ Modified `packages/licoimg/src/main.js`
❌ Modified `/home/leonidas/develop/shared/project/licoproj/packages/licoimg/src/main.js`
```

**In documentation:**
```markdown
✅ Check `.agent/rules/core/identity.md`
❌ Check `/home/leonidas/develop/shared/project/licoproj/.agent/rules/core/identity.md`
```

### Exceptions (Where Absolute Paths Are Acceptable)

**1. System-level documentation (not in repo):**
- `~/.gemini/antigravity/brain/` (Antigravity system path)
- `/usr/local/bin/gh` (system binary location)

**2. AI-internal artifacts (not committed):**
- Task plans in `~/.gemini/`
- Temporary files

**3. Explicitly documenting external tools:**
```markdown
The gh CLI is located at `/home/leonidas/.agent/runtimes/gh_2.40.1_linux_amd64/bin/gh`
```
(Only when documenting the tool installation itself)

## Implementation

### Detection Strategy
Use pre-commit hooks or AI self-review to detect absolute paths:

```bash
# Detect absolute paths in staged files
git diff --cached | grep -E "^[+].*(/home/|/Users/|C:\\)" 
```

### Remediation
If absolute path is detected:
1. Convert to relative path from repository root
2. Use backticks for file paths in markdown
3. Remove username/sensitive directory names

### Proposed Rule Location
Add to `.agent/rules/development/git-operations.md`:

```markdown
## Path Usage in Repository Content

**NEVER use absolute paths in:**
- Commit messages
- Issue comments
- PR descriptions
- Documentation files

**ALWAYS use relative paths from repository root.**

**Rationale**: Security, portability, privacy.
```

## Origin
This principle was identified during the development of Issue #6 (README expansion) and has been a recurring guideline in Lico's workflow.

Reference: `.agent/rules/README.md` line 4:
> "Follow the **Agent Rules Index** strictly, especially the prohibition of absolute paths and reliance on relative paths."

## Impact
- **High security**: Prevents information leakage
- **High portability**: Repository works anywhere
- **Low disruption**: Easy to follow with awareness
- **Scope**: All repository-facing content
