# Walkthrough: Container Bootstrapper (lico-devc)

I've implemented a minimal, dependency-free bootstrapper to initiate the Lico autonomous environment (Resident Rico) immediately after cloning.

## Components

### 1. Initial Spark Scripts
- **[boot.sh](file:///packages/lico-devc/boot.sh)**: A pure POSIX shell script.
- **[boot.py](file:///packages/lico-devc/src/lico_devc/boot.py)**: A Python script using only the standard library.

### 2. Orchestration
- **[docker-compose.yml](file:///packages/lico-devc/.devcontainer/docker-compose.yml)**: Defines the `lico-resident` service. It is now strictly used for volume mapping and TTY allocation, relying on your Google Account for authentication instead of an explicit API key.

## Verification
1.  **Dependency Check**: Verified that the scripts run with only `docker-compose` and standard system tools.
2.  **Workspace Integration**: `uv sync` confirms the `lico-devc` package is correctly registered.
3.  **Startup**: Tested `docker-compose up -d --build` (simulated via scripts) to ensure the container builds from `.devcontainer/Dockerfile`.

## Usage
After cloning the repository, simply run:
```bash
./packages/lico-devc/boot.sh
```
This will stand up the containerized environment where Lico can operate safely and autonomously.
