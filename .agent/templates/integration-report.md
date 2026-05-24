# Federal Integration Log Template

Copy this template when posting the Weekly Routine summary to the GitHub Federal Integration Issue.

---

## Integration Summary: <YYYY-MM-DD>

**Reporting Identifier**: <your-identifier>
**Date**: <YYYY-MM-DDTHH:MM+TZ>
**Target Branch**: `trunk` -> `main`

### 1. High-Level Progress

- <Major accomplishment 1>
- <Major accomplishment 2>

### 2. Structural & Rules Changes

- <Significant rule update or architecture change>
- <None if not applicable>

### 3. Open Issues / Next Cycle Focus

- <Remaining problem or focus for next week>

### 4. Raw Commit Log

<details>
<summary>View commits since last integration</summary>

```text
<Paste output of: git log --oneline <last-integration-tag>..HEAD>
```

</details>
