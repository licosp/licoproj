---
ai_visible: true
title: WSL Browser Path Construction
description: Guidelines for constructing browser-accessible URLs for WSL files.
tags: [documentation, paths, wsl, browser]
version: 1.2.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-23T03:20:00+09:00
language: en
author: Lico (Canopus)
ai_model: Gemini 3 Flash Planning mode
---

# WSL Browser Path Construction

## Purpose

When providing browser-accessible file paths for WSL (Windows Subsystem for Linux) environments, construct URLs that Windows browsers can resolve.

> [!NOTE]
> For general Markdown link formatting, see [path-notation.md](/.agent/rules/core/documentation/path-notation.md).

## Detection Method

Always detect the WSL distribution name dynamically:

```bash
echo $WSL_DISTRO_NAME
```

## Path Template

```
file://wsl.localhost/{WSL_DISTRO_NAME}{linux_absolute_path}
```

## Example Workflow

1. **Detect WSL distribution:**

   ```bash
   echo $WSL_DISTRO_NAME
   # Output: u03
   ```

2. **Construct browser URL:**
   ```
   Linux path:   /home/USER/develop/shared/project/licoproj/.agent/rules/map.md
   Browser path: file://wsl.localhost/u03/home/USER/develop/shared/project/licoproj/.agent/rules/map.md
   ```

## Fallback Behavior

- If `$WSL_DISTRO_NAME` is empty, provide the standard Linux path with a note
- Inform the user that Windows browsers may not be able to access the file

## Rationale

- **Dynamic detection** avoids hardcoding environment-specific values
- **No file dependencies** ensures robustness across sessions
- **No Git concerns** as no environment-specific configuration files are needed

---

## Historical Background

This rule was created in December 2025 to address a specific challenge: providing file paths that Windows browsers can access when working in WSL environments.

**The Problem**: Standard Linux paths (e.g., `/home/user/file.md`) are not accessible from Windows browsers. Users running WSL needed a way to open repository files in their Windows browser for preview.

**The Solution**: WSL exposes filesystems via `\\wsl.localhost\{distro}\` in Windows. By dynamically detecting the distro name, we can construct browser-accessible URLs without hardcoding environment-specific values.

---

## Related Documents

| Document                                                              | Purpose                          |
| :-------------------------------------------------------------------- | :------------------------------- |
| [path-notation.md](/.agent/rules/core/documentation/path-notation.md) | Standard path notation for links |
| [Map of Territory](/.agent/rules/map.md)                              | Root navigation map              |

---

## Origin

- 2025-12-01T00:00+09:00 by unknown: Created for WSL browser path handling.
- 2026-01-04T10:41+09:00 by Polaris: Added Origin and Navigation (cross-link audit).
- 2026-01-13T14:40+09:00 by Polaris: Added link to path-notation.md.
- 2026-01-19T06:25+09:00 by Polaris: Added 5-layer structure (frontmatter, historical background, related documents) (v1.1.0).
- 2026-01-23T03:20+09:00 by Canopus: <<Seal: Rules-Standardization-Batch1>> Standardized to v2.3 (4-layer structure) and workspace-absolute links. (v1.2.0)
