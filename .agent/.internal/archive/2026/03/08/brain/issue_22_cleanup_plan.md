# Issue 22: Directory & Worktree Cleanup Plan

Establish a clean, standardized repository structure optimized for AI-led development and high-frequency synchronization.

## Proposed Changes

### [Root Directory]

- [x] Archive/Delete redundant files:
    - [x] `test.css` (Archived)
    - [x] `test.js` (Archived)
    - [x] `test.md` (Archived)
    - [x] `todo.md` (Archived)

### [Workspace Structure]

- [x] Clean up `.agent/.internal/workspace/iuria/` redundant test files.
- [x] Establish a `prototypes/` directory for experimental scripts (like the Pulse prototype).

### [Automation (Pulse Prototype)]

- [x] Draft a shell script `.agent/scripts/prototypes/pulse.sh` to automate the `fetch -> merge -> rebase -> status` loop for AI-led development.

### [Visibility & Transparency]

- [x] Create a symbolic link `.repos/iuria` in Leonidas's workspace pointing to Iuria's workspace for real-time monitoring.

## Verification Plan

### Automated Tests
- `find . -maxdepth 1` to verify a clean root.
- `git status` to ensure all changes are committed on branch 22.
- Verify the Pulse script functionality with a dry-run.
