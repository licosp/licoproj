#!/usr/bin/env python3
import json
import os
import subprocess
import sys

ACTIVE_REL = os.environ.get("LICO_ACTIVE_REL", "project/licoproj")
CONFIG_PATH = f"/workspace/{ACTIVE_REL}/packages/lico-devc/residents.json"

def run(cmd, check=True):
    print(f"[Provision] Executing: {' '.join(cmd)}")
    result = subprocess.run(cmd, check=check, capture_output=True, text=True)
    if result.stdout:
        print(result.stdout)
    if result.stderr:
        print(result.stderr, file=sys.stderr)
    return result

def main():
    print("--- Lico Village Provisioning System ---")
    
    if not os.path.exists(CONFIG_PATH):
        print(f"[Error] Config not found: {CONFIG_PATH}")
        # Fallback to starting sshd if possible, or exit
        sys.exit(1)

    with open(CONFIG_PATH, "r") as f:
        config = json.load(f)

    site_config = config.get("site_config", {})
    global_env = {
        "LANG": site_config.get("LANG", "C.UTF-8"),
        "TZ": site_config.get("TZ", "UTC"),
        "PYTHONPYCACHEPREFIX": f"/workspace/{ACTIVE_REL}/.temp/pycache",
        "UV_CACHE_DIR": f"/workspace/{ACTIVE_REL}/.temp/uv-cache",
        "YARN_CACHE_FOLDER": f"/workspace/{ACTIVE_REL}/.temp/yarn-cache",
        "RUFF_CACHE_DIR": f"/workspace/{ACTIVE_REL}/.temp/ruff-cache",
        "MYPY_CACHE_DIR": f"/workspace/{ACTIVE_REL}/.temp/mypy-cache",
        "PIP_CACHE_DIR": f"/workspace/{ACTIVE_REL}/.temp/pip-cache",
        "npm_config_cache": f"/workspace/{ACTIVE_REL}/.temp/npm-cache",
        "PYTEST_ADDOPTS": f"-o cache_dir=/workspace/{ACTIVE_REL}/.temp/pytest-cache"
    }

    # 0. Create Common Group (for shared resources)
    COMMON_GROUP = "residents"
    COMMON_GID = 2000
    try:
        run(["groupadd", "-g", str(COMMON_GID), COMMON_GROUP], check=False)
        print(f"[Provision] Common group '{COMMON_GROUP}' (GID:{COMMON_GID}) ensured.")
    except Exception:
        pass

    for resident in config.get("residents", []):
        name = resident["name"]
        uid = resident["uid"]
        gid = resident.get("gid", uid)
        shell = resident.get("shell", "/bin/bash")
        w_sudo = resident.get("sudo", False)
        password = resident.get("password")

        print(f"[Resident] Setting up: {name} (UID:{uid})")

        # 1. Create Individual Group
        try:
            run(["groupadd", "-g", str(gid), name], check=False)
        except Exception:
            pass

        # 2. Create User and Add to Common Group
        try:
            run([
                "useradd", 
                "-u", str(uid), 
                "-g", str(gid), 
                "-G", COMMON_GROUP,  # Add to residents group
                "-m", 
                "-s", shell, 
                name
            ], check=False)
        except Exception:
            # If user exists, ensure they are in the group
            run(["usermod", "-aG", COMMON_GROUP, name], check=False)

        # 3. Sudo Privileges
        if w_sudo:
            sudo_line = f"{name} ALL=(ALL) NOPASSWD:ALL"
            # Ensure we don't duplicate lines
            with open("/etc/sudoers", "r") as r:
                content = r.read()
            if sudo_line not in content:
                with open("/etc/sudoers", "a") as sudoers:
                    sudoers.write(f"\n{sudo_line}\n")
                print(f"[Resident] {name} granted sudo privileges.")

        # 4. Password (for SSH)
        if password:
            process = subprocess.Popen(['chpasswd'], stdin=subprocess.PIPE, text=True)
            process.communicate(input=f"{name}:{password}")
            print(f"[Resident] Password set for {name}.")

        # 5. Shell Enhancement: Auto-cd to /workspace
        bashrc_path = f"/home/{name}/.bashrc"
        if os.path.exists(bashrc_path):
            with open(bashrc_path, "a") as bashrc:
                bashrc.write(f"\n# Auto-cd to active workspace\ncd /workspace/{ACTIVE_REL}\n")
                bashrc.write("\n# Village Global Environment\n")
                for key, value in global_env.items():
                    bashrc.write(f'export {key}="{value}"\n')
            print(f"[Resident] {name} shell configured with global environment.")

    # 6. Shared Directory Permissions (Optional but recommended)
    # Ensure /workspace is group-writable by 'residents'
    run(["chgrp", "-R", COMMON_GROUP, "/workspace"], check=False)
    run(["chmod", "-R", "g+w", "/workspace"], check=False)
    print(f"[Provision] /workspace is now group-writable by '{COMMON_GROUP}'.")

    # 6. Global SSH Setup (Ensure directory exists)
    if not os.path.exists("/var/run/sshd"):
        os.makedirs("/var/run/sshd")

    print("[Provision] Setup complete. Starting SSH daemon...")
    # Exec into sshd so it becomes PID 1
    os.execv("/usr/sbin/sshd", ["/usr/sbin/sshd", "-D"])

if __name__ == "__main__":
    main()
