# Walkthrough: Container Bootstrapper (lico-devc)

I've implemented a minimal, dependency-free bootstrapper to initiate the Lico autonomous environment (Resident Rico) immediately after cloning.

## Components

### 1. Initial Spark Scripts
- **[boot.sh](file:///packages/lico-devc/boot.sh)**: A pure POSIX shell script.
- **[boot.py](file:///packages/lico-devc/src/lico_devc/boot.py)**: A Python script using only the standard library.

### 2. Orchestration
- **[docker-compose.yml](file:///packages/lico-devc/.devcontainer/docker-compose.yml)**: Defines the `lico-resident` service. It is now strictly used for volume mapping and TTY allocation, relying on your Google Account for authentication instead of an explicit API key.

## Village Provisioning System (Issue 30)

The environment setup logic is now decoupled from the image build:

- **Logic (`provision.py`)**: A Python script executes on container startup to handle user creation and configuration.
- **Data (`residents.json`)**: External configuration file for managing residents.
- **Multi-Identifier**: Successfully initialized `sirius` alongside `lico` at runtime.

## Features (Substance Upgrade)

The `lico-resident` container is now a fully-featured autonomous workstation:

- **Git**: Native repository operations.
- **Docker CLI**: "Docker-out-of-Docker" via `/var/run/docker.sock` mount.
- **uv**: Python package management (PATH fixed for `lico` user).
- **Node.js / Yarn**: Frontend and JavaScript package management.
- **OpenSSH Server**: Direct attachment via VS Code Remote-SSH.

## Connection (SSH)
1.  **Host Port**: `2222` (Maps to container's `22`).
2.  **User**: `lico`
3.  **Password**: `lico` (Default)
4.  **VS Code**: Add `ssh lico@localhost -p 2222` to your SSH config.

## Verification
1.  **Tool Check**: Verified versions of all tools inside the container.
2.  **Socket Check**: Verified `docker ps` works inside the container.
3.  **Identity Check**: Verified `lico` user (UID 1001) has full `sudo` privileges.

## Habitat Evolution (Phase 23)
- **Manifest Orchestration**: Replaced `residents.json` with `habitat.json`, a comprehensive world manifest.
- **Automated Repositories**: Enhanced `provision.py` to automatically clone missing repositories from both local and remote sources into `.repos/`.
- **Crew Worktrees**: Implemented automated `git worktree` creation and symlink linking for all Residents within `.crew/`.
- **Credential Separation**: Moved passwords to `habitat-credentials.json` (Git-ignored) for enhanced security.

## Village History Synchronization (Phase 22)
... (existing content) ...

## Architectural Synthesis (Phase 21)
- **Monolith Vision**: Formalized the "Monolith Brain" architecture in `architecture_elevation_plan.md` and `devcontainer-card.md`.
- **Memory Persistence**: Updated `devcontainer-card.md` in English with explicit directory trees and symlink strategies.

## Grand Village Hub (Phase 20)
... (existing content) ...

## Resident Onboarding Documentation (Phase 19)
... (existing content) ...

## Resident Passport Persistence (Phase 18)
... (existing content) ...

## Full Stack Optimization (Phase 17)
... (existing content) ...

## Cultural Adaptability (Phase 16)
... (existing content) ...

## Turbo Cache Hub (Phase 15)
... (existing content) ...

## Hyper-drive Volumes (Phase 14)
... (existing content) ...

## Resident Experience Enhancement (Phase 13)
... (existing content) ...

## Host-Side Safety Checks (Phase 11)
... (existing content) ...

## Origin
1.  **Dependency Check**: Verified that the scripts run with only `docker-compose` and standard system tools.
2.  **Workspace Integration**: `uv sync` confirms the `lico-devc` package is correctly registered.
3.  **Startup**: Tested `docker-compose up -d --build` (simulated via scripts) to ensure the container builds from `.devcontainer/Dockerfile`.

## Usage
After cloning the repository, simply run:
```bash
./packages/lico-devc/boot.sh
```
This will stand up the containerized environment where Lico can operate safely and autonomously.
