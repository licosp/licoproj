# Linter: Empty Directory (lico-lint-empty-dir)

Create a custom linter to identify and notify about empty directories within the project, helping maintain repository hygiene.

## Proposed Changes (TDD focused)

### [Test Infrastructure]

#### [NEW] [test_linter.py](file:///packages/lico-lint-empty-dir/tests/test_linter.py)
- **Scenarios**:
  - Detection of a truly empty directory.
  - Ignoring directories with files.
  - Ignoring directories with sub-directories.
  - Ignoring directories matching `exclude_dirs` (e.g., `.git`).

### [Liner Refactoring]

#### [MODIFY] [main.py](file:///packages/lico-lint-empty-dir/src/lico_lint_empty_dir/main.py)
- Refactor the procedural scan into a testable class or functional unit `EmptyDirLinter`.

### [Container Bootstrapper: lico-devc]

#### [NEW] [boot.sh](file:///packages/lico-devc/boot.sh)
- A pure POSIX shell script to call `docker-compose`.

#### [NEW] [boot.py](file:///packages/lico-devc/src/lico_devc/boot.py)
- A Python script using only the standard library (`subprocess`, `os`, `sys`) to manage the container lifecycle on the host.

#### [NEW] [docker-compose.yml](file:///packages/lico-devc/.devcontainer/docker-compose.yml)
- Define the `rico-resident` service mapping the project root to `/workspace`.

#### [NEW] [Dockerfile](file:///packages/lico-devc/.devcontainer/Dockerfile)
- Base: `python:3.12-slim-bookworm` (minimal).
- Tools: `uv` (core), `git` (management).
- Role: The "Clean Room" where Lico operates.

## Verification Plan (TDD)

1. **Red**: Run `uv run pytest packages/lico-lint-empty-dir/tests` -> Expect failure.
2. **Green**: Implement logic -> Expect pass.
3. **Refactor**: Polish code and verify again.
