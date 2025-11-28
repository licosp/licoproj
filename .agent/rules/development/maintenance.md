---
description: Guidelines for maintaining project consistency and documentation
---

# Project Maintenance Guidelines

## Hook File Synchronization

### Core Requirement

**Hook files must always be synchronized to maintain consistency across different AI models.**

### Affected Files

The following hook files must contain identical content:

- `CODE_OF_CONDUCT.md`
- `.github/copilot-instructions.md`

### Synchronization Protocol

1. **When updating rules**: Modify the primary hook file first
2. **Immediate sync**: Copy content to all other hook files
3. **Verification**: Ensure diff shows no differences
4. **Documentation**: Update `.agent/rules/.updated` with synchronization note

### Primary Hook File

**`CODE_OF_CONDUCT.md`** serves as the primary hook file for:
- General AI assistants
- Documentation consistency
- User-facing behavioral guidelines

### Secondary Hook Files

**`.github/copilot-instructions.md`** serves as:
- GitHub Copilot specific entry point
- IDE-integrated AI assistance

### Implementation

#### Sync Command
```bash
# Sync .github/copilot-instructions.md with CODE_OF_CONDUCT.md
cp CODE_OF_CONDUCT.md .github/copilot-instructions.md
```

#### Verification
```bash
# Verify synchronization
diff CODE_OF_CONDUCT.md .github/copilot-instructions.md
# Should return no output if synchronized
```

### Rationale

- **Consistency**: All AI models receive identical behavioral guidelines
- **Maintenance**: Single source of truth reduces synchronization errors
- **Reliability**: Prevents divergent behavior between different AI models
- **Transparency**: Clear protocol ensures accountability

### Exception Handling

If hook files must differ:
1. Document the specific differences and rationale
2. Create separate rule files for divergent requirements
3. Maintain synchronization for all common content

## Issue Archival Standards

### Purpose
Archive GitHub issue data locally for offline access and migration support.

### Location
Store in `.agent/issues/` directory with structured JSON format.

### File Naming
`issue-{number}-github-complete-data.json`

### Data Structure
```json
{
  "metadata": {
    "description": "Purpose and capture info",
    "capture_timestamp": "ISO8601",
    "purpose": ["offline_access", "recovery", "reference", "migration"]
  },
  "issue": { /* Complete issue data */ },
  "comments": [ /* All comments */ ],
  "related_pull_requests": [ /* Linked PRs */ ],
  "related_branches": [ /* Connected branches */ ],
  "statistics": { /* Summary stats */ }
}
```

### Update Triggers
- When issue status changes (open/close)
- When new comments are added
- Before major repository operations
- During migration planning
