"""Centralized repository for log and UI messages."""

from types import SimpleNamespace


# Message Catalog
LicoMsg = SimpleNamespace(
    # General execution messages (lico-exec)
    EXEC=SimpleNamespace(
        START_RUN="Running command: {label} -> {cmd}",
        START_LAUNCH="Launching process: {label} -> {cmd}",
        CMD_SUCCESS="Command completed: {label}",
        CMD_FAILURE="Command failed [{code}]: {label}",
        PROCESS_STARTED="Asynchronous process started: {label} (PID: {pid})",
        ERR_OUTPUT="Error output: {stderr}",
    ),
    # Backup related messages (lico-backup)
    BACKUP=SimpleNamespace(
        START="Syncing full workspace: {src} -> {dest}",
        SUCCESS="Workspace backup complete.",
        ERR_SRC_NOT_FOUND="Error: Source directory {src} does not exist.",
        ERR_FAILED="Error during workspace backup: {error}",
    ),
    # Config related messages (lico-config)
    CONFIG=SimpleNamespace(
        LOAD_SUCCESS="Configuration loaded from: {path}",
        VALIDATION_ERROR="Invalid configuration: {error}",
        ERR_NOT_FOUND="Config file not found: {path}",
        ERR_APP_SECTION="Missing or invalid 'app' section",
        ERR_APP_SLEEP="Missing 'app.sleep'",
        ERR_APP_COMMANDS="'app.commands' must be a list",
        ERR_SYNC_SECTION="Missing or invalid 'sync' section",
        ERR_SYNC_BRANCH="Missing 'sync.branch' section",
        ERR_SYNC_TARGET="'sync.target' must be a list",
        ERR_WINDOWS_SECTION="Missing or invalid 'windows' section",
        ERR_PATH_ABSOLUTE="Path for '{key}' must be absolute: {path}",
        ERR_INVALID_TYPE="Invalid value type for '{key}' in windows section",
        ERR_STRUCT="Configuration structure error: {error}",
    ),
)
