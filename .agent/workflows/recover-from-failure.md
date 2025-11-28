---
description: Standardized workflow for recovering from failed development plans or AI errors
target_role: AI_AGENT
---

# Development Plan Recovery Workflow

## 1. Context & Objective
- **Goal**: Restore system stability, capture lost context, and learn from failures when a development plan goes wrong.
- **Trigger**: User indicates a plan failure, or AI detects significant deviation/error.
- **Constraint**: Do NOT modify files outside the designated recovery directory without explicit user confirmation.

## 2. Execution Steps

### Step 1: Emergency Evacuation (Snapshot)
- [ ] **Create Directory**: Create a timestamped recovery directory (e.g., `.agent/.archive/recovery_YYYY-MM-DDTHH-MM-SS+TZ`).
    - Create subdirectories: `snapshot/` and `workspace/`.
- [ ] **Snapshot**: Copy all relevant "in-flight", "broken", or "context-heavy" files to `snapshot/`.
    - **Crucial**: Ensure no data is lost during this copy.

### Step 2: Failure Analysis
- [ ] **Analyze**: Read the plan or logs that led to the failure (now in `snapshot/`).
- [ ] **Identify**: Pinpoint specific "hallucinations", "over-reaching" actions, or logic errors.
- [ ] **Output**: Write findings to `workspace/failure_analysis.md`.

### Step 3: Supervisor Interview (Human Input)
- [ ] **Interview**: Ask the user (supervisor) the following questions:
    1.  **Lost Information**: What specific data/files were lost?
    2.  **Original Intent**: What was the goal of the failed plan?
    3.  **Failure Cause**: What specific errors or behaviors were observed?
    4.  **Ideal Outcome**: What should have happened?
- [ ] **Record**: Save answers to `workspace/supervisor_post_mortem.md`.

### Step 4: Workspace Cleanup
- [ ] **Identify**: List "debris" files in the main workspace (files created by the failed plan).
- [ ] **Proposal**: Create a `cleanup_list.md` in `workspace/`.
- [ ] **Approval**: Request user review of the cleanup list.
- [ ] **Execution**: Delete files ONLY after explicit user approval.

## 3. Completion Criteria
- [ ] `snapshot/` contains all relevant state.
- [ ] `workspace/failure_analysis.md` documents the error.
- [ ] `workspace/supervisor_post_mortem.md` contains user feedback.
- [ ] Main workspace is clean and stable.
