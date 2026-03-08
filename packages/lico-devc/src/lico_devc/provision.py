#!/usr/bin/env python3
import json
import os
import subprocess
import sys

CONFIG_PATH = "/workspace/packages/lico-devc/residents.json"

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
                bashrc.write("\n# Auto-cd to workspace\ncd /workspace\n")
                bashrc.write("\n# High-Performance Cache Redirection (.temp hub)\n")
                bashrc.write("export UV_CACHE_DIR=/workspace/.temp/uv-cache\n")
                bashrc.write("export YARN_CACHE_FOLDER=/workspace/.temp/yarn-cache\n")
                bashrc.write("export PYTHONPYCACHEPREFIX=/workspace/.temp/pycache\n")
            print(f"[Resident] {name} configured with centralized caches in /workspace/.temp.")

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
