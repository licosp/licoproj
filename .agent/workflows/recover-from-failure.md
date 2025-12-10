---
description: Standardized workflow for recovering from failed development plans or AI errors
---

# Development Plan Recovery Workflow

> [!NOTE]
> For emergency backup **before** context loss, see [emergency-backup.md](emergency-backup.md).
> This workflow is for **after** a failure has occurred.

## When to Use

- User indicates a plan failure
- AI detects significant deviation or error
- Recovery from a crashed session where data was lost

---

## Prerequisites

If emergency backup was NOT performed, first run `/emergency-backup` to preserve current state.

---

## Steps

### Step 1: Failure Analysis

1. Read the plan or logs that led to the failure
2. Identify specific issues:
   - Hallucinations
   - Over-reaching actions
   - Logic errors
3. Document findings in `.agent/.internal/workspace/failure_analysis.md`

### Step 2: Supervisor Interview (Human Input)

Ask the user the following:
1. **Lost Information**: What specific data/files were lost?
2. **Original Intent**: What was the goal of the failed plan?
3. **Failure Cause**: What specific errors or behaviors were observed?
4. **Ideal Outcome**: What should have happened?

Record answers in `.agent/.internal/workspace/supervisor_post_mortem.md`

### Step 3: Workspace Cleanup

1. Identify "debris" files created by the failed plan
2. Create a cleanup proposal list
3. Request user approval before deleting anything
4. Execute cleanup only after explicit approval

---

## Completion Criteria

- [ ] Failure analysis documented
- [ ] User feedback recorded
- [ ] Main workspace is clean and stable

---

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [emergency-backup.md](emergency-backup.md) | Pre-failure emergency backup procedure |
