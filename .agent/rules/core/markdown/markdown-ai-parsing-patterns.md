---
description: Anti-patterns to avoid and examples of optimal AI-optimized markdown
---

# Markdown AI-Parsing Patterns

## When to Use AI-Optimized Markdown

- **Automation Scripts**: Markdown files parsed by Python/Node scripts
- **AI-to-AI Communication**: Passing structured information between AI systems
- **Specification Documents**: Technical specs where precision is critical
- **Logging and Records**: Machine-readable logs with structured format
- **Configuration Guides**: Where consistency matters for parsing

## When to Use Human-Readable Markdown

- **User Documentation**: Guides intended for human readers
- **Blog Posts**: Content prioritizing engagement and visual appeal
- **README Files**: Project introductions and getting-started guides
- **Meeting Notes**: Flexible capture of ideas and discussions

## Contrast with Human-Readability Guidelines

| Aspect | AI-Optimized | Human-Readable |
|--------|--------------|-----------------|
| Primary Goal | Machine parsing efficiency | Visual scanning and appeal |
| Emojis | Minimal/eliminated | Encouraged for landmarks |
| Whitespace | Minimal and structural | Generous breathing room |
| Emphasis | Bold only for keywords | Bold, italics, decorative styles |
| Lists | Strict consistency | Flexible markers |
| Line Length | 80-100 characters | No hard limit |
| Redundancy | Eliminated | Acceptable if clarifying |
| Decorative Elements | None | Encouraged (rules, separators) |

## Robust AI Instruction Patterns

### Low-Compute Constraints
For models with limited reasoning or context windows:

1.  **Atomic Steps Principle**
    - One action per step.
    - **Bad**: "Create file and write content."
    - **Good**:
      1. Create file.
      2. Write content.

2.  **Explicit Verification**
    - Mandate verification after *every* state-changing action.
    - Example: "Run `ls` to confirm file creation."

3.  **Linearity**
    - Avoid complex branching (`if-then-else`).
    - Flatten logic into linear sequences where possible.

### Resumability & Idempotency
Ensure workflows can recover from forced termination:

1.  **Idempotent Commands**
    - Use commands that are safe to re-run.
    - **Bad**: `mkdir dir` (fails if exists)
    - **Good**: `mkdir -p dir`
    - **Bad**: `echo "line" >> file` (duplicates)
    - **Good**: `grep -q "line" file || echo "line" >> file`

2.  **Self-Correcting Pre-conditions**
    - Verify state before acting.
    - Example: "Check if `node_modules` exists; if not, run `npm install`."

3.  **Atomic Writes**
    - Write to temporary file -> Move to final path.
    - Prevents partial file corruption on interrupt.

## Anti-Patterns (Avoid These)

```markdown
<!-- WRONG: Mixed emphasis -->
This is ***very important*** text.

<!-- WRONG: Inconsistent lists -->
- First item
* Second item
+ Third item

<!-- WRONG: Multiple blank lines -->
## Section


This text has excessive whitespace.

<!-- WRONG: Nested heading levels -->
# Title
## Section
##### Skipped levels

<!-- WRONG: Inline links scattered -->
See [this guide](url1) and [this resource](url2) and [this tool](url3).

<!-- WRONG: Unclear relationships -->
Next.
Also this.
Finally, that.
```

## Good Examples

### Example 1: Structured Procedure

```markdown
---
description: Steps to initialize a project
---

# Project Initialization

## Overview
This document outlines the standard initialization process.

## Prerequisites
- Node.js version 16 or higher
- npm version 8 or higher
- Git installed and configured

## Steps

### 1. Clone Repository
```bash
git clone https://github.com/example/project.git
cd project
```

### 2. Install Dependencies
```bash
npm install
```

### 3. Configure Environment
Create `.env` file with required variables:
- API_KEY: Your API key
- NODE_ENV: Set to "development"

## Verification
Run `npm test` to confirm installation.
```

### Example 2: API Reference

```markdown
# API Reference

## Authentication

Use Bearer token authentication for all requests.

```
Authorization: Bearer <your-token>
```

## Endpoints

### GET /users
Retrieve list of all users.

- Query Parameters:
  - page: Page number (default: 1)
  - limit: Items per page (default: 10)

- Response: 200 OK
  ```json
  {
    "users": [
      {"id": 1, "name": "User One"},
      {"id": 2, "name": "User Two"}
    ]
  }
  ```

### POST /users
Create new user.

- Request Body:
  ```json
  {
    "name": "New User",
    "email": "user@example.com"
  }
  ```

- Response: 201 Created
```

## Decision Framework

Choose based on primary audience:
- **Audience: AI Systems** → Use AI-Optimized Markdown
- **Audience: Humans (with AI reading secondarily)** → Use Human-Readable Markdown
- **Mixed Audience** → Err toward human-readable unless parsing is critical
