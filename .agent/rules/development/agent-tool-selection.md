---
description: Policy for prioritizing Standard Linux Commands over AI-specific tools for reproducibility and robustness
---

# Agent Tool Selection Policy

## Core Philosophy

**"Reproducibility > Convenience"**

Antigravity tools (AI-specific wrappers) are "Convenience Wrappers" optimized for JSON parsing and short-term memory ease.
Standard Linux Commands are "Foundational Tools" optimized for reproducibility, verifiability, and persistent state management.

For any task involving bulk processing, state persistence, or reproducibility, **priority MUST be given to standard Linux commands.**

---

## Tool Classification Matrix

### Group 1: Essential Capabilities (Irreplaceable)
**Status**: **MANDATORY**
Capabilities that do not exist in a standard Linux shell environment.

| Tool Name | Usage | Linux Alternative |
|:--- |:--- |:--- |
| `task_boundary` | Managing task state and UI. | None |
| `notify_user` | Communicating with the user. | None |
| `browser_subagent` | Operating a GUI web browser. | None (w3m/lynx are limited) |
| `generate_image` | Creating visual assets. | None |

---

### Group 2: Surgical Safety (Safety > Raw Power)
**Status**: **PREFERRED (for existing code)**
Tools that offer atomic, safer modification of code than complex shell oneliners.

| Tool Name | Usage | Linux Alternative | Reason for Preference |
|:--- |:--- |:--- |:--- |
| `replace_file_content` | Editing specific blocks. | `sed`, `awk`, `perl` | `sed` is prone to disastrous syntax errors in complex replacements. |
| `multi_replace_file_content` | Multiple edits in one file. | `sed` scripts | Safer atomic commit/revert capability. |

**Policy**: Do NOT use `sed -i` for complex code refactoring. Use these tools.

---

### Group 3: Semantic Analysis (Efficiency > Parsing)
**Status**: **ALLOWED (for analysis)**
Tools that parse code structure (AST-like) more effectively than regex.

| Tool Name | Usage | Linux Alternative | Reason for Preference |
|:--- |:--- |:--- |:--- |
| `view_code_item` | Reading a specific function/class. | `grep` + line reckoning | Reduces token usage by extracting only relevant symbols. |
| `view_file_outline` | Listing symbols in a file. | `ctags` | `ctags` may not be installed/configured; Outline is reliable. |

---

### Group 4: Filesystem Operations (Standardization > Convenience)
**Status**: **RESTRICTED (Ad-hoc Only)**
Tools that wrap standard filesystem commands. These create a "Black Box" effect and rely on AI memory.

**Policy**:
- **Single File / Quick Check**: AI Tools OK.
- **Bulk / Search / State Tracking**: **LINUX COMMANDS MANDATORY.**

| Tool Name | Usage context | **Preferred Linux Command** | Reason |
|:--- |:--- |:--- |:--- |
| `grep_search` | Search text. | **`grep`** (with redirection) | `grep` output can be saved to a file (Todo list). |
| `find_by_name` | Find files. | **`find`** or **`fd`** | `find` allows piping to xargs or saving lists. |
| `list_dir` | List contents. | **`ls -R`** or **`tree`** | `ls` options are infinitely more flexible. |
| `view_file` | Read file content. | **`cat`**, **`head`**, **`less`** | `view_file` has arbitrary line limits (800 lines). `cat` has none. |

---

### Group 5: Deprecated / Dangerous
**Status**: **BANNED (for editing)**
Tools that pose inherent risks of data loss.

| Tool Name | Risk | Safe Alternative |
|:--- |:--- |:--- |
| `write_to_file` | **Truncation Risk**. Overwriting an existing file based on a partial `view_file` read causes permanent data deletion. | `replace_file_content` (Edit) or `cat > file` (Rewrite) |

---

## Decision Flowchart

1. **Is it an Agent/Browser action?**
   - YES -> Use **Group 1 Tools**.

2. **Is it editing Code?**
   - YES -> Use **Group 2 Tools**. (Avoid `sed` unless simple config change).

3. **Is it a Bulk Search or List generation?**
   - YES -> **STOP.** Use **Linux Commands** (`grep`, `find`) and redirect to a file.
   - NO (One file check) -> Group 3 or 4 Tools are acceptable.

4. **Is it creating a text file?**
   - Use `write_to_file` (for new) or `cat >` (standard). Both are fine.

---

## Related Rules

- **[File Operation Safety Standards](file-operations.md)**: Detailed safety protocols for Group 2 (Surgical Safety) and Group 5 (Deprecated) tools.
- **[Problem Solving](problem-solving.md)**: General philosophy on reproducibility and systematic debugging which aligns with Group 4 (Filesystem Operations).

