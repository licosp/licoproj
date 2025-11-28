# Git Operations Standards

## Purpose
Define comprehensive behavioral standards for all Git operations including commits, branches, conflict resolution, and security practices.

## Core Principles

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

#### 2.5 Body (Optional)
- MUST be separated from description by a blank line
- MAY consist of multiple paragraphs separated by blank lines
- SHOULD explain:
  - **Why** the change was made
  - **Impact** and side effects
  - **Implementation** details if complex

**Example**:
```
feat: add user authentication module

This change introduces JWT-based authentication to secure API endpoints.
The implementation uses bcrypt for password hashing and includes
session management with automatic token refresh.

This affects all protected routes and requires database migration.
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
- **Labels**: Match commit type (`feat`, `fix`, etc.)

#### 4.4 Idempotency
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
