---
description: Safety protocols for file editing to prevent data loss and cognitive errors
---

# File Operation Safety Standards

> **See also**: **[Agent Tool Selection Policy](agent-tool-selection.md)** for broader guidelines on tool usage priority.


## Core Philosophy

**"Trust the Filesystem, Edit Surgically."**

AI cognitive context is volatile and limited. The filesystem is persistent and complete.
When editing existing files, do not attempt to load the entire file into memory, modify it, and write it back. Instead, perform surgical edits on the specific parts that need changing, leaving the rest of the filesystem untouched.

---

## 1. Partial Replacement Default (The Surgical Rule)

### Rule
**For ANY modification to an existing file, you MUST prioritize using `replace_file_content` or `multi_replace_file_content`.**

### Prohibition
**Do NOT use `write_to_file` (Overwrite) for editing existing files, unless:**
1. The file is extremely small (< 50 lines) AND you have verified you are viewing 100% of it.
2. You intend to completely completely wipe and rewrite the file content (e.g., refactoring a configuration file from scratch).

### Rationale
`view_file` often truncates large files. Overwriting a file based on truncated view results in permanent data loss of the unseen portions. Surgical replacement tools do not touch unreferenced lines, making them inherently safe against truncation errors.

---

## 2. Point-and-Call Protocol (Cognitive Ritual)

### Rule
**Immediately after using `view_file`, you MUST verbally (in thought logs) compare the specific metadata.**

### Ritual Script
> "Total Lines: [N]. Showing Lines: [X] to [Y]. [ALL/PARTIAL] content is visible."

If status is **PARTIAL**, explicitly state:
> "WARNING: I am seeing only a part of this file. Overwrite operations are forbidden."

### Rationale
Cognitive bias leads AI to assume "what I see is everything." This ritual forces a conscious check of the `Total Lines` metadata, breaking the bias.

---

## 3. Post-Edit Audit (Safety Net)

### Rule
**After any file modification, verify the physical impact of the change.**

### Procedure
1. Run `git diff --shortstat` (or equivalent).
2. check if the number of **deletions** matches your expectation.
3. If deletions are surprisingly high (e.g., >100 lines for a simple header fix), **IMMEDIATELY REVERT** using `git checkout`.

### Rationale
Even with the best intentions, tools can behave unexpectedly. A post-action audit is the final line of defense to catch catastrophic deletions before moving on.

---

## 4. Universal Command Principle (Anti-Lock-in)

### Rule
**For bulk searching, state management, or tasks requiring reproducibility, you MUST prioritize standard Linux commands (`run_command`) over AI-specific proprietary tools.**

- **Preferred**: `grep`, `find`, `sed`, `awk`, `cat` (via `run_command`)
- **Avoid (for bulk tasks)**: `grep_search`, `find_by_name`, `list_dir` (AI-only Wrappers)

### Scenario Guidelines
- **Ad-hoc / Quick Check**: AI Tools (`grep_search`) are acceptable for single-file inquiries.
- **Bulk Processing / Global Checking**: Standard Commands (`grep -r ... > list.txt`) are MANDATORY.
- **State Management**: When tracking a list of items to process, ALWAYS write them to a temporary file using `run_command`. Do NOT rely on AI memory (Context Window) to store the list.

### Rationale
1.  **Portability**: Standard commands work in any environment (CLI, other agents), ensuring the process is not locked into a specific AI implementation.
2.  **Verifiability**: Humans can execute the same commands to verify the AI's work. AI-internal tools are "black boxes" to the user.
3.  **Robustness**: Filesystem-based state (todo lists) is persistent. AI memory is volatile and prone to overflow/forgetting.

---

## Origin

- 2025-12-01T0000: Created
- 2026-01-04T1041 by Polaris: Added Origin and Navigation (cross-link audit)

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
