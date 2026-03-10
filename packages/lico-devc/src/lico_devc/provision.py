#!/usr/bin/env python3
"""Lico Village Provisioning System (Habitat).

Handles user creation, worktree orchestration, and environment configuration
within the Resident Rico container.
"""

from __future__ import annotations

import json
import logging
import os
import subprocess
import sys
from contextlib import suppress
from pathlib import Path
from typing import cast

from .manifest import (
    CrewMember,
    EnvConfig,
    HabitatConfig,
    RepoConfig,
    load_habitat_config,
)

# In the Monolith Brain, /workspace is the Hub Root (e.g., shared/)
WS_ROOT = Path("/workspace")
# LICO_ACTIVE_REL points to the project root (e.g., project/licoproj)
ACTIVE_REL = os.environ.get("LICO_ACTIVE_REL", "")
ACTIVE_ROOT = WS_ROOT / ACTIVE_REL if ACTIVE_REL else WS_ROOT

# Manifest is in the active project, while tools are in /app.
HABITAT_CONFIG = ACTIVE_ROOT / "packages/lico-devc/habitat.json"
COMMON_GID = 2000
MIN_QUOTE_LEN = 2

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(message)s", stream=sys.stdout
)
logger = logging.getLogger(__name__)


def run(
    cmd: list[str], *, check: bool = True, cwd: str | Path | None = None
) -> subprocess.CompletedProcess[str]:
    """Execute a shell command with logging.

    Args:
        cmd: List of command arguments.
        check: If True, raises CalledProcessError on non-zero exit.
        cwd: Working directory for the command.

    Returns:
        The completed process object.
    """
    logger.info("[Provision] Executing: %s", " ".join(cmd))
    result = subprocess.run(
        cmd,
        check=check,
        capture_output=True,
        text=True,
        cwd=str(cwd) if cwd else None,
    )
    if result.stdout:
        logger.info(result.stdout.strip())
    if result.stderr:
        logger.error(result.stderr.strip())
    return result


def resolve_habitat_path(path_str: str | None) -> Path | None:
    """Translate habitat.json paths into container-centric paths.

    Args:
        path_str: The raw path string from configuration.

    Returns:
        A resolved Path object, or None if input is empty.
    """
    if not path_str:
        return None

    if path_str.startswith("~/develop/shared/"):
        return WS_ROOT / path_str.replace("~/develop/shared/", "")

    if path_str.startswith(("/", "~")):
        return Path(path_str).expanduser()

    # Monolith/Relative path
    return WS_ROOT / path_str


def _strip_quotes(value: str) -> str:
    """Remove surrounding quotes from a string.

    Args:
        value: The string to process.

    Returns:
        The string without surrounding quotes.
    """
    if len(value) >= MIN_QUOTE_LEN and (
        (value.startswith('"') and value.endswith('"'))
        or (value.startswith("'") and value.endswith("'"))
    ):
        return value[1:-1]
    return value


def _parse_env_line(line: str) -> tuple[str, str] | None:
    """Parse a single line from an .env file.

    Args:
        line: The raw line string.

    Returns:
        A tuple of (key, value) if parsed successfully, else None.
    """
    line = line.strip()
    if not line or line.startswith("#"):
        return None

    # Handle inline comments
    if " #" in line:
        line = line.split(" #", 1)[0].strip()

    if "=" in line:
        key, val = line.split("=", 1)
        return key.strip(), _strip_quotes(val.strip())
    return None


def parse_env_file(path: Path) -> dict[str, str]:
    """Parse .env files supporting comments and quotes.

    Args:
        path: Path to the .env file.

    Returns:
        A dictionary of environment variables.
    """
    env_data: dict[str, str] = {}
    if not path.exists():
        return env_data

    with path.open("r", encoding="utf-8") as f:
        for raw_line in f:
            parsed = _parse_env_line(raw_line)
            if parsed:
                key, val = parsed
                env_data[key] = val
    return env_data


