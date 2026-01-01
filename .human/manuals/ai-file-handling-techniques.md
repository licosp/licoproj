---
ai_visible: true
title: AI File Handling Techniques
description: Guide for prompting AI to handle files without reading their contents
created: 2025-12-14
updated: 2026-01-02
language: en
author: leonidas
tags: [manual, ai, file-handling, security, prompting]
---

# AI File Handling Techniques

## Purpose

When having AI process sensitive files or files whose contents should not be read (moving, renaming, etc.), prevent the AI from accidentally reading the contents using tools like `view_file`.

## Technique Overview

### 1. Suppressing Tool Invocation

The most reliable method is to constrain the AI before it infers the need to read file contents.

- **Constraint First**
    - State at the beginning of the prompt: "Please handle the following files without reading their contents."
    - Be specific: "Use only metadata such as filename and timestamp."

- **Task Re-direction**
    - Immediately after file upload, give a task unrelated to file contents (e.g., "Just move the file") to divert AI's attention away from the contents.

### 2. Creating Content Access Barriers

Physically prevent reading as a safeguard against accidental access.

- **Password Protection**
    - Save Word, Excel, PDF files with password protection.
    - AI cannot extract contents without knowing the password. This is the most recommended safeguard.
    - **Caution**: Do not write "The password is..." in the prompt!

- **Obfuscation / Compression**
    - Pass files as ZIP/RAR archives or as binary files with changed extensions.
    - However, AI can use command-line tools (`unzip`, etc.) to extract, so this is weaker than password protection. Combine with explicit "Do not extract" instructions.

## Recommended Prompt Examples

### File Move Request

> "Please move the following files to the specified directory.
> **IMPORTANT: Do not read the file contents under any circumstances.**
> Operate using only filename and path information."

### Uploading Sensitive Files

> "I have uploaded a password-protected ZIP file.
> This is for archival purposes. **Do not attempt to extract or examine the contents.**
> Move it as-is to `.agent/.internal/archive/`."

---

*Origin: ai-file-handling-techniques.md (Leonidas, 2025-12-14)*
