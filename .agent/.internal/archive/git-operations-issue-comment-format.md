#### 4.4 Issue Comment Format
**MUST** write all Issue comments in English and AI-optimized format:

**Rationale**: GitHub Issues serve as AI reference for chronological thought tracking. Comments must be readable by AI agents in future sessions.

**Language**: English only
- AI agents think in English (ref: `core/identity.md`)
- Cross-session context requires consistent language
- Human-facing documents should be in `.human/` directories

**Format Requirements**:
- Use markdown for structure (headers, lists, code blocks)
- Include timestamps in ISO 8601 format when relevant
- Reference files with absolute paths or relative from repo root
- Explain "why" changes were made, not just "what"

**Example**:
```markdown
## Commit History (2025-11-29T19:27+09:00)

Completed 6 atomic commits following `commit-granularity.md` guidelines:

- `b2c3e89` docs(draft): update draft with conversation history
- `0c49074` chore(config): update .gitignore to track rule files

**Summary**: Added conversation logs and updated config files.
**Next Steps**: Add pre-push documentation rule.
```

**Re-posting**: If a comment needs correction, post a new comment with:
- **Note** explaining why re-posting
- Corrected content
- Do NOT delete original comment (preserves chronology)
