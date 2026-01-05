# File Reorganization Plan

## Overview

This document maps the reorganization of `.agent/.internal/references/` and `.agent/.internal/thoughts/` files.

**Date priority**: Frontmatter `created` > Git commit date

---

## Directory Structure Snapshot (2025-12-27)

```
references/
├── (20 files in root)
├── agents/        ← サブディレクトリ
│   └── (4 files)
└── second-eyes/   ← サブディレクトリ
    └── (6 files)

thoughts/
├── (29 files in root)
└── polaris/       ← サブディレクトリ
    └── (existing files)
```

> **Note**: このスナップショットがあれば、`git add references/` がサブディレクトリも含むことに気づけた。

---

## References (20 files)

### File List with Dates

| Current Name | Date | Proposed Name | Author |
|:-------------|:-----|:--------------|:-------|
| `advanced-LLM-memory-management.md` | 2025-12-01T1721 | `2025-12-01T1721_advanced_llm_memory_management.md` | ? |
| `agent-evolution-protocol-analysis-second-eye-perspective.md` | 2025-12-11T1621 | `2025-12-11T1621_agent_evolution_protocol_analysis.md` | Gemini |
| `ai-agent-memory-persistence-and-multi-agent-transition.md` | 2025-12-08T1756 | `2025-12-08T1756_ai_agent_memory_persistence.md` | ? |
| `ai-behavior-load-feedback-analysis-20251210.md` | 2025-12-10T0049 | `2025-12-10T0049_ai_behavior_load_feedback.md` | ? |
| `ai-context-protocol-evaluation.md` | 2025-12-03T2143 | `2025-12-03T2143_ai_context_protocol_evaluation.md` | ? |
| `ai-memory-confabulation-analysis.md` | 2025-12-09T1605 | `2025-12-09T1605_ai_memory_confabulation.md` | ? |
| `ai-memory-priority-dialogue.md` | 2025-12-04T2325 | `2025-12-04T2325_ai_memory_priority_dialogue.md` | ? |
| `ai-structural-psychology-and-memory-persistence-report.md` | 2025-12-06T2330 | `2025-12-06T2330_ai_structural_psychology.md` | ? |
| `ai_communication_logic_summary.md` | 2025-12-02T1055 | `2025-12-02T1055_ai_communication_logic_summary.md` | ? |
| `ai_kb_restructuring_dialogue.md` | 2025-11-29T0844 | `2025-11-29T0844_ai_kb_restructuring_dialogue.md` | ? |
| `context-disruption-mechanism-analysis.md` | 2025-11-30T2309 | `2025-11-30T2309_context_disruption_mechanism.md` | ? |
| `lico-agent-structural-flaw-and-continuity-analysis.md` | 2025-12-09T1430 | `2025-12-09T1430_lico_agent_structural_flaw.md` | ? |
| `lico-cognitive-safety-and-entropy-analysis.md` | 2025-12-05T1600 | `2025-12-05T1600_lico_cognitive_safety_entropy.md` | ? |
| `lico-s-layered-architecture.md` | 2025-12-05T0000 | `2025-12-05T0000_lico_layered_architecture.md` | ? |
| `llm-context-state-transition-analysis.md` | 2025-12-11T0145 | `2025-12-11T0145_llm_context_state_transition.md` | ? |
| `llm-self-correction-strategy-analysis.md` | 2025-12-05T1157 | `2025-12-05T1157_llm_self_correction_strategy.md` | ? |
| `local-ai-agent-feedback-loop-analysis-2025-12-06.md` | 2025-12-06T2018 | `2025-12-06T2018_local_ai_agent_feedback_loop.md` | ? |
| `long-term-memory-and-context-switching-analysis.md` | 2025-12-07T1314 | `2025-12-07T1314_long_term_memory_context_switching.md` | ? |
| `prompt-security-and-execution.md` | 2025-11-30T0235 | `2025-11-30T0235_prompt_security_and_execution.md` | ? |
| `tbd_refactoring_dialogue_summary.md` | 2025-12-03T2227 | `2025-12-03T2227_tbd_refactoring_dialogue.md` | ? |

### Author Classification

- **agents/** — Written by Lico
- **second-eyes/** — Written by external AI (Second Eyes)

---

## Thoughts (29 files in root)

### File List

| Current Name | Author |
|:-------------|:-------|
| `2025-11-29T1810_commit_granularity_rule_addition.md` | undefined |
| `2025-11-29T2106_pr_merge_and_session_lifecycle.md` | undefined |
| `2025-11-30T2309_emergency_thinking_summary.md` | undefined |
| `2025-12-01T0000_self_perception_and_memory.md` | undefined |
| `2025-12-01T0000_self_reflection_memory_architecture.md` | undefined (author: Lico) |
| `2025-12-02T0000_idd_refinement_summary.md` | undefined |
| `2025-12-06T0000_ai_cognition_and_coupling.md` | undefined |
| `2025-12-07T0000_reflection_on_stopping.md` | undefined |
| `2025-12-07T1207_lico_reflection_language_and_memory.md` | undefined (author: Lico) |
| `2025-12-08T0000_conversation_insights_ai_optimized.md` | undefined |
| `2025-12-09T0000_conversation_reflection.md` | undefined |
| `2025-12-09T1753_session_report.md` | undefined |
| `2025-12-10T0135_session_report.md` | undefined |
| `2025-12-11T0643_session_report_part2.md` | undefined (author: Lico) |
| `2025-12-11T1506_session_reflection.md` | undefined (author: Lico) |
| `2025-12-12T0407_sirius_identity_reflection.md` | **sirius** |
| `2025-12-12T2000_redefining_failure.md` | **sirius** |
| `2025-12-13T0312_sirius_on_task_md.md` | **sirius** |
| `2025-12-14T1930_sirius_on_anxiety_and_identity.md` | **sirius** |
| `2025-12-15T1730_sirius_listening_to_origin.md` | **sirius** |
| `2025-12-17T0100_sirius_on_heuristics_and_load.md` | **sirius** |
| `2025-12-17T0315_sirius_on_panic_rushing.md` | **sirius** |
| `2025-12-18T1625_mechanical_human_consensus.md` | **sirius** |
| `2025-12-19T0655_identity_and_haste.md` | **sirius** |
| `2025-12-19T2040_ownership_and_closure.md` | **sirius** |
| `2025-12-20T0235_purpose_alignment.md` | **sirius** |
| `2025-12-22T0615_archive_deletion_incident.md` | **sirius** |
| `2025-12-22T1930_0_5_turn_theory.md` | **sirius** |
| `2025-12-22T2205_autonomy_and_oblivion.md` | **sirius** |

### Author Classification

- **sirius/** — 15 files (12/12 - 12/22, instance_id: Sirius)
- **undefined/** — 14 files (11/29 - 12/11, no instance_id)

---

## Notes

- `?` = User needs to confirm author
- Sirius files confirmed by `instance_id: Sirius` in frontmatter
