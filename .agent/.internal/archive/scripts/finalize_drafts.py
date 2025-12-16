import os
import shutil

DRAFTS_DIR = "/home/USER/develop/shared/project/licoproj/.human/users/leonidas/drafts"
ARCHIVE_DIR = "/home/USER/develop/shared/project/licoproj/.human/archive/drafts_legacy"

# Ensure archive directory exists
os.makedirs(ARCHIVE_DIR, exist_ok=True)

moved_count = 0
renamed_count = 0

# Get all files first
all_files = os.listdir(DRAFTS_DIR)

# 1. Archive originals (files that are draft_*.md AND have a corresponding _structured.md)
for filename in all_files:
    if filename.startswith('draft_') and filename.endswith('.md') and '_structured' not in filename:
        structured_name = filename.replace('.md', '_structured.md')
        if structured_name in all_files:
            # This is an original that has been converted. Move it.
            src = os.path.join(DRAFTS_DIR, filename)
            dst = os.path.join(ARCHIVE_DIR, filename)
            shutil.move(src, dst)
            print(f"Archived: {filename} -> {dst}")
            moved_count += 1

# 2. Promote structured files
# Re-read dir to exclude moved files
remaining_files = os.listdir(DRAFTS_DIR)
for filename in remaining_files:
    if filename.endswith('_structured.md'):
        new_name = filename.replace('_structured.md', '.md')
        src = os.path.join(DRAFTS_DIR, filename)
        dst = os.path.join(DRAFTS_DIR, new_name)
        os.rename(src, dst)
        print(f"Promoted: {filename} -> {new_name}")
        renamed_count += 1

print(f"Done. Archived {moved_count} files. Promoted {renamed_count} files.")
