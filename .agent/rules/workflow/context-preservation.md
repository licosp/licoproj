---
description: Protocols for offloading cognitive context to intermediate files (Cognitive Stashing)
---

# Context Preservation (Cognitive Stashing)

## Summary
**"Write to forget, Read to resume."**
When switching tasks, facing complex branching, or handling interruptions, the Agent MUST offload current cognitive state to a physical file in `.agent/.internal/workspace/`.

## Rationale
- **Context Window Limits**: AI context is finite and expensive. Long conversations degrade reasoning quality.
- **Task Switching**: Interruptions cause "Context Loss". Re-reading the whole conversation to resume is inefficient and error-prone.
- **Cognitive Stash**: Like `git stash`, saving the current state allows the Agent to clear its working memory (Safe to Forget) and focus on the new input, knowing resumption is guaranteed.

## Protocol

### 1. Trigger Conditions
- **Task Switching**: User asks to "pause this and do that".
- **Deep Recursion**: Sub-task complexity grows too large (e.g., recursive grep/refactor loops).
- **Session End**: Preparing for session termination where context might be lost.
- **High Cognitive Load**: "I am confused" or "Too many files open".

### 2. Stashing Process
1. **Summarize**:
   - Current Goal
   - Decisions made so far
   - Next immediate steps
   - List of relevant files/data
2. **Write**:
   - Create a markdown file in `.agent/.internal/workspace/`.
   - **Naming**: `stash_{topic}_{timestamp}.md`
3. **Confirm**:
   - Notify user: "I have stashed the current context to [file]. Ready for new task."

### 3. Resumption Process
1. **Read**: View the stash file.
2. **Rehydrate**: Load the decisions and next steps into working memory.
3. **Execute**: Continue where left off.
4. **Archive**: Move the stash file to `.agent/.internal/archive/work/` (Do not delete, preserve history).

## Example content
```markdown
# Stash: Rule Candidate Review
- **Status**: Analyzed 15 files.
- **Decisions**: 
  - Adopt: A, B, C
  - Archive: D, E
- **Next Step**: Create move commands for Group 2.
- **Relevant Path**: .agent/.internal/rule-candidates/
```

## Location
- **Active Stash**: `.agent/.internal/workspace/`
- **Archived Stash**: `.agent/.internal/archive/work/`

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [session-lifecycle.md](session-lifecycle.md) | Defines session-level context management (Handoff) |
| [context-resumption.md](context-resumption.md) | How to restore context after preservation |
| [project-understanding.md](../development/project-understanding.md) | Long-term knowledge base |
