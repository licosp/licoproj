---
ai_visible: true
title: Package lico-memory
description: Behavioral rules for the lico-memory UV package.
tags: [package, rules, lico-memory]
version: 1.0.0
created: 2026-03-21T19:25:19+09:00
updated: 2026-03-21T19:25:19+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# lico-memory

## Objective

This file serves as the Agent-facing behavioral rule for the `lico-memory` workspace package.

Assorted CLI utilities for managing Lico's environment and logs.

## Tools

### 1. `lico-jsonl-converter`

A powerful utility to manage Gemini CLI's monolithic L3 memory files by converting them into Git-friendly, date-partitioned JSONL (JSON Lines) format.

#### Why use this?

- **Git Efficiency**: Monolithic JSON files cause massive diffs and repository bloat. JSONL allows Git to track only the new lines (turns) added.
- **Normalization**: Automatically sorts JSON keys alphabetically (`sort_keys=True`) so that changes in the CLI tool's version don't cause unnecessary diff fluctuations.
- **Idempotency**: Implements message ID-based deduplication. You can run the converter multiple times against the same input, and only new messages will be appended.
- **Chronological Integrity**: Merges new data with existing logs and re-sorts everything by timestamp to ensure the history is always perfectly sequential.

#### Usage

```bash
uv run lico-jsonl-converter <input_json_path> <output_root_dir>
```

#### Example Workflows

Depending on the data source, the directory structure varies slightly:

**A. Agent Logs (Dict-based)**
Extracts metadata to `metadata.json` and messages to `messages/YYYY/MM/DD/log.jsonl`.

- **Agate**: `~/.gemini/tmp/crew-agate/chats/session-2026-03-17T22-57-0a52b7b8.json`
- **Alexandrite**: `~/.gemini/tmp/crew-alexandrite/chats/session-2026-03-18T19-26-ee0b5358.json`
- **Protostar-a**: `~/.gemini/tmp/licoproj/chats/session-2026-02-07T10-59-18d4d68a.json`
- **Protostar-b**: `~/.gemini/tmp/licoproj/chats/session-2026-03-12T09-55-304a77a6.json`

**B. User Logs (List-based)**
Partitions directly into `YYYY/MM/DD/log.jsonl` (no metadata file).

- **Leonidas**: `~/.gemini/tmp/**/logs.json`

#### Recommended Destination

`.repos/.licoshdw/conversations_cli/identifiers/<id>/`

## Tool Usage Constraints

- **When to use**: Refer to the package's specific capabilities.
- **How to use**: Execute via `uv run lico-memory`.

---

## Related Documents

| Document                                                   | Purpose                    |
| :--------------------------------------------------------- | :------------------------- |
| [`lico-memory/README.md`](/packages/lico-memory/README.md) | Package structural pointer |
| [Map of Territory](/.agent/rules/map.md)                   | Root navigation map        |

---

## Origin

- 2026-03-21T1925 by Sirius: Created to fulfill the UV Package architecture aggregation.
