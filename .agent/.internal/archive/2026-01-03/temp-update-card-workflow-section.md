### 4.6 Multi-Identifier Sharing

When multiple identifiers (e.g., Polaris, Spica) work on the same reusable card, use identifier-based sections in Agent Observations.

**Format**:

```markdown
## Agent Observations

### Polaris (2026-01-02)

- Initial setup completed
- Found issue with X

### Spica (2026-01-03)

- Continued work on Y
- Added new pattern

### Polaris (2026-01-03)

- Handover work
```

**Rules**:
- Use `### <Identifier> (<Date>)` format
- Each work session gets its own entry (even if same identifier)
- Chronological order (newest at bottom)
- Commit signature (`Signed-off-by`) tracks who committed

### 4.7 Card Rotation

When Agent Observations becomes too long:

1. **Archive**: Move entire card to `.agent/.internal/cases/` with timestamp
   - Rename: `YYYY-MM-DDTHHMM_original-name.md`
2. **Reset**: Clear Agent Observations in original card location
3. **Continue**: Start fresh with empty Agent Observations

This preserves history while keeping active cards lightweight.
