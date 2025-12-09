---
description: Proposal for sanitizing IDE-specific file protocols in external content
created: 2025-11-30T20:06:53+09:00
status: proposal
category: security-and-portability
---

# IDE Protocol Sanitization for External Content

## Summary
NEVER expose IDE-specific file protocols (e.g., `cci:7://file:///`, `vscode://file/`, etc.) in external-facing content. Always convert to relative paths before publishing to GitHub issues, PRs, or commits.

## Problem

### What is `cci:7://file:///`?
- **`cci:7://`**: Cursor editor's internal file protocol
- **`file:///`**: Standard file URI scheme
- **Combined**: Forms an IDE-specific absolute file path reference

### Example of the Problem
```
❌ See cci:7://file:///home/leonidas/develop/shared/project/licoproj/.agent/rules/README.md
✅ See `.agent/rules/README.md`
```

### Why This Happens
AI receives file references from the IDE in the form of URIs:
- Internally useful for navigation within the editor
- **NOT suitable for external consumption**

When generating GitHub content, the AI may accidentally output these internal URIs without sanitization.

## Security & Privacy Risks

**Even worse than plain absolute paths:**
1. **Reveals username**: `/home/leonidas/...`
2. **Reveals directory structure**: `.../develop/shared/project/...`
3. **Reveals IDE choice**: `cci:7://` → using Cursor
4. **Non-portable**: Links are broken for anyone else
5. **Non-clickable**: GitHub doesn't recognize `cci:7://` protocol

## Rules

### Detection Patterns

**Common IDE protocols to sanitize:**
- `cci:7://file:///` (Cursor)
- `vscode://file/` (VS Code)
- `file:///` (generic file URI)
- `vscode-remote://` (VS Code Remote)

### Sanitization Algorithm

```
Input:  cci:7://file:///home/leonidas/develop/shared/project/licoproj/.agent/rules/README.md
Step 1: Remove protocol → /home/leonidas/develop/shared/project/licoproj/.agent/rules/README.md
Step 2: Extract relative path → .agent/rules/README.md
Step 3: Format as markdown code → `.agent/rules/README.md`
Output: `.agent/rules/README.md`
```

### Conversion Examples

| ❌ Internal URI | ✅ Relative Path |
|----------------|------------------|
| `cci:7://file:///home/user/repo/src/main.js` | `src/main.js` |
| `vscode://file//home/user/repo/README.md` | `README.md` |
| `file:///home/user/repo/.agent/rules/core/identity.md` | `.agent/rules/core/identity.md` |

## Implementation

### Pre-Publish Check
Before generating GitHub content (issue comments, PR descriptions), run:

```javascript
function sanitizePath(text) {
  // Remove IDE protocols
  let cleaned = text.replace(/cci:\d+:\/\/file:\/\/|vscode:\/\/file\/|file:\/\/\//g, '');
  
  // Extract relative path from absolute path
  const repoRoot = '/home/leonidas/develop/shared/project/licoproj/';
  if (cleaned.includes(repoRoot)) {
    cleaned = cleaned.replace(repoRoot, '');
  }
  
  // Remove other absolute path prefixes
  cleaned = cleaned.replace(/^\/home\/[^/]+\/.*?licoproj\//, '');
  
  return cleaned;
}
```

### AI Self-Review Checklist
Before publishing to GitHub:
- [ ] No `cci:7://` protocols
- [ ] No `vscode://` protocols
- [ ] No `file:///` URIs
- [ ] All file references are relative paths
- [ ] All paths are wrapped in backticks

### Proposed Rule Location
Add to `.agent/rules/development/git-operations.md`:

```markdown
## Path Sanitization for External Content

Before publishing to GitHub (issues, PRs, commits):

**NEVER expose IDE protocols:**
- ❌ `cci:7://file:///...`
- ❌ `vscode://file/...`
- ❌ `file:///...`

**ALWAYS convert to relative paths:**
- ✅ `.agent/rules/README.md`
- ✅ `packages/licoimg/src/main.js`

**Algorithm:**
1. Detect IDE protocol prefix
2. Remove protocol and absolute path prefix
3. Extract relative path from repository root
4. Wrap in backticks for markdown
```

## Origin
This issue was identified by the user during Issue #8 development, noting that Lico occasionally generates GitHub comments containing `cci:7://file:///home/***/***/' paths.

Quote from user:
> "リコが生成するイシューやPRのコメント生成時にたまに見かけます"
> (I sometimes see this when Lico generates issue or PR comments)

## Impact
- **High security**: Prevents username and path leakage
- **High usability**: GitHub links become clickable and portable
- **Medium complexity**: Requires pattern matching and string manipulation
- **Scope**: All GitHub-facing content (issues, PRs, commits)

## Related Proposals
- `absolute-path-prohibition_2025-11-30T19-58-07+09-00.md` (base principle)
