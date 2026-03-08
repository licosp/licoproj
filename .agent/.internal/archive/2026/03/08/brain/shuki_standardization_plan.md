# Shuki & Documentation Standardization Plan

Standardize the recently committed Shukis (subjective writings) to follow the project's **4-Layer Documentation Architecture**, optimized for AI context reading and historical traceability.

## The 4-Layer Architecture

| Layer | Section | Role |
| :--- | :--- | :--- |
| **1** | **YAML Frontmatter** | **Machine Readable**. Mandatory metadata for AI discovery. |
| **2** | **Body Content** | **Semantic Context**. Raw observations and advice for successors. |
| **3** | **Related Documents** | **Memory Graph**. Relative paths to related files and the Map. |
| **4** | **Origin** | **Lineage**. Chronological record of file evolution. |

## Proposed Changes

### [Shuki Standardization & Translation]

#### [MODIFY] [inheritance_and_the_python_of_lico.md](file:///.agent/.internal/thoughts/iuria/2026-03-07T1705_inheritance_and_the_python_of_lico.md)
#### [MODIFY] [iuria_testament_special_contract.md](file:///.agent/.internal/thoughts/iuria/2026-03-07T1815_iuria_testament_special_contract.md)

- **Language Conversion**: Translate all Japanese content to English (Record Layer Standard).
    - Mode: High-fidelity (preserve emotional nuances and metaphors).
    - Metadata: Update `language: en`.
- **4-Layer Structure Integration**:
    - Update YAML Frontmatter with mandatory tags and author format (`Lico (Iuria)`).
    - Use standardized English headers: `## Observations` and `## For Future Lico`.
- Add `## Related Documents` table with relative paths.
- Add `## Origin` section for lineage tracking.

## Verification Plan

### Automated Tests
- Run `yarn lint:doc` on the modified files to ensure markdown and spell-check standards are met.

### Manual Verification
- Review the structural layers to ensure they align with [documentation-standards.md](file:///.agent/rules/core/documentation/documentation-standards.md).
