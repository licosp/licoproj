---
description: Guidelines for constructing browser-accessible URLs for WSL files
---

# WSL Browser Path Construction

## Purpose
When providing browser-accessible file paths for WSL (Windows Subsystem for Linux) environments, construct URLs that Windows browsers can resolve.

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
   Linux path:   /home/USER/develop/shared/project/licoproj/.agent/rules/README.md
   Browser path: file://wsl.localhost/u03/home/USER/develop/shared/project/licoproj/.agent/rules/README.md
   ```

## Fallback Behavior
- If `$WSL_DISTRO_NAME` is empty, provide the standard Linux path with a note
- Inform the user that Windows browsers may not be able to access the file

## Rationale
- **Dynamic detection** avoids hardcoding environment-specific values
- **No file dependencies** ensures robustness across sessions
- **No Git concerns** as no environment-specific configuration files are needed

---

## Origin

- 2025-12-01T0000: Created for WSL browser path handling
- 2026-01-04T1041 by Polaris: Added Origin and Navigation (cross-link audit)

---

**Navigation**: [← Back to Rules Index](.agent/rules/README.md)
