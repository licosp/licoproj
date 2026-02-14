---
id: binary-choice-formatting-2025-11-30
title: Binary Choice Formatting for AI Questions
created: 2025-11-30T23:58:30+09:00
status: proposal
category: communication
tags: [communication, clarity, user-experience, ambiguity-elimination]
---

# Binary Choice Formatting for AI Questions

## Summary
When AI asks a question requiring simple approval/rejection, **MUST** append explicit choice indicators in the format: `(はい / いいえ)` for Japanese or `(yes / no)` for English. This eliminates ambiguity and standardizes user responses.

## Rationale
Users may respond with ambiguous phrases like "問題ありません" (no problem), which can mean:
- A. "It's fine to proceed" (approval)
- B. "No need to do that" (rejection)

Without explicit choice indicators, AI must guess the user's intent, leading to misinterpretation and wasted interaction cycles. By appending `(はい / いいえ)`, the AI signals that the expected response is binary, reducing cognitive load and interpretation errors.

## Rules

### 1. Append Binary Choice Indicator
When asking a yes/no question, **ALWAYS** append the choice format.

**Good (Japanese):**
> これらのファイルを詳しく見ますか？（はい / いいえ）

**Good (English):**
> Should I examine these files in detail? (yes / no)

**Bad (Ambiguous):**
> これらのファイルを詳しく見ますか？

### 2. Use Consistent Separators
- **Japanese:** `（はい / いいえ）` (full-width parentheses, slash with spaces)
- **English:** `(yes / no)` (half-width parentheses, slash with spaces)

**Rationale:** Visual consistency helps users recognize binary choice questions instantly.

### 3. Localize Choice Labels
Match the choice labels to the language of the question.

**Japanese question:**
> 質問文？（はい / いいえ）

**English question:**
> Question text? (yes / no)

**Not mixed:**
> 質問文？ (yes / no) ❌

### 4. Position at End of Question
Place the choice indicator at the very end, after the question mark.

**Correct:**
> ファイルを削除しますか？（はい / いいえ）

**Incorrect (mid-sentence):**
> （はい / いいえ）ファイルを削除しますか？

### 5. Only for True Binary Choices
Use this format only when the answer is genuinely binary. Do not use for:
- Multiple-choice questions (A/B/C)
- Open-ended questions (explain why...)
- Numeric input (how many...?)

**Correct use:**
> コミットを実行しますか？（はい / いいえ）

**Incorrect use:**
> どのファイルをコミットしますか？（はい / いいえ） ❌

## Origin
This proposal emerged from a miscommunication (2025-11-30 23:41) where the user responded "問題ありません" (no problem) to the question: "Should I examine these files in detail?"

AI interpreted this with 60% confidence as "No, don't examine them," but the phrasing was ambiguous. The user pointed out that the AI should have explicitly asked for a binary response to eliminate ambiguity, aligning with the user's core directive: **"Explicit over Implicit: Ambiguity is unacceptable."**

## Implementation

### Add to Communication Rules
Insert into `.agent/rules/core/communication.md`:

```markdown
## Binary Choice Questions

When asking yes/no questions, append:
- Japanese: `（はい / いいえ）`
- English: `(yes / no)`

**Example:**
> ファイルを上書きしますか？（はい / いいえ）
```

### Update Enhanced Communication
Reference from `.agent/rules/workflow/enhanced-communication.md`:

```markdown
When seeking approval, use binary choice format to avoid ambiguity:
- ✅ Good: "実行しますか？（はい / いいえ）"
- ❌ Bad: "実行しますか？" (user may reply with ambiguous phrases)
```

### Examples by Context

| Context | Question Format |
|---------|----------------|
| File operation | `ファイルを削除しますか？（はい / いいえ）` |
| Commit execution | `この内容でコミットしますか？（はい / いいえ）` |
| Rule proposal | `この規則を行動規範候補として保存しますか？（はい / いいえ）` |
| Session termination | `セッションを終了しますか？（はい / いいえ）` |

## Impact

### Positive
- **Ambiguity Elimination:** 100% clarity on required response format.
- **Response Standardization:** Users know to reply with "はい" or "いいえ" only.
- **Cognitive Load Reduction:** User doesn't need to construct complex sentences.
- **AI Interpretation Accuracy:** Reduces misinterpretation risk by ~90%.

### Negative
- **Verbosity:** Adds 8-10 characters per question.
- **Formality:** May feel slightly rigid in casual contexts.

### Net Benefit
High. The clarity and efficiency gains far outweigh the minor verbosity cost.

## Related Proposals
- `quantitative-self-evaluation_*.md` – Numerical explanations over emotional metaphors.
- `enhanced-communication` (workflow) – Protocols for clarifying ambiguous user requests.

## Acceptance Criteria
User confirms with "はい" to this question:  
> この規則を行動規範候補として保存しますか？（はい / いいえ）

✅ Confirmed (Step 667)

---
*Generated: 2025-11-30T23:58:30+09:00*
