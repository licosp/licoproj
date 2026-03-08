import os
import subprocess
import sys

def find_hub_root():
    current = os.path.abspath(os.getcwd())
    while current != "/":
        dirs = os.listdir(current)
        if "project" in dirs and "crew" in dirs:
            return current
        current = os.path.dirname(current)
    # Fallback: assume 3 levels up from boot script's project root
    return os.path.abspath(os.path.join(os.getcwd(), "../../.."))

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

    # 3. Discover Hub Root and Active Rel Path
    # This allows us to mount the whole world while knowing where our project is
    hub_root = find_hub_root()
    active_rel_path = os.path.relpath(os.getcwd(), hub_root)
    print(f"[Hub] Root: {hub_root}")
    print(f"[Hub] Active: {active_rel_path}")

    # 4. Up the container
    print("[Action] Starting lico-resident container...")
    try:
        # Pass discovery variables to compose
        env = os.environ.copy()
        env["LICO_HUB_ROOT"] = hub_root
        env["LICO_ACTIVE_REL"] = active_rel_path

        compose_path = "packages/lico-devc/.devcontainer/docker-compose.yml"
        subprocess.run(["docker", "compose", "-f", compose_path, "up", "-d", "--build"], env=env, check=True)
        print("[Success] Container is running in the background.")
        print("[Status] Connect via VS Code (Dev Containers) or SSH.")
    except subprocess.CalledProcessError as e:
        print(f"[Error] Failed to start container: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
