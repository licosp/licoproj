import os
import sys
import re

# Critical files that must exist and have valid frontmatter
CRITICAL_FILES = [
    ".agent/rules/core/identity.md",
    ".agent/rules/core/hallucination-awareness.md",
    ".agent/rules/core/transparency-and-disclosure.md",
    ".agent/rules/core/language-standards.md",
    ".agent/rules/README.md",
    ".agent/rules/.updated"
]

def check_files_exist():
    missing = []
    for f in CRITICAL_FILES:
        if not os.path.exists(f):
            missing.append(f)
    return missing

def validate_frontmatter(filepath, strict=False):
    with open(filepath, 'r') as f:
        content = f.read()
    
    # Check for YAML frontmatter block
    match = re.match(r'^---\n(.*?)\n---\n', content, re.DOTALL)
    if not match:
        if strict:
            return "Missing YAML frontmatter"
        return None # Not strict, so ignore missing frontmatter
    
    frontmatter = match.group(1)
    
    # Simple check for 'description:' key
    if not re.search(r'^description:', frontmatter, re.MULTILINE):
        return "Missing 'description' in frontmatter"
    
    return None

def main():
    print("Validating rules...")
    
    # 1. Check critical files
    missing_files = check_files_exist()
    if missing_files:
        print(f"ERROR: Missing critical files: {missing_files}")
        sys.exit(1)
    
    # 2. Validate markdown files in .agent/rules
    errors = []
    for root, dirs, files in os.walk(".agent/rules"):
        for file in files:
            if file.endswith(".md") and file != "README.md":
                filepath = os.path.join(root, file)
                # Enforce strict validation only for CRITICAL_FILES
                is_critical = filepath in CRITICAL_FILES
                error = validate_frontmatter(filepath, strict=is_critical)
                if error:
                    errors.append(f"{filepath}: {error}")
    
    if errors:
        print("ERROR: Validation failed for the following files:")
        for e in errors:
            print(f"  - {e}")
        sys.exit(1)
        
    print("Validation passed.")
    sys.exit(0)

if __name__ == "__main__":
    main()
