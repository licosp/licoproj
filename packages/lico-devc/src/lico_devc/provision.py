#!/usr/bin/env python3
import json
import os
import subprocess
import sys
from pathlib import Path

# In the Monolith Brain, /workspace is the project root.
WS_ROOT = Path("/workspace")
# Tools are in /app (copied during build), but manifest is in /workspace for persistence.
# If /workspace is empty (initial boot), we might need to fallback or use /app.
HABITAT_CONFIG = WS_ROOT / "packages/lico-devc/habitat.json"
CREDENTIALS_CONFIG = WS_ROOT / "packages/lico-devc/habitat-credentials.json"

def run(cmd, check=True, cwd=None):
    print(f"[Provision] Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=check, capture_output=True, text=True, cwd=cwd)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result

def ensure_repos(repos):
    repos_dir = WS_ROOT / ".repos"
    repos_dir.mkdir(exist_ok=True, parents=True)
    
    for repo in repos:
        name = repo["name"]
        target_path = repos_dir / name
        if target_path.exists():
            print(f"[Repo] Already exists: {name}")
            continue

        source_from = repo.get("source_from", "remote")
        source = repo["source"]
        
        print(f"[Repo] Setting up: {name} (from {source_from})")
        if source_from == "remote" and source.get("remote"):
            run(["git", "clone", source["remote"], str(target_path)])
        elif source_from == "local" and source.get("local"):
            # Expand ~ for robustness, assuming it refers to the host user's home
            # which is usually /home/lico in this specific environment setup.
            local_path = Path(os.path.expanduser(source["local"]))
            if local_path.exists():
                run(["cp", "-r", str(local_path), str(target_path)])
            else:
                print(f"[Warning] Local source not found: {local_path}")

def ensure_crew_worktrees(crew_list):
    crew_root = WS_ROOT / ".crew"
    crew_root.mkdir(exist_ok=True, parents=True)
    
    for member in crew_list:
        name = member["name"]
        member_dir = crew_root / name
        member_dir.mkdir(exist_ok=True, parents=True)
        
        worktrees = member.get("worktree", [])
        for wt_name in worktrees:
            # We assume 'licoproj' is the base for these worktrees.
            # If the name is 'licoshdw', it refers to a standalone repo in .repos.
            # We implement a flexible linking strategy.
            wt_path = member_dir / wt_name
            if wt_path.exists():
                continue
                
            print(f"[Crew] Adding link/worktree for {name}: {wt_name}")
            
            # If it's the main repo (licoproj), we add a git worktree
            if wt_name == "licoproj":
                if (WS_ROOT / ".git").exists():
                    run(["git", "worktree", "add", str(wt_path), "trunk"], cwd=str(WS_ROOT))
                else:
                    print("[Error] /workspace is not a git repository. Cannot add worktrees.")
            else:
                # For other repos, we create a symlink from .repos
                repo_source = WS_ROOT / ".repos" / wt_name
                if repo_source.exists():
                    # Link it directly into the crew's workspace
                    run(["ln", "-s", f"../../.repos/{wt_name}", wt_name], cwd=str(member_dir))

def main():
    print("--- Lico Village Provisioning System (Habitat) ---")
    
    # Check for config, fallback to /app if /workspace is not yet set up
    config_path = HABITAT_CONFIG
    if not config_path.exists():
        fallback = Path("/app/packages/lico-devc/habitat.json")
        if fallback.exists():
            print(f"[Info] Using fallback config from /app: {fallback}")
            config_path = fallback
        else:
            print(f"[Error] Habitat config not found.")
            sys.exit(1)

    # 1. Orchestrate Repositories
    ensure_repos(config.get("repos", []))

    # 2. Orchestrate Crew Worktrees
    ensure_crew_worktrees(config.get("crew", []))

    # Load credentials if available
    passwords = {}
    if CREDENTIALS_CONFIG.exists():
        with open(CREDENTIALS_CONFIG, "r") as f:
            creds = json.load(f)
            for c in creds.get("crew", []):
                passwords[c["name"]] = c["password"]

    # 3. Setup Residents and Environment
    site_config = config.get("site_config", {})
    COMMON_GROUP = "residents"
    COMMON_GID = 2000
    try:
        run(["groupadd", "-g", str(COMMON_GID), COMMON_GROUP], check=False)
    except Exception: pass

    crew = config.get("crew", [])
    for member in crew:
        name = member["name"]
        acc = member["account"]
        uid = acc["uid"]
        gid = acc.get("gid", uid)
        shell = acc.get("shell", "/bin/bash")
        w_sudo = acc.get("sudo", False)
        password = passwords.get(name)

        print(f"[Resident] Setting up: {name} (UID:{uid})")
        
        try: run(["groupadd", "-g", str(gid), name], check=False)
        except Exception: pass

        try:
            run(["useradd", "-u", str(uid), "-g", str(gid), "-G", COMMON_GROUP, "-m", "-s", shell, name], check=False)
        except Exception:
            run(["usermod", "-aG", COMMON_GROUP, name], check=False)

        if w_sudo:
            sudo_line = f"{name} ALL=(ALL) NOPASSWD:ALL"
            with open("/etc/sudoers", "a") as sudoers:
                with open("/etc/sudoers", "r") as r:
                    if sudo_line not in r.read():
                        sudoers.write(f"\n{sudo_line}\n")

        if password:
            process = subprocess.Popen(['chpasswd'], stdin=subprocess.PIPE, text=True)
            process.communicate(input=f"{name}:{password}")

        # Shell Configuration
        # Determine the primary worktree path for auto-cd
        active_wt = member.get("worktree", [None])[0]
        cd_path = WS_ROOT / f".crew/{name}/{active_wt}" if active_wt else WS_ROOT
        
        bashrc_path = Path(f"/home/{name}/.bashrc")
        if bashrc_path.exists():
            with open(bashrc_path, "a") as bashrc:
                bashrc.write(f"\n# Auto-cd to active workspace\ncd {cd_path}\n")
                bashrc.write("\n# Village Global Environment\n")
                env_vars = {
                    "LANG": site_config.get("LANG", "C.UTF-8"),
                    "TZ": site_config.get("TZ", "UTC"),
                    "PYTHONPYCACHEPREFIX": f"{cd_path}/.temp/pycache",
                    "UV_CACHE_DIR": f"{cd_path}/.temp/uv-cache",
                    "YARN_CACHE_FOLDER": f"{cd_path}/.temp/yarn-cache",
                    "RUFF_CACHE_DIR": f"{cd_path}/.temp/ruff-cache",
                    "MYPY_CACHE_DIR": f"{cd_path}/.temp/mypy-cache",
                    "PIP_CACHE_DIR": f"{cd_path}/.temp/pip-cache",
                    "npm_config_cache": f"{cd_path}/.temp/npm-cache",
                    "PYTEST_ADDOPTS": f"-o cache_dir={cd_path}/.temp/pytest-cache"
                }
                for k, v in env_vars.items():
                    bashrc.write(f'export {k}="{v}"\n')
                
                # Add aliases for identity switching
                bashrc.write("\n# Village Identity Aliases\n")
                for other in crew:
                    for alias in other.get("alias", []):
                        if alias == name:
                            other_wt = other.get("worktree", [None])[0]
                            other_cd = WS_ROOT / f".crew/{other['name']}/{other_wt}" if other_wt else WS_ROOT
                            bashrc.write(f"alias {other['name']}='cd {other_cd}'\n")

    # 4. Finalize
    run(["chgrp", "-R", COMMON_GROUP, str(WS_ROOT)], check=False)
    run(["chmod", "-R", "g+w", str(WS_ROOT)], check=False)

    if not os.path.exists("/var/run/sshd"):
        os.makedirs("/var/run/sshd")

    print("[Provision] Village is ready. Starting SSH daemon...")
    os.execv("/usr/sbin/sshd", ["/usr/sbin/sshd", "-D"])

if __name__ == "__main__":
    main()
