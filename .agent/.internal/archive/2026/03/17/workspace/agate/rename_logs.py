import os
import re
import subprocess
from pathlib import Path

base_dir = Path(".repos/.licoshdw/conversations")
old_pattern = re.compile(r"^([a-z]+)-conversation-(\d{4}-\d{2}-\d{2})\.md$")

for md_file in base_dir.rglob("*.md"):
    if not md_file.is_file():
        continue
    
    # Skip if already renamed
    if re.match(r"^\d{4}-\d{2}-\d{2}T\d{4}_", md_file.name):
        continue

    m = old_pattern.match(md_file.name)
    if not m:
        # print(f"Skipping {md_file.name} (does not match old pattern)")
        continue

    identifier = m.group(1)
    
    date_part = None
    created_time = "0000"
    
    try:
        content = md_file.read_text(encoding="utf-8")
        # Match "created: 2026-01-31T20:17:00+09:00"
        # Or "created: 2026-01-31"
        match = re.search(r"^created:\s*(\d{4}-\d{2}-\d{2})(?:T(\d{2}):?(\d{2}))?", content, re.MULTILINE)
        if match:
            date_part = match.group(1)
            if match.group(2) and match.group(3):
                created_time = match.group(2) + match.group(3)
        else:
            date_part = m.group(2) # Fallback to date in filename
    except Exception as e:
        print(f"Error reading {md_file}: {e}")
        continue

    if not date_part:
        continue

    new_name = f"{date_part}T{created_time}_{identifier}-conversation.md"
    new_path = md_file.with_name(new_name)
    
    print(f"{md_file.name} -> {new_name}")
    
    # Git mv
    rel_old = md_file.relative_to(".repos/.licoshdw")
    rel_new = new_path.relative_to(".repos/.licoshdw")
    subprocess.run(["git", "mv", str(rel_old), str(rel_new)], cwd=".repos/.licoshdw", check=True)

    # We also need to update the title inside the frontmatter if necessary?
    # No, user just asked to rename the files: "今使っている会話ファイルの命名規則が古かったので、それをリネームします...過去のファイルもそのパターンに直せますか？"
