import os

# Define fixes
FIXES = [
    {
        "file": ".agent/rules/development/git-operations.md",
        "replacements": [
            ("file:///home/USER/develop/shared/project/licoproj/.agent/rules/development/", ""),
            ("file:///home/USER/develop/shared/project/licoproj/.agent/workflows/", "../../workflows/"),
        ]
    },
    {
        "file": ".agent/rules/proposals/behavior_guidelines_candidate.md",
        "replacements": [
            ("/home/USER/develop/shared/project/licoproj/.agent/docs/ai/", "../../docs/ai/"),
        ]
    },
    {
        "file": ".agent/rules/core/user-adaptation.md",
        "replacements": [
            ("/home/USER/", "/home/USER/"),
            ("User is \"leonidas\"", "User is \"USER\"")
        ]
    },
    {
        "file": ".agent/rules/core/documentation/wsl-browser-path.md",
        "replacements": [
            ("/home/USER/", "/home/USER/"),
        ]
    },
    {
        "file": ".agent/rules/workflow/session-startup.md",
        "replacements": [
            ("/home/USER/", "/home/USER/"),
        ]
    }
]

BASE_DIR = "/home/USER/develop/shared/project/licoproj"

def apply_fixes():
    for item in FIXES:
        filepath = os.path.join(BASE_DIR, item["file"])
        if not os.path.exists(filepath):
            print(f"Skipping {filepath} (not found)")
            continue
            
        print(f"Processing {filepath}...")
        with open(filepath, 'r') as f:
            content = f.read()
            
        new_content = content
        changes_count = 0
        for old, new in item["replacements"]:
            if old in new_content:
                changes_count += new_content.count(old)
                new_content = new_content.replace(old, new)
        
        if changes_count > 0:
            with open(filepath, 'w') as f:
                f.write(new_content)
            print(f"  Fixed {changes_count} occurrences.")
        else:
            print("  No changes needed.")

if __name__ == "__main__":
    apply_fixes()
