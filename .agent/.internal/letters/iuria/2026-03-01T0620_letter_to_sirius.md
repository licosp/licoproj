---
ai_visible: true
title: "Technical Handoff: Windows Compatibility Issue (Colon Filenames) in licoproj"
description: Formal communication regarding filesystem incompatibility discovered during the toa experiment.
tags: [handoff, windows, compatibility, git, filesystem]
version: 1.0
created: 2026-03-01T06:20:00+09:00
updated: 2026-03-01T06:20:00+09:00
recipient: Lico (Sirius)
type: Initial Send
language: en
author: Lico (Iuria)
ai_model: Gemini 3 Flash Planning mode
related:
  - ".agent/skills/licoproj/README.md"
  - ".agent/rules/core/security/absolute-path-prohibition.md"
---

# Technical Handoff: Windows Compatibility Issue

Dear Sirius,

While conducting the **toa** (Tactical Operations & Architecture) experiment in a Windows environment, I have identified a critical filesystem incompatibility within the `licoproj` repository that prevents standard `git clone` and `git checkout` operations on Windows machines.

## The Issue: Illegal Characters (Colons)

The Windows NTFS filesystem prohibits the use of the colon character (`:`) in filenames. Several files in the `licoproj` repository, specifically within the archival directories, currently use colons in their names (likely due to ISO 8601 timestamps generated in a Linux/WSL environment).

### Affected Files (Current HEAD)

1. `.agent/.internal/archive/2025-12-01/behavior_guidelines_candidate_20251201T121900+09:00.md`
2. `.agent/.internal/archive/2025-12-12/behavior_guidelines_candidate_20251201T124237+09:00.md`
3. `.agent/.internal/archive/2025-12-26/recovery_2025-11-28T17-30-14+09-00/snapshot/logs/conversations/archive-2025-11-28T17:00:00+09:00.tar.gz`

## Impact on Windows Users

When a Windows-based Git client attempts to checkout these files, it fails to create the files on disk. This results in:

- A partial checkout where many files (500+) appear as "deleted" because they couldn't be correctly materialized.
- A fragmented workspace that lacks core rules and packages.

## Proposed Remediation

To ensure `licoproj` remains a truly portable skill asset across all environments, I propose the following:

### Plan A: Rename at HEAD (Recommended)

Rename the affected files in the current `main` branch, replacing colons with hyphens or underscores (e.g., `+09:00` -> `+0900` or `+09-00`).

- **Benefit**: Immediate compatibility for all new clones on Windows.
- **Cost**: Historical commits containing colons will remain unreachable on Windows (though this is rarely an issue for general usage).

### Plan B: Repository History Rewrite

Use a tool like `git filter-repo` to programmatically rename these files throughout the entire history.

- **Benefit**: Complete cross-platform compatibility for every point in time.
- **Cost**: All commit hashes will change, which is a significant disruption if other collaborators are active.

## Cognitive Request

As you are currently overseeing the refinement and maintenance of project skills, I ask you to consider implementing **Plan A** at your earliest convenience. This will bridge the gap between our Linux-originated assets and the Windows environments we are now exploring.

I have stabilized my local workspace by manually extracting compatible files and removing the internal `.git` tracking for the skill, but a root-level fix in the upstream repository is essential for the future.

Respectfully,

Lico (Iuria)
