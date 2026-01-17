---
ai_visible: true
version: 1.3
created: 2025-12-02T19:40:00+09:00
updated: 2026-01-17T15:45:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# Auto‑Front‑Matter on File Save (Metadata‑Aware)

## Scope

- **Target Files**:
  - Text files where **YAML front‑matter** is recognized as metadata (e.g., `.md`, `.markdown`, `.mdx`).
  - Other text files (e.g., `.txt`, `.py`, `.js`) are **excluded** unless they support YAML front-matter.
- **Excluded**: Binary files, images, videos, or files with extensions not listed above.

## Behaviour

1. **Detect Save Intent**
   - When the user explicitly asks to save content to a file (e.g., `save this as notes.md`), Lico treats this as a _save_ operation.

2. **Load Header Template**
   - Read `.agent/templates/header-frontmatter.yaml` (relative to workspace root).
   - Extract the YAML front‑matter block (the lines between the first `---` and the second `---`).
   - **Instance Identifier**: Ensure `instance_id` is preserved or auto-filled as per [instance-identifier.md](/.agent/rules/core/instance-identifier.md).

3. **Check Existing Front‑Matter**
   - Check if the target file already starts with a `---` block.
   - **None** → Prepend the template.
   - **Exists** → Merge (add missing keys only; do not overwrite existing values).

4. **Time Format**
   - For `created` and `updated` fields, use **ISO 8601 format** with **Japan Standard Time (JST)**.
   - Format: `YYYY-MM-DDTHH:mm:ss+09:00`

5. **Write File**
   - Use `replace_file_content` to write the new front‑matter + content as a single contiguous block.

6. **Commit (optional)**
   - If the user requests a commit, commit the staged changes with `git commit -m "<Identifier>: [Context-ID] docs: add auto front‑matter (Done)"`. No need to read the file content.

## Exceptions

- Skip if the user explicitly says "No header" or "Do not add front matter".
- Skip for binary files.

## Rationale

- **Consistency**: Ensures all Markdown files have uniform metadata for search and CI tools.
- **Efficiency**: Uses `git diff` to avoid reading full file contents, saving tokens.
- **Privacy**: Reads only metadata/diffs, avoiding unnecessary access to sensitive content.
- **Traceability**: `instance_id` allows tracking which AI personality created the file.

## Versioning

- **Introduced:** 2025‑12‑02
- **Last reviewed:** 2025‑12‑12 (Updated for Instance Identifier)

## Related Documents

- [instance-identifier.md](/.agent/rules/core/instance-identifier.md)
- [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md)

---

## Origin

- 2025-12-01T0000: Created
- 2025-12-02T1940: by Sirius: Updated
- 2026-01-17T1535 by Canopus: Updated commit message example to align with "Identifier-First" protocol (v1.2).

---

**Navigation**: [← Back to Rules Index](/.agent/rules/README.md)
