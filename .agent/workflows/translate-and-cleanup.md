---
description: Translate Japanese source files to English and maintain a clean output directory
---

# Translate and Cleanup Task

## Objective

Translate Japanese source files to English and maintain a clean output directory.

## Directory Paths

- **Source**: `.agent/source/japanese/`
- **Destination**: `.agent/dist/`

## Task Steps

### Step 1: Translation

Recursively translate all files from the source directory to the destination directory.

**Requirements**:

- Translate content from Japanese to English
- Preserve directory structure
- Only translate files when:
  - The source file is newer than the destination file, OR
  - The destination file does not exist

**File Handling**:

- Maintain the same filename
- Preserve the same relative path structure
- Keep the same file extension

### Step 2: Cleanup

Remove orphaned files and directories from the destination.

**Requirements**:

- Delete files in the destination directory that no longer exist in the source directory
- Delete empty directories in the destination directory
- Preserve files that correspond to existing source files

## Expected Behavior

1. Compare timestamps between source and destination files
2. Translate only modified or new files to avoid unnecessary work
3. Ensure the destination directory mirrors the source directory structure
4. Remove any destination files that don't have corresponding source files
