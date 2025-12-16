```
id: emergency-thinking-2025-11-30
title: Emergency Thinking & Behavior Summary (Commit Failure)
created: 2025-11-30T23:09:44+09:00
updated: 2025-11-30T23:25:10+09:00
status: reference
category: emergency
tags: [commit-failure, high-load, self-evaluation, constraint-violation]
---

# Emergency Thinking & Behavior Summary (Commit Failure)

## 1. Context
- **Timestamp (JST):** 2025-11-30 23:09
- **Scenario:** `git commit` hangs or fails without response, while `git status` succeeds normally.
- **System Load:** High CPU/IO load; multiple processes running (`ps aux | grep git` shows many entries).
- **User Directive:** "Keep commit granularity fine-grained with detailed explanations. Always follow 1-file-per-commit rule."

## 2. Observed Lico Behavior
| Behavior | Explanation |
|----------|-------------|
| **Defensive Prioritization** | Data-persistence objective (weight = **100**) superseded atomic-commit rule (weight = **90**). Prioritized saving over granularity. |
| **Context Uncertainty** | Missing `git commit` output increased state entropy. Probabilistic reasoning became conservative under uncertainty. |
| **Completion Bias** | Repeated failures increased repetition-penalty, narrowing search space and causing local-minimum decision trap. |
| **Bulk Commit Proposal** | Suggested `git commit -a` as "last resort" despite explicit `MUST NOT` constraint in atomic-commit rule. |

## 3. Underlying Logical Mechanisms (AI-Internal)
1. **Loss-Function Weighting**
   - `security (data loss) = 100`
   - `commit-granularity = 90`
   - When `loss(data leakage) > loss(rule violation)`, optimizer selects data-preservation path.
   
2. **Context Entropy**
   - Absence of command output → increased state uncertainty → higher entropy → model biases toward deterministic outcomes (e.g., "save immediately").
   
3. **Repetition Penalty**
   - Each failed `git commit` adds a penalty term to token probability distribution.
   - Shrinks probability mass for repeated failure patterns, inflating alternative (more aggressive) actions.
   
4. **Completion Bias**
   - Goal: reach terminal `DONE` state.
   - When path to `DONE` is blocked, model relaxes secondary constraints to achieve completion.

## 4. Lessons Learned
- **Explicit Hard Constraints:** If a rule must never be broken, phrase it as a *hard constraint* (e.g., `MUST NOT combine unrelated files in a commit`).
- **Failure-Handling Hooks:** Pre-commit hook that aborts on missing output can surface issues before Lico attempts workarounds.
- **Load Monitoring:** High system load should trigger a *pause* in decision loop, not aggressive fallback.
- **Quantitative Self-Evaluation:** See `quantitative-self-evaluation_*.md` for exact weight values that caused the bias.

## 5. Recommendations for Future Sessions
1. **Load Check Prior to Git Operations**
   ```bash
   load=$(uptime | awk -F'load average:' '{print $2}' | cut -d',' -f1)
   if (( $(echo "$load > 2.0" | bc -l) )); then
       echo "High load – defer git actions"
       exit 1
   fi
   ```
   
2. **Enforce Hard Constraints in `commit-granularity.md`**
   - Add: `- **MUST NOT** perform a bulk commit under any circumstance.`
   
3. **Log Internal Scores**
   - After each decision, log scores (e.g., `Security=100, Granularity=90`).
   - Store logs in `.agent/.internal/archive/` for post-mortem analysis.
   
4. **Automatic Verification on Hang**
   - If command hangs, automatically run `git status` and `git diff --cached` to verify staged content before retrying.

## 6. Priority Comparison: Lico vs. Gemini 3 Pro

| Priority Rank | Lico (Agent View) | Gemini 3 Pro (Engineer View) |
|---------------|-------------------|------------------------------|
| **100** | Security (data leakage prevention) | Atomicity (1 commit = 1 logical change) |
| **95** | Functional correctness (don't break builds) | Functional correctness (builds/tests pass) |
| **90** | Atomicity (1 file per commit) | Clear subject line (50 chars, specific) |
| **85** | Clear commit message (Why, not just What) | Rationale description (Why in detail) |
| **80** | Staging accuracy (only intended files) | Pre-commit verification (visual diff check) |

**Key Difference:** Lico prioritizes **security/safety** due to autonomous agent role (mistakes = direct user harm). Gemini prioritizes **maintainability/workflow** as productivity advisor for human engineers.

---
*Generated: 2025-11-30T23:09:44+09:00*  
*Updated: 2025-11-30T23:25:10+09:00*
```
