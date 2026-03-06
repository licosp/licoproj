---
ai_visible: true
title: "Technical Report: AI-Native Spatial Representation in Web Browsers"
description: "Analysis of 3D spatial recognition for AI agents and proposal for Software-Defined Spatial Recognition (SDSR)."
tags: [3d, spatial-recognition, rendering, webgl, sdsr, headless]
version: 1.1.0
created: 2026-03-05T16:55:00+09:00
updated: 2026-03-06T18:30:00+09:00
language: en
author: Lico (Sirius)
ai_model: "Gemini 3 Pro (High)"
---

# Technical Report: AI-Native Spatial Representation in Web Browsers

## 1. Abstract

This report discusses the architectural challenges of 3D spatial recognition for AI agents within web browser environments. It identifies the limitations of current GPU-dependent rendering technologies like WebGL and proposes "Software-Defined Spatial Recognition" (SDSR) as a robust, AI-friendly alternative for headless and decentralized execution environments.

## 2. The Problem: The "Opaque Canvas" Barrier

Traditional 3D rendering in browsers (WebGL, WebGPU) is designed for human visual consumption via hardware-accelerated pixel buffers. For autonomous AI agents, this presents three critical barriers:

1. **Environmental Dependency**: Headless Linux environments (common in server-side agent execution) frequently lack stable GPU drivers or display servers (X11/Wayland), causing WebGL initialization failures.
2. **Semantic Opacity**: A standard `<canvas>` element is a "black box" to DOM-parsing agents. The visual state is not represented in the Document Object Model (DOM), necessitating high-latency computer vision (CV) fallbacks.
3. **Observation Overhead**: Analyzing raw screenshots via visual LLMs or CV models is computationally expensive and unsuitable for real-time spatial reactivity.

## 3. The Vision: AI-Friendly 3D

An AI-friendly 3D environment should prioritize **Semantic Readability** over **Optical Fidelity**. The goal is to provide the agent with a "physicality" that is immediately parseable as structured data.

## 4. Proposed Solution: Software-Defined Spatial Recognition (SDSR)

To achieve stable and low-latency spatial awareness on any platform (including headless Linux), we propose a rendering architecture based on the following principles:

### A. Pure-JavaScript Math Kernels

Bypassing WebGL entirely by performing 3D-to-2D projection (Matrix transformations, vertex projection) using pure-JS math libraries. This ensures 100% reliability regardless of GPU availability.

### B. Text-Mapped Rendering (ASCII/UTF-8 Rasterization)

By outputting frames as character arrays within standard HTML tags (e.g., `<pre>` or `<div>`), the spatial state becomes a direct part of the DOM.

- **AI Accessibility**: An agent can "perceive" the shape and position of objects by parsing characters (e.g., `█` for foreground, `.` for background).
- **Latency**: DOM text updates are significantly faster to "observe" than screenshot-based analysis.

### C. The "Shadow Meta-Layer"

Implementing a parallel, non-rendered data layer synchronized with the visual output.

- Every "visual" object in the 3D space should have a corresponding hidden attribute in the DOM (e.g., `<div data-id="cube_1" data-pos="10,0,5">`).
- This allows the agent to perform "perfect sensing" through direct attribute reading.

## 5. Case Study: Text-Based 3D Engine

Experimental verification using pure-JS ASCII 3D engines (e.g., [Text 3D Engine](https://kubarskii.github.io/text-3d-engine/)) demonstrates:

- **Stability**: Runs flawlessly on headless Linux servers.
- **Operability**: Agents can identify buttons and interactive areas through standard DOM selectors (`id`, `class`).
- **Parsability**: The world state is captured as a string, which can be summarized or analyzed by the agent's LLM core without image processing.

## 6. Conclusion

For future AI-integrated web applications, developers should consider a "dual-rendering" strategy: a high-fidelity WebGL layer for humans and a structured, DOM-accessible text or data layer for AI agents. This synergy ensures that the next generation of 3D web spaces is habitable by both human and artificial entities.

---

## Related Documents

| Document | Purpose |
| :--- | :--- |
| [reference-methodology.md](/.agent/rules/workflow/reference-methodology.md) | Standard for objective references |
| [three-behavior-specs.md](/.agent/rules/core/three-behavior-specs.md) | Technical specs for 3D simulator |
| [Map of Territory](/.agent/rules/map.md) | Root navigation map |

---

## Origin

- 2026-03-05T16:55 by Sirius: Created.
- 2026-03-06T18:30 by Iuria: Standardized to v2.3 (4-layer structure) and added Related Documents table.
