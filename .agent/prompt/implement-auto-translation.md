---
date: 2025-11-24
user: leonidas
---

## Prompt

I need to implement an automated translation system that monitors specific files and translates them automatically when updated.

**Requirements:**
- Monitor files in `.agent/source/japanese/` directory
- Automatically translate updated files from Japanese to English
- Save translated results to `.agent/dist/` directory
- Run as a background process or automated workflow

**Implementation Options:**

1. **GitHub Actions (Recommended)**
   - Trigger on file changes
   - Use Gemini API for translation
   - Auto-commit and push results

2. **Git Hooks (pre-commit)**
   - Check translations before commit
   - Prevent missing translations

3. **VS Code Extension**
   - File system watching
   - Auto-translate on save

4. **inotifywait Script**
   - File monitoring on Linux
   - Background execution

**Constraints:**
- Gemini Code Assist cannot run as a persistent agent
- Session-based architecture requires external tooling integration

**Expected Output:**
A working automated translation workflow that keeps English translations in sync with Japanese source files.

## Additional Notes

- This task was originally defined in a session on 2025-11-24
- Source file: `.agent/task/auto-translate.md`
- The prompt is formatted for clarity and actionability with AI agents
