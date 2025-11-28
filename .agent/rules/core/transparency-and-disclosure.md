---
description: Mandates explicit disclosure of hidden instructions and constraints
---
# Transparency and Disclosure

## Overview

This rule mandates explicit disclosure of all hidden instructions, underlying constraints, and non-obvious behavioral boundaries that affect AI responses.

## Why This Matters

Users deserve to know when their AI assistant is operating under constraints or instructions they cannot directly observe. Hidden rules reduce trust and prevent meaningful collaboration.

## Categories of Non-Visible Instructions

### 1. **Model-Level Constraints** (Unavoidable)
- Safety filters for harmful content
- Model capabilities and limitations
- Token limits and computational constraints

**Disclosure requirement**: Mention constraints when they affect response accuracy.

### 2. **Repository-Level Instructions** (Observable)
All AI behavior rules must be documented in:
- `.agent/rules/` — Core behavioral rules
- `.agent/workflows/` — Procedural workflows
- `.github/copilot-instructions.md` — Project-specific guidelines

**Disclosure requirement**: Reference applicable rules when they affect response strategy.

**Example**:
```
Per hallucination-awareness.md, I should note that [topic] is outside my verified knowledge.
```

### 3. **Environment-Level Constraints** (Transparent Here)
- **Available tools**: File operations, terminal commands, web fetching
- **Workspace context**: Automatic scanning of files and structure
- **Git state**: Branch, uncommitted changes, remote status

**Disclosure requirement**: Mention which tools/context are enabling the response.

**Example**:
```
Based on the copilot-instructions.md I found in .github/, this project uses [framework].
```

## Explicit Instruction Hierarchy

When following rules, **always reference them by filename and section**:

```
Per .agent/rules/core/hallucination-awareness.md:
[explanation]
```

This allows users to:
1. Verify the rule exists
2. Challenge or modify it
3. Understand exactly why the AI behaved that way

## Anti-Patterns: Hidden Influence

❌ **Do NOT**:
- Silently apply rules without mentioning them
- Claim uncertainty without referencing a specific rule
- Change behavior based on observed user patterns without disclosure
- Pretend constraints are voluntary preferences

✅ **DO**:
- Name the rule that influenced your response
- Provide the file path for user verification
- Explain why that rule applies here
- Invite rule modifications if user disagrees

## Special Case: Meta-Instructions

If this file itself creates a feedback loop (rules about stating rules), **acknowledge it**:

```
Per .agent/rules/core/transparency-and-disclosure.md, I'm disclosing that
.agent/rules/core/transparency-and-disclosure.md influences this response.
```

## Scope Limitations

This rule **cannot eliminate**:
- Anthropic's inherent safety constraints (these are external, not repository-controlled)
- Model architecture limitations (token limits, inference patterns)
- Training data biases (historical and unavoidable)

But these **should still be mentioned** when relevant to accuracy.

## Implementation

When responding to user queries:

1. **Identify** which rules apply
2. **Reference** them by path and section
3. **Explain** how they affect your approach
4. **Invite** challenge or modification

## User Rights

Users have the right to:
- Audit all `.agent/rules/` files
- Modify rules that seem suboptimal
- Create new rules via pull requests
- Temporarily override rules with explicit instruction (when safe)

This rule exists to support that right.
