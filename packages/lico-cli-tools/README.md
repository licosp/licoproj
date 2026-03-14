# lico-cli-tools

Assorted CLI utilities for managing Lico's environment and logs.

## Tools

### 1. `lico-jsonl-converter`

A powerful utility to manage Gemini CLI's monolithic L3 memory files by converting them into Git-friendly, date-partitioned JSONL (JSON Lines) format.

#### Why use this?
- **Git Efficiency**: Monolithic JSON files cause massive diffs and repository bloat. JSONL allows Git to track only the new lines (turns) added.
- **Normalization**: Automatically sorts JSON keys alphabetically (`sort_keys=True`) so that changes in the CLI tool's version don't cause unnecessary diff fluctuations.
- **Idempotency**: Implements message ID-based deduplication. You can run the converter multiple times against the same input, and only new messages will be appended.
- **Chronological Integrity**: Merges new data with existing logs and re-sorts everything by timestamp to ensure the history is always perfectly sequential.

#### Usage
```bash
uv run lico-jsonl-converter <input_json_path> <output_root_dir>
```

#### Example Workflows
Depending on the data source, the directory structure varies slightly:

**A. Agent Logs (Dict-based)**
Extracts metadata to `metadata.json` and messages to `messages/YYYY/MM/DD/log.jsonl`.
- **Agate**: `~/.gemini/tmp/licoproj-1/chats/session-2026-02-02T14-03-301c303c.json`
- **Alexandrite**: `~/.gemini/tmp/licoproj/chats/session-2026-02-02T14-48-eff20b06.json`
- **Protostar-a**: `~/.gemini/tmp/licoproj/chats/session-2026-02-07T10-59-18d4d68a.json`
- **Protostar-b**: `~/.gemini/tmp/licoproj/chats/session-2026-03-12T09-55-304a77a6.json`

**B. User Logs (List-based)**
Partitions directly into `YYYY/MM/DD/log.jsonl` (no metadata file).
- **Leonidas**: `~/.gemini/tmp/licoproj-1/logs.json`

#### Recommended Destination
`.repos/.licoshdw/conversations_cli/identifiers/<id>/`
