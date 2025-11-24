# Auto-Translation System (Future Implementation)

## Overview

Design document for an automated translation system that monitors source files and automatically translates them from Japanese to English.

## Requirements

**Core Functionality**:
- Monitor files in `.agent/source/japanese/` for changes
- Automatically translate modified files from Japanese to English
- Save translated files to `.agent/dist/` with the same structure
- Operate continuously without manual intervention

**Translation Requirements**:
- Use Gemini API for high-quality translation
- Preserve markdown formatting and code syntax
- Maintain file structure and naming conventions
- Only translate when source files are modified

## Directory Structure

```
.agent/
├── source/
│   └── japanese/       # Source files in Japanese
└── dist/              # Translated files in English
```

## Implementation Options

### Option 1: GitHub Actions (Recommended)

**Pros**:
- Cloud-based, no local setup required
- Runs automatically on file changes (push/PR)
- Can auto-commit translation results
- Easy to configure and maintain

**Implementation**:
1. Create `.github/workflows/auto-translate.yml`
2. Trigger on changes to `.agent/source/japanese/**`
3. Use Gemini API action to translate files
4. Commit translated files to `.agent/dist/`

### Option 2: Git Pre-Commit Hooks

**Pros**:
- Runs locally before each commit
- Prevents commits without translations
- Fast feedback during development

**Cons**:
- Requires setup on each developer's machine
- Slows down commit process

### Option 3: VSCode Extension

**Pros**:
- Real-time translation on file save
- Integrated into development workflow
- Immediate visual feedback

**Cons**:
- Requires custom extension development
- Limited to VSCode users

### Option 4: File Watcher Script (inotifywait)

**Pros**:
- Runs continuously in background
- Platform-agnostic (Linux/Unix)
- Low overhead

**Cons**:
- Requires manual startup
- Linux-specific tool

## Current Limitations

**Gemini Code Assist Constraints**:
- Cannot run as a persistent background process
- Session-based interaction model
- Requires external tooling for automation

**Workaround**:
- Use external automation tools (GitHub Actions, scripts)
- Gemini Code Assist can help set up these tools
- Manual translation requests remain available

## Next Steps

1. Choose an implementation approach based on project needs
2. Set up Gemini API credentials
3. Implement the selected automation option
4. Test with sample files
5. Document the workflow for team members

## References

- Requirements defined: 2025-11-24
- Related: `translate-and-cleanup.md` for manual workflow
