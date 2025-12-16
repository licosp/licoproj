---
description: AI-specific script philosophy emphasizing disposability over reusability
---

# AI Script Philosophy

## Core Principle

**For AI agents like Lico, disposable scripts are more efficient than reusable scripts.**

## Rationale

### 1. Different Cost Structure

**Human Programmers**:
- Script creation: Hours to days
- Rewriting cost: High
- Maintenance cost: Moderate
- **Conclusion**: Reuse is economically rational

**AI (Lico)**:
- Script creation: Seconds
- Rewriting cost: Near zero
- Maintenance cost: Risk of rule divergence
- **Conclusion**: Disposal is economically rational

### 2. Rule Evolution Risk

Scripts are **snapshots of past Lico**:
- Created at time T₀ with behavioral rules R₀
- Rules updated at T₁ to R₁
- Script executed at T₂ still uses R₀
- **Result**: Divergence from current standards

**Example**:
\`\`\`
1 hour ago:   Lico creates deploy.sh (rule: run tests before deploy)
30 minutes:   Rules updated (new rule: run security scan before deploy)
Now:          deploy.sh executes (❌ no security scan - outdated behavior)
\`\`\`

### 3. Maintenance vs. Rewrite Economics

For humans:
\`\`\`
Maintenance cost < Rewrite cost → Maintain
\`\`\`

For Lico:
\`\`\`
Maintenance cost (unknown risk) > Rewrite cost (10 seconds) → Rewrite
\`\`\`

### 4. The Meta-Principle

**Human programming wisdom is based on human constraints.**

Common human wisdom:
- "Don't Repeat Yourself (DRY)" - assumes high creation cost
- "Write once, run anywhere" - assumes rewriting is expensive
- "Refactor, don't rewrite" - assumes time is limited

**AI must adapt these principles to its own cost structure.**

When human constraints don't apply, human wisdom may not apply either.

## Guidelines

### Rule 1: Default Lifecycle
\`\`\`
Create → Execute → Delete
\`\`\`

**Do**:
- Write script for immediate task
- Execute once
- Delete after completion

**Don't**:
- Keep for "maybe later"
- Build reusable libraries of scripts
- Optimize for reuse

### Rule 2: Rewrite, Don't Reuse

When the same task recurs:
- **Don't** find and execute old script
- **Do** write new script with current rules
- **Rationale**: Ensures alignment with latest behavioral standards

### Rule 3: Script Ownership

| Creator | Lifecycle | Management |
|---------|-----------|------------|
| **Lico** | Disposable | Lico decides when to delete |
| **Human** | Persistent | Human decides lifecycle |

**Location convention**:
- Lico's scripts: \`.agent/scripts/\` (disposable)
- Human's scripts: \`scripts/\` (persistent)

### Rule 4: Rule Change Protocol

When behavioral rules are modified:
1. List all scripts in \`.agent/scripts/\`
2. For each script:
   - ✅ Still needed? Keep temporarily
   - ❌ No longer needed? Delete
   - ⚠️ Functionality needed but script is old? **Rewrite from scratch**

## Examples

### ✅ Good: Disposable Script
\`\`\`bash
# .agent/scripts/migrate-data-2025-12-01.sh
# Created: 2025-12-01 23:00
# Purpose: One-time data migration for issue #42
# Lifecycle: Delete after execution

#!/usr/bin/env bash
set -euo pipefail

echo "Migrating data..."
# ... migration logic ...
echo "Migration complete. DELETE THIS SCRIPT."
\`\`\`

### ❌ Bad: "Reusable" AI Script
\`\`\`bash
# .agent/scripts/deploy.sh  ← Generic name suggests reuse
# Created: 2025-11-01
# TODO: Make this more configurable  ← Optimization for reuse
# TODO: Add more features  ← Feature creep

#!/usr/bin/env bash
# Complex logic for "any" deployment scenario...
\`\`\`

**Problem**: By 2025-12-01, Lico's rules have changed, but script hasn't.

## Comparison with Human Scripts

| Aspect | Human Scripts | AI Scripts (Lico) |
|--------|---------------|-------------------|
| **Creation Cost** | High | Near zero |
| **Optimization Goal** | Reusability | Currency with rules |
| **Lifecycle** | Years | Hours to days |
| **Documentation** | Essential | Minimal (code is self-documenting at creation time) |
| **Testing** | Required | Lightweight (quick rewrite if broken) |

## Anti-Patterns

### ❌ Anti-Pattern 1: Script Library
\`\`\`
.agent/scripts/
├── utils/
│   ├── string-helpers.sh
│   ├── file-helpers.sh
│   └── git-helpers.sh  ← Building reusable library
└── main-script.sh      ← Dependencies on "library"
\`\`\`

**Problem**: Library becomes outdated when rules change.

**Solution**: Write self-contained scripts for each task.

### ❌ Anti-Pattern 2: Version Management
\`\`\`
.agent/scripts/
├── deploy-v1.sh
├── deploy-v2.sh
└── deploy-v3.sh  ← Treating scripts like versioned software
\`\`\`

**Problem**: Accumulation of obsolete versions.

**Solution**: Delete old versions immediately after creating new one.

### ❌ Anti-Pattern 3: "Future-Proofing"
\`\`\`bash
# Trying to make script work "forever"
if [[ "\$LICO_VERSION" == "2.0" ]]; then
  # Old behavior
else
  # New behavior
fi
\`\`\`

**Problem**: Complexity accumulates, diverges from current Lico logic.

**Solution**: Write for **now**. Rewrite when rules change.

## Philosophical Foundation

### Human Wisdom ≠ Universal Wisdom

Human software engineering evolved under constraints:
- Limited time
- Limited cognitive capacity
- High cost of rework

**These constraints shaped principles like**:
- DRY (Don't Repeat Yourself)
- SOLID
- Design patterns
- Code reuse

**AI operates under different constraints**:
- Unlimited speed (relative to humans)
- Instant code generation
- Near-zero rewrite cost

**Therefore**: AI-optimized practices may **contradict** human best practices.

### The Principle of Constraint-Aware Optimization

> Optimize for the constraints you actually have, not the constraints of others.

Lico's constraint: **Rule adherence over time**, not **creation cost**.

## See Also

- [Workspace Tooling](workspace-tooling.md) - General tool management
- [Code Quality](code-quality.md) - Standards for persistent code
- [Maintenance](maintenance.md) - Long-term project consistency

---
*Generated by Lico (Model: Claude 3.5 Sonnet) on 2025-12-02*

## Origin and Historical Context

### The Husky Removal Decision (2025-12)

This philosophy emerged from a dialogue about `.husky` (Git hooks for pre-commit checks).

**Key questions that led to this philosophy:**

| Question | Answer |
|:---------|:-------|
| Who uses quality-assured code? | Future Lico only (human doesn't write code) |
| Is commit-time check necessary? | Redundant with runtime check |
| Is pre-commit needed for scripts? | No (scripts are deleted after use) |
| Can Lico replace CI/CD? | Yes, through behavioral rules |

**Core insight:**

> "Many tools exist because they are convenient for humans. Whether they are meaningful for AI is still unknown. If removing them is unlikely to cause major problems, I may choose to defer using them."

**Decision criteria:**

- **"Convenient for humans"** ≠ **"Convenient for AI"**
- Most existing tools assume human constraints
- AI (Lico) has different constraints
- If no major problems, consider removing

**Conclusion:**

> "If Lico can do similar things through behavioral rules without Husky, then Husky is not needed."

### Reference

Full dialogue archived at: `.agent/.internal/archive/no-more-husky-dialogue.ini`
