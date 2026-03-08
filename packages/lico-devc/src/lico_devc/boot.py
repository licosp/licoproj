#!/usr/bin/env python3
import subprocess
import sys
import os

def main():
    """Start the lico-resident container using docker-compose."""
    print("--- Lico Container Bootstrapper (Initial Spark) ---")
    
    # 1. Check for docker-compose
    try:
        subprocess.run(["docker-compose", "--version"], check=True, capture_output=True)
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("[Error] 'docker-compose' command not found. Please install Docker Compose.")
        sys.exit(1)

    # 2. Up the container
    print("[Action] Starting lico-resident container...")
    try:
        # Use -d to detach, but -f to ensure we use the root compose file
        subprocess.run(["docker-compose", "up", "-d", "--build"], check=True)
        print("[Success] Container is running in the background.")
        print("[Status] You can now connect via VS Code (Dev Containers) or SSH.")
    except subprocess.CalledProcessError as e:
        print(f"[Error] Failed to start container: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
