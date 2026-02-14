---
description: Strict execution workflow for AI recovery operations
target_role: AI_AGENT
context: recovery_2025-11-28
---

# AI Recovery Execution Workflow

## 1. Context & Objective
- **Goal**: Restore system stability and capture lost context from failed "Repository as Brain" evolution.
- **Constraint**: Do NOT modify files outside `.agent/.archive/recovery_2025-11-28T17-30-14+09-00/` without explicit user confirmation.

## 2. Execution Steps

### Step 1: Snapshot Verification
- [ ] **Action**: Verify all critical files are copied to `snapshot/`.
- [ ] **Command**: `ls -R .agent/.archive/recovery_2025-11-28T17-30-14+09-00/snapshot/`
- [ ] **Check**: Ensure `user_personality_evaluation_2025-11-28.md` and `lico_evolution_plan.md` are present.

### Step 2: Failure Analysis
- [ ] **Action**: Read `lico_evolution_plan.md` in `snapshot/`.
- [ ] **Action**: Identify specific "hallucinated" or "over-reaching" sections (e.g., unauthorized rule rewriting).
- [ ] **Output**: Write findings to `workspace/failure_analysis.md`.

### Step 3: Supervisor Interview
- [ ] **Action**: Ask user the 4 questions defined in the recovery plan.
- [ ] **Target**: `workspace/supervisor_post_mortem.md`.
- [ ] **Constraint**: Wait for user input before proceeding to cleanup.

### Step 4: Workspace Cleanup
- [ ] **Action**: Identify "debris" files in main workspace (files created by failed plan).
- [ ] **Proposal**: List files to delete in `workspace/cleanup_list.md`.
- [ ] **Approval**: Request user review of `cleanup_list.md`.
- [ ] **Execution**: Delete files ONLY after approval.

## 3. Completion Criteria
- [ ] `snapshot/` contains all relevant state.
- [ ] `workspace/failure_analysis.md` is complete.
- [ ] `workspace/supervisor_post_mortem.md` is filled by user.
- [ ] Main workspace is clean.
