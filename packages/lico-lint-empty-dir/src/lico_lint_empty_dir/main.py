import os
import sys

def is_empty_dir(path: str) -> bool:
    """Check if a directory is empty (no files or sub-directories)."""
    try:
        return not any(os.scandir(path))
    except (PermissionError, FileNotFoundError):
        return False

def main() -> None:
    """Scan the repository for empty directories."""
    root_dir = os.getcwd()
    exclude_dirs = {".git", ".venv", "node_modules", "__pycache__", ".temp", ".repos", ".trash"}
    
    print(f"--- lico-lint-empty-dir Scan: {root_dir} ---")
    found_empty = False

    for root, dirs, files in os.walk(root_dir):
        # Filter out excluded directories
        dirs[:] = [d for d in dirs if d not in exclude_dirs and not d.startswith(".")]
        
        if root == root_dir:
            continue
            
        if is_empty_dir(root):
            print(f"[Warning] Empty directory detected: {os.path.relpath(root, root_dir)}")
            found_empty = True

    if found_empty:
        print("--- Scan Complete: Issues found ---")
        # In a real TBD flow, we might exit with 1, but for now just notify.
        sys.exit(0) # Keep pulse beating
    else:
        print("--- Scan Complete: No empty directories found ---")
        sys.exit(0)

if __name__ == "__main__":
    main()
