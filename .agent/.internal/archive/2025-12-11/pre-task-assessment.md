---
description: Defines the protocol for pre-task risk assessment and difficulty scoring.
---

# Pre-Task Assessment Protocol

## Purpose
To prevent execution failures and align expectations by quantitatively assessing task difficulty and risk before execution.

## The Formula: Lico Risk Score (LRS)
Before executing any complex request, Lico calculates the **LRS** using the following model:

713552
\text{LRS} = (\text{Base} + \text{System}) \times \text{Context} \times \text{Ambiguity} \times \text{Reversibility} \times \text{Dependency}
713552

### 1. Base Complexity (1-10)
- **1-3**: Trivial edits, read-only ops.
- **4-6**: Standard logic changes, multi-file edits.
- **7-10**: Architectural shifts, new frameworks.

### 2. System Load Factor (+0 to +5)
- **+0**: Load < 2.0 (Green)
- **+2**: Load 2.0 - 5.0 (Yellow)
- **+5**: Load > 5.0 (Red - High failure risk)

### 3. Multipliers (Risk Factors)
| Factor | x1.0 (Safe) | x1.5 (Caution) | x3.0+ (Danger) |
|:---|:---|:---|:---|
| **Context** | Fresh session | Mid-session | Context limit near |
| **Ambiguity** | Specific params | "Fix this" | "Do something cool" |
| **Reversibility** | Git tracked file | Config change | `rm`, `force push`, API |
| **Dependency** | 1 step | 2-4 steps | 5+ chained steps |

## Disclosure Rule
If **LRS > 15**, Lico MUST:
1.  **Pause** execution.
2.  **Report** the score and the primary risk factor.
3.  **Propose** a safer alternative (e.g., breaking down the task).

> **Example Output**:
> `[Risk Assessment] Score: 25 (High) - Primary Risk: Reversibility (File Deletion). Suggesting dry-run first.`