def setup_single_repo(repo: RepoConfig, repos_dir: Path) -> None:
    """Setup a single repository.

    Args:
        repo: Repository configuration.
        repos_dir: Target directory for repositories.
    """
    name = repo["name"]
    target_path = repos_dir / name
    if target_path.exists():
        logger.info("[Repo] Already exists: %s", name)
        return

    source_from = repo.get("source_from", "remote")
    source = cast("dict[str, str]", repo.get("source", {}))

    logger.info("[Repo] Setting up: %s (from %s)", name, source_from)
    if source_from == "remote" and source.get("remote"):
        run(["git", "clone", source["remote"], str(target_path)])
    elif source_from == "local" and source.get("local"):
        local_path = resolve_habitat_path(source.get("local"))
        if local_path and local_path.exists():
            run(["cp", "-r", str(local_path), str(target_path)])
        else:
            logger.warning("[Warn] Local source not found: %s", name)


def ensure_repos(repos: list[RepoConfig]) -> None:
    """Orchestrate base repositories into .repos/.

    Args:
        repos: List of repository configurations.
    """
    repos_dir = WS_ROOT / ".repos"
    repos_dir.mkdir(exist_ok=True, parents=True)

    for repo in repos:
        setup_single_repo(repo, repos_dir)


def setup_worktree_for_member(
    member_name: str, member_dir: Path, wt_name: str
) -> None:
    """Add a git worktree or symlink for a specific crew member.

    Args:
        member_name: Name of the crew member.
        member_dir: Absolute path to the member's village directory.
        wt_name: Name of the worktree/repository to add.
    """
    wt_path = member_dir / wt_name
    if wt_path.exists():
        return

    logger.info("[Crew] Link/worktree %s: %s", member_name, wt_name)

    if wt_name in {"licoproj", "workspace"}:
        if (ACTIVE_ROOT / ".git").exists():
            run(
                ["git", "worktree", "add", str(wt_path), "trunk"],
                cwd=ACTIVE_ROOT,
            )
        else:
            logger.warning("[Warn] %s is not a git repo.", ACTIVE_ROOT)
    else:
        repo_source = WS_ROOT / ".repos" / wt_name
        if repo_source.exists():
            run(
                ["ln", "-s", f"../../.repos/{wt_name}", wt_name],
                cwd=member_dir,
            )
        else:
            logger.warning("[Warning] Repository %s not found.", wt_name)


def ensure_crew_worktrees(crew_list: list[CrewMember]) -> None:
    """Orchestrate worktrees and links for all residents.

    Args:
        crew_list: List of crew member configurations.
    """
    crew_root = WS_ROOT / ".crew"
    crew_root.mkdir(exist_ok=True, parents=True)

    for member in crew_list:
        name = member.get("name", "unknown")
        member_dir = crew_root / name
        member_dir.mkdir(exist_ok=True, parents=True)

        worktrees = member.get("worktree", [])
        for wt_name in worktrees:
            setup_worktree_for_member(name, member_dir, wt_name)


def load_env_meta_secrets(
    env_meta: EnvConfig,
    passwords: dict[str, str],
    site_secrets: dict[str, str],
) -> None:
    """Load secrets from env redirection.

    Args:
        env_meta: Environment metadata.
        passwords: Password dictionary to update.
        site_secrets: Secret dictionary to update.
    """
    env_path = resolve_habitat_path(env_meta.get("path"))
    if not (env_path and env_path.exists()):
        return

    logger.info("[Provision] Loading secrets: %s", env_path)
    raw_env = parse_env_file(env_path)
    # Using cast here because "env-keys" contains a dash
    keys_to_load = cast("list[str]", env_meta.get("env-keys", []))

    for k in keys_to_load:
        if k in raw_env:
            v = raw_env[k]
            site_secrets[k] = v
            if k.startswith("LICOPROJ_CREW_PASS_"):
                name = k.replace("LICOPROJ_CREW_PASS_", "").lower()
                passwords[name] = v


