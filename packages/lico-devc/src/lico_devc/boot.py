#!/usr/bin/env python3
import subprocess
import sys

def main():
    """Start the lico-resident container using docker compose."""
    print("--- Lico Container Bootstrapper (Initial Spark) ---")
    
    # 1. Check for docker compose
    try:
        subprocess.run(["docker", "compose", "version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[Error] 'docker compose' command not found. Please install Docker Compose.")
        sys.exit(1)

    # 2. Safety Check: Host-side 'residents' group (GID 2000)
    # This ensures UID/GID consistency for file editing.
    try:
        import grp
        try:
            grp.getgrgid(2000)
        except KeyError:
            print("[Warning] Host-side 'residents' group (GID 2000) not found.")
            print("          To avoid permission issues, please run:")
            print("          sudo groupadd -g 2000 residents")
            print("          sudo usermod -aG residents $USER")
    except ImportError:
        # Fallback for systems where grp isn't available
        pass

    # 3. Up the container
    print("[Action] Starting lico-resident container...")
    try:
        # Use -d to detach, but -f to ensure we use the specific modular compose file
        compose_path = "packages/lico-devc/.devcontainer/docker-compose.yml"
        subprocess.run(["docker", "compose", "-f", compose_path, "up", "-d", "--build"], check=True)
        print("[Success] Container is running in the background.")
        print("[Status] Connect via VS Code (Dev Containers) or SSH.")
    except subprocess.CalledProcessError as e:
        print(f"[Error] Failed to start container: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
