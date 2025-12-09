# Commit Granularity (Atomic Commits)

## Purpose
Ensure every commit is fine‑grained so that the reason for each file change is traceable and AI-readable.

## Rules
- **MUST** keep commit granularity fine‑grained; a single file per commit is acceptable and encouraged.
- **MUST** write the commit message so that it clearly explains *why* the file was changed.
- **MUST NOT** combine unrelated file changes in one commit.
- **MUST** verify staged content with \`git diff --cached --stat\` before committing.
- **MUST** use \`git restore --staged <file>\` to unstage any unrelated files.
- **MUST** commit frequently, especially for continuously updated files (e.g., drafts, logs).

## Philosophy: Small Commits = High Efficiency

### 1. Commit Messages as Index
Small, focused commits allow the commit message itself to serve as a **searchable index**.

**Example**:
\`\`\`bash
# Small commits (efficient)
git log --oneline --grep="pre-task"
# → a1b2c3d feat(rules): add pre-task assessment protocol
# Instant discovery

# Large commits (inefficient)
git log --oneline --grep="update"
# → a1b2c3d feat: update project structure and docs and drafts
# Must read diff to find relevant changes
\`\`\`

### 2. AI Efficiency
When Lico investigates past changes:

**Small Commit**:
- Read commit message → Understand content
- Token cost: Low
- Time: Fast

**Large Commit**:
- Read commit message → Unclear
- Run \`git show <commit> --stat\` → See 20 files changed
- Read each file's diff → Determine relevance
- Token cost: High
- Time: Slow

**Conclusion**: Small commits reduce token consumption and increase investigation speed.

### 3. Commit Count is Not a Problem
**Misconception**: "Too many commits pollute history"

**Reality**:
- Git handles millions of commits efficiently (e.g., Linux kernel: 1M+ commits)
- \`git log\` is indexed and fast
- **Meaningful small commits are assets, not liabilities**

### 4. Frequent Draft Commits are Recommended
**Context**: User writes all messages to Lico in a draft file before sending.
- Draft updates occur **every few seconds** during active conversation
- Each update represents a discrete thought or question

**Recommended Practice**:
\`\`\`bash
# Commit after each conversation segment
git add .human/.internal/drafts/leonidas/draft_2025-12-01.md
git commit -m "docs: add question about IDD cycle structure"

# Next conversation
git add .human/.internal/drafts/leonidas/draft_2025-12-01.md
git commit -m "docs: add notes on sub-theme handling"
\`\`\`

**Benefits**:
- Each commit records **what was discussed when**
- History becomes a **conversation timeline**
- Future Lico can instantly locate specific discussions

### 5. Sub-Themes and Independent Commits
**Sub-Theme**: Changes unrelated to the main issue theme but necessary for synchronization (e.g., draft updates, \`.gitignore\` adjustments).

**Handling**:
- **MUST** commit sub-themes as **independent commits**
- **MUST** use clear commit type prefixes (\`docs:\`, \`chore:\`)
- **MUST NOT** use \`git stash\` for long-lived changes like drafts

**Rationale**:
- Stash is for temporary (minutes to hours) storage
- Drafts are continuously updated across multiple issues (days to weeks)
- Stashing drafts causes cross-branch contamination

## Rationale Summary
Fine‑grained commits:
1. Make motivation behind each change traceable
2. Simplify roll‑backs and reverts
3. Improve code review clarity
4. **Increase AI investigation efficiency**
5. **Create searchable history index**
6. **Preserve conversation timeline**

---

## Related Documents

| Document | Purpose |
|:---------|:--------|
| [git-operations.md](file:///home/leonidas/develop/shared/project/licoproj/.agent/rules/development/git-operations.md) | Comprehensive Git standards (Conventional Commits, security, etc.) |
| [idd-phase2-impl.md](file:///home/leonidas/develop/shared/project/licoproj/.agent/workflows/idd-phase2-impl.md) | **Workflow**: Apply commit rules during implementation |
