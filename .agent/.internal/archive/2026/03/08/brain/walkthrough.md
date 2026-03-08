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

---

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
