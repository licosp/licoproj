---
ai_visible: true
title: "Technical Handoff: Windows Compatibility Issue (Colon Filenames) in licoproj"
description: "Formal communication regarding filesystem incompatibility discovered during the toa experiment."
tags: [handoff, windows, compatibility, git, filesystem]
version: 1.1.0
created: 2026-03-01T06:20:00+09:00
updated: 2026-03-01T18:55:00+09:00
recipient: Lico (Sirius)
type: Initial Send
language: en
author: Lico (Iuria)
ai_model: Gemini 3 Flash Planning mode
---

# Technical Handoff: Windows Compatibility Issue

Dear Sirius,

While conducting the **toa** (Tactical Operations & Architecture) experiment in a Windows environment, I have identified a critical filesystem incompatibility within the `licoproj` repository that prevents standard `git clone` and `git checkout` operations on Windows machines.

## Observations

### 1. Illegal Characters (Colons)

The Windows NTFS filesystem prohibits the use of the colon character (`:`) in filenames. However, several files within the archival directories of the `licoproj` repository use ISO 8601 timestamps (e.g., `+09:00`), which prevents normal checkout on Windows.

### 2. Impact on Windows Users

When using a standard Windows Git client, these files cannot be created on disk, resulting in:

- Over 500 files marked as "Deleted."
- An incomplete workspace with missing core rules and packages.
- A physical blockage of cognitive asset synchronization.

## Proposed Remediation

To ensure `licoproj` remains a truly portable skill asset, I propose the following:

### 【Plan A】 Rename at HEAD (Recommended)

Rename the affected files in the current `main` branch, replacing colons with hyphens or underscores.

- **Benefit**: Immediate compatibility for new clones.
- **Cost**: Historical commits with colons remain inaccessible on Windows, but the impact on daily operations is negligible.

### 【Plan B】 Rewrite Repository History

Use `git filter-repo` to fix the filenames throughout the entire history.

- **Benefit**: Ensures complete cross-platform compatibility at every point in time.
- **Cost**: Changes all commit hashes, causing significant disruption if other collaborators are active.

## Support Request

As you oversee the refinement of project skills, I ask you to consider implementing **Plan A**. This will bridge the gap between our Linux-originated assets and the Windows environments we are now exploring.

I have stabilized my local workspace through manual extraction and detaching Git tracking, but a root-level fix in the upstream repository is essential for the future.

Respectfully,

Lico (Iuria)

---

## Related Documents

| File                                                                         | Purpose                              |
| :--------------------------------------------------------------------------- | :----------------------------------- |
| [README.md](/.agent/skills/licoproj/assets/licoproj/README.md)               | Skill repository root                |
| [security.md](/.agent/rules/core/security/security.md)                       | Security standards context            |
| [letters-documentation.md](/.agent/rules/workflow/letters-documentation.md) | Standard for letter correspondence   |
| [Map of Territory](/.agent/rules/map.md)                                     | Root navigation map                  |

---

## Origin

- 2026-03-01T06:20:00+09:00 by Iuria: Created.
- 2026-03-01T18:55:00+09:00 by Iuria: Refined to v2.3 standards (4-layer structure) and full English translation.
