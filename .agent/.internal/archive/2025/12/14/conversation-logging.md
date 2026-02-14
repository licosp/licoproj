# Conversation Logging

## Purpose
Log all interactions between users and Lico (AI) for future reference and learning. Logs are designed to be machine-readable and parsable by AI systems.

## Log Location
`.agent/logs/conversations/log_YYYY-MM-DD.md`

## Logging Rules
- Log **every** interaction, not just significant questions
- Use structured format optimized for AI consumption
- Avoid decorative elements; prioritize clarity and parseability
- Use ISO 8601 format for timestamps

## Log Entry Format
```markdown
---
timestamp: YYYY-MM-DDTHH:MM:SS+TZ:TZ
human: [Human name]
ai: Lico
model: [AI model name]
---

### Q
[User's question or request]

### A
[Lico's response summary]

---
```

## Model Name Examples
- `Gemini 2.0 Flash Thinking`
- `Gemini 3 Pro High`
- `Claude Sonnet 4.5 Thinking`
- `GPT-4o`

## Directory Structure
Ensure the logs directory exists:
```bash
mkdir -p .agent/logs/conversations
```

## Notes
- Each day uses a single file: `log_YYYY-MM-DD.md`
- Entries are appended chronologically
- Response summaries should be concise but complete
- Include tool calls and significant actions in the response summary