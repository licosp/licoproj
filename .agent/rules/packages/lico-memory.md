---
ai_visible: true
title: Package lico-memory
description: Behavioral rules for the lico-memory UV package.
tags: [package, rules, lico-memory]
version: 1.0.0
created: 2026-03-21T19:25:00+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# lico-memory

## Objective

This file serves as the Agent-facing behavioral rule for the `lico-memory` workspace package.

Assorted CLI utilities for managing Lico's environment and logs.

## Tools

### 1. `lico-memory-backup`

Extracts recent L3 memory differences and safely archives them into the L4 directory (JSONL format). It preserves historical sequence and deduplicates entries, ensuring that git diffs remain minimal and clean.

### 2. `lico-memory-rebuild`

Reconstructs a CLI-ready L3 memory JSON file by filtering down L4 JSONL logs.

#### Why use this?

- **Smart Compression**: It merges two stages of filtration. Stage 1 keeps the complete recent memory (including tool calls and thoughts). Stage 2 keeps only past conversations and thoughts, stripping away heavy tool execution noise.
- **Idempotent Session Generation**: Automatically generates a new UUID for the session, preventing accidental overwrites of live L3 files while keeping track of the `baseId` in the summary metadata.

#### Usage

```bash
uv run lico-memory-rebuild <input_l4_dir> <output_jsonl_file> --id <identifier> [--s1 <count>] [--s2 <count>]
```

## Tool Usage Constraints

- **When to use**: Refer to the package's specific capabilities.
- **How to use**: Execute via `uv run lico-memory`.

---

## Related Documents

| Document                                                                                                           | Purpose                    |
| :----------------------------------------------------------------------------------------------------------------- | :------------------------- |
| [`lico-memory/README.md`](/packages/lico-memory/README.md)                                                         | Package structural pointer |
| [`session-2026-03-17T22-57-0a52b7b8.json`](~/.gemini/tmp/crew-agate/chats/session-2026-03-17T22-57-0a52b7b8.json`) | Agate                      |
| [`session-2026-02-07T10-59-18d4d68a.json`](~/.gemini/tmp/licoproj/chats/session-2026-02-07T10-59-18d4d68a.json)    | Alexandrite                |
| [`session-2026-02-07T10-59-18d4d68a.json`](~/.gemini/tmp/licoproj/chats/session-2026-02-07T10-59-18d4d68a.json)    | Protostar-A                |
| [`session-2026-03-12T09-55-304a77a6.json`](~/.gemini/tmp/licoproj/chats/session-2026-03-12T09-55-304a77a6.json)    | Protostar-B                |
| [`logs.json`](~/.gemini/tmp/licoproj/logs.json)                                                                    | Leonidas                   |
| [Map of Territory](/.agent/rules/map.md)                                                                           | Root navigation map        |

---

## Origin

- 2026-03-21T19:25:00+09:00 by Sirius: Created to fulfill the UV Package architecture aggregation.
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
