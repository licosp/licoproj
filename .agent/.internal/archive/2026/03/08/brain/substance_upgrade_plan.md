# Issue 28: Resident Substance Upgrade

Provide the essential toolsets (Substance) to the `lico-resident` container to enable full autonomy and package management capabilities.

## Proposed Changes

### 1. `Dockerfile` [packages/lico-devc/.devcontainer/Dockerfile](file:///home/lico/develop/shared/crew/iuria/licoproj/packages/lico-devc/.devcontainer/Dockerfile)

- Install Docker CLI (for Docker-out-of-Docker via socket).
- Install Node.js and Yarn.
- Install OpenSSH Server (for direct VS Code attachment).
- Fix `uv` installation path and environment variables.

### 2. `docker-compose.yml` [packages/lico-devc/.devcontainer/docker-compose.yml](file:///home/lico/develop/shared/crew/iuria/licoproj/packages/lico-devc/.devcontainer/docker-compose.yml)

- Mount `/var/run/docker.sock` to enable Docker-out-of-Docker.
- Expose port 22 (mapped to a host port like 2222) for SSH access.

## Verification Plan

### Automated Tests
- Run `boot.sh` and verify versions of `git`, `docker`, `uv`, `yarn`, and `ssh` inside the container.
- Test `docker ps` inside the container to verify socket connectivity.
- Verify SSH service is running (`service ssh status`).
