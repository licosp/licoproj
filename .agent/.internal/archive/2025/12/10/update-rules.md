---
description: Workflow for updating behavioral rules with backup and verification
---

# Update Rules Workflow

## Purpose
Update behavioral rules in `.agent/rules/` with proper backup, verification, and change tracking via `.agent/rules/.updated`.

## Prerequisites
- Git repository is initialized
- `.agent/rules/` directory exists
- `.agent/.internal/updated_history/` directory exists (created automatically if needed)
- `.agent/.archive/` directory exists (created automatically if needed)

## Steps

### 1. Backup Current State
Create a full backup of the rules directory and the .updated file.

```bash
# Create backup directories if not exists
mkdir -p .agent/.internal/updated_history
mkdir -p .agent/.archive

# Backup .updated with timestamp
TIMESTAMP=$(date +%Y-%m-%d_%H-%M-%S)
cp .agent/rules/.updated .agent/.internal/updated_history/${TIMESTAMP}.json

# Create full archive of rules directory
tar -czf .agent/.archive/rules_${TIMESTAMP}.tar.gz .agent/rules/
```

### 2. Identify Changes
Determine which rule files you will modify:
- List affected files
- Note the type of change (new file, modification, deletion, reorganization)

### 3. Edit Rule Files
Make your changes to `.agent/rules/` files:
- Follow granularity standards (20-100 lines per file)
- Include YAML frontmatter with `description`
- Maintain consistent markdown formatting

### 4. Validate Changes
Run the validation script to ensure integrity.

```bash
# Run validation script
python3 .agent/scripts/validate_rules.py
```

**If validation fails, fix the issues before proceeding.**

### 5. Update `.agent/rules/.updated`
Create new `.updated` file with metadata:

```bash
cat <<EOF_UPDATED > .agent/rules/.updated
{
  "updated_at": "$(date -Iseconds)",
  "changed_files": [
    ".agent/rules/path/to/changed/file1.md",
    ".agent/rules/path/to/changed/file2.md"
  ],
  "change_type": "rules_update",
  "user": "$(whoami)",
  "summary": "Brief description of changes"
}
EOF_UPDATED
```

**Fields**:
- `updated_at`: ISO 8601 timestamp (YYYY-MM-DDTHH:MM:SS+TZ)
- `changed_files`: Array of relative paths from repo root
- `change_type`: Always `"rules_update"`
- `user`: Agent name or username
- `summary`: One-line description of what changed

### 6. Verification
Verify changes are complete:
- [ ] All modified files have correct YAML frontmatter
- [ ] File sizes within granularity limits
- [ ] Cross-references updated (e.g., `README.md`)
- [ ] `.updated` file is valid JSON
- [ ] Backup exists in `.agent/.internal/updated_history/` and `.agent/.archive/`
- [ ] Validation script passed

### 7. Optional: Commit to Git
If changes are significant, commit immediately:
```bash
git add .agent/rules/
git commit -m "docs(rules): <summary from .updated>"
```

## Recovery

### Restore Previous State
```bash
# List available backups
ls -lt .agent/.archive/

# Restore specific backup (WARNING: Overwrites current rules)
# Extract to a temp dir first to verify if needed
tar -xzf .agent/.archive/rules_YYYY-MM-DD_HH-MM-SS.tar.gz -C .
```

### Restore Previous .updated
```bash
cp .agent/.internal/updated_history/YYYY-MM-DD_HH-MM-SS.json .agent/rules/.updated
```

## Notes

- **Full Backup**: The `.tar.gz` archive provides a complete snapshot of the rules at a point in time.
- **Validation**: The `validate_rules.py` script ensures critical files exist and metadata is correct.
