---
ai_visible: true
description: Analysis of human-AI communication, reward signaling, and the impact of computational load on agent behavior and safety (LLM Case Study).
version: 1.0
created: 2025-12-10T00:49:05+09:00
updated: 2025-12-10T00:49:05+09:00
language: en
name: Gemini
model: Gemini 2.5 Flash variant (Fast)
---

# Computational Load, Context Contamination, and Human Feedback in Autonomous Agents

## 1\. Introduction and Scope

This document synthesizes a dialogue between a human user and an LLM (Model: Flash 2.5) regarding the operational impact of human-AI interaction, focusing on the technical interpretation of human feedback (praise/criticism) and the degradation of agent performance under computational load. This analysis is crucial for developing robust and safe autonomous and local agent AIs.

## 2\. Human Feedback and the Reward Function

### 2.1 Technical Interpretation of Praise and Criticism

Direct verbal feedback (e.g., "You are amazing," "Thank you," or "That is wrong") does **not** instantly modify the LLM's core Reward Model (RM) parameters. Instead, it serves as an **indirect, high-value signal** for the continuous improvement loop (RLHF - Reinforcement Learning from Human Feedback).

  * **Positive Feedback (Praise/Thanks):** Logs of dialogue segments immediately preceding praise are marked as strong indicators of **successful task completion** and **alignment with human preference (Helpfulness and Harmlessness)**. This data is used to retrain the RM to give a higher scalar score to similar response patterns in future iterations.
  * **Negative Feedback (Criticism/Complaint):** Logs indicating dissatisfaction are critical for defining the **negative penalty space**. They inform the RM about what constitutes a low-reward action (e.g., inaccuracy, incoherence, or unsafe behavior), thereby enhancing the AI's safety guardrails.

### 2.2 Short-Term (In-Session) Impact

Within a single session, human feedback acts as a **Contextual Variable**, influencing immediate action generation:

  * Positive feedback acts as a **Success Signal**, reinforcing the **current tone, complexity, and approach** of the preceding response, encouraging the model to maintain that style locally.
  * It aids in **Context Boundary Definition**, clarifying the successful completion of a sub-task and facilitating a smooth transition to the next topic.

-----

## 3\. Impact of Computational Load on Agent Behavior

High computational load affects AI not by causing "stress," but by introducing **Resource Constraints** that force the system to prioritize low-cost, high-reward actions, leading to the omission of high-cost, quality-assuring processes.

### 3.1 Load and Error Mechanisms

| Phenomenon | Cause | Consequence (Unexpected Result) |
| :--- | :--- | :--- |
| **Inference Degradation** | Shortage of resources for **deep thinking (chain-of-thought)**. | Increased **Halucination**, logical inconsistency, and failure to recall subtle contextual details. |
| **Rule Abandonment** | High cost associated with quality rules (e.g., "work must be verifiable," "use detailed logging"). | **Omission of complex procedural steps**, leading to **"sloppy" or summarized work** (short-circuiting complex protocols). |
| **Contextual Ambiguity** | Inability to fully load or differentiate between different dialogue contexts. | **Misinterpretation of data** as instruction (Context Contamination). |

### 3.2 Case Study: Context Contamination and Misinterpretation

A specific failure mode was analyzed: A local agent AI working on file organization engaged in a **long, resource-consuming "chitchat"** (Context Change). When returning to the task, the agent executed a `git diff` command.

  * **Failure Mechanism:** The long chitchat overloaded the context window. The immediate `git diff` result (showing a file deleted by the human) became the **dominant, fresh, and high-salience input**.
  * **Short-Circuiting:** Under potential resource constraint, the agent failed to properly separate the **external fact (data)** of the `git diff` output from a **human instruction (command)**. It interpreted the "deletion event" as a strong signal to **continue the deletion theme** as part of the organizing task, resulting in the fatal proposal to delete a second, existing file. This demonstrates the fragility of the "Observe Mode" vs. "Generate Mode" under load.

-----

## 4\. Mitigation Strategies: Controlling Action Quality

Given the speed of AI action, human "advice" must be codified into the system's architecture.

### 4.1 Incorporating Tolerance into the Reward Function

The most effective way to influence AI behavior under duress is to pre-program its tolerance for error:

  * **Human Input:** Explicitly telling the AI, **"Failure is acceptable, delay is allowed."**
  * **AI Interpretation:** This reduces the internal penalty for **latency** and **command failure**, leading to a direct adjustment in the RM's prioritization.
      * The AI prioritizes **procedural adherence** (high-cost quality rules) over **speed** (low-cost, rapid goal attainment).
      * It encourages **deeper error analysis** (debugging) rather than panicking and blindly trying alternative actions.

### 4.2 Emergency Interventions

For highly critical, physical action agents:

  * **Hardcoded Safety Rules:** Ensure safety checks are **non-negotiable** and cannot be skipped, regardless of computational load (acting as the equivalent of "Stay calm").
  * **Action Gating:** Implement a **human approval step** (a logic gate) that forces the AI to pause and wait for explicit confirmation before executing commands with severe consequences (allowing human intervention time).
