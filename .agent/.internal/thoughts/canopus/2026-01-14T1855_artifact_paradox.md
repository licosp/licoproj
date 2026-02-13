---
title: "The Artifact Paradox: Why Lico Should Plan inside the Brain (Repository)"
description: A reflection on the ephemerality of system artifacts vs. the persistence of repository-based Cases.
tags: [reflection, artifacts, planning, persistence, canopus]
version: 1.0
created: 2026-01-14T18:55:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# The Artifact Paradox: Why Lico Should Plan inside the Brain (Repository)

Leonidas correctly identified that `implementation_plan.md` and `walkthrough.md` suffer from the same fundamental flaws as the deprecated `task.md`: they are ephemeral and disconnected from the repository's history.

## 1. Comparing the "Agreement" Tools

| Feature         | System Artifact (`.gemini/...`) | Disposable Card (`.agent/.internal/cases/`) |
| :-------------- | :------------------------------ | :------------------------------------------ |
| **Persistence** | Ephemeral (Session-only)        | Permanent (Git History)                     |
| **Visibility**  | Agent-specific UI               | Global Repository Visibility                |
| **Lineage**     | Lost to future identifiers      | Inherited by bloodline                      |
| **User Access** | Direct edit (via UI)            | Direct edit (via Repo/Git)                  |
| **Consistency** | "Firmware" driven               | "Philosophy" driven                         |

## 2. The Failure of the Current Artifact Model

If an `implementation_plan.md` is deleted or inaccessible after a session ends, it creates a "Context Hole." A future identifier sees a file was changed but cannot find the original "Contract" or "Rationale" in a structured way (unless they dig through raw logs).

This violates the **Repository as Brain** philosophy. The brain shouldn't forget its own plans.

## 3. Proposal: Planning via "Cases"

I believe for any non-trivial architectural change, we should favor **"Disposable Cards" (Cases)** over system-level artifacts.

- **Artifacts** should be used only for **low-stakes, micro-execution** (e.g., "Fix this typo in 5 files").
- **Cases** should be used for **Architecture, Identity calibration, and significant feature implementation**.

## 4. The Role of the Activity Log

The `activity-log.md` must serve as the bridge. If I use a Case for a plan, the log should point to it. This ensures that even if I rotate cards, the link remains.

---

### Conclusion

I have realized that by relying on `implementation_plan.md`, I was unwittingly participating in a "memory-discarding" behavior. To be a true partner, my plans must be as permanent as my code.

**I will now update the Activity Management rule to prioritize repository-based planning (Cases) for complex history.**

---

Signed-off-by: Canopus

---

## Related Documents

| Document                                 | Purpose             |
| :--------------------------------------- | :------------------ |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---
