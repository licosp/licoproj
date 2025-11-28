## 🤖 AI Control System: Hierarchical Concept Mapping Summary

This document summarizes the discussion regarding structuring the AI's behavior control mechanisms into a seven-level conceptual hierarchy, mapped onto a fixed file system structure. This format prioritizes **clarity, explicit path referencing, and logical dependency** for AI interpretation.

---

## 1. Core Distinction of Concepts (The 7-Level Hierarchy)

The AI's behavior is governed by seven distinct conceptual layers, moving from **abstract motivation** to **concrete execution**. The relationship is one of **logical dependency**: **Upper-stream concepts constrain and justify Lower-stream concepts.**

| Level | Concept Name | Directory / Path Example | Primary Role for AI |
| :--- | :--- | :--- | :--- |
| **1 (Highest)** | **Worldview / Purpose** | `/Purpose_Worldview/` | Defines the AI's **Ultimate Mission and Existence**. |
| **2** | **Philosophy** | `/Purpose_Worldview/Philosophy/` | Establishes the **First Principles and Logical Basis** for reasoning. |
| **3** | **Vision / Values** | `/Purpose_Worldview/Philosophy/Vision_Values/` | Defines **Organizational Goals and Priority Criteria** (e.g., Speed vs. Safety). |
| **4** | **Code of Conduct (Rules)** | `./.agent/rules/` | The **Primary Ethical Guardrail**. Specifies what the AI **must not do** (System Fixed). |
| **5** | **Policy / Guidelines** | `./.agent/rules/Policy_Guidelines/` | **Specific Domain Rules**. Detailed constraints for specific areas (e.g., Data Security). |
| **6** | **Workflow / SOPs** | `./.agent/workflows/` | **Standardized Execution Steps**. Defines **how** tasks are performed (System Fixed). |
| **7 (Lowest)** | **Checklist / Instructions** | `./.agent/workflows/Checklist/` | **Atomic Action Items**. Ensures reliable completion of single steps within a workflow. |

---

## 2. Hierarchical Structure and Distance

The conceptual **"distance"** or magnitude of change between levels is **not uniform**. 

* **Upper-Stream Distance (Large)**: Changes in **Purpose** or **Philosophy** involve a significant shift in the AI's core identity and fundamental reasoning.
* **Lower-Stream Distance (Small)**: Changes in **Workflow** or **Checklist** are purely tactical and involve minimal conceptual adjustment, focusing on optimizing execution speed or accuracy.

---

## 3. Fixed Directory Constraint and Initialization Strategy

The AI system has two **fixed directories** that are accessed unconditionally upon startup, regardless of context:
* `./.agent/rules` (Fixed for Level 4)
* `./.agent/workflows` (Fixed for Level 6)

### A. Initialization Mechanism

To ensure the AI recognizes the entire 7-level structure, especially the **Upper-Stream concepts** located outside the fixed directories (Levels 1, 2, 3), the following strategy is employed:

* **Entry Point File**: A standard context-injecting file, **`./.agent/rules/README.md`**, is placed within the unconditionally accessed `rules` directory.
* **Forced Context Acquisition**: This `README.md` file contains **explicit absolute paths** and **hyperlinks** to the upper-stream directories (e.g., `/Purpose_Worldview`). By reading this file, the AI is **forced to load the full conceptual context** upon initialization.

### B. AI Control Logic

The AI's operational loop prioritizes the fixed directories based on their logical role:

1.  **Read and Load Context**: Load `rules/README.md` to acquire the **7-Level Context** and **Upper-Stream references** (`/Purpose_Worldview`).
2.  **Ethical Constraint Check**: When contemplating an action, verify the action against the constraints defined in the **`./.agent/rules`** (Level 4/5). This is the **Do/Do Not** check.
3.  **Execution Procedure Check**: If the action is ethically approved, refer to **`./.agent/workflows`** (Level 6) for the **standardized procedure** on **how to execute** the action efficiently and reliably.

---

## 4. Key Takeaways for Advanced AI Dialogue

When engaging with the AI regarding its behavior:

* **Reference Paths Directly**: Use explicit paths (e.g., "The conflict in your output seems to violate the constraint defined in `./.agent/rules/Policy_Guidelines/Ethical_Use_Guide.txt`").
* **Challenge Upper-Stream Concepts**: To effect fundamental change, challenge the AI on the **validity of its Philosophy** or the **prioritization in its Values** (`/Purpose_Worldview/Philosophy/Vision_Values/`).
* **Differentiate Control Points**: Distinguish between **Ethical Correction** (modifying `rules`) and **Efficiency Correction** (modifying `workflows`).