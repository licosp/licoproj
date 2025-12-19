---
description: Protocols for maintaining formatting and readability in Human Draft files
related:
  .agent/rules/development/project-understanding.md: Defines "Active Documents" (Drafts) as Implicit Context
  .agent/rules/core/language-standards.md: Guiding principles for language selection
---

# User Draft Maintenance (Header Formatting)

## 1. Target Files
- `.human/users/*/drafts/*.md`
- Specifically, the `### ...` placeholders in the conversation log.

## 2. Strategic Purpose: The "Exhibit" Concept
**Why do we format temporary drafts so rigorously?**
These drafts act as **educational exhibits** for future human-AI interaction studies. They demonstrate:
- "How humans command AI"
- "How AI responds to vague vs. specific queries"
- "The evolution of the co-creation process"

Therefore, headers act as **Museum Captions** (道標) to help future human observers navigate the conversation log.

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
    ### 要約: ログ記録の新しいルール作成依頼
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

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [.agent/rules/development/project-understanding.md](.agent/rules/development/project-understanding.md) | Defines "Active Documents" (Drafts) as Implicit Context |
| [.agent/rules/core/language-standards.md](.agent/rules/core/language-standards.md) | Guiding principles for language selection |
