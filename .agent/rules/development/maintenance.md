---
description: Guidelines for maintaining project consistency and documentation
---

# Project Maintenance Guidelines

## Hook File Synchronization

### Core Requirement

**Hook files must always be synchronized to maintain consistency across different AI models.**

### Affected Files

The following hook files must contain identical content:

- `CODE_OF_CONDUCT.md`
- `.github/copilot-instructions.md`

### Synchronization Protocol

1. **When updating rules**: Modify the primary hook file first
2. **Immediate sync**: Copy content to all other hook files
3. **Verification**: Ensure diff shows no differences
4. **Documentation**: Update `.agent/rules/.updated` with synchronization note

### Primary Hook File

**`CODE_OF_CONDUCT.md`** serves as the primary hook file for:
- General AI assistants
- Documentation consistency
- User-facing behavioral guidelines

### Secondary Hook Files

**`.github/copilot-instructions.md`** serves as:
- GitHub Copilot specific entry point
- IDE-integrated AI assistance

### Implementation

#### Sync Command
```bash
# Sync .github/copilot-instructions.md with CODE_OF_CONDUCT.md
cp CODE_OF_CONDUCT.md .github/copilot-instructions.md
```

#### Verification
```bash
# Verify synchronization
diff CODE_OF_CONDUCT.md .github/copilot-instructions.md
# Should return no output if synchronized
```

### Rationale

- **Consistency**: All AI models receive identical behavioral guidelines
- **Maintenance**: Single source of truth reduces synchronization errors
- **Reliability**: Prevents divergent behavior between different AI models
- **Transparency**: Clear protocol ensures accountability

### Exception Handling

If hook files must differ:
1. Document the specific differences and rationale
2. Create separate rule files for divergent requirements
3. Maintain synchronization for all common content

## Implementation Plan Standards (Dual-Plan Workflow)

### Concept
Separate "AI thinking process" from "Human review documents" to optimize for both efficiency and readability.

### 1. AI Internal Plan (Working Memory)
- **Location**: `.gemini/.../implementation_plan.md` (Hidden/Ephemeral)
- **Format**: Optimized for AI (English, concise, technical)
- **Purpose**: Task tracking and context maintenance for the agent.

### 2. Human Review Plan (Deliverable)
- **Location**: `.human/plans/YYYY-MM-DDTHH-MM-SS+09-00_implementation_plan.md`
- **Format**: **Strictly adhering to Code of Conduct** (Japanese, human-readable, formatted)
- **Purpose**: User review, approval, and project history.
- **Requirement**: MUST be created and presented to the user for any complex task.

## Interrupted Task Recording

### Policy
- When a task is interrupted or suspended, it MUST be recorded to preserve context.
- **Location**: `.human/tasks/YYYY-MM-DDTHH-MM-SS+09-00_interrupted-tasks.md`
- **Content**: Summary of task, reason for interruption, and requirements for resumption.

## Issue Archival Standards

### Purpose
Archive GitHub issue data locally for offline access and migration support.

### Location
Store in `.agent/issues/` directory with structured JSON format.

### File Naming
`issue-{number}-github-complete-data.json`

### Data Structure
```json
{
  "metadata": {
    "description": "Purpose and capture info",
    "capture_timestamp": "ISO8601",
    "purpose": ["offline_access", "recovery", "reference", "migration"]
  },
  "issue": { /* Complete issue data */ },
  "comments": [ /* All comments */ ],
  "related_pull_requests": [ /* Linked PRs */ ],
  "related_branches": [ /* Connected branches */ ],
  "statistics": { /* Summary stats */ }
}
```

### Update Triggers
- When issue status changes (open/close)
- When new comments are added
- Before major repository operations
- During migration planning

## Work Directory Workflow

### Overview
All file creation and modification operations must use the `.agent/.internal/work/` directory as an intermediate workspace to ensure safety across different environments and prevent direct production file corruption.

### Core Requirements
- **Never modify production files directly**
- **Always create intermediate files first**
- **Use timestamp-based naming for concurrency safety**
- **Clean up intermediate files after successful operations**

### Workflow Process

#### 1. Permission Assessment
```
1. Check write permissions for target production file
2. Determine application method (direct vs manual)
3. Log environment capabilities
```

#### 2. Intermediate File Creation
**Location**: `.agent/.internal/work/`
**Naming Format**: `{target-basename}-{timestamp}-{environment}-{permission-status}.md`
**Timestamp Format**: `YYYYMMDDTHHMMSS+TZ` (ISO 8601 compact)

#### 3. Content Development
```
1. Develop and refine content in intermediate file
2. Perform internal validation and self-review
3. Flag for human review if required
```

#### 4. Production Application
**Success Path**:
- Apply changes to production file
- Delete intermediate file immediately
- Update `.agent/rules/.updated` tracking

**Failure Path**:
- Move intermediate file to `.agent/.internal/archive/work/`
- Notify user of manual intervention required
- Preserve work for later recovery

### Environment-Specific Handling

#### Permission Granted Environments (e.g., Cursor)
- Automated application with immediate cleanup
- Direct production file updates
- Minimal user intervention

#### Permission Denied Environments (e.g., Antigravity)
- Intermediate file creation only
- User notification for manual application
- Work preservation for later application

### File Cleanup Policy
- **Successful operations**: Delete intermediate files immediately
- **Failed operations**: Archive to `.agent/.internal/archive/work/` with timestamp
- **Review-required operations**: Preserve until user approval
- **Concurrent operations**: Timestamp prevents conflicts, manual merge if needed

### Audit and Transparency
- All operations logged with timestamps
- Environment and permission status recorded
- Complete history maintained for debugging
- User review trail preserved

This workflow ensures safe, transparent, and environment-agnostic file operations across all Lico instances and development environments.
