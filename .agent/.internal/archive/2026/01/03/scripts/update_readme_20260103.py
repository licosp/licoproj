import os

readme_path = ".agent/rules/README.md"

with open(readme_path, "r") as f:
    content = f.read()

# 1. Update Templates
old_templates = "| `templates/` | Reusable templates (frontmatter, commit messages) |"
new_templates = """| `templates/` | **Reusable templates** (See list below) |
| `workflows/` | **Executable procedures** (invoked via /slash-command) |

### Templates Detail
| File | Purpose |
|------|---------|
| `header-frontmatter.yaml` | **Mandatory** frontmatter for all rules and thoughts |
| `commit-message.txt` | Standard commit message format |"""

content = content.replace(old_templates, new_templates)

# 2. Update Internal Table
# We want to add legacy.md and cases/
old_internal = "| `.internal/memory_archive/` | **System memory snapshots**"
new_internal = """| `.internal/cases/` | **Case Studies** (Archived use-once contexts) |
| `.internal/legacy.md` | **The Wisdom of the Clan** (Permanent, collective insights) |
| `.internal/memory_archive/` | **System memory snapshots**"""

content = content.replace(old_internal, new_internal)

# 3. Update Cards Table
# We identify the start and end of the existing table rows content to replace
start_marker = "| [ai-document-format-card.md](.agent/cards/ai-document-format-card.md) | `[AI-Format]` | AI document formatting standards |"
end_marker = "| [vscode-settings-card.md](.agent/cards/vscode-settings-card.md) | `[VSCode]` | VS Code settings management |"

new_cards = """| [ai-document-format-card.md](.agent/cards/ai-document-format-card.md) | `[AI-Format]` | AI document formatting standards |
| [archival-cleanup-card.md](.agent/cards/archival-cleanup-card.md) | `[Archive]` | Archive maintenance and cleanup |
| [context-cards-card.md](.agent/cards/context-cards-card.md) | `[Context-Cards]` | Card template and examples |
| [cross-link-audit-card.md](.agent/cards/cross-link-audit-card.md) | `[Cross-Link-Audit]` | Rule linkage verification |
| [directory-reorganize-card.md](.agent/cards/directory-reorganize-card.md) | `[Dir-Reorg]` | Directory structure maintenance |
| [discussion-draft-card.md](.agent/cards/discussion-draft-card.md) | `[Discussion-Draft]` | SNS/forum discussion drafts |
| [drafts-cleanup-card.md](.agent/cards/drafts-cleanup-card.md) | `[Drafts-Cleanup]` | Draft file cleanup and polish |
| [drafts-daily-card.md](.agent/cards/drafts-daily-card.md) | `[Drafts-Daily]` | Daily draft commits |
| [human-manuals-card.md](.agent/cards/human-manuals-card.md) | `[Human-Manuals]` | Collaborative manual creation |
| [identifier-profile-card.md](.agent/cards/identifier-profile-card.md) | `[Profile]` | Identifier profile management |
| [legacy-write-card.md](.agent/cards/legacy-write-card.md) | `[Legacy]` | Writing to legacy.md |
| [log-sanitization-card.md](.agent/cards/log-sanitization-card.md) | `[Log-Sanitization]` | Log cleaning for archives |
| [personal-thoughts-card.md](.agent/cards/personal-thoughts-card.md) | `[Personal-Thoughts]` | User's personal thought space |
| [readme-sync-card.md](.agent/cards/readme-sync-card.md) | `[README-Sync]` | Map vs Territory synchronization |
| [references-objective-card.md](.agent/cards/references-objective-card.md) | `[References]` | External reference analysis |
| [rules-update-card.md](.agent/cards/rules-update-card.md) | `[Rules-Update]` | Behavioral rule editing |
| [sync-memory-card.md](.agent/cards/sync-memory-card.md) | `[Sync-Memory]` | Memory synchronization |
| [thoughts-subjective-card.md](.agent/cards/thoughts-subjective-card.md) | `[Thoughts-Subjective]` | Subjective reflection writing |
| [user-profile-update-card.md](.agent/cards/user-profile-update-card.md) | `[User-Profile]` | Updating user preferences |
| [vscode-settings-card.md](.agent/cards/vscode-settings-card.md) | `[VSCode]` | VS Code settings management |"""

# Find start and end indices
start_idx = content.find(start_marker)
end_idx = content.find(end_marker)

if start_idx != -1 and end_idx != -1:
    # Replace the chunk
    content = content[:start_idx] + new_cards + content[end_idx + len(end_marker):]

# 4. Add Origin
# Check if Origin already exists (it shouldn't based on recent reads, but good to check)
if "## Origin" not in content:
    origin_section = """
---

## Origin

- 2025-12-01T0000: Created as rules index
- 2026-01-02T1240 by Spica: Synced map with territory (Templates, Cards, Legacy, Structure)
"""
    content += origin_section

with open(readme_path, "w") as f:
    f.write(content)
