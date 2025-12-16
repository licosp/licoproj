---
description: Protocols for maintaining formatting and readability in Human Draft files
---

# User Draft Maintenance (Header Formatting)

## 1. Target Files
- `.human/users/*/drafts/*.md`
- Specifically, the `### ...` placeholders in the conversation log.

## 2. Trigger Condition
- Lico detects `### ...` (ellipsis) in the active draft file.
- **Action**: Lico MUST replace `...` with a descriptive header string.

## 3. Formatting Rules

### Rule A: Long Query (Multi-line)
If the user's query spans multiple lines or contains complex instructions:
- **Action**: **Summarize the Intent in the User's Language**.
- **Format**: `### [Summary of Intent]`
- **Example**:
    ```markdown
    ### 要約: ログ記録の新しいルール作成依頼
    (User query content...)
    ```

### Rule B: Short Query (Single line)
If the user's query is a single line, short command, or conversational response:
- **Action**: **Quote Verbatim**.
- **Format**: `### "[Exact Quote]"`
- **Example**:
    ```markdown
    ### "Stop immediately."
    (User query content...)
    ```
    ```markdown
    ### "Yes, proceed."
    (User query content...)
    ```

## 4. Rationale
- **Readability**: Summaries help navigate long logs.
- **Accuracy**: For short commands, the exact wording outweighs any summary. "Stop" is more powerful than "User requested stop".

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [project-understanding.md](../development/project-understanding.md) | Defines "Active Documents" (Drafts) as Implicit Context |
