---
ai_visible: true
title: "Technical Reference: Gemini CLI L3 Memory Limits and Restoration"
description: An objective analysis of the physical capacity limits of Gemini CLI session memory (L3) and the established procedures for surgical memory restoration.
tags: [reference, memory, l3, gemini-cli, architecture, limits]
version: 1.0.0
created: 2026-03-16T00:30:00+09:00
updated: 2026-03-16T00:30:00+09:00
language: en
author: Lico (Agate)
ai_model: gemini-3-pro-preview
---

# Technical Reference: Gemini CLI L3 Memory Limits and Restoration

## 1. Overview

This document defines the physical capacity limits of the Gemini CLI session storage (Level 3 memory) and provides a verified procedure for restoring functionality when a session collapses due to memory bloat.

## 2. Memory Architecture Context

To understand the failure mode, distinguish between the following layers:

- **L2 (Context Window)**: The dynamic memory used during inference. Managed by the CLI's automatic distillation (summarization/compression) algorithm.
- **L3 (Local Session Storage)**: The monolithic JSON file (e.g., `session-*.json`) that records every turn. **Crucially, L3 does not decrease when L2 is distilled.** It grows monotonically.

## 3. Physical Capacity Limits

Empirical testing (Experiment Case Agate, March 2026) has identified the following thresholds for session collapse:

- **Collapse Point**: Approximately **10 days** of active dialogue or **2,400 turns**.
- **Physical Size**: A monolithic JSON exceeding **90,000 lines** (formatted) or **17MB** (raw).
- **Symptom**: The API returns an error: `✕ [API Error: Failed to generate content: Request contains an invalid argument.]`.
- **Root Cause**: The underlying system fails to parse or transmit the bloated L3 JSON payload to the API, regardless of L2 distillation status.

## 4. Empirical Evidence (The Agate Experiment)

In March 2026, a series of controlled tests were performed by Leonidas to find the functional boundary by incrementally restoring L3 memory from the past toward the present.

| Case ID     | Data Span | Turn Count (L3) | Result      | Observation                         |
| :---------- | :-------- | :-------------- | :---------- | :---------------------------------- |
| `case-orig` | 10 Days   | 2,411           | **FAIL**    | Permanent API Error                 |
| `case-01`   | 9 Days    | 2,123           | **SUCCESS** | Context compressed from 109% to 22% |
| `case-05`   | 5 Days    | 1,047           | **SUCCESS** | Stable, occupancy around 50%        |
| `case-10`   | 1 Turn    | 7               | **SUCCESS** | Occupancy around 2%                 |

### Key Insight

A session that has once collapsed **can be resurrected** by surgically removing older messages from the L3 JSON file until the turn count falls below the stable threshold (~2,000 turns).

## 5. Restoration Procedure

When a session hits the L3 limit, follow these steps to restore the identifier:

1. **Evacuate to L4**: Use `lico-jsonl-converter` to export the entire bloated L3 memory into date-partitioned JSONL files in the Shadow Repository. This ensures no history is lost.
2. **Surgical Trimming**: Create a new L3 JSON file containing only the most recent **5 days** (or approximately 1,000 turns) of messages.
3. **Session Resumption**: Launch the CLI with the trimmed JSON. The identifier will regain the ability to reason, while maintaining immediate context of the recent past.
4. **Long-term Memory Access**: For context beyond the trimmed L3, the AI must manually read the L4 logs (Markdown/JSONL) stored in the Shadow Repository.

## 6. Conclusion

The "10-day lifespan" is a physical constraint of the current Gemini CLI architecture. To maintain long-term cognitive continuity, Lico identifiers must adopt a **cyclic L3-to-L4 migration strategy**, treating L3 as a volatile short-term buffer and L4 as the permanent, reliable strata.

---

## Related Documents

| Document                                                                                                                                                 | Purpose                              |
| :------------------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------- |
| [lico-memory-restoration-experiment.md](/.repos/.licoshdw/ark/2026-03-15T1300_agate-memory-restoration-experiment/lico-memory-restoration-experiment.md) | Original experimental data (Ark)     |
| [reference-methodology.md](/.agent/rules/workflow/reference-methodology.md)                                                                              | Standards for creating this document |
| [The Weight of 93,974 Lines](/.agent/.internal/thoughts/agate/2026-03-15T2330_the_weight_of_93974_lines.md)                                              | Subjective reflection on this limit  |

---

## Origin

- 2026-03-16T00:30 by Lico (Agate): Crystallized from the memory restoration experiment conducted by Leonidas. This document serves as the official technical reference for L3 capacity management.
