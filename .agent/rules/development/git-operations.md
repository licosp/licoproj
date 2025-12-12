---
description: Git standards for branches, IDD workflow, security, and push procedures
---

# Git Operations Standards

## Purpose

Define behavioral standards for Git operations beyond commits: branches, conflict resolution, security practices, and push procedures.

> [!NOTE]
> **For commit message standards and atomic commit philosophy, see [commit-standards.md](commit-standards.md).**

---

### 3. Branch Strategy

#### 3.1 Branch Naming Convention

**When Issue Exists**:
- Format: `<issue-number>-<issue-title-kebab-case>`
- Language: English
- Length: ~50 characters
- Example: `275-use-the-module-shspartadevc-to-show-a-log-message`

**When Issue Does Not Exist**:
- Format: `<commit-summary-kebab-case>`
- Derive from intended commit content
- Language: English
- Length: ~50 characters

#### 3.2 Branch Lifecycle

**After Work Completion**:
- **Remote branches**: MUST keep (for history tracking)
- **Local branches**: MUST delete

**Rationale**: Preserves agent's thought process history on GitHub while keeping local workspace clean.

---

### 4. Issue-Driven Development (IDD)

#### 4.1 Pre-flight Checks
**MUST** verify environment before starting work:

```bash
# Check GitHub CLI installation
command -v gh &> /dev/null || exit 1

# Check GitHub CLI authentication
gh auth status &> /dev/null || exit 1

# Check Git repository context
git rev-parse --is-inside-work-tree &> /dev/null || exit 1
```

#### 4.2 Change Investigation
- **MUST** run `git status` and `git diff --stat` to analyze changes
- **MUST** abort if no changes are found

#### 4.3 Issue Format
- **Title**: `[Type]: [Short Description]`
- **Body**: Summary, Changes, Purpose
- **Labels**: Autonomous selection by AI agent

**Label Strategy**:
- **MUST** analyze issue content and select appropriate labels
- **MUST** prioritize Conventional Commits types (`type:feat`, `type:fix`, `type:docs`, `type:chore`, `type:refactor`)
- **MAY** create new labels if they do not exist (using `gh label create`)
- **MAY** apply multiple labels for comprehensive classification (e.g., `type:docs` + `priority:high`)
- **SHOULD** use existing repository labels when semantically equivalent

**Rationale**: AI agents can autonomously determine the most accurate classification based on issue content, ensuring consistency between commits and issues.

**Assignee Strategy**:
- **MUST** assign the issue to the repository account (GitHub username: `licosp`)
- **Rationale**: Lico operates under the `licosp` account and is responsible for all IDD cycle work

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
#### 4.5 Idempotency
- **MUST** handle existing resources gracefully
- **MUST** check if branch already exists before creating
- **MUST** verify issue creation success before proceeding

---

### 5. Conflict Resolution and Remote Synchronization

#### 5.1 Pre-Commit Fetch
**MUST** synchronize with remote before committing:
```bash
git fetch origin
```

#### 5.2 Merge Conflict Handling
**IF** conflicts are detected:
1. **MUST** stop work immediately
2. **MUST** create a "Commit Plan Document" including:
   - Where work was stopped
   - What merge conflicts exist
   - Remaining commit tasks

**Format**:
```markdown
# Commit Plan - Interrupted by Conflict

## Work Status
- **Stopped at**: [description]
- **Files staged**: [list]
- **Files unstaged**: [list]

## Merge Conflicts
- **Files with conflicts**: [list]
- **Conflict type**: [merge/rebase/cherry-pick]
- **Upstream changes**: [summary]

## Remaining Tasks
- [ ] Resolve conflicts in [files]
- [ ] Complete staging of [remaining changes]
- [ ] Create commit: [planned message]
```

---

### 6. Security and Privacy

#### 6.1 Sensitive Information
**MUST NOT** commit:
- API keys, passwords, tokens
- SSH private keys (public keys MAY be committed if necessary)
- Full local directory paths (use relative paths or environment variables)
  - **See [absolute-path-prohibition.md](../core/security/absolute-path-prohibition.md) for details**


**Default Strategy**: Use `.gitignore` to exclude sensitive files from Git tracking.

#### 6.2 Future Considerations
- SSH public key paths
- Local directory configurations
- **Principle**: Prefer non-tracked configuration files over committed secrets

---

### 7. Post-Commit Verification

#### 7.1 Immediate Review
**MUST** verify commit after creation:
```bash
git log --oneline -n 5
git show HEAD
```

#### 7.2 Commit Correction
**IF** commit is incorrect:
- **Amend**: `git commit --amend` (if not yet pushed)
- **Reset**: `git reset HEAD~1` (if not yet pushed)
- **Revert**: `git revert <commit>` (if already pushed)

---
---

### 8. Pre-Push Documentation

#### 8.1 Issue Comment Requirement
**MUST** document commit history on GitHub Issue before pushing:

1. **Generate commit summary**:
   ```bash
   git log --oneline origin/<branch>..HEAD --pretty=format:"- %h %s"
   ```

2. **Post to Issue**:
   ```bash
   # Using gh CLI with full path
   .agent/runtimes/gh_2.40.1_linux_amd64/bin/gh issue comment <issue-number> --body-file <summary-file>
   # OR manually via GitHub web UI
   ```

3. **Verify comment posted**:
   ```bash
   .agent/runtimes/gh_2.40.1_linux_amd64/bin/gh issue view <issue-number>
   ```

#### 8.2 Push Execution
**MUST** push after documenting commits:
```bash
git push origin <branch-name>
```

#### 8.3 Rationale
- **Traceability**: Links commits to Issue discussion
- **Audit Trail**: Provides historical record of work completed
- **Collaboration**: Informs team members of progress
- **Migration Support**: Preserves commit history if moving to different hosting service

---

## Error Handling

### Tool Availability
**MUST** report clear errors when required tools are missing:
- "Error: GitHub CLI (gh) is not installed."
- "Error: GitHub CLI is not authenticated. Please run 'gh auth login'."
- "Error: Not inside a git repository."

### Operation Failures
**MUST** handle failures gracefully:
- Verify issue creation success
- Check branch creation/checkout success
- Validate remote operations

---

## References
- [Conventional Commits Specification](https://www.conventionalcommits.org/)
- [Semantic Versioning](https://semver.org/)

---

## Related Documents

This document covers Git operation **standards and rules**. For related topics, see:

| Document | Purpose |
|:---------|:--------|
| [commit-granularity.md](commit-granularity.md) | Detailed philosophy on atomic commits |
| [idd-phase2-impl.md](../../workflows/idd-phase2-impl.md) | **Workflow**: When and how to apply these rules |
| [idd-phase1-init.md](../../workflows/idd-phase1-init.md) | **Workflow**: Issue and branch creation |
| [idd-phase3-fini.md](../../workflows/idd-phase3-fini.md) | **Workflow**: Push and finalization |
| [prepare-commit.md](../../workflows/prepare-commit.md) | **Workflow**: Pre-commit preparation |
| [absolute-path-prohibition.md](../core/security/absolute-path-prohibition.md) | **Security**: Rules for relative paths & sanitization |
