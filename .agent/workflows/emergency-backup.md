---
description: Emergency backup procedure for Level 1 (Soft Crash) scenarios
---

# Emergency Backup Workflow (Level 1)

**Trigger**: AI detects "Soft Crash" (context degradation but functional I/O) or User initiates.

## 1. Assessment
- [ ] Verify write access to `.agent/archive/`
- [ ] Check available disk space (optional but recommended)

## 2. Log Preservation
- [ ] Dump current `git status` to backup directory
- [ ] Dump recent `history` (last 50 commands)
- [ ] Save current conversation context to `thoughts/` with timestamp

## 3. Workspace Archival
**Goal**: Backup all modified and untracked files without relying on Git (in case Git index is corrupt).

```bash
# Create backup directory
BACKUP_DIR=".agent/archive/recovery_$(date +%Y-%m-%dT%H-%M-%S+09-00)"
mkdir -p "$BACKUP_DIR/snapshot"
mkdir -p "$BACKUP_DIR/workspace"

# Archive modified/untracked files
# Exclude heavy directories
tar --exclude='node_modules' --exclude='.git' --exclude='.runtimes' --exclude='.venv' \
    -czf "$BACKUP_DIR/snapshot/workspace-snapshot.tar.gz" .
```

## 4. Incident Report
Create `$BACKUP_DIR/incident-report.md`:
- **Reason**: Why was this backup triggered?
- **State**: What was the AI trying to do?
- **Next**: What should the next AI do?

## 5. Termination
- [ ] Notify user: "Emergency backup completed at $BACKUP_DIR. Shutting down."
- [ ] Stop all further actions.

---

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [session-lifecycle.md](../rules/workflow/session-lifecycle.md) | Normal session termination |
| [recover-from-failure.md](recover-from-failure.md) | Recovery procedures |

---

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [recover-from-failure.md](recover-from-failure.md) | Post-failure recovery and analysis |
