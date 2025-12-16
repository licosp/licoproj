---
description: Protocols for deleting files safely using the '.trash' directory.
---

# File Deletion Protocol

## Summary
**NEVER use `rm` or `git rm` command for content files.**
Instead, **ALWAYS use `mv` to move files to the `.trash/` directory.**

## Rationale
AI agents (and humans) are prone to irreversible errors when using destructive commands (`rm`).
The `.trash/` directory serves as a **local safety net** (Limbo), allowing for recovery from:
- Hallucinations (deleting the wrong file)
- Impulsive decisions (deleting too early)
- Contextual misunderstandings

This aligns with the ["Trash Bin" concept in OS GUIs](../../core/user-adaptation.md), mitigating the risk of "Void Deletion".

## Rules

### 1. Default Action: Move to Trash
When you determine a file is "unnecessary" or "noise":

**❌ Forbidden:**
```bash
rm funny_pictures.md
git rm funny_pictures.md
```

**✅ Required:**
```bash
mv funny_pictures.md .trash/
# If the file was git-tracked, git will detect this as a deletion, which is fine.
# The file content is preserved locally in .trash/.
```

### 2. The `.trash` Directory
- **Location**: `/.trash/` (Root)
- **Status**: Git-ignored (locally preserved, but excluded from repo history).
- **Maintenance**: Empty only upon explicit user instruction or when disk space is critical.

### 3. Archives vs. Trash
Distinguish between "Historical Context" and "Noise":

| Type | Definition | Action | Destination |
|:---|:---|:---|:---|
| **Archive** | Valuable context, history, or reference. | Move | `.human/archive/` or `.agent/archive/` |
| **Trash** | Noise, temporary tests, mistakes, or "surely useless". | Move | `.trash/` |

### 4. Exceptions (Where `rm` is Allowed)
- **Automatic generated files**: Build artifacts (`dist/`, `build/`), caches (`__pycache__/`).
- **Temporary work files**: Explicitly created in `.agent/.internal/work/` for strict temporary use.

## References
- [maintenance.md](maintenance.md): Archival standards
- [git-operations.md](git-operations.md): Git status handling
