import os, subprocess, sys

def find_hub_root():
    """Discover the Universe Root by looking for 'project' and 'crew' folders."""
    current = os.path.abspath(os.getcwd())
    while current != "/":
        dirs = os.listdir(current)
        if "project" in dirs and "crew" in dirs:
            return current
        current = os.path.dirname(current)
    # Fallback: traverse up from script location
    return os.path.abspath(os.path.join(os.path.dirname(__file__), "../../../.."))

def main():
    print("--- Lico Container Bootstrapper (Bare Spark) ---")
    
    hub_root = find_hub_root()
    active_rel = os.path.relpath(os.getcwd(), hub_root)
    print(f"[Hub] Root: {hub_root} | Active: {active_rel}")

    env = os.environ.copy()
    env.update({"LICO_HUB_ROOT": hub_root, "LICO_ACTIVE_REL": active_rel})
    
    try:
        compose_path = "packages/lico-devc/.devcontainer/docker-compose.yml"
        subprocess.run(["docker", "compose", "-f", compose_path, "up", "-d", "--build"], env=env, check=True)
        print("[Success] Container is running. Connect via VS Code or SSH.")
    except Exception as e:
        print(f"[Error] Failed to start container: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
