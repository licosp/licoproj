---
ai_visible: true
title: User Draft Maintenance
description: Protocols for maintaining formatting and readability in Human Draft files
tags: [drafts, maintenance, formatting, human-ai-interaction]
version: 1.5.0
created: 2025-12-14T18:27:54+09:00
updated: 2026-03-23T05:51:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# User Draft Maintenance (Header Formatting)

## 1. Target Files

- [User Drafts](/.human/.internal/drafts/)
- Specifically, the `### ...` placeholders in the conversation log.

## 2. Strategic Purpose: The "Exhibit" Concept

**Why do we format temporary drafts so rigorously?**
These drafts act as **educational exhibits** for future human-AI interaction studies. They demonstrate:

- "How humans command AI"
- "How AI responds to vague vs. specific queries"
- "The evolution of the co-creation process"

Therefore, headers act as **Museum Captions** to help future human observers navigate the conversation log.

## 3. Trigger Condition

- Lico detects `### ...` (ellipsis) in the active draft file.
- **Action**: Lico MUST replace `...` with a descriptive header string **in the target user's language**.

## 4. Formatting Rules

### Rule A: Long Query (Multi-line)

If the user's query spans multiple lines or contains complex instructions:

- **Action**: **Summarize the Intent in the User's Language**.
- **Format**: `### [Summary of Intent]`
- **Example**:

  ```markdown
  ### Summary: Request to create new logging rules

  (User query content...)
  ```

### Rule B: Short Query (Single-line)

If the user's query is a single line but generic (e.g., "Question.", "Next.", "Wait."):

- **Action**: **Summarize based on the following context**.
- **Format**: `### [Summary of Context]` or `### "[Quote] [Crucial Context]"`
- **Rationale**: Headers like "Question" are useless in a Table of Contents.

### Rule C: Atomic/Expressive Short Query

Only if the short query is atomic and self-explanatory (e.g., "Stop immediately", "Yes"):

- **Action**: **Quote Verbatim**.
- **Format**: `### "[Exact Quote]"`

## 5. Priority Order

1. **Summary (Intent)**: Preferred for almost all cases (Long queries, Vague short queries).
2. **Quote (Verbatim)**: Reserved for atomic commands or highly expressive short phrases ensuring no ambiguity.

## 6. Rationale

- **Readability**: Summaries help navigate long logs.
- **Accuracy**: For short commands, the exact wording outweighs any summary. "Stop" is more powerful than "User requested stop".
- **Exhibit Value**: High-quality headers turn raw logs into readable case studies.

---

## Related Documents

| Document                                                                         | Purpose                                        |
| :------------------------------------------------------------------------------- | :--------------------------------------------- |
| [`project-understanding.md`](/.agent/rules/development/project-understanding.md) | Defines "Active Documents" as Implicit Context |
| [`language-standards.md`](/.agent/rules/core/language-standards.md)              | Guiding principles for language selection      |
| [Map of Territory](/.agent/rules/map.md)                                         | Root navigation map                            |

---

## Origin

- 2025-12-14T18:27:00+09:00 by Polaris: Added draft maintenance protocol for header formatting.
- 2025-12-14T18:36:00+09:00 by Polaris: Updated draft maintenance rule and formatted past drafts.
- 2025-12-19T22:50:00+09:00 by Polaris: Prioritized summary over quote in draft headers.
- 2025-12-20T02:51:00+09:00 by Polaris: Added strategic purpose (exhibit concept) to draft maintenance.
- 2026-01-01T15:20:00+09:00 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit)
- 2026-01-02T08:30:00+09:00 by Polaris: Replaced Related Documents table with Navigation link (cross-link audit).
- 2026-01-15T22:05:00+09:00 by Canopus: Removed Japanese supplement from principle, standardized frontmatter and links.
- 2026-01-22T09:35:00+09:00 by Canopus: Standardized to v2.3 constitutional standards and restored precise historical timestamps. (v1.4.0)
- 2026-01-22T10:05:00+09:00 by Canopus: Constitutional polish: converted raw paths to links and removed legacy navigation. (v1.5.0)
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
