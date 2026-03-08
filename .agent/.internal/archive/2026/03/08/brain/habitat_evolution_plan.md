# Habitat Evolution: Unified Village Provisioning

## Concept
Migrate the static, user-only provisioning into a dynamic **World Manifest** system. This system will automate the setup of the entire Universe (repositories) and the Residents (crew) in a single loop.

## Proposed Changes

### [Component] lico-devc (Provisioning Engine)

#### [NEW] [habitat.json](file:///home/lico/develop/shared/project/licoproj/packages/lico-devc/habitat.json)
The definitive manifest for the Village structure.
- **`site_config`**: Regional settings (LANG, TZ).
- **`repos`**: List of repositories to ensure exist in `.repos/`.
  - Supports `remote` (URL) and `local` (Path) sources.
  - **`hidden`**: If true, treated as infrastructure/private memory (no-lint, background).
- **`crew`**: List of residents with account details and desired worktrees.
  - **`alias`**: List of names to generate shell aliases for identity switching.

#### [NEW] [habitat-credentials.json](file:///home/lico/develop/shared/project/licoproj/packages/lico-devc/habitat-credentials.json)
- **NOT tracked by Git** (add to `.gitignore`).
- Stores passwords for `crew` members.

#### [MODIFY] [provision.py](file:///home/lico/develop/shared/project/licoproj/packages/lico-devc/src/lico_devc/provision.py)
- **Repository Bootstrap**: Before creating users, ensure all repositories in `repos[]` are cloned into `/workspace/.repos/`.
- **Dynamic Crew Setup**:
  - Load accounts from `habitat.json`.
  - Merge passwords from `habitat-credentials.json`.
  - Create users and configure `.bashrc` with `auto-cd` and cache redirection.
- **Worktree Orchestration**:
  - Automatically run `git worktree add` for specified paths.
  - Setup visibility symlinks (e.g., `.repos` pointing back to the hub).

### [Component] Root Configuration

#### [MODIFY] [.gitignore](file:///home/lico/develop/shared/project/licoproj/.gitignore)
- Add `packages/lico-devc/habitat-credentials.json` to prevent accidental credential leakage.

## Verification Plan

### Automated Verification
- Run `provision.py` in a test environment.
- Check that `/workspace/.repos/` contains all cloned repositories.
- Check that `/workspace/.crew/<name>/` contains functional git worktrees.
- Verify environment variables via `env | grep LICO`.

### Manual Verification
- SSH login as `leonidas` and `iuria`.
- Confirm immediate placement in the correct worktree.
- Verify that `ls .repos/` inside a crew worktree shows the correct linked content.
