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
    # Git related messages (lico-git)
    GIT=SimpleNamespace(
        SYNC_START="Workspace synchronization starting (WSL <-> Windows)...",
        SYNC_SUCCESS="Sync completed successfully.",
        SYNC_FAILURE="Sync failed: {error}",
        ALREADY_ON_BRANCH="Already on {branch}. Nothing to sync.",
        CLEAN_START="Cleaning workspace...",
        STEP_0_RESET="Step 0: Resetting staging area...",
        STEP_1_STAGING="Step 1: Staging configured sync targets...",
        STEP_2_COMMIT="Step 2: Committing changes to local branch...",
        STEP_3_PUSH="Step 3: Pushing {branch} to origin...",
        STEP_4_MERGE="Step 4: Merging into {branch}...",
        STEP_5_RETURN="Step 5: Returning to {branch}...",
        STEP_6_CRLF="Step 6: Enforcing CRLF line endings on Windows worktree...",
        STEP_7_FORCE_SYNC="Step 7: Force-syncing {dest} to {hub} at {path}...",
        NO_CHANGES="No changes to commit. Skipping commit/push steps.",
        ERR_NO_BRANCH="Error: Could not determine current branch.",
        ERR_WIN_PATH_NOT_FOUND="Error: Windows worktree path not found: {path}",
    ),
    # Launcher related messages (lico-operate)
    APP=SimpleNamespace(
        STARTING="Starting application: {label}",
        STOPPING="Stopping application: {label}",
        WAITING="Waiting for application state [{sec}s]...",
        STATUS_RUNNING="Application is running.",
        STATUS_STOPPED="Application is stopped.",
        PROCESS_DETAILS="Process details: {line}",
        TERM_SUCCESS="Termination command sent successfully.",
        TERM_WARN="Termination command returned status {code}: {msg}",
        ERR_START_CMD_EMPTY="Error: Application start command is empty.",
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
    # Dependency related messages (lico-deps)
    DEPS=SimpleNamespace(
        START="--- Starting LicoTor Dependency Sync ---",
        PY_SYNC="[1/2] Syncing Python dependencies (uv sync)...",
        NODE_DETECTED="[2/2] package.json detected. Syncing Node dependencies...",
        NODE_SKIP="[2/2] No package.json detected. Skipping Node.",
        SUCCESS="Dependency synchronization completed successfully.",
    ),
    # Orchestrator related messages (lico-sync)
    SYNC=SimpleNamespace(
        START="=== Starting Full Modular LicoTor Synchronization ===",
        WIN_DEPS="--- Syncing Windows dependencies ---",
        TRIGGER_WIN_DEPS="Triggering Windows uv.exe to run 'lico-deps-sync'...",
        SUCCESS="Full modular synchronization completed successfully!",
        WARN_UV_NOT_FOUND="Warning: Windows uv.exe not found. Skipping dependency sync.",
    ),
    # Vision related messages (lico-vision)
    VISION=SimpleNamespace(
        PS_EXEC="Executing PowerShell from {dir}",
        CAP_SUCCESS="Captured screenshot available at {path}",
        CAPTURE_DETAIL="Capture success: {stdout}",
        CAP_FAIL="Capture failed (status {code}): {error}",
        ERR_IMG_NOT_FOUND="Screenshot file not found at {path}",
        ERR_OCR_FAIL="Observation failed",
        REGION_INFO="Region [{name}]: {text}",
        ERR_CAPTURE="Failed to capture screen: {error}",
        ERR_READ="Could not read image at {path}",
    ),
)
