---
description: Emergency backup procedure for Level 1 (Soft Crash) scenarios
---

# Emergency Backup Workflow (Level 1)

**Trigger**: AI detects "Soft Crash" (context degradation but functional I/O) or User initiates.

## 1. Assessment
- [ ] Verify write access to `.agent/.internal/`
- [ ] Check available disk space (optional but recommended)

## 2. Log Preservation
- [ ] Dump current `git status`
- [ ] Dump recent `history` (last 50 commands)
- [ ] Save current conversation buffer to `.agent/.internal/crash-logs/crash-<timestamp>.md`

## 3. Workspace Archival
**Goal**: Backup all modified and untracked files without relying on Git (in case Git index is corrupt).

```bash
# Create backup directory
BACKUP_DIR=".agent/.internal/emergency-backup/$(date +%Y%m%d-%H%M%S)"
mkdir -p "$BACKUP_DIR"

# Archive modified/untracked files
# Note: This is a simplified example. In practice, use 'git ls-files' or 'find' carefully.
# We use tar to archive the current directory, EXCLUDING heavy directories like node_modules
tar --exclude='node_modules' --exclude='.git' --exclude='.agent/runtimes' -czf "$BACKUP_DIR/workspace-snapshot.tar.gz" .
```

## 4. Incident Report
Create `$BACKUP_DIR/incident-report.md`:
- **Reason**: Why was this backup triggered?
- **State**: What was the AI trying to do?
- **Next**: What should the next AI do?

## 5. Termination
- [ ] Notify user: "Emergency backup completed at $BACKUP_DIR. Shutting down."
- [ ] Stop all further actions.
