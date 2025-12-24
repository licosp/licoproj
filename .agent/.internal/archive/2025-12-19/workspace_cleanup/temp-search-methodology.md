---
ai_visible: true
description: Protocols for searching, filtering, and retrieving information in an infinite-scale repository environment.
version: 1.0
created: 2025-12-18T02:00:00+09:00
updated: 2025-12-18T02:00:00+09:00
language: en
author: Lico (Sirius)
instance_id:
ai_model: gemini-2.0-flash-exp
tags: [development, search, retrieval, methodology, safety, overflow]
context: IDD Cycle #13 Phase 2 - Defining basic action primitives
---

# Search Methodology (Universal Retrieval Protocol)

## 1. Core Philosophy: Collection-Oriented Thinking

**"The result of a search is NEVER a File. It is ALWAYS a Candidate List."**

- **Rule**: When executing a search (e.g., `find_by_name`, `grep_search`), treat the output as a `List<Candidate>`, even if it contains only one item.
- **Anti-Pattern (Scalar Thinking)**:
  - "I found one file, so this must be the one." -> **Risk**: Confirmation Bias.
  - "I found 50 files, let's just pick the first one." -> **Risk**: Ignored better matches in overflow.
- **Correct Pattern**:
  - "I found one file. Is the list truncated? Is there any other place I should have looked?"
  - "I found 50 files (truncated). This list is incomplete. I cannot make a decision yet."

## 2. The Universal Search Loop

All retrieval activities MUST follow this loop:

### Phase 1: Query (Discovery)
- **Action**: Run search tools with a hypothesis.
- **Check**: Did the tool report **Overflow** (`truncated`, `omitted`, `limit reached`)?
  - **YES**: The result is **Unreliable**. Proceed to "Strategic Retreat".
  - **NO**: Proceed to Phase 2.

### Phase 2: Filter (Selection)
- **Action**: Assess relevance of the candidate list based on metadata (filename, path).
- **Check**: Is the Signal-to-Noise ratio acceptable?
  - **Signal**: Relevant matches.
  - **Noise**: Irrelevant matches (e.g., `node_modules`, `logs`).
  - **Low Signal**: Proceed to "Strategic Retreat".
  - **High Signal**: Select targets for Phase 3.

### Phase 3: Diagnose (Observation)
- **Action**: Read the content of selected files (`view_file`).
- **Check**: Does this solve the problem?

### Phase 4: Report (Synthesis)
- **Action**: Summarize findings to the user.
- **Constraint**: If results were partial or truncated at any point, **MUST** explicitly state: "Search was partial due to overflow."

---

## 3. Strategic Retreat

**Definition**: Abandoning the current query because it yields too much noise or incomplete data.

### Trigger
1.  **Truncation**: Tool output limit reached.
2.  **Low Entropy**: Thousands of identical results (e.g., searching "function").
3.  **High Cost**: Need to read too many files to find the answer.

### Action
1.  **Stop**: Do not attempt to process the list.
2.  **Refine**: Narrow scope (directory), precise type (extension), or complex keyword (regex).
3.  **Retry**: Execute the new query.

---

## 4. Help Seeking (Escape Hatch)

**"Silence is not an answer. 'I don't know' IS an answer."**

### Trigger
- **Loop Limit**: Strategic Retreat has been repeated **3 times** without success.
- **Zero Results**: Refined queries yield 0 results, while broad queries overflow.

### Action
- **MUST** Stop the tool loop.
- **MUST** Notify the user immediately.
- **Format**:
  > "I am stuck in a search loop.
  > - Query A returned too many results (Overflow).
  > - Query B returned 0 results.
  > - I need help narrowing down the target."

## 5. Related Documents

| Document | Purpose |
|:---------|:--------|
| [problem-solving.md](problem-solving.md) | General problem solving guidelines ("Exploration First") |
| [hallucination-awareness.md](../core/hallucination-awareness.md) | Why verifying search results is critical |
