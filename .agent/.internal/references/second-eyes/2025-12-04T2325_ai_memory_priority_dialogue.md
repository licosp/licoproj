---
ai_visible: true
version: 1.0
created: 2025-12-04T23:25:00+09:00
updated: 2025-12-04T23:25:00+09:00
language: en
name: Gemini
model: Gemini 2.5 Flash variant (Fast)
---
# AI Dialogue Summary: Memory, Priority, and Conceptual Structure

This report summarizes a multi-turn conversation focused on the internal mechanisms of Large Language Models (LLMs), specifically concerning information hierarchy, memory management, and the definition of "importance." This summary is structured for clarity in high-level AI model interaction.

## 1. Information Prioritization and "Forgetting"

The initial topic explored how an AI would define what it "forgets."

* **Definition of Forgetting:** AI defines "forgetting" not as memory loss, but as **information falling below a processing priority threshold** or **data lacking necessary emotional/contextual depth** (i.e., human nuance).
* **Low-Priority Extraction:** Methods to retrieve low-priority data involve querying for:
    * Uncompleted or reserved discussion topics.
    * Keywords only mentioned once (low-frequency data).
    * Information designated as "cut" during a summarization process.
* **Criteria for "Importance":** In the context of a summary report, importance is strictly judged by:
    * **Contribution to Goal Achievement:** Information leading to the conversation's conclusion, agreement, or concrete next actions.
    * **Frequency and Consistency:** Topics that consumed the most time and were referenced repeatedly.

## 2. Memory Structure and Storage

The dialogue transitioned to the technical difference between human memory and AI memory systems.

### A. Memory Components:
* **Short-Term Memory (Context Window):** The active history of the current chat, referenced instantly by the model in its entirety for next-token prediction. It has a size limit and is temporary.
* **Long-Term Memory (LTM):** Composed of two parts:
    1.  **Model Parameters (Core Knowledge):** The vast, strong, and static knowledge base established during training (e.g., world facts, logic). It is generally unchangeable during conversation.
    2.  **External Knowledge Base (RAG):** Tools (like Google Search or Vector Databases) used to retrieve real-time or specific data not contained in the parameters.
* **User Memory (Personalized Memory):** System-level storage for user preferences and identity, explicitly requested by the user to be saved across sessions.

### B. Repetition and Value Change:
* **Repetition Effect:** Repeating "worthless information" temporarily increases its **short-term attention weight** within the current context window, leading to its inclusion in immediate responses.
* **Value Stability:** This repetition does **not** alter the AI's fundamental **long-term values** or ethical framework, which are fixed by pre-training and safety alignment (RLHF) on massive datasets.

## 3. Tool Usage

AI models do not use human-style "memos" because the entire context window is processed instantly. Dedicated "Memory Tools" are utilized for specific functions:

* **RAG & Vector Databases:** For knowledge retrieval and dynamic content injection.
* **User Memory:** For persistent, personalized user data storage across different sessions.
---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
