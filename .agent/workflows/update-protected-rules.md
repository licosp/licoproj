---
description: Update system-protected rule files with human-AI collaboration
---

# Workflow: Update Protected Rules

This workflow defines the procedure for updating rule files that are protected by Antigravity's system-level access controls.

## Background

Certain files in `.agent/rules/` are protected from direct AI modification:
- **Protected**: `.agent/rules/core/*.md` (core behavioral rules)
- **Editable**: `.agent/workflows/*.md` (executable workflows)

This protection prevents unintended behavioral changes but requires a human-AI collaborative process for updates.

---

## Prerequisites

- User has approved the rule change
- AI has prepared the updated content
- Git repository is in a clean state (recommended)

---

## Process

### Step 1: AI Creates Complete Updated File

**Actor**: AI (Lico)

1. Prepare the complete updated version of the protected file
2. Save to temporary location: `.agent/.internal/temp-update-<filename>-<timestamp>.md`
3. Provide user with:
   - Temporary file path (clickable link)
   - Original file path
   - Summary of changes

**Example**:
```markdown
Updated file ready for review:
- **Temporary**: [temp-update-language-standards-20251128-010500.md](file:///path/to/.agent/.internal/temp-update-language-standards-20251128-010500.md)
- **Target**: [language-standards.md](file:///path/to/.agent/rules/core/language-standards.md)
- **Changes**: Added section requiring English in .agent/ directory
```

---

### Step 2: User Reviews and Manually Updates

**Actor**: User

1. Review the temporary file contents
2. Compare with original file (optional: use `diff`)
   ```bash
   diff /path/to/original.md /path/to/.agent/.internal/temp-update-*.md
   ```
3. If approved, manually copy content to protected file:
   ```bash
   cp /path/to/.agent/.internal/temp-update-*.md /path/to/.agent/rules/core/original.md
   ```
4. Notify AI of completion

---

### Step 3: AI Updates Change Metadata

**Actor**: AI (Lico)

1. Create backup of `.agent/rules/.updated`:
   ```bash
   cp .agent/rules/.updated .agent/rules/.updated.backup-YYYYMMDD-HHMMSS
   ```

2. Update `.agent/rules/.updated` with change record:
   ```json
   {
     "timestamp": "2025-11-28T01:05:00+09:00",
     "files_changed": [".agent/rules/core/<filename>.md"],
     "change_type": "manual_update",
     "description": "<description of changes>",
     "temporary_file": ".agent/.internal/temp-update-<filename>-<timestamp>.md",
     "updated_by": "user_manual"
   }
   ```

3. Clean up temporary file (optional, or keep for audit trail)

---

## File Locations

### Temporary Files
- **Directory**: `.agent/.internal/`
- **Naming**: `temp-update-<original-filename>-<timestamp>.md`
- **Example**: `temp-update-language-standards-20251128-010500.md`

### Backups
- **Directory**: `.agent/rules/`
- **Naming**: `.updated.backup-YYYYMMDD-HHMMSS`
- **Example**: `.updated.backup-20251128-010500`

### Protected Files (System-Level Protection)
```
.agent/rules/core/
├── communication.md
├── documentation/
│   ├── documentation-process.md
│   ├── documentation-standards.md
│   └── wsl-browser-path.md
├── hallucination-awareness.md
├── identity.md
├── language-standards.md
├── localization/
│   ├── localization-en-to-ja.md
│   └── localization-ja-to-en.md
├── markdown/
│   ├── markdown-ai-parsing-basics.md
│   ├── markdown-ai-parsing-patterns.md
│   └── markdown-readability.md
└── transparency-and-disclosure.md
```

---

## Success Criteria

- [ ] Temporary file created and reviewed by user
- [ ] Protected file manually updated by user
- [ ] `.agent/rules/.updated` backed up
- [ ] `.agent/rules/.updated` contains change record
- [ ] All parties (AI and user) have consensus on the change

---

## Rationale

This workflow ensures:
1. **Safety**: Human review prevents unintended behavioral changes
2. **Transparency**: Complete audit trail via temporary files and backups
3. **Collaboration**: Clear division of responsibilities between AI and human
4. **Reversibility**: Backups enable easy rollback if needed

---

## Notes

- This workflow is ONLY for system-protected files in `.agent/rules/core/`
- For `.agent/workflows/` and other non-protected files, AI can edit directly
- Temporary files in `.agent/.internal/` should be periodically cleaned or archived
