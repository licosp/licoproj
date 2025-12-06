---
description: Guidelines for managing development tools and dependencies within workspaces
---

# Workspace-Centric Tooling

## Core Principle

**Install libraries and tools within the workspace whenever possible. Manage tools through the repository to enhance portability.**

## Guidelines

### 1. Workspace-First Approach

- **Prefer workspace dependencies** over global installations
- **Document tool versions** in `package.json` or equivalent
- **Use workspace scripts** for common operations

### 2. Tool Management

#### ✅ Recommended: Workspace Installation (Node.js)
```json
{
  "devDependencies": {
    "eslint": "^9.17.0",
    "prettier": "^3.6.2",
    "gh": "^2.8.9"
  },
  "scripts": {
    "lint": "eslint .",
    "format": "prettier --write .",
    "gh": "gh"
  }
}
```

#### ✅ Recommended: Workspace Installation (Python)
We use `uv` for Python project management, installed locally in the workspace.

- **Location**: `.agent/runtimes/bin/uv`
- **Virtual Env**: `.venv/` (created by `uv venv`)
- **Usage**:
  ```bash
  # Activate environment
  source .venv/bin/activate
  
  # Run commands via uv
  .agent/runtimes/bin/uv pip install <package>
  ```

#### ❌ Avoid: Global Installation
```bash
# Avoid these when workspace alternative exists
npm install -g eslint
pip install --user <package>
```

### 3. Portability Benefits

- **Environment Consistency**: Same tools across different machines
- **Version Control**: Tool versions tracked in repository
- **Easy Setup**: `yarn install` or `uv sync` sets up complete environment
- **Collaboration**: Team members use identical tooling

### 4. When Global Installation is Acceptable

- **System-level runtimes**: Node.js, Python (base interpreter), etc.
- **OS tools**: git, curl, etc.
- **IDE-specific tools**: When workspace alternative doesn't exist
- **Performance-critical tools**: When local installation impacts performance significantly

### 5. Implementation

#### Yarn Workspaces
```json
{
  "workspaces": ["packages/*"],
  "devDependencies": {
    "tool-name": "^version"
  }
}
```

#### Tool Execution
```bash
# Preferred: Workspace-local execution
npx yarn lint
npx yarn gh issue list
.agent/runtimes/bin/uv run <command>

# Avoid: Global execution
eslint .
gh issue list
```

## Rationale

This approach ensures:
- **Reproducible environments** across development machines
- **Simplified onboarding** for new team members
- **Version consistency** through repository management
- **Reduced environment conflicts** between projects
