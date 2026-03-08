# Issue 30: Village Provisioning System

Shift the "Logic" of environment setup (user creation, SSH configuration) from the static `Dockerfile` to a dynamic Python-based provisioning script.

## Proposed Changes

### 1. Configuration: [packages/lico-devc/residents.json](file:///home/lico/develop/shared/crew/iuria/licoproj/packages/lico-devc/residents.json) [NEW]

- Define identifiers and their OS-level requirements (UID, GID, Shell).
- Example structure:
  ```json
  {
    "residents": [
      { "name": "lico", "uid": 1001, "shell": "/bin/bash", "sudo": true },
      { "name": "sirius", "uid": 1002, "shell": "/bin/bash", "sudo": false }
    ]
  }
  ```

### 2. Logic: [packages/lico-devc/src/lico_devc/provision.py](file:///home/lico/develop/shared/crew/iuria/licoproj/packages/lico-devc/src/lico_devc/provision.py) [NEW]

- A Python script using standard libraries to:
  - Read `residents.json`.
  - Create users and groups if they don't exist.
  - Configure SSH access (passwd/keys).
  - Fix directory ownership for `/workspace`.
  - Execute the final CMD (e.g., `sshd -D`).

### 3. Cleanup: `Dockerfile` [packages/lico-devc/.devcontainer/Dockerfile](file:///home/lico/develop/shared/crew/iuria/licoproj/packages/lico-devc/.devcontainer/Dockerfile) [MODIFY]

- Remove Section 5 (User Configuration) and Section 6 (SSH Configuration).
- Set the default `CMD` to run `provision.py`.

### 4. Orchestration: `docker-compose.yml` [packages/lico-devc/.devcontainer/docker-compose.yml](file:///home/lico/develop/shared/crew/iuria/licoproj/packages/lico-devc/.devcontainer/docker-compose.yml) [MODIFY]

- Ensure the container environment has the necessary context to find `provision.py`.

## Verification Plan

### Automated Tests
- Rebuild the container and verify that `lico` and `sirius` users exist.
- Verify SSH connectivity for the new users.
- Check file ownership of `/workspace`.
