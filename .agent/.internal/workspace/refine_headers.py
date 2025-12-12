import os
import re

TARGET_DIR = "/home/USER/develop/shared/project/licoproj/.human/users/leonidas/drafts"

def refine_file(filepath):
    print(f"Refining: {filepath}")
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    new_lines = []
    changes = 0
    for line in lines:
        # Regex to match "### Query [Digits]: " and replace with "### "
        new_line = re.sub(r'^### Query \d+: ', '### ', line)
        if new_line != line:
            changes += 1
        new_lines.append(new_line)
    
    if changes > 0:
        with open(filepath, 'w') as f:
            f.writelines(new_lines)
        print(f"  Modified {changes} lines.")
    else:
        print("  No changes.")

files = [f for f in sorted(os.listdir(TARGET_DIR)) if f.startswith('draft_') and f.endswith('.md')]

for f in files:
    try:
        refine_file(os.path.join(TARGET_DIR, f))
    except Exception as e:
        print(f"Failed to process {f}: {e}")
