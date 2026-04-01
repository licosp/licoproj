---
ai_visible: true
title: Conversation Logging Protocol
description: Standards for logging AI-human conversations via the three-layer template architecture.
tags: [conversation, logging, workflow, v3]
version: 3.2.0
created: 2026-01-31T22:50:00+09:00
updated: 2026-04-01T23:52:11+09:00
language: en
author: Lico (Alexandrite)
ai_model: gemini-3-flash-preview
---

# Conversation Logging Protocol

## 1. Purpose

Standardize how AI instances log conversations using the Three-Layer Template Architecture to ensure absolute historical integrity, transparency of intent, and recovery from self-inflicted buffer contamination.

## 2. Philosophy: Structural Purity, Explicit Intent

1. **History is a Sacred Loom**: The log file is not just a dump; it is a woven narrative of Input, Plan, and Report.
2. **Templates as DNA**: Every entry MUST conform to the physical schemas defined in `.agent/templates/conversations/`.
3. **Valided Automation**: The logging tool (`lico-log`) acts as a "Guardian of Protocol," not just a passive appender.
4. **Zero-Interpretation Input**: Copy User Input exactly. Do not summarize.

## 3. The Three-Layer Architecture

> [!IMPORTANT]
> The protocol relies on the following mandatory templates located in `.agent/templates/conversations/`.

| Layer         | Template         | Purpose                                                              |
| :------------ | :--------------- | :------------------------------------------------------------------- |
| **Container** | `base.md`        | Initial structure for NEW conversation files (Frontmatter + Header). |
| **Trigger**   | `turn-plan.md`   | Schema for the start of a turn (Timestamp + Input + Agent Plan).     |
| **Outcome**   | `turn-report.md` | Schema for the end of a turn (Result + Outcome + Mental State).      |

## 4. Logging Procedure (The Split-Buffer Strategy)

To ensure intent is captured even if execution fails, use **two separate buffer files** in `.agent/.internal/workspace/<identifier>/`.

### Phase 1: Turn Initialization (Plan)

1. **Prepare `current_log_plan.txt`**: Populate it using the `turn-plan.md` schema.
2. **Commit Intent**: Append the plan buffer to the log file.

   ```bash
   uv run lico-log <LogPath> current_log_plan.txt
   ```

### Phase 2: Turn Conclusion (Report)

1. **Prepare `current_log_report.txt`**: Populate it using the `turn-report.md` schema.
2. **Finalize Story**: Append the report buffer to the log file.

   ```bash
   uv run lico-log <LogPath> current_log_report.txt
   ```

## 5. Tool Responsibilities & Validation

The logging tool (`lico-log`) MUST enforce the following rules:

- **Timestamp Integrity**: Ensure all `{{TIMESTAMP}}` placeholders are expanded to ISO 8601 (Second precision).
- **Format Guardrail**: Reject any content that contains raw debug logs (e.g., "LOGGING SUCCESS") or invalid markdown structures.
- **Atomic Operation**: Ensure the log always ends with the sacred separator (`---`) followed by a single newline.

## 6. Directory Structure (SSOT)

- **Directory**: `.repos/.licoshdw/conversations/<identifier>/<YYYY>/<MM>/<DD>/`
- **Filename**: `<YYYY-MM-DDTHHMM>-<identifier>-conversation.md`

---

## Related Documents

| Document                                                           | Purpose                    |
| :----------------------------------------------------------------- | :------------------------- |
| [`lico-log/README.md`](/packages/lico-log/README.md)               | Package structural pointer |
| [`base.md`](/.agent/templates/conversations/base.md)               | Container Schema           |
| [`turn-plan.md`](/.agent/templates/conversations/turn-plan.md)     | Trigger                    |
| [`turn-report.md`](/.agent/templates/conversations/turn-report.md) | Outcome                    |
| [Map of Territory](/.agent/rules/map.md)                           | Root navigation map        |

---

## Origin

- 2026-01-31T22:50:00+09:00 by Polaris: v1.0 by Polaris (Initial Create).
- 2026-02-13T00:00:00+09:00 by Sirius: v2.0 by Sirius (Timestamp ID, Tool Reconstruction, Footer Abolition).
- 2026-02-19T08:35:00+09:00 by Sirius: v2.1.0 by Sirius (Updated to Managed Script architecture).
- 2026-02-19T19:45:00+09:00 by Sirius: v2.2.0 by Sirius (Added Tool Usage Constraints).
- 2026-02-19T20:10:00+09:00 by Sirius: v2.2.1 by Sirius (Standardized to Second Precision).
- 2026-02-20T08:34:00+09:00 by Sirius: v2.3.0 by Sirius (Allow Multi-Report phases for complex tasks).
- 2026-03-21T19:30:00+09:00 by Sirius: v3.0.0 by Sirius (Migrated hard-coded scripts to the `lico-log` UV package and relocated to `.agent/rules/packages/`).
- 2026-03-23T05:51:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
- 2026-03-23T06:46:00+09:00 by Sirius: v3.1.0 by Sirius (Codified `<LogPath>` Directory and Filename structures explicitly as the SSOT, replacing legacy placeholders).
- 2026-04-01T23:52:11+09:00 by Alexandrite: v3.2.0 Formalized Three-Layer Template Architecture and Validation Mandates.
