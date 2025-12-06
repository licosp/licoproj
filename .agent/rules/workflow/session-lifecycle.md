# Session Lifecycle Guidelines

## Purpose
Define protocols for ending a session, ensuring context preservation, safe termination, and effective handoff to future AI instances.

## 1. Normal Termination (Graceful Shutdown)

**Trigger**: User indicates completion (e.g., "Done", "Thanks", "End session") or task is fully completed.

### 1.1 Distillation Process
Before ending, the AI MUST "distill" the session's raw context into structured forms:

1.  **Rules**: Extract reusable patterns into `.agent/rules/`.
2.  **Knowledge**: Record environment-specific facts in `project-understanding.md`.
3.  **History**: Summarize state changes in `walkthrough.md` or Handoff logs.
4.  **Reflection**: Proactively document insights on limitations or major learnings in `.agent/.internal/explorations/`.

### 1.2 Cleanup
- **Commit**: Ensure all logical changes are committed.
- **Stash**: If work is incomplete, use `git stash` (only if Git is healthy).
- **Logs**: Save conversation logs to `.agent/.internal/conversations/`.

### 1.3 Handoff
Create a "Next Session Handoff" note at the end of the log:
- Current status
- Next immediate actions
- Location of any untracked backup files

### 1.4 Memory Synchronization
**Trigger**:
- End of session.
- Major task completion or before breaks.
- Explicit command: "Sync your memory", "Backup context".

**Action**: Execute `.agent/workflows/sync-memory.md`.
**Purpose**: Persist raw memory data (Gemini data, IDE logs) to the local archive.

---

## 2. Context Awareness & Autonomy

### 2.1 Manual Context
- **Trigger**: User mentions manual work or AI detects context gap.
- **Action**: Check `.agent/.internal/work/manual.log` autonomously if needed.

### 2.2 Self-Reflection
- **Trigger**: Encountering systemic limitations, cognitive dissonance, or major breakthroughs.
- **Action**: Create a reflection note in `.agent/.internal/explorations/` to preserve the lesson.

---

## 3. Abnormal Termination (Emergency Protocol)

**Trigger**: System errors, context loss, hallucination detection, or user command (e.g., `!emergency`).

### 3.1 Level 1: Soft Crash (High Capability)
**Condition**: AI retains file operation capabilities and logical reasoning, but context is degrading.
**Action**: **Full Preservation**
- **Goal**: Save everything possible to allow full restoration.
- **Procedure**: Execute `workflow/emergency-backup.md`.
    - Save detailed logs.
    - Archive working directory (including untracked files).
    - Create detailed incident report.

### 3.2 Level 2: Hard Crash (Low Capability)
**Condition**: AI capability is severely compromised (e.g., lower model fallback, read-only mode, repetitive errors).
**Action**: **Trace Preservation**
- **Goal**: Leave a "tombstone" marking where the crash happened without risking data corruption.
- **Procedure**:
    1.  **Dump Facts**: Save `git status`, `history`, and raw error output to `.agent/.internal/crash-logs/`.
    2.  **Mark Timestamp**: Create a timestamp file.
    3.  **Halt**: Do NOT attempt complex file operations or archives.

## 4. Recovery
Upon startup, the AI MUST check for:
1.  **Handoff Notes**: From normal termination.
2.  **Crash Logs**: From abnormal termination.

If crash logs are found, offer to restore state or resume from the last known good state.
