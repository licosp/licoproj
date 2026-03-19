---
context_id: "[Pkg-Shim]"
default_phase: "(Setup)"
ai_visible: true
version: 1.0.0
created: 2026-02-15T20:30:00+09:00
updated: 2026-03-19T00:00:00+09:00
tags: ["shim", "shell", "safety", "environment", "package"]
language: en
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Context Whiteboard: Package lico-shim

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.

---

## Agent Observations

### Sirius (2026-02-15)

#### Context

- **リコの行動（コマンド入力）を変えずに、結果を安全にする**ための取り組みです。
- 具体的には、危険なコマンド（`grep` 等）を同名のラッパースクリプト（Shim）に置き換えます。
- これにより、リコが誤って重いディレクトリ（`node_modules` 等）を検索するのを防ぎます。

### Searched by intent

- Where are the scripts? -> `.agent/scripts/`
- Where is the config? -> `.agent/scripts/shim_ignore_dirs`
- How is it activated? -> Symlinked to `.runtimes/bin/` and added to PATH (conceptually).

#### Shim Architecture

- **Source**: `.agent/scripts/<command>`
- **Config**: `.agent/scripts/shim_ignore_dirs`
- **Deployment**: Symlink to `.runtimes/bin/<command>` (or appropriate bin dir).

#### Implementation Status

- [x] Create Context Card (This file)
- [x] Create Ignore Config
- [x] Create `grep` Shim
- [x] Create `mv` Shim
- [x] Create `rm` Shim
- [x] Create `git` Shim (Block Hard Reset)
- [x] Activate Shim (Link)

### Sirius (2026-02-20)

- **Fix**: Updated `rm` shim to use Script-Relative Absolute Path for `.trash/`.
  - **Issue**: `git rev-parse` caused `.trash/` creation in CWD if inside another git repo (e.g. `.shadow/`).
  - **Resolution**: `$(dirname $(readlink -f $0))/../..` ensures Workspace Root.

---

## Related Documents

| Document                                                          | Purpose                 |
| :---------------------------------------------------------------- | :---------------------- |
| [`environment-specs.md`](/.agent/rules/core/environment-specs.md) | Environment definitions |
| [Map of Territory](/.agent/rules/map.md)                          | Root navigation map     |

---

## Origin

- 2026-02-15T20:30 by Sirius: Created for command shim implementation.