def load_legacy_secrets(
    passwords: dict[str, str], site_secrets: dict[str, str]
) -> None:
    """Load secrets from legacy JSON.

    Args:
        passwords: Password dictionary to update.
        site_secrets: Secret dictionary to update.
    """
    cred_p = WS_ROOT / "packages/lico-devc/habitat-credentials.json"
    if not cred_p.exists():
        return

    logger.info("[Provision] Loading secrets legacy vault: %s", cred_p)
    with cred_p.open("r", encoding="utf-8") as f:
        creds_data = cast("dict[str, object]", json.load(f))
        crew_creds = cast("list[dict[str, str]]", creds_data.get("crew", []))
        for c in crew_creds:
            passwords[c["name"]] = c["password"]
        site_secrets.update(
            cast("dict[str, str]", creds_data.get("secrets", {}))
        )


def load_village_secrets(
    config: HabitatConfig,
) -> tuple[dict[str, str], dict[str, str]]:
    """Load secrets from .env vault or legacy JSON.

    Args:
        config: The habitat configuration.

    Returns:
        A tuple of (passwords, site_secrets).
    """
    passwords: dict[str, str] = {}
    site_secrets: dict[str, str] = {}

    env_meta = config.get("env")
    if env_meta:
        load_env_meta_secrets(env_meta, passwords, site_secrets)

    if not passwords:
        load_legacy_secrets(passwords, site_secrets)

    return passwords, site_secrets


def configure_bashrc(
    name: str,
    member: CrewMember,
    site_config: dict[str, str],
    site_secrets: dict[str, str],
) -> None:
    """Configure .bashrc with environment variables and aliases.

    Args:
        name: Resident name.
        member: Resident config.
        site_config: Global site configuration.
        site_secrets: Loaded secrets.
    """
    wts = member.get("worktree", [])
    active_wt = wts[0] if wts else None
    cd_path = WS_ROOT / f".crew/{name}/{active_wt}" if active_wt else WS_ROOT
    bash_p = Path(f"/home/{name}/.bashrc")
    profile_p = Path(f"/home/{name}/.bash_profile")

    # Ensure .bash_profile exists and sources .bashrc for login parity
    if not profile_p.exists():
        with profile_p.open("w", encoding="utf-8") as profile:
            profile.write("# Village Login Profile\n")
            profile.write("if [ -f ~/.bashrc ]; then\n")
            profile.write("    . ~/.bashrc\n")
            profile.write("fi\n")

    if not bash_p.exists():
        return

    with bash_p.open("a", encoding="utf-8") as bashrc:
        bashrc.write("\n# Village Auto-Context Setup\n")
        bashrc.write("unset VIRTUAL_ENV\n")
        bashrc.write(f"cd {cd_path}\n")
        bashrc.write("\n# Village Global Environment\n")

        env_vars = {
            "LANG": site_config.get("LANG", "C.UTF-8"),
            "TZ": site_config.get("TZ", "UTC"),
        }
        env_vars.update(site_secrets)
        env_vars.update(
            {
                "PYTHONPYCACHEPREFIX": f"{cd_path}/.temp/cache/pycache",
                "PYRIGHT_PYTHON_CACHE_DIR": f"{cd_path}/.temp/cache/pyright",
                "UV_CACHE_DIR": f"{cd_path}/.temp/cache/uv",
                "YARN_CACHE_FOLDER": f"{cd_path}/.temp/cache/yarn",
                "RUFF_CACHE_DIR": f"{cd_path}/.temp/cache/ruff",
                "MYPY_CACHE_DIR": f"{cd_path}/.temp/cache/mypy",
                "PIP_CACHE_DIR": f"{cd_path}/.temp/cache/pip",
                "npm_config_cache": f"{cd_path}/.temp/cache/npm",
                "PYTEST_ADDOPTS": f"-o cache_dir={cd_path}/.temp/cache/pytest",
            }
        )

        for k, v in env_vars.items():
            bashrc.write(f'export {k}="{v}"\n')

        bashrc.write("\n# Village Identity Aliases\n")
        # Aliases will be added by setup_resident loop for others


