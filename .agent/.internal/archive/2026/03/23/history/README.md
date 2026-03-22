---
ai_visible: true
title: "History Directory"
description: "Monthly records of activity and shadow repository history."
tags: [history, activity, shadow, directory]
version: 1.0.0
created: 2026-03-20T23:40:00+09:00
updated: 2026-03-20T23:40:00+09:00
language: en
author: Lico (Polaris)
ai_model: Claude Opus 4.6 (Thinking) Planning mode
---

# History

Monthly records split from the former monolithic log files to reduce merge conflicts and improve manageability.

## Structure

```text
history/
├── activity/    # Identifier activities (Read/Write/Update/etc.)
│   ├── 2026-01-activity.md
│   ├── 2026-02-activity.md
│   └── 2026-03-activity.md
└── shadow/      # Shadow repository commit history
    └── 2026-02-shadow.md
```

## Conventions

- **Filename**: `YYYY-MM-activity.md` / `YYYY-MM-shadow.md`
- **New month**: Create a new file with the table header when the first entry of a new month is recorded.
- **Frozen months**: Past month files should not be modified except for corrections.

## Origin

- Migrated from `.agent/.internal/activity-log.md` and `.agent/.internal/shadow-history.md` on 2026-03-20 by Polaris.
- Reason: Merge conflict during trunk integration caused data loss in the monolithic activity log (1082 → 270 lines).
