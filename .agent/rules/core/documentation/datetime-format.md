---
ai_visible: true
title: DateTime Format Standard
description: Standard datetime format for file naming and timestamps.
tags: [datetime, format, standards, iso8601]
version: 1.2.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-02-19T20:10:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
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
   _Note: This does NOT prevent collaboration in other timezones; the explicit offset makes conversion trivial._

---

## Format Specification

**Standard**: ISO 8601 with Japan timezone (+09:00)

### For Timestamps (in content)

```text
YYYY-MM-DDTHH:MM:SS+09:00
```

**Example**: `2025-12-11T01:09:25+09:00`

### For File Names

```text
YYYY-MM-DDTHHMM_description.md
```

**Example**: `2025-12-11T0109_session_report.md`

**Note**: Colons (`:`) and some special characters are avoided in file names for cross-platform compatibility.

---

## Rules

| Situation               | Format                      |
| :---------------------- | :-------------------------- |
| Timestamp in content    | `YYYY-MM-DDTHH:MM:SS+09:00` |
| Origin (Historical Log) | `YYYY-MM-DDTHH:MM:SS+09:00` |
| Conversation Log        | `YYYY-MM-DDTHH:MM:SS+09:00` |
| File name prefix        | `YYYY-MM-DDTHHMM_`          |
| Unknown time            | Use `T0000` (midnight)      |
| Date only needed        | `YYYY-MM-DD`                |

---

## Acceptance of Resolution (Nuance Preservation)

When recording historical entries (Origin):

1. **Precision Standard**: The standard format for `Origin` is `YYYY-MM-DDTHH:MM:SS+09:00`.
2. **Handle Incomplete Data**: If the source data (e.g., from an old commit) lacks minutes or hours, do NOT invent "00" entries to satisfy the format if it falsely implies precision.
3. **Primary Principle**: Accuracy to the known source takes precedence over strict format compliance, but for NEW entries, the standard MUST be followed.

---

## Examples

### File Names

```text
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

| Document                                                                                  | Purpose                               |
| :---------------------------------------------------------------------------------------- | :------------------------------------ |
| [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md) | Meta-requirements for dates in Origin |
| [Map of Territory](/.agent/rules/map.md)                                                  | Root navigation map                   |

---

## Origin

- 2025-12-01T0000: Created as datetime format standards.
- 2026-01-02T0828 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit).
- 2026-01-23T03:15:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch1>> Standardized to v2.3 (4-layer structure) and workspace-absolute links. (v1.1.0)
- 2026-01-28T18:00:00+09:00 by Canopus: Added standardization for Origin (history) timestamps and Acceptance of Resolution principle. (v1.2.0)
- 2026-02-19T20:10:00+09:00 by Sirius: Reaffirmed Second Precision (HH:MM:SS) for concurrency support. (v1.3.0)
