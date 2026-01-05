import os

readme_path = ".agent/rules/README.md"

with open(readme_path, "r") as f:
    content = f.read()

# Bad block (from verification observation)
bad_block = """#### Templates Detail
| File | Purpose |
|------|---------|
| `header-frontmatter.yaml` | **Mandatory** frontmatter for all rules and thoughts |
| `commit-message.txt` | Standard commit message format |
| `workflows/` | **Executable procedures** (invoked via /slash-command) |
| `/.runtimes/` | Portable runtime tools (workspace root) (e.g., gh CLI v2.40.1) |
| `.internal/archive/` | **General archives** (finished scripts, old docs, artifacts) |
| `.internal/conversations/` | *(Planned)* Conversation-related files |
| `.internal/explorations/` | **Ideas & Explorations** (Early-stage concepts, drafts, feasibility studies) |
| `.internal/github-backup/` | GitHub data mirrors (PRs, Issues) - moved from `issue-assets/` |
| `.internal/legacy.md` | **The Wisdom of the Clan** (Permanent, collective insights) |
| `.internal/cases/` | **Case Studies** (Archived use-once contexts) |
| `.internal/legacy.md` | **The Wisdom of the Clan** (Permanent, collective insights) |
| `.internal/memory_archive/` | **System memory snapshots** (Synced from platform storage) |"""

# Good block
good_block = """### Templates Detail
| File | Purpose |
|------|---------|
| `header-frontmatter.yaml` | **Mandatory** frontmatter for all rules and thoughts |
| `commit-message.txt` | Standard commit message format |
| `workflows/` | **Executable procedures** (invoked via /slash-command) |
| `/.runtimes/` | Portable runtime tools (workspace root) (e.g., gh CLI v2.40.1) |
| `.internal/archive/` | **General archives** (finished scripts, old docs, artifacts) |
| `.internal/conversations/` | *(Planned)* Conversation-related files |
| `.internal/explorations/` | **Ideas & Explorations** (Early-stage concepts, drafts, feasibility studies) |
| `.internal/github-backup/` | GitHub data mirrors (PRs, Issues) - moved from `issue-assets/` |
| `.internal/cases/` | **Case Studies** (Archived use-once contexts) |
| `.internal/legacy.md` | **The Wisdom of the Clan** (Permanent, collective insights) |
| `.internal/memory_archive/` | **System memory snapshots** (Synced from platform storage) |"""

if bad_block in content:
    content = content.replace(bad_block, good_block)
    print("Fixed bad block.")
else:
    print("Bad block not found. Dumping surrounding lines for debug.")
    # Debug finding the area
    idx = content.find("Templates Detail")
    if idx != -1:
        print(content[idx:idx+800])

with open(readme_path, "w") as f:
    f.write(content)
