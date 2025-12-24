---
description: Proposal for standardized timestamp format across all files
created: 2025-11-30T19:52:20+09:00
status: proposal
category: documentation-standards
---

# Standardized Timestamp Format

## Summary
All timestamps in the repository MUST use ISO 8601 format with Japan timezone (+09:00) for consistency and machine readability.

## Rationale
Timestamps appear in multiple contexts:
- YAML frontmatter (`created`, `updated` fields)
- File naming (e.g., `idea_2025-11-30T19-52-20+09-00.md`)
- Git commit messages (automatic)
- Conversation logs
- Archive directories

**Inconsistent formats create problems:**
- Difficult to sort chronologically
- Ambiguous timezone interpretation
- Hard to parse programmatically
- Confusion between different date conventions (US vs EU vs ISO)

**Benefits of standardization:**
- Unambiguous chronological ordering
- Machine-parsable for AI tools
- Human-readable with clear timezone
- Consistent across all Lico artifacts

## Standard Format

### ISO 8601 with Japan Timezone

**Format:** `YYYY-MM-DDTHH:MM:SS+09:00`

**Examples:**
- `2025-11-30T19:52:20+09:00` (full timestamp)
- `2025-11-30` (date only, when time is not relevant)

### Usage Contexts

#### 1. YAML Frontmatter
```yaml
---
created: 2025-11-30T19:52:20+09:00
updated: 2025-11-30T20:15:30+09:00
---
```

#### 2. File Naming
When timestamps are part of filenames, use format: `YYYY-MM-DDTHH-MM-SS+09-00`
(Replace colons with hyphens for filesystem compatibility)

**Examples:**
- `idea_2025-11-30T19-52-20+09-00.md`
- `backup_2025-11-30T19-52-20+09-00.json`

#### 3. Generated Comments
```markdown
*Generated on 2025-11-30T19:52:20+09:00*
```

#### 4. Archive Directories
```
.agent/.archive/recovery_2025-11-30T19-52-20+09-00/
```

## Timezone Rationale

**Why Japan Time (+09:00)?**
1. User (lyouta) is based in Japan
2. Consistent with user's work hours and context
3. Avoids UTC conversion mental overhead
4. Reflects the primary operator's timezone

**Note:** This does NOT prevent collaboration with users in other timezones. The timezone is explicitly stated (+09:00), so conversion is trivial.

## Implementation

### Proposed Rule Location
Add to `.agent/rules/core/documentation/documentation-standards.md`:

```markdown
## Timestamp Format

All timestamps MUST use ISO 8601 format with Japan timezone:

- **Full timestamp**: `YYYY-MM-DDTHH:MM:SS+09:00`
- **Date only**: `YYYY-MM-DD`
- **In filenames**: `YYYY-MM-DDTHH-MM-SS+09-00` (colons → hyphens)

**Rationale**: Unambiguous, machine-parsable, human-readable.
```

### Migration Strategy
- **New files**: Apply standard immediately
- **Existing files**: Update opportunistically when editing
- **No retroactive mass-update**: Preserve historical context

## Examples from Current Repository

**Conforming:**
- `ai-first-writing-style_2025-11-30T19-23-04+09-00.md` ✅
- `created: 2025-11-30T19:48:43+09:00` ✅

**Non-conforming (examples to avoid):**
- `Nov 28, 2025` ❌ (ambiguous, not machine-parsable)
- `2025/11/30` ❌ (format unclear)
- `2025-11-30 19:52` ❌ (missing timezone)

## Impact
- **Low disruption**: Only affects new files
- **High value**: Consistency across all temporal records
- **Scope**: Repository-wide standard
