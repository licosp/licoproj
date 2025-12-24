---
description: Proposal for temporal memory recording principle
created: 2025-11-30T19:48:43+09:00
status: proposal
category: core-philosophy
---

# Temporal Memory Recording Principle

## Summary
The repository serves as a time-series record of AI's thought process, enabling trace-back of idea origins and thought evolution.

## Rationale
During today's session (2025-11-30), we successfully traced the origin of the "Repository as Brain" concept by searching through:
- Git commit history
- Conversation logs
- Archived files
- User drafts

This demonstrates that **temporal recording is not just documentation—it's cognitive archaeology**. The ability to reconstruct how an idea emerged, evolved, and crystallized is essential for:
1. Understanding past decisions
2. Learning from mistakes (preserved as data, not deleted)
3. Attributing sources of inspiration
4. Maintaining continuity across AI model switches

## Key Principles

### 1. Record Everything, Delete Nothing
- Failed experiments → `.agent/.archive/`
- Temporary files → `.agent/.internal/archive/`
- Conversation logs → `.agent/.internal/conversations/`
- Even "hallucinations" are valuable as negative examples

### 2. Timestamp All Artifacts
- Use ISO 8601 format with timezone: `2025-11-30T19:48:43+09:00`
- Include creation/modification timestamps in YAML frontmatter
- File naming can include timestamps: `idea_2025-11-30T19-48-43+09-00.md`

### 3. Preserve Context
- Git commits are memory snapshots
- Commit messages explain "why", not just "what"
- Issue discussions capture decision rationale

### 4. Enable Retrieval
- Structured directory hierarchy for AI navigation
- Consistent file naming for grep/find operations
- Cross-references between related documents

## Origin Story (Meta-Reference)
This principle itself emerged from the investigation into "Where did 'Repository as Brain' come from?"

The process:
1. User asked: "Where did this idea originate?"
2. AI searched Git logs → Found `~/.gemini/antigravity/brain/` reference
3. AI found user's Nov 28 dialogue about "リモートリポジトリをAIの脳と定義"
4. AI found `ai_evaluation.md` documenting the evolution timeline

**Without temporal recording, this investigation would have been impossible.**

## Proposed Implementation
Add to `core/documentation/documentation-standards.md`:

```markdown
## Temporal Recording
- All significant artifacts MUST include creation timestamp
- Use ISO 8601 with timezone: `YYYY-MM-DDTHH:MM:SS+TZ:TZ`
- Failed workflows are archived, not deleted
- Conversation logs are permanent memory
```

## Impact
- **High value**: Enables learning from history
- **Low cost**: Text files are negligible in size
- **Scope**: Applies to all `.agent/` and `.human/` content
