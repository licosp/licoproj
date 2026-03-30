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
        ARTIFACT_START="Syncing {src} -> {dest}",
        ARTIFACT_ERR="Error syncing {src}: {error}",
        ARTIFACT_SUCCESS="Artifact backup complete.",
    ),
    # Pipeline related messages (lico-pipeline)
    PIPELINE=SimpleNamespace(
        START="\n🚀 Starting Lico Pipeline ({mode} | {targets})...\n",
        TOOL_HEADER="--- {tool} ---",
        SEPARATOR="",
    ),
    # Shim related messages (lico-shim)
    SHIM=SimpleNamespace(
        BLOCKED_SHADOW="❌ [Shim] BLOCKED: Operating on .shadow/ from root is forbidden. cd first.",
        BLOCKED_RESTRICTED="❌ [Shim] BLOCKED: 'git {arg}' is restricted to prevent data loss.",
        BLOCKED_RESET_HARD="❌ [Shim] BLOCKED: 'git reset --hard' destroys history. Use --soft or bypass.",
        USAGE="Usage: lico-shim <command> [args...]",
        ERR_UNKNOWN="❌ [Shim] ERROR: Unknown shim command '{command}'.",
    ),
    # Lint related messages (lico-lint)
    LINT=SimpleNamespace(
        EMPTY_DIR_START="--- lico-lint-empty-dir Scan: {path} ---",
        EMPTY_DIR_FOUND="[Warning] Empty directory detected: {path}",
        EMPTY_DIR_ISSUE="--- Scan Complete: Issues found ---",
        EMPTY_DIR_NONE="--- Scan Complete: No empty directories found ---",
    ),
    # Environment management messages (lico-devc)
    DEVC=SimpleNamespace(
        BOOT_START="--- Lico Container Bootstrapper (Bare Spark) ---",
        ERR_ENV_MISMATCH="[Error] Environment Mismatch. Expected: {expected}, Actual: {actual}",
        WARN_CRED_MISSING="[Warning] Credentials Missing at {path}. Please ensure your Vault is active.",
        HUB_INFO="[Hub] Root: {root} | Active: {active}",
        SUCCESS_RUNNING="[Success] Container is running. Connect via VS Code/SSH.",
        PROVISION_START="--- Lico Village Provisioning System (Habitat) ---",
        REPO_ALREADY_EXISTS="[Repo] Already exists: {name}",
        REPO_SETUP="[Repo] Setting up: {name} (from {source})",
        WARN_LOCAL_SOURCE_NOT_FOUND="[Warn] Local source not found: {name}",
        CREW_LINK="[Crew] Link/worktree {member}: {name}",
        WARN_NOT_GIT_REPO="[Warn] {path} is not a git repo.",
        WARN_REPO_NOT_FOUND="[Warning] Repository {name} not found.",
        LOAD_SECRETS="[Provision] Loading secrets: {path}",
        RESIDENT_SETUP="[Resident] Setting up: {name} (UID:{uid})",
        WARN_GID_MISMATCH="[Warn] Host GID {gid} mismatch.",
        ERR_HABITAT_NOT_FOUND="[Error] Habitat config not found.",
        ERR_START_FAILED="[Error] Failed to start container",
        ERR_BOOT_FATAL="[Fatal] Unexpected error",

        PROVISION_EXEC="[Provision] Executing: {cmd}",
        LOAD_LEGACY_SECRETS="[Provision] Loading secrets legacy vault: {path}",

    ),
    # Memory related messages (lico-memory)
    MEMORY=SimpleNamespace(
        FILTER_START="Scanning memory files from: {path}",
        FILTER_SCANNING="Reading: {file}",
        FILTER_SUMMARY_HEADER="--- Extraction Summary ---",
        FILTER_QUOTA="Target Quota: Stage1={s1}, Stage2={s2}",
        FILTER_ACTUAL_COLLECTED="Actually Collected: Stage1={s1}, Stage2={s2}",
        FILTER_FOUND="Found {count} message objects.",
        FILTER_FILES_ACCESSED="Files accessed (newest to oldest):",
        FILTER_FILE_ENTRY="  - {file}",
        FILTER_OLDEST_TIMESTAMP="Oldest extracted line timestamp: {ts}",
        FILTER_TOTAL_TURNS="Total extracted turns: {count}",
        FILTER_SAVED="Saved filtered JSONL to: {path}",
        BACKUP_START="Starting memory backup from {path}...",
        BACKUP_JSON_ERROR="Error: Failed to parse JSON: {error}",
        BACKUP_STRUCT_ERROR="Error: Unknown JSON root structure.",
        BACKUP_NO_MSG="No messages found in JSON.",
        BACKUP_ENTRY="  - {id} ({ts})",
        PACK_SUMMARY_HEADER="--- Packaging Summary ---",
        PACK_COUNT="Messages packed: {count}",
        PACK_SESSION_ID="New Session ID: {id}",
        PACK_BASE_ID="Base Session ID: {id}",
        PACK_SUMMARY_TEXT="Summary generated: {text}",
        PACK_SIZE="Final JSON Size: {size} bytes",
        PACK_SAVED="Saved to: {path}",
        ERR_NOT_FOUND="Error: File not found: {path}",
        ERR_INVALID_JSON="Warning: Failed to parse line in {path}: {error}",
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
