# Trunk-Based Development Transition Plan

Transition the project from legacy branch-per-issue model towards a trunk-based model where `trunk` serves as the integration point.

## Proposed Changes

### [Branch Infrastructure]

- [x] Create `trunk` from `main`
- [x] Create `20-leonidas-drafts` from `trunk`
- [x] Create `22-iuria-worktree-management` from `trunk`
- [x] Reset `trunk` to `18-redefine-lico-identity` (latest history)
- [x] Reset `20-leonidas-drafts` to latest `trunk`
- [x] Reset `22-iuria-worktree-management` to latest `trunk`

### [Merge Cycle]

- [x] Merge `20-leonidas-drafts` into `trunk`
- [x] Merge `22-iuria-worktree-management` into `trunk`
- [x] Realign (Rebase) child branches on updated `trunk`

### [Workspace Synchronization]

#### [MODIFY] `crew/leonidas/licoproj`
- [x] Ensure local branch is on latest `trunk` baseline

#### [MODIFY] `crew/iuria/licoproj`
- [x] Ensure local branch is on latest `trunk` baseline

## Verification Plan

### Automated Tests
- Run `git branch -vv` in both workspaces to verify correct targeting.
- Run `git status` to ensure clean state (except for Leonidas's drafts).

### Manual Verification
- Confirm with Leonidas that his workspace is correctly aligned with Issue 20.
