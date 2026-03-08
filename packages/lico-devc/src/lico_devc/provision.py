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

    for resident in config.get("residents", []):
        name = resident["name"]
        uid = resident["uid"]
        gid = resident.get("gid", uid)
        shell = resident.get("shell", "/bin/bash")
        w_sudo = resident.get("sudo", False)
        password = resident.get("password")

        print(f"[Resident] Setting up: {name} (UID:{uid})")

        # 1. Create Group
        try:
            run(["groupadd", "-g", str(gid), name], check=False)
        except Exception:
            pass

        # 2. Create User
        try:
            run([
                "useradd", 
                "-u", str(uid), 
                "-g", str(gid), 
                "-m", 
                "-s", shell, 
                name
            ], check=False)
        except Exception:
            pass

        # 3. Sudo Privileges
        if w_sudo:
            sudo_line = f"{name} ALL=(ALL) NOPASSWD:ALL"
            with open("/etc/sudoers", "a") as sudoers:
                sudoers.write(f"\n{sudo_line}\n")
            print(f"[Resident] {name} granted sudo privileges.")

        # 4. Password (for SSH)
        if password:
            process = subprocess.Popen(['chpasswd'], stdin=subprocess.PIPE, text=True)
            process.communicate(input=f"{name}:{password}")
            print(f"[Resident] Password set for {name}.")

    # 5. Global SSH Setup (Ensure directory exists)
    if not os.path.exists("/var/run/sshd"):
        os.makedirs("/var/run/sshd")

    print("[Provision] Setup complete. Starting SSH daemon...")
    # Exec into sshd so it becomes PID 1
    os.execv("/usr/sbin/sshd", ["/usr/sbin/sshd", "-D"])

if __name__ == "__main__":
    main()
