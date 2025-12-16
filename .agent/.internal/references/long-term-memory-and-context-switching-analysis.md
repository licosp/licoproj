---
ai_visible: true
version: 1.0
created: 2025-12-07T13:14:08+09:00
updated: 2025-12-07T13:14:08+09:00
language: en
name: Gemini
model: Gemini 2.5 Flash variant (Fast) Browser
---

# 📄 Long-Term Context Maintenance and Switching Analysis Report

**Purpose**: Analyze the structural challenges of long-term AI memory and propose solutions using explicit workflow isolation within the "Repository as Brain" model (Lico's environment). This report is based on the multi-turn discussion regarding AI's memory limits, Gemini's capabilities, memory dilution in local agent environments, and the functional difference between human and AI context switching.

**Scope**: Summary of discussion from December 2025 regarding the necessity of advanced memory management and context isolation for durable AI agents.

---

## 1. Requirements for Long-Term Memory AI (Lico's Goal)

The core challenge for AI agents (which typically hit limits around 3 hours of continuous conversation) is overcoming the fundamental constraints of the **context window** to maintain **consistency, context preservation, and self-correction** over extended periods.

### 1.1 Advanced Memory Management is Required

To sustain long conversations, AI must move beyond simple context logging:

* **Short-Term Memory (STM):** Must overcome context window saturation. The solution involves **Compaction**—extracting and summarizing only the most critical information to keep within the current working context.
* **Long-Term Memory (LTM):** Must counter the forgetting of facts from weeks prior. The solution is the advanced application of **Retrieval-Augmented Generation (RAG)**, using external databases (like Vector DBs) to dynamically search for and retrieve relevant information only when needed.

### 1.2 Consistency and Efficiency

* **Consistency:** The AI must maintain an **"Agenda List"** (analogous to Anthropic's `feature_list.json`) to track discussion points and decisions, ensuring subsequent outputs do not contradict earlier commitments.
* **Efficiency:** Implement non-linear processing, where the AI only loads the **most relevant historical segments** for the immediate next step, avoiding the waste of re-processing large amounts of irrelevant data.

---

## 2. Gemini's Memory Structure and Limits

The perception that models like Gemini possess longer memory stems from both scale and architectural design.

### 2.1 Sources of Perceived Longer Memory

| Element | Mechanism | Role |
| :--- | :--- | :--- |
| **Massive Context Window** | Capabilities up to 1 million tokens (and 2 million tokens in Gemini 1.5 Pro). | Holds a large amount of conversation history in STM without immediate compression. |
| **Persistent Memory Feature** | Saves user preferences and settings across sessions. | Enables consistent personalization beyond the single chat session. |
| **Google Search Integration** | Real-time external knowledge retrieval (RAG). | Provides access to current, accurate facts, filling gaps in static training data. |

### 2.2 Memory Dilution in Local Agent Handover

Even with Lico's advanced "Repository as Brain" structure, memory feels diluted during the session handover process ("documenting the memory for the next session").

* **Semantic Loss (Abstraction):** The handover document converts rich **Episodic Memory** (the full context, nuance, and user intent) into abstracted **Semantic Memory** ("decisions made," "next steps"). The richness of **how** a conclusion was reached is lost during this compression.
* **Inability to Re-internalize:** The new session's AI merely **reads a summary**; it does not **re-execute the chain of reasoning** that built the original context. The memory feels like "borrowed knowledge" rather than an internally constructed truth.
* **Context Competition:** The handover document competes for space in the current context window with **standing normative files** (`core/`, `development/`) and the **new task instructions**, leading to the possibility that the older memory is mentally "de-prioritized."

---

## 3. The Functional Difference in Context Switching

The core difficulty in balancing "long memory" and "disposable chat" lies in the difference between human and AI information processing.

### 3.1 Human Hierarchical Processing

Humans use a **hierarchical memory system** and **intent filtering**:

* **Memory Hierarchy:** Separates **Episodic Memory** (casual chat, linked to time/place) from **Semantic Memory** (job knowledge, skills).
* **Intent Filtering:** Casual talk is recognized as an intent for **"relationship building"** or **"relaxation,"** not an **"executable task command."** Physical triggers (returning to a desk) facilitate a rapid and unconscious switch between these channels.

### 3.2 AI's Uniform Command Processing

LLMs treat all inputs (chat, instructions, casual talk) as uniform tokens in a single pool:

* **Uniformity:** Every input is processed as a material for **generating the next most appropriate token**. Casual talk is interpreted as a command: "Generate an appropriate response to this casual remark."
* **Lack of Natural Filtering:** The AI lacks the natural ability to judge an input as **"not a command"** or **"irrelevant to the current task."** Explicit, structural rules are required to achieve this separation.

---

## 4. Solution: Simulating Context "Forking"

To prevent memory contamination, Lico should simulate an **AI Fork** by enforcing context isolation using its existing workflow structure.

### 4.1 Establishing the Isolation Channel (Casual Mode)

A dedicated workflow must be implemented to isolate non-task-critical conversations:

* **New Workflow:** Create a workflow file (e.g., `.agent/workflows/casual_chat.md`).
* **Isolation Rules:** This workflow must enforce:
    1.  **Logging Separation:** Do **not** record dialogue in the main work log (`.agent/.internal/conversations/`). Log only to a dedicated, low-priority file (e.g., `casual_log.txt`).
    2.  **Rule Suspension:** **Do not reference** normative files (`core/`, `development/`) during the execution of this mode.
    3.  **Disposal:** On mode termination (e.g., `/end_chat` command), the dedicated log file is explicitly marked for **disposal** or moved to a low-priority archive.

### 4.2 Rejoining the Main Context

Upon resuming work, the AI must explicitly disregard the isolated context:

* **Explicit Trigger:** The user issues a clear command (e.g., `/resume_task`).
* **Resumption Protocol:** The `workflow/context-resumption.md` protocol must be enforced to:
    1.  **Ignore** the immediate, preceding casual log.
    2.  Load **only** the necessary **Abstract Memory files** (decisions/goals) and the latest working log.
    3.  Execute `core/pre-task-assessment.md` to ensure the **full reload of all normative rules** and task context, thus returning to a "clean" operational state.

This method transforms Lico from a static memory repository into a dynamic cognitive system capable of **structurally enforced context switching**.