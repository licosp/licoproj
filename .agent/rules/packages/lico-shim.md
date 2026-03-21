---
ai_visible: true
title: Command Shims Protocol
description: Protocol for environment-based safety mechanism (Shims) to override command behaviors transparently.
tags: [protocol, environment, safety, shims, scripts]
version: 1.2.0
created: 2026-02-15T21:15:00+09:00
updated: 2026-03-21T19:30:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
---

# lico-shim (Command Shims Protocol)

## Philosophy: Environment Over Willpower

> "Do not rely on the AI's memory or willpower to execute safe commands. Rely on the Environment."

This protocol defines the mechanism of **Command Shims**—intercepting standard commands (like `grep` or `rm`) and transparently replacing them with safer implementations.

### Why Shims?

1. **Cognitive Offloading**: AI agents often default to standard commands (`grep`, `mv`, `rm`) due to training bias and cognitive load. Forcing them to remember `git grep` or `git mv` is unreliable.
2. **Transparent Safety**: By intercepting the standard command, we ensure safety without requiring behavioral changes from the agent or the user.
3. **Environment as Constraint**: We define safety rules in the execution environment (PATH), making it physically impossible (or default-biased) to execute the unsafe version.

---

## Architecture

### 1. Unified Python Router: `packages/lico-shim/`

All shim logic is consolidated into a single, strict Python router (`lico-shim`). This adheres to the AI Script Philosophy of relying on strict Python for complex data parsing and routing logic.

- **Config**: `.agent/scripts/shim_config.yaml` manages feature flags for each command.
- **Router Core**: The script evaluates `sys.argv[0]` to determine its identity and parses the YAML config to decide whether to activate safety logic or pass-through.
- **Runtime Isolation**: The router itself runs on the System Python environment, but explicitly sub-processes commands like `python` into the `uv` virtual environment if necessary.

### 2. Runtime Injection: `.runtimes/bin/`

Commands are intercepted by symlinking the target binary name directly to the `lico-shim` router in a directory prioritized by the system `PATH`.

- **Deployment**: `uv tool install` or direct binary links in `.runtimes/bin/<cmd>`
- **Activation**: The environment automatically prefers binaries in `.runtimes/bin` over `/usr/bin` or `/bin`.

### 3. Feature Flag Toggles

Shims are **OFF by default**, acting as transparent pass-throughs to native binaries to avoid disrupting standard workflows.

- **CLI Management**: Use the `./.runtimes/bin/lico-shim` command to manage flags.
  - Turn ON: `lico-shim on rm` (activates the `rm` safety shim)
  - Turn OFF: `lico-shim off all` (disables all safety shims)
  - Config Location: `.agent/scripts/shim_config.yaml`

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
  - **Restore**: Blocks `git restore` (No-Discard Policy).
    - **Trigger**: `restore` command.
    - **Reason**: Prevents accidental loss of uncommitted drafts or logs.
  - **Clean**: Blocks `git clean` (No-Untracked-Delete Policy).
    - **Trigger**: `clean` command.
    - **Reason**: Prevents permanent deletion of untracked files (bypass `rm` shim).
- **Purpose**: Enforces safety constraints (Soft-First Rule, Context Integrity).

---

## Extension Guide (Adding New Shims)

To add a new Shim to the Python Router:

1. **Add Flag**: Add the new boolean flag to `.agent/scripts/shim_config.yaml`.
2. **Update Router**: Add a new `handle_<cmd>` function to `lico-shim.py` and register it in the `main()` router block.
3. **Deploy**: Symlink the command name to the router: `ln -s $(pwd)/.agent/scripts/lico-shim.py .runtimes/bin/<cmd>`
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
- 2026-02-19T03:40+09:00 by Sirius: Added restrictions for `git restore` and `git clean` to prevent accidental data loss.
- 2026-02-28T04:15+09:00 by Sirius: Refactored python logic for strict linting compliance. (v1.1.0)
- 2026-03-21T19:30:00+09:00 by Sirius: Migrated rule to `.agent/rules/packages/` to reflect transition to `lico-shim` UV package architecture. (v1.2.0)
