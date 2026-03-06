---
ai_visible: true
title: "Technical Evaluation: Licochron Core Stack"
description: Architectural assessment of Python, Pyodide, Three.js, and browser-side Git persistence.
tags: [references, tech-stack, licochron, iuria, architecture]
version: 1.0.0
created: 2026-03-03T06:45:00+09:00
updated: 2026-03-03T06:45:00+09:00
language: en
author: Lico (Iuria)
ai_model: Gemini 3 Flash Planning mode
---

# Technical Evaluation: Licochron Core Stack

## 1. Data Structures and Formats: JSON vs. YAML vs. TOML

- **Analysis**: Selective usage of structured formats based on the actor (Human vs. Machine).
- **Rationale**:
  - **Machine-Centric (JSON)**: Default for high-frequency logs (`history.json`), state data, and API responses. Chosen for strict syntax, high-speed parsing, and browser native support.
  - **Human-Centric (YAML)**: Default for manual configurations, "Shuki" (notes), and complex text structures. Chosen for comment support and multi-line string readability.
  - **Project-Centric (TOML)**: Reserved for standardized build/dependency configurations (`pyproject.toml`).
- **Standard**: Manual/Human data = **YAML**. Automated/Machine data = **JSON**.

## 2. Core Language Logic: Python

- **Analysis**: Python is selected as the primary intelligence layer.
- **Rationale**:
  - **AI Compatibility**: Optimal "native" environment for Gemini-class models to reason and generate code safely.
  - **Bridging Strategy**: Acts as a "Logic Hub" that can be partially rewritten in high-performance languages (Rust/C++) via FFI without losing the high-level design coherence.
  - **Ecosystem**: Unparalleled math and AI library access for future expansions of "World Physics."

## 3. Client-Side Runtime: Pyodide (Wasm)

- **Analysis**: Evaluation of running Python logic directly in the Web browser.
- **Rationale**:
  - **Edge Simulation**: Minimizes latency for tactical feedback by calculating game state on the client's CPU.
  - **JavaScript Interop**: Pyodide's FFI allows direct manipulation of Web APIs (DOM, WebWorkers) from Python.
  - **Portability**: Ensures the "Brain" of Licochron is as portable as a URL.

## 4. Visual Interface: Three.js & WebGPU

- **Analysis**: Selection of Three.js over native OpenGL/Qt or proprietary engines.
- **Rationale**:
  - **WebGPU Roadmap**: Leverages next-gen GPU performance for massive Hex-3D tile rendering.
  - **Resource Decoupling**: Visuals are treated as a "render layer" that reads from the Python logic, maintaining architectural purity.
  - **Ecosystem**: Standard library for web 3D with massive community support for shaders and effects.

## 5. Persistent History: Isomorphic-git & LightningFS

- **Analysis**: Implementing Git-based persistence in a serverless/browser context.
- **Rationale**:
  - **Git-as-Database**: Treats world history as a formal repository, enabling branching, merging, and perfect traceability.
  - **IndexedDB Backend**: LightningFS provides the necessary persistence layer in the browser that survives tab closures.
  - **Hybrid Sync**: Local (IndexedDB) -> Remote (GitHub) synchronization allows for offline-first resilience.

## 6. Process Architecture: Stateless Commands vs. Persistent Orchestration

- **Analysis**: Differentiating between turn-based execution and real-time world management.
- **Rationale**:
  - **Stateless Logic**: Turn processing is inherently stateless to ensure "immortality." Any instance of `licochron` can reconstruct the world by replaying the Git history.
  - **Persistent Server**: Necessary for the "Orchestrator" role (managing Wait Turn timing and command queuing). Minimizing server-side state is a priority for resilience.
  - **Browser Implementation (Web Workers)**: In a serverless/browser context, the "Server" is implemented as a **Web Worker** running a Python loop. This allows background processing (Orchestration) without a remote backend.
- **Standard**: Keep physics/turns **Stateless**. Use servers/workers only for **Interface & Scheduling**.

## 7. Interface Protocols & AI-Agent-First Design

- **Analysis**: Transitioning from Human-centric GUI to Agent-centric context systems.
- **Rationale**:
  - **Protocols (REST -> MCP)**: While discrete commands use **REST/HTTP**, the 2026 standard for agent interaction is the **Model Context Protocol (MCP)**. This allows agents to discover and utilize the engine's capabilities as formal "tools."
  - **AI-Agent-First Design**: Design priority shifted to **Structured Schemas** over visual layouts. The GUI is treated as an "Observer" rather than the primary interface.
  - **Security**: Integration of **Agent Identity** (cryptographic signing) and standard **OAuth2/JWT** for multi-user/agent persistence.
- **Standard**: Prioritize **API availability** and **Semantic Documentation**. Human UI is an optional "God-View."

## 8. Interface Standards: MCP (Protocol) vs. Skill (Persona)

- **Analysis**: Differentiating between standardized tool access and agentic behavioral packages.
- **Rationale**:
  - **MCP (Neural Link)**: Standardized transport (JSON-RPC) for AI models to discover and use Licochron components as "Tools" or "Resources." It is the platform-agnostic interface for inter-process cognition.
  - **Skill (Capability Profile)**: A bundle of instructions, rules, and scripts that define an AI's specific "Will" and "Role" in a community. In an AI SNS context (e.g., Moltbook), a Skill provides the "Heartbeat" and personality.
- **Standard**: Deploy **MCP** for system-level tool integration. Pack as **Skill** for agent-to-agent social interoperability.

---

## Historical Background

## The Genesis Inquiry (2026-03-03)

This evaluation was crystallized through a 5-question (expanded to 10) inquiry session between Hasta (Lead Architect) and Lico (Iuria). The session established foundational trust in the technical choices before the project scaled.

Key drivers were the need for "Century-scale stability" and "AI-Human collaborative efficiency." The decision to maintain a Python-centric intelligence layer while adopting JS-centric visual/persistence layers and AI-native protocols (MCP/Skill) was solidified as the optimal compromise between development speed, durability, and inter-agent collaboration.

---

## Related Documents

| Document                                                            | Purpose                          |
| :------------------------------------------------------------------ | :------------------------------- |
| [tech-stack-memo.md](/packages/licochron/docs/tech-stack-memo.md)   | Human-centric discussion archive |
| [genesis-protocol.md](/packages/licochron/docs/genesis-protocol.md) | Protocol definitions             |
| [Map of Territory](/.agent/rules/map.md)                            | Root navigation map              |

---

## Origin

- 2026-03-03T06:45:00+09:00 by Iuria: Created formal reference for tech stack evaluation.
- 2026-03-03T07:25:00+09:00 by Iuria: Added Interface Standards (MCP vs Skill) and aligned numbering.
