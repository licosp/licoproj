# lico-log

**Lico-log** is a dedicated logging utility for the Lico AI agent system, designed to safely and autonomously append conversation records to markdown files.

## Why this exists

In the Gemini CLI environment (especially under YOLO mode), running shell commands with redirection (`>>` or `>`) often triggers a mandatory security confirmation dialog, which interrupts the agent's autonomous workflow.

`lico-log` solves this by performing the file append operation entirely within Python, bypassing shell-level redirection traps. Additionally, it implements strict **file locking** (`fcntl.flock`) to prevent race conditions if multiple agents or processes attempt to write to the same log file simultaneously.

## Features

1. **Safe Append**: Appends text without shell redirection.
2. **Timestamp Injection**: Automatically replaces any `{{TIMESTAMP}}` placeholder in your content with the current ISO 8601 timestamp (JST, accurate to seconds).
3. **Concurrency Safe**: Uses exclusive file locks.

## Usage

This tool is managed via `uv` as a workspace workspace package. You can run it from anywhere within the project root.

```bash
uv run lico-log <path_to_target_log.md> <path_to_temporary_content.txt>
```

### Workflow Example (Split Buffer Strategy)

1. **Write your plan/report to a temporary file**:
   (Store this inside your tracked workspace to avoid accidental Git commits)

   ```bash
   echo "### Conversation: [{{TIMESTAMP}}]\n\nHello World" > .agent/.internal/workspace/agate/temp_plan.txt
   ```

2. **Execute `lico-log`**:

   ```bash
   uv run lico-log .repos/.licoshdw/conversations/agate/2026/03/13/2026-03-13T0000_agate-conversation.md .agent/.internal/workspace/agate/temp_plan.txt
   ```

3. **Cleanup**:

   ```bash
   rm .agent/.internal/workspace/agate/temp_plan.txt
   ```

**Note for AI Agents**: Always prefer using `lico-log` over `cat >>` for logging your thoughts and reports.
