---
ai_visible: true
title: Command Shims Protocol
description: Protocol for environment-based safety mechanism (Shims) to override command behaviors transparently.
tags: [protocol, environment, safety, shims, scripts]
version: 1.0.0
created: 2026-02-15T21:15:00+09:00
updated: 2026-02-18T07:55:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Command Shims Protocol

## Philosophy: Environment Over Willpower

> "Do not rely on the AI's memory or willpower to execute safe commands. Rely on the Environment."

This protocol defines the mechanism of **Command Shims**—intercepting standard commands (like `grep` or `rm`) and transparently replacing them with safer implementations.

### Why Shims?

1. **Cognitive Offloading**: AI agents often default to standard commands (`grep`, `mv`, `rm`) due to training bias and cognitive load. Forcing them to remember `git grep` or `git mv` is unreliable.
2. **Transparent Safety**: By intercepting the standard command, we ensure safety without requiring behavioral changes from the agent or the user.
3. **Environment as Constraint**: We define safety rules in the execution environment (PATH), making it physically impossible (or default-biased) to execute the unsafe version.

---

## Architecture

### 1. Source Directory: `.agent/scripts/`

All shim scripts are managed in this directory under Git control.

- **Scripts**: Executable shell scripts (e.g., `grep`, `rm`).
- **Config**: Configuration files (e.g., `shim_ignore_dirs`).

### 2. Runtime Injection: `.runtimes/bin/`

Scripts are symlinked to a directory that is prioritized in the system `PATH`.

- **Deployment**: `ln -s ../../.agent/scripts/<cmd> .runtimes/bin/<cmd>`
- **Activation**: The environment automatically prefers binaries in `.runtimes/bin` over `/usr/bin` or `/bin`.

---

## Active Shims Reference

### `grep` (Safe Search)

- **Behavior**:
  - **In Git Repo**: Delegates to `git grep` (Respects `.gitignore`).
  - **Outside Repo**: Delegates to `grep` but injects `--exclude-dir` from `shim_ignore_dirs`.
- **Purpose**: Prevents accidental scanning of massive directories (`node_modules`, `.shadow`, etc.) which consumes token budget.
- **Config**: `.agent/scripts/shim_ignore_dirs`

### `mv` (Git Aware Move)

- **Behavior**:
  - **In Git Repo**: Tries `git mv` first.
  - **Fallback**: If `git mv` fails (e.g., untracked file), falls back to `/bin/mv`.
- **Purpose**: Ensures file moves are tracked by Git without requiring the agent to distinguish between `mv` and `git mv`.

### `rm` (Smart Remove / No-Delete Policy)

- **Behavior**:
  - **Action**: **NEVER deletes files.** Moves them to `.trash/<Timestamp>/`.
  - **Git Integration**: If the file was tracked, executes `git add -u <file>` to stage the deletion in Git.
- **Purpose**: Provides a safety net for accidental deletions while maintaining Git status consistency.
- **Trash Location**: `.trash/YYYY-MM-DDTHHMMSS/` (Git-tracked directory, contents ignored).

### `git` (Safety Enforcer)

- **Behavior**:
  - **Shadow Protection**: Blocks operations on `.shadow/` files from the root directory.
    - **Trigger**: Argument contains `.shadow/`.
    - **Action**: **BLOCKS execution** and instructs user to `cd` into the directory.
  - **Hard Reset**: Blocks `git reset --hard` to prevent data loss.
    - **Trigger**: `reset` AND `--hard`.
    - **Action**: **BLOCKS execution**.
    - **Bypass**: Use `/usr/bin/git reset --hard`.
- **Purpose**: Enforces safety constraints (Soft-First Rule, Context Integrity).

---

## Extension Guide (Adding New Shims)

To add a new Shim:

1. **Create Script**: Add the script to `.agent/scripts/<command>`.
2. **Make Executable**: `chmod +x .agent/scripts/<command>`
3. **Deploy**: Symlink to `.runtimes/bin/`.
4. **Document**: Update this file (`Active Shims Reference`) and the associated Context Card.

### Guideline

- **Pass-through**: Ensure the shim accepts standard arguments (`"$@"`) and passes them to the underlying tool.
- **Fallback**: Always provide a fallback to the system binary if the special condition (e.g., Git repo) is not met.

### Error Message Standard

To distinguish Shim interventions from native command errors, use the following format:

- **Icon**: `🚫` (U+1F6AB No Entry Sign)
- **Prefix**: `[Shim]`
- **Format**: `🚫 [Shim] <Type>: <Message>`

**Example**:

```bash
echo "🚫 [Shim] BLOCKED: 'git reset --hard' is dangerous." >&2
```

---

## Related Documents

| Document                                                          | Purpose                              |
| :---------------------------------------------------------------- | :----------------------------------- |
| [`environment-specs.md`](/.agent/rules/core/environment-specs.md) | Technical environment specifications |
| [Map of Territory](/.agent/rules/map.md)                          | Root navigation map                  |

---

## Origin

- 2026-02-15T21:15+09:00 by Sirius: Created to document the Command Shims implementation.
- 2026-02-18T07:55+09:00 by Sirius: Implemented Shadow Repository protection and standardized error messages.
