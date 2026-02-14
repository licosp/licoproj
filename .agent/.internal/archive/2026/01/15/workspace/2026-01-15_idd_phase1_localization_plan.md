# Localization Plan: IDD Phase 1 & 3

Standardize the root operational procedures into English while preserving functional Japanese triggers, conforming to Lico documentation standards.

## Objectives
- Port `idd-phase1-init.md` and `idd-phase3-fini.md` contents to English.
- Preserve specific Japanese terms for triggers (STOP conditions).
- Ensure conformity with `header-frontmatter.yaml` and `documentation-standards.md`.
- Integrate 'Step 0: Alignment' (Ritual) into workflows.
- Add environment variable cleanup (`unset`).

## Proposed Changes

### [Standardized] [idd-phase1-init.md](/.agent/workflows/idd-phase1-init.md)
- Full frontmatter, Step 0 ritual, localized troubleshooting, and environment cleanup.
- Standardized `Origin` and `Navigation`.

### [Standardized] [idd-phase3-fini.md](/.agent/workflows/idd-phase3-fini.md)
- Full frontmatter, Step 0 ritual, localized safety warnings (Stash/Merge), and environment cleanup.
- Standardized `Origin` and `Navigation`.

### [ARCHIVE]
- Original versions moved to `.agent/.internal/archive/2026-01-15/workflows/`.

## Verification Results
- [x] Zero absolute paths in workflows.
- [x] Root-relative link format verified.
- [x] Japanese STOP conditions present as safety valves.
- [x] Frontmatter keys and `Origin` date format standardized.
