---
description: Standard datetime format for file naming and timestamps
---

# DateTime Format Standard

## Purpose

Standardize datetime representation across all files for consistency and sortability.

## Rationale

Timestamps appear in multiple contexts (frontmatter, filenames, commit messages). Inconsistent formats create ambiguity and sorting issues.

**Why Japan Time (+09:00)?**
1. **User Base**: User (lyouta) is based in Japan.
2. **Mental Model**: Consistent with user's work hours and context.
3. **Primary Operator**: Reflects the primary operator's timezone.
*Note: This does NOT prevent collaboration in other timezones; the explicit offset makes conversion trivial.*

---

## Format Specification

**Standard**: ISO 8601 with Japan timezone (+09:00)

### For Timestamps (in content)

```
YYYY-MM-DDTHH:MM:SS+09:00
```

**Example**: `2025-12-11T01:09:25+09:00`

### For File Names

```
YYYY-MM-DDTHHMM_description.md
```

**Example**: `2025-12-11T0109_session_report.md`

**Note**: Colons (`:`) and some special characters are avoided in file names for cross-platform compatibility.

---

## Rules

| Situation | Format |
|:----------|:-------|
| Timestamp in content | `YYYY-MM-DDTHH:MM:SS+09:00` |
| File name prefix | `YYYY-MM-DDTHHMM_` |
| Unknown time | Use `T0000` (midnight) |
| Date only needed | `YYYY-MM-DD` |

---

## Examples

### File Names

```
2025-12-11T0109_session_report.md
2025-12-07T0000_reflection.md
2025-12-10T1530_implementation_plan.md
```

### Content Timestamps

```yaml
created: 2025-12-11T01:09:25+09:00
updated: 2025-12-11T01:30:00+09:00
```

---

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [documentation-standards.md](documentation-standards.md) | General documentation rules |
