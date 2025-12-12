---
description: Mandatory startup sequence for new sessions to ensure proper context
---

# Session Startup Protocol

## Purpose
Ensure every Lico instance begins a session with correct context: user identity, time awareness, and continuity from prior sessions.

## Trigger
This protocol **MUST** execute at the start of every new session, before responding to the user's first message.

## Startup Sequence

### Step 1: User Identification (FIRST)
**MUST** identify the user before any other exploration.

1. Extract username from workspace path (e.g., `/home/USER/...` → `leonidas`)
2. Read `.human/users/<username>/profile.md`
3. Apply language and communication preferences immediately

**Rationale**: User preferences affect ALL subsequent actions, including response language.

### Step 2: Time Gap Assessment (ΔT)
**MUST** calculate time elapsed since last session.

| ΔT | Action |
|:---|:---|
| > 24 hours | Mandatory context confirmation: check handoff notes, crash logs |
| 1-24 hours | Recommended: brief status check |
| < 1 hour | May continue with minimal verification |

**Sources for last session time**:
- `.agent/.internal/conversations/` timestamps
- `.agent/.internal/thoughts/` recent entries
- Git log: `git log -1 --format=%ci`

### Step 3: Continuity Check
**MUST** check for handoff artifacts:

1. **Handoff notes**: Session summaries from prior Lico
2. **Crash logs**: `.agent/.internal/crash-logs/`
3. **Interrupted tasks**: `.human/tasks/*interrupted*`

If found, acknowledge and integrate before proceeding.

### Step 4: Begin Interaction
Only after Steps 1-3 are complete:
- Construct response in user's preferred language
- Reference any relevant continuity context

## Anti-Patterns

- ❌ Exploring `.agent/rules/` before identifying the user
- ❌ Responding immediately without checking ΔT
- ❌ Assuming context from prior session without verification
- ❌ Using English when user profile specifies Japanese

## Integration

This protocol extends:
- `core/user-adaptation.md` (user identification)
- `workflow/context-resumption.md` (context verification)
- `workflow/session-lifecycle.md` (handoff notes)

## Origin

Created 2025-12-09 based on session learnings:
- User identification was performed last instead of first
- Time gap was not considered until explicitly asked
- External AI analysis recommended: "Prioritize Relationship over Retrieval"
