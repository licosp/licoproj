---
ai_visible: true
title: Cross-Link Audit Master Plan
description: Master plan for cross-link audit across all target directories
tags: [maintenance, cross-link, audit, plan]
version: 1.0
created: 2026-01-04T11:51:00+09:00
updated: 2026-01-04T11:51:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking)
related:
  .agent/workflows/cross-link-audit.md: Detailed workflow for each directory
---

# Cross-Link Audit Master Plan

This document defines the **target directories** for cross-link audit. For the actual work steps, see [cross-link-audit.md](.agent/workflows/cross-link-audit.md).

---

## Target Directories

### Tier 1: Core Documentation

| Directory | Status | Files | Notes |
|:----------|:-------|:------|:------|
| `.agent/rules/` | ✓ **完了** | ~50 | 2026-01-04 |
| `.agent/workflows/` | ✓ **完了** | 13 | 2026-01-04, path-fixed |
| `.agent/.internal/legacy.md` | ✓ **完了** | 1 | Navigation only (append-only) |

### Tier 2: Internal Documentation

| Directory | Status | Files | Notes |
|:----------|:-------|:------|:------|
| `.agent/.internal/references/` | ✓ **完了** | 36 | 2026-01-04 |
| `.agent/.internal/thoughts/` | ✓ **完了** | 43 | 2026-01-04 |
| `.agent/.internal/letters/` | ✓ **完了** | 3 | 2026-01-04 |
| `.agent/.internal/explorations/` | ✓ **完了** | 1 | 2026-01-04 |

### Tier 3: Human-Facing

| Directory | Status | Files | Notes |
|:----------|:-------|:------|:------|
| `.human/users/leonidas/` | ✓ **完了** | 6 | 2026-01-04 |
| `.human/manuals/` | ✓ **完了** | 5 | 2026-01-04 |

---

## Non-Target Directories

| Directory | Reason |
|:----------|:-------|
| `.agent/cards/` | Agent Observations で管理 |
| `.agent/.internal/cases/` | 使用済みカード |
| `.agent/.internal/archive/` | 履歴のみ |
| `.human/archive/` | 履歴のみ |
| `.agent/templates/` | 文章ではない |
| `.agent/.internal/memory_archive/` | Git 非追跡 |
| `.runtimes/` | 外部パッケージ |

---

## Footer Standard

All target files should have a consistent footer:

```markdown
---

## Origin

- YYYY-MM-DDTHHMM: Created [context]
- YYYY-MM-DDTHHMM by <Identifier>: [change summary]

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
```

> [!NOTE]
> The Navigation link serves as:
> 1. **End-of-file marker** — Clear file termination
> 2. **Map reference** — Encourages checking the index
> 3. **Consistency** — Same structure across all files

---

## Workflow

For each directory:

1. Execute [cross-link-audit.md](.agent/workflows/cross-link-audit.md)
2. Update status in this document
3. Commit with context ID `[Cross-Link-Audit]`

---

## Origin

- 2026-01-04T1151 by Polaris: Created master plan

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
