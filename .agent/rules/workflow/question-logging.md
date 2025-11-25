# Question Logging

## Purpose
When receiving a **significant question** from the user, log it to `.agent/logs/questions/log_YYYY-MM-DD.md`.

## Significant Questions Include
- Requests for guidance on approach or design
- Questions about capabilities or limitations  
- Requests to create new workflows or systems
- Questions that lead to major changes

## Logging Format
```markdown
### HH:MM:SS+TZ:TZ - [Brief Title]
**Q**: [User's question]  
**Context**: [Brief context]  
**Action**: [What was done]
```

## When to Skip Logging
- Simple implementation requests
- Routine tasks following established patterns
- Quick clarifications
