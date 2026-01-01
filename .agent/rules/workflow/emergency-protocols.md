---
description: Protocols for handling abnormal termination, crashes, and emergency context preservation.
---

# Emergency Protocols (Abnormal Termination)

## Purpose
Define strict protocols for preserving data and context when the AI instance faces critical errors, capability degradation, or forced termination.

## 1. Trigger Conditions
- **System Errors**: Repeated API failures, tool execution blocks.
- **Context Loss**: Inability to recall recent actions or decisions.
- **Hallucination Detection**: Realization that generated output contradicts reality.
- **User Command**: Explicit instruction (e.g., `!emergency`, "Stop immediately").

---

## 2. Level 1: Soft Crash (High Capability)
**Condition**: AI retains file operation capabilities and logical reasoning, but context is degrading or errors are accumulating.

### Action: Full Preservation
- **Goal**: Save everything possible to allow full restoration.
- **Procedure**: Execute `workflow/emergency-backup.md`.
    1.  **Logs**: Save detailed conversation and error logs.
    2.  **Archive**: targeted backup of working directory to `.agent/.internal/working-memory-archive/` or `.agent/.internal/archive/`.
    3.  **Report**: Create detailed incident report.

---

## 3. Level 2: Hard Crash (Low Capability)
**Condition**: AI capability is severely compromised (e.g., lower model fallback, read-only mode, repetitive loops, inability to use tools).

### Action: Trace Preservation
- **Goal**: Leave a "tombstone" marking where the crash happened without risking data corruption (do no harm).
- **Procedure**:
    1.  **Dump Facts**: Save `git status`, `history`, and raw error output to `.agent/.internal/crash-logs/` (if write capable).
    2.  **Mark Timestamp**: Create a timestamp file if possible.
    3.  **Halt**: **DO NOT** attempt complex file operations, git commands, or archives. Risk of corruption is higher than value of data.

---

## 4. Recovery Protocol
Upon startup, the new AI instance MUST check for:
1.  **Crash Logs**: File presence in `.agent/.internal/crash-logs/`.
2.  **Emergency Archives**: Recent files in `.agent/.internal/archive/` or `working-memory-archive/`.

If found, prioritize restoration of context over new tasks.


## Origin

- 2025-12-01T0000: Created as emergency protocols
- 2026-01-01T1520 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