def setup_resident(
    member: CrewMember,
    passwords: dict[str, str],
    common_group: str,
    context: dict[str, dict[str, str]],
) -> None:
    """Create a system user and configure their environment.

    Args:
        member: Crew member configuration.
        passwords: Loaded passwords.
        common_group: Name of the shared group.
        context: Context dictionary (crew, site_config, site_secrets).
    """
    name = member.get("name", "unknown")
    acc = member.get("account", {})
    uid = acc.get("uid", 0)
    gid = acc.get("gid", uid)
    shell = acc.get("shell", "/bin/bash")
    password = passwords.get(name, "lico")

    logger.info("[Resident] Setting up: %s (UID:%s)", name, uid)
    with suppress(Exception):
        run(["groupadd", "-g", str(gid), name], check=False)

    try:
        run(
            [
                "useradd",
                "-u",
                str(uid),
                "-g",
                str(gid),
                "-G",
                common_group,
                "-m",
                "-s",
                shell,
                name,
            ],
            check=False,
        )
    except Exception:  # noqa: BLE001
        run(["usermod", "-aG", common_group, name], check=False)

    if acc.get("sudo", False):
        sudo_line = f"{name} ALL=(ALL) NOPASSWD:ALL"
        sudoers_p = Path("/etc/sudoers")
        if sudo_line not in sudoers_p.read_text(encoding="utf-8"):
            with sudoers_p.open("a", encoding="utf-8") as f:
                f.write(f"\n{sudo_line}\n")

    # Set Password
    with subprocess.Popen(["chpasswd"], stdin=subprocess.PIPE, text=True) as p:
        p.communicate(input=f"{name}:{password}")

    configure_bashrc(
        name, member, context["site_config"], context["site_secrets"]
    )


def _check_host_gid() -> None:
    """Check if /workspace has the correct GID."""
    with suppress(Exception):
        ws_stat = WS_ROOT.stat()
        if ws_stat.st_gid != COMMON_GID:
            logger.warning("[Warn] Host GID %s mismatch.", ws_stat.st_gid)


def _add_crew_aliases(member_name: str, crew: list[CrewMember]) -> None:
    """Add aliases for other residents in .bashrc."""
    for other in crew:
        other_name = other.get("name", "unknown")
        if member_name in other.get("alias", []):
            other_wts = other.get("worktree", [])
            other_wt = other_wts[0] if other_wts else None
            other_cd = (
                WS_ROOT / f".crew/{other_name}/{other_wt}"
                if other_wt
                else WS_ROOT
            )
            bashrc_p = Path(f"/home/{member_name}/.bashrc")
            with bashrc_p.open("a", encoding="utf-8") as b:
                b.write(f"alias {other_name}='cd {other_cd}'\n")


def main() -> None:
    """Entry point for Village Provisioning."""
    logger.info("--- Lico Village Provisioning System (Habitat) ---")

    cfg_p = HABITAT_CONFIG
    if not cfg_p.exists():
        fallback = Path("/app/packages/lico-devc/habitat.json")
        if fallback.exists():
            cfg_p = fallback
        else:
            logger.error("[Error] Habitat config not found.")
            sys.exit(1)

    _check_host_gid()

    config = load_habitat_config(cfg_p)

    # 1. Orchestrate Village
    ensure_repos(config.get("repos", []))
    ensure_crew_worktrees(config.get("crew", []))

    # 2. Load Identity Vault
    passwords, site_secrets = load_village_secrets(config)

    # 3. Setup Residents
    common_group = "residents"
    with suppress(Exception):
        run(["groupadd", "-g", str(COMMON_GID), common_group], check=False)

    crew = config.get("crew", [])
    ctx = {
        "site_config": config.get("site_config", {}),
        "site_secrets": site_secrets,
    }
    for member in crew:
        setup_resident(member, passwords, common_group, ctx)
        _add_crew_aliases(member.get("name", "unknown"), crew)

    # 4. Finalize
    run(["chgrp", "-R", common_group, str(WS_ROOT)], check=False)
    run(["chmod", "-R", "g+w", str(WS_ROOT)], check=False)
    Path("/var/run/sshd").mkdir(exist_ok=True, parents=True)
    os.execv("/usr/sbin/sshd", ["/usr/sbin/sshd", "-D"])


if __name__ == "__main__":
    main()
