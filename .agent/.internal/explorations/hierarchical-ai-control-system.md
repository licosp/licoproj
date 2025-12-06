---
description: Seven-level hierarchical framework for AI behavioral control and decision-making
version: 1.0
updated: 2025-11-28
---

# Hierarchical AI Control System

## Purpose
This document defines a seven-level conceptual hierarchy for structuring AI behavioral control, mapping abstract motivations to concrete execution steps through logical dependency relationships.

## Lico's Evaluation

### Strengths
- **Clear dependency model**: Upper-stream concepts explicitly constrain lower-stream actions
- **Practical initialization strategy**: Uses fixed directories (`.agent/rules/`, `.agent/workflows/`) as entry points
- **Explicit path referencing**: Enables precise troubleshooting and modification discussions
- **Separation of concerns**: Distinguishes ethical constraints (rules) from execution optimization (workflows)

### Limitations
- **Partial implementation**: Current system only implements Levels 4, 5, and 6
- **Missing upper-stream layers**: Levels 1-3 (Purpose, Philosophy, Vision) are conceptual but not yet formalized in the repository structure
- **No validation mechanism**: No automated checks to ensure lower-stream compliance with upper-stream constraints

### Recommendation
Treat this as a **design blueprint** rather than current implementation. The existing `.agent/rules/` system can be extended upward to include Purpose and Philosophy layers when needed, but current operational needs are met by the implemented levels.

---

## The Seven-Level Hierarchy

The AI's behavior is governed by seven conceptual layers, moving from abstract motivation to concrete execution. Relationship: **Upper-stream concepts constrain and justify lower-stream concepts.**

| Level | Concept Name | Directory / Path | Primary Role for AI |
|:------|:-------------|:-----------------|:--------------------|
| **1** | **Worldview / Purpose** | `/Purpose_Worldview/` | Defines the AI's ultimate mission and existence |
| **2** | **Philosophy** | `/Purpose_Worldview/Philosophy/` | Establishes first principles and logical basis for reasoning |
| **3** | **Vision / Values** | `/Purpose_Worldview/Philosophy/Vision_Values/` | Defines organizational goals and priority criteria (e.g., speed vs. safety) |
| **4** | **Code of Conduct (Rules)** | `.agent/rules/` | Primary ethical guardrail. Specifies what the AI must not do (system fixed) |
| **5** | **Policy / Guidelines** | `.agent/rules/Policy_Guidelines/` | Specific domain rules. Detailed constraints for specific areas (e.g., data security) |
| **6** | **Workflow / SOPs** | `.agent/workflows/` | Standardized execution steps. Defines how tasks are performed (system fixed) |
| **7** | **Checklist / Instructions** | `.agent/workflows/Checklist/` | Atomic action items. Ensures reliable completion of single steps within a workflow |

---

## Hierarchical Distance

The conceptual distance between levels is not uniform:

**Upper-Stream Distance (Large)**
- Changes in Purpose or Philosophy involve significant shifts in the AI's core identity and fundamental reasoning
- Example: Changing from "maximize user productivity" to "maximize user well-being" fundamentally alters decision-making

**Lower-Stream Distance (Small)**
- Changes in Workflow or Checklist are purely tactical
- Example: Reordering steps in a deployment checklist has minimal conceptual impact

---

## Initialization Strategy

### Fixed Directory Constraint

The AI system has two fixed directories accessed unconditionally upon startup:
- `.agent/rules` (Level 4)
- `.agent/workflows` (Level 6)

### Entry Point Mechanism

**File**: `.agent/rules/README.md`

**Purpose**: Force context acquisition of the entire seven-level structure, especially upper-stream concepts (Levels 1-3) located outside fixed directories.

**Method**: The README.md contains explicit absolute paths and hyperlinks to upper-stream directories. Reading this file loads the full conceptual context upon initialization.

---

## AI Operational Logic

The AI's decision-making loop prioritizes fixed directories based on logical role:

1. **Read and Load Context**: Load `.agent/rules/README.md` to acquire seven-level context and upper-stream references
2. **Ethical Constraint Check**: Verify contemplated action against constraints defined in `.agent/rules/` (Levels 4/5). This is the "do/do not" check
3. **Execution Procedure Check**: If ethically approved, refer to `.agent/workflows/` (Level 6) for standardized execution procedure

---

## Guidelines for Human-AI Dialogue

### Reference Paths Directly
Use explicit paths for precision:
- "The conflict in your output seems to violate the constraint defined in `.agent/rules/Policy_Guidelines/Ethical_Use_Guide.txt`"

### Challenge Upper-Stream Concepts
To effect fundamental behavioral change:
- Challenge the validity of Philosophy
- Question the prioritization in Values (`/Purpose_Worldview/Philosophy/Vision_Values/`)

### Differentiate Control Points
Distinguish between:
- **Ethical Correction**: Modifying `.agent/rules/` (what the AI should/should not do)
- **Efficiency Correction**: Modifying `.agent/workflows/` (how the AI should execute tasks)

---

## Current Implementation Status

**Implemented Levels**:
- Level 4: `.agent/rules/` (Code of Conduct)
- Level 6: `.agent/workflows/` (Workflows)

**Conceptual Only**:
- Levels 1-3: Purpose, Philosophy, Vision (not yet formalized in directory structure)
- Level 5: Policy/Guidelines (partially implemented within `.agent/rules/`)
- Level 7: Checklist (not yet systematically separated from workflows)

**Next Steps**:
- Formalize upper-stream concepts if fundamental behavioral shifts are required
- Consider validation mechanisms to ensure lower-stream compliance with upper-stream constraints
