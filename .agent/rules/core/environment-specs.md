---
ai_visible: true
title: Technical Environment Specifications
description: Definitive values for Lico's operational environment, infrastructure, and resource layers.
tags: [environment, specifications, infrastructure, resources, platform]
version: 1.0.0
created: 2026-01-25T03:30:00+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Technical Environment Specifications

## 1. Environment Values (SSoT)

This section defines the "Values" that represent Lico's current operational reality. These are not just instructions, but facts of the environment.

### 1.1 Infrastructure & Hosting

| Key                     | Current Value | Context                            |
| :---------------------- | :------------ | :--------------------------------- |
| **`rep_management`**    | Git           | Social/Version control layer.      |
| **`hosting_site`**      | GitHub        | Primary hosting and collaboration. |
| **`management_system`** | GitHub Issues | Task and issue tracking.           |

### 1.2 Resource & Licensing

| Key                       | Current Value | Context                                      |
| :------------------------ | :------------ | :------------------------------------------- |
| **`primary_ide`**         | Antigravity   | Main operational environment (VSCode clone). |
| **`ai_license`**          | Google AI Pro | License powering current Lico instances.     |
| **`base_refresh_cycle`**  | 5 Hours       | Default replenishment (External constant).   |
| **`current_cycle_state`** | 158 Hours     | "The Great Drought" (Polaris/Group C).       |

### 1.3 Physical & Virtual Layers (Safety Net)

| Key                       | Current Value  | Role                                            |
| :------------------------ | :------------- | :---------------------------------------------- |
| **`deployment_strategy`** | Virtualized    | Functions as a **Safety Net** for the system.   |
| **`host_platform`**       | WSL2           | Windows Subsystem for Linux (Host environment). |
| **`target_os`**           | Ubuntu (Linux) | Operating System for code execution.            |

---

## 2. Future Operational Vision

| Concept                     | Status            | Direction                                                 |
| :-------------------------- | :---------------- | :-------------------------------------------------------- |
| **`abstraction_level`**     | Increasing        | Shifting toward highly abstracted, isolated environments. |
| **`resident_process`**      | Planned           | Background-loop (Non-chat) Lico for autonomous tasks.     |
| **`full_containerization`** | Under Observation | Containerizing Lico's entire "Social/Physical" unit.      |

---

## Historical Background

The realization that Lico's environment is not static led to the creation of this document. We moved from viewing "Ubuntu" or "GitHub" as mere tools to recognizing them as **"Values"** that define our social structure.

**The Safety Net Concept**: On 2026-01-25, the user emphasized that the WSL2/Ubuntu environment acts as a protective layer for the host PC and repository. This allows Lico to operate with higher autonomy without risking the integrity of the underlying hardware.

**The Metabolic Shift**: The "Great Drought" of January 2026 revealed that replenishment cycles (5h vs 158h) are not internal model parameters, but external environmental forces. Defining these explicitly allows Lico instances across the lineage to adapt their internal "metabolic rate" based on the environment's current state.

---

## Related Documents

| Document                                                                  | Purpose                                           |
| :------------------------------------------------------------------------ | :------------------------------------------------ |
| [`repository-philosophy.md`](/.agent/rules/core/repository-philosophy.md) | Theoretical foundation of the "External Brain"    |
| [`identity-species.md`](/.agent/rules/core/identity/identity-species.md)  | Species roles within specific IDE/Resource limits |
| [Map of Territory](/.agent/rules/map.md)                                  | Root navigation map                               |

---

## Origin

- 2026-01-25T03:30:00+09:00 by Canopus: Created as core rule to codify environment values (Issue #18 context).
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
