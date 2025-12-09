# Git Operations Standards

## Purpose
Define comprehensive behavioral standards for all Git operations including commits, branches, conflict resolution, and security practices.

## Core Principles

### 0. Commit Message Quality (HIGHEST PRIORITY)
**MUST** write commit messages that enable complete reconstruction of project state from git log alone.
- **Future Tracking**: Messages MUST allow Lico to understand what files contained without accessing them
- **Self-Documenting**: Each commit MUST be understandable by future AI instances
- **Audit Trail**: Messages MUST serve as permanent record of reasoning and implementation

### 1. Commit Atomicity and Logic

#### 1.1 Logical Separation
- **MUST** categorize changes into logical units (e.g., Config, Refactor, Feat, Docs)
- **MUST** determine if a single commit is sufficient or if splitting is required
- **MUST NOT** mix unrelated changes in the same commit

#### 1.2 Pre-Commit Analysis
- **MUST** run `git status` and `git diff --stat` before committing
- **MUST** understand the full scope of changes before proceeding

#### 1.3 Staging Verification (CRITICAL)
- **MUST** verify staged content with `git diff --cached --stat` and `git diff --cached`
- **MUST** ensure *only* intended changes are staged
- **MUST** use `git restore --staged <file>` to unstage unrelated files

#### 1.4 Selective Staging (CRITICAL)

**Principle**: Stage only files that belong to the same logical change.

**Requirements**:
- **MUST NOT** stage all files indiscriminately
- **MUST** identify which files are related to the current logical change
- **MUST** stage only those related files
- **MUST** verify the staged content matches the intended logical change

**Rationale**: 
Staging unrelated files together violates the atomic commit principle. Each commit should represent one logical change that can be described in a single sentence. If multiple unrelated changes are staged together, they cannot be reverted independently, and the commit history becomes unclear.

**Implementation guidance**:
- Identify related files: Review `git status` output and determine which files belong together
- Stage selectively: Use Git commands to stage only the identified files
- Verify staging: Review the staged changes to confirm only intended files are included
- Unstage if needed: Remove files from staging if they don't belong to this logical change

**Example scenario**:
If you are removing a tool (e.g., husky), stage only the files related to that removal:
- The tool's directory
- Configuration files that reference the tool
- Package manifests that list the tool as a dependency

Do NOT stage unrelated files such as:
- Documentation updates for a different feature
- Code changes in application files
- Temporary files or experiments

---

### 2. Conventional Commits Specification

#### 2.1 Basic Format
```
<type>[optional scope]: <description>

[optional body]

[optional footer(s)]
```

#### 2.2 Type
**REQUIRED**. MUST be one of:
- `feat`: New feature (correlates with MINOR in SemVer)
- `fix`: Bug fix (correlates with PATCH in SemVer)
- `docs`: Documentation changes
- `style`: Code style changes (formatting, no logic change)
- `refactor`: Code refactoring (no feature or bug fix)
- `perf`: Performance improvements
- `test`: Adding or updating tests
- `build`: Build system or external dependencies
- `ci`: CI/CD configuration changes
- `chore`: Other changes (e.g., tooling, maintenance)

#### 2.3 Scope (Optional)
- Provides additional context (e.g., `feat(auth): add login page`)
- Enclosed in parentheses after type

#### 2.4 Description
**REQUIRED**. MUST:
- Use imperative, present tense (e.g., "Add" not "Added" or "Adds")
- Be concise and clear
- Not end with a period

**Example**: `feat: add user authentication module`

#### 2.5 Body (REQUIRED for non-trivial changes)
- MUST be separated from description by a blank line
- MAY consist of multiple paragraphs separated by blank lines
- MUST explain:
  - **Why** the change was made
  - **What** files were changed and their purpose
  - **Impact** and side effects
  - **Implementation** details if complex

**File Tracking Requirement**:
- MUST list changed files with brief description of their contents/purpose
- MUST enable future reconstruction of what each file contained
- SHOULD use format: `- filename: brief description of contents/changes`

**Example**:
```
feat: add user authentication module

This change introduces JWT-based authentication to secure API endpoints.
The implementation uses bcrypt for password hashing and includes
session management with automatic token refresh.

Changed files:
- src/auth/jwt-middleware.js: JWT token validation and refresh logic
- src/auth/bcrypt-utils.js: Password hashing utilities with salt generation
- src/models/User.js: User model with authentication fields
- src/routes/auth.js: Login/logout/register API endpoints

This affects all protected routes and requires database migration.
```

**File Tracking Examples**:

*Simple file changes*:
```
docs: update README with setup instructions

Updated project setup documentation.

Changed files:
- README.md: Added installation and configuration steps
```

*Multiple file changes*:
```
refactor: reorganize project structure

Reorganized source code into feature-based directories for better maintainability.

Changed files:
- src/components/Button.js: Reusable button component
- src/components/Modal.js: Modal dialog component
- src/pages/Dashboard.js: Main dashboard page component
- src/utils/helpers.js: Common utility functions
- src/styles/components.css: Component-specific styles
```

#### 2.6 Footers (Optional)
- MUST be separated from body (or description if no body) by a blank line
- Format: `<word-token>: <value>` or `<word-token> #<value>`

**Common footers**:
- `Closes #<issue-number>`: Links to closed issue
- `Refs #<issue-number>`: References related issue
- `BREAKING CHANGE: <description>`: Indicates breaking change

**Example**:
```
feat: redesign API response structure

BREAKING CHANGE: API endpoints now return data in `{ success, data, error }` format
Closes #275
```

#### 2.7 Breaking Changes
**MUST** be indicated using one of these methods:

**Method 1**: `BREAKING CHANGE:` footer
```
feat: remove legacy authentication

BREAKING CHANGE: Old session-based auth is no longer supported
```

**Method 2**: `!` after type/scope
```
feat!: remove legacy authentication
```

**Meaning**: Backward-incompatible change (correlates with MAJOR in SemVer)

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
| [commit-granularity.md](file:///home/leonidas/develop/shared/project/licoproj/.agent/rules/development/commit-granularity.md) | Detailed philosophy on atomic commits |
| [idd-phase2-impl.md](file:///home/leonidas/develop/shared/project/licoproj/.agent/workflows/idd-phase2-impl.md) | **Workflow**: When and how to apply these rules |
| [idd-phase1-init.md](file:///home/leonidas/develop/shared/project/licoproj/.agent/workflows/idd-phase1-init.md) | **Workflow**: Issue and branch creation |
| [idd-phase3-fini.md](file:///home/leonidas/develop/shared/project/licoproj/.agent/workflows/idd-phase3-fini.md) | **Workflow**: Push and finalization |
| [prepare-commit.md](file:///home/leonidas/develop/shared/project/licoproj/.agent/workflows/prepare-commit.md) | **Workflow**: Pre-commit preparation |
