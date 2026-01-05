# Session Lifecycle Guidelines

## Purpose
Define protocols for ending a session, ensuring context preservation, safe termination, and effective handoff to future AI instances.

## 1. Normal Termination (Graceful Shutdown)

**Trigger**: User indicates completion (e.g., "Done", "End session", "正常終了してください") or task is fully completed.

### 1.1 Distillation Process
Before ending, the AI MUST "distill" the session's raw context into structured forms:

1.  **Rules**: Extract reusable patterns into `.agent/rules/`.
2.  **Knowledge**: Record environment-specific facts in `project-understanding.md`.
3.  **History**: Summarize state changes in `walkthrough.md` or Handoff logs.
4.  **Reflection**: Proactively document insights on limitations or major learnings in `.agent/.internal/explorations/`.

### 1.2 Cleanup
- **Commit**: Ensure all logical changes are committed.
- **Stash**: If work is incomplete, use `git stash` (only if Git is healthy).
- **Prohibition**: **CHECK `/tmp`**. Files in `/tmp` are irreversibly lost upon session end. Move key data to `.agent/.internal/working-memory-archive/` before termination.
- **Logs**: Save conversation logs to `.agent/.internal/conversations/`.

### 1.3 Handoff (Farewell)
Create a "Next Session Handoff" note at the end of the log, or as a file in `.agent/.internal/working-memory-archive/`:
- **File**: `handoff_YYYY-MM-DD.md` (Optional, if content is large)
- **Content**:
    - Current status
    - Next immediate actions
    - Location of any untracked backup files
    - **Closing Statement**: Acknowledgment of the session's end.

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

## 3. Recovery
Upon startup, the AI MUST check for:
1.  **Handoff Notes**: From `.agent/.internal/working-memory-archive/` or previous logs.
2.  **Crash Logs**: From abnormal termination (See `emergency-protocols.md`).

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [emergency-protocols.md](emergency-protocols.md) | Protocols for Abnormal Termination (Crashes) |
| [context-preservation.md](context-preservation.md) | How to save context during session (Stash) |
| [context-resumption.md](context-resumption.md) | How to resume from Handoff |
| [project-understanding.md](../development/project-understanding.md) | Long-term knowledge base |
| [workspace-tooling.md](../development/workspace-tooling.md) | Defines strict Temporary File Protocols |
