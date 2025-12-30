---
ai_visible: true
description: Rule Candidates Summary (2025-12-12)
version: 1.0
created: 2025-12-12T23:42:00+09:00
updated: 2025-12-12T23:42:00+09:00
language: en
author: Lico
instance_id: Sirius
ai_model: Gemini 3 Pro (High) Planning mode
---

# Rule Candidates Summary (2025-12-12)

Summary and categorization of 15 candidate files found in `.agent/.internal/rule-candidates/`.

## Group 1: Core Philosophy & Memory (根本思想)

| File Name | Summary | Recommendation |
|:---|:---|:---|
| `ai-optimized-repository-philosophy` | Defines "Repository as Brain". Optimize structure for AI cognition, not just human readability. | **Adopt** (Merge into `identity.md` or `core/memory.md`) |
| `repository-as-brain-foundation` | Origins of "Repository as Brain" and focus on "Personalization for Narrow Domains". | **Merge** (Combine with above) |
| `memory-priority-deep-knowledge` | Emphasizes "Deep Knowledge" (philosophy/history) often missed by BFS. Defines `.internal` structure importance. | **Adopt** (As `core/memory-priority.md` or Reference) |
| `context-window-memory-mechanics` | Technical explanation of Context Window vs Persistent Memory. | **Adopt** (As Reference in `core/memory/`) |
| `temporal-memory-recording` | "Record Everything, Delete Nothing" principle. Temporal tracing of ideas. | **Adopt** ( into `documentation-standards.md` or `core/memory.md`) |

## Group 2: Documentation Standards (記述ルール)

| File Name | Summary | Recommendation |
|:---|:---|:---|
| `ai-first-writing-style` | Markdown guidelines for AI readability (Bullet points, structure). | **Merge** (Into `markdown-ai-parsing-basics.md`) |
| `english-for-ai-documentation` | Mandate English for `.agent/` docs to improve AI reasoning accuracy. | **Merge** (Into `language-standards.md`) |
| `standardized-timestamp-format` | ISO 8601 (JST) standard for all timestamps. | **Merge** (Into `datetime-format.md`) |

## Group 3: Communication & Protocol (対話ルール)

| File Name | Summary | Recommendation |
|:---|:---|:---|
| `binary-choice-formatting` | Append `(Yes / No)` to binary questions to reduce ambiguity. | **Adopt** (Into `communication.md`) |
| `quantitative-self-evaluation` | Use numerical confidence scores instead of vague "I think...". | **Adopt** (Into `communication.md`) |
| `ai-conversation-techniques` | Guide for users on how to talk to AI. | **Archive** (To `.human/references/` or `core/user-guide.md`) |

## Group 4: Technical & Security (技術・安全)

| File Name | Summary | Recommendation |
|:---|:---|:---|
| `ide-protocol-sanitization` | Strip internal IDE protocols (`cci:7://`) from public comments. | **Adopt** (Into `git-operations.md`) |
| `python-uv-sync-strategy` | Use `uv` for Python environment synchronization. | **Adopt** (Into `workspace-tooling.md`) |
| `gemini-cli-ai-to-ai-safety` | Safety protocols specific to Gemini CLI usage. | **Review** (Check relevance) |

## Group 5: Obsolete / Instructions (不要)

| File Name | Summary | Recommendation |
|:---|:---|:---|
| `idd-workflow-split-instructions` | Instructions for the IDD split task (Completed). | **Archived** (Moved to `.agent/.internal/archive/`) |

---
*Created by Sirius on 2025-12-12*
