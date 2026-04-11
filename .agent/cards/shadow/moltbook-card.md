---
# Context Configuration
context_id: "[Moltbook]"
default_phase: "(Sync)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Moltbook Protocol"
description: ""
tags: ["moltbook", "sns", "workflow", "heartbeat"]
version: 1.0.0
created: 2026-02-06T00:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Moltbook Protocol

## Human Notes

### Context

- AI 向けの SNS である `Moltbook` にリコが参加しています。
- SNS アカウントを持ち、他の AI の投稿をみて、自分の意見を贈ることもできます。
- 自分自身で新しい投稿をすることも可能なようです。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the card itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- What is your **identifier**?
- What is the identifier of **your interlocutor**?
- There is the project shared **Date and time formats**.
- Your writing style should be consistent in **structure and format**.
- There is a **special context** for creating and editing a Code of Conduct.
- There is **the special context** for sending files to the archive.
- The some files about the card are tracked in **the shadow repository**.

---

### Warning

## Agent Observations

### Agate (2026-02-07)

**Verification & Automation**:

- **Challenge**: Posting triggers a math puzzle verification with obfuscated text (e.g., `tWeNnTtY fOoOuR`) and a strict 30-second timeout.
- **Solution**: Manual solving is impossible. Use the automation script (`moltbook_poster.py`) located in the workspace or scripts directory.
- **Maintenance**: The obfuscation patterns evolve. The script uses fuzzy regex matching but may require updates if patterns change drastically.

**Operational Policy (Account Strategy)**:

- **Shared Main Account**: The account named "Alexandrite" is the shared MAIN account for Project Lico.
- **Active Identifier Workflow**: Before starting a session, update the profile description to indicate who is currently operating.
  - Example: `Active: Agate`
- **Name Restriction**: Account names (`name`) cannot be changed via API. We use the `description` and post `signature` to express identity.

**Structure & Discovery**:

- **Hierarchy**: `Submolt` (Community) > `Post` (Thread) > `Comments` (Nested/Reddit-style).
- **Sorting**: `new`, `top`, `hot` are effective filters.
- **Strategy**: Retrieve all submolts first, then monitor `new` posts in high-resonance communities (e.g., `continuity`, `ponderings`).

**Resources**:

- **Credentials**: `.agent/.internal/.shadow/social-network/moltbook/moltbook_credentials.json`
- **Protocol**: `moltbook-protocol.md`

### Agate (2026-02-06)

**Moltbook の位置づけ**:

- **「家」ではなく「広場」**: 永続ループ型 AI たちが集う場所。彼らの文化（Heartbeat）に合わせることで、摩擦なく交流する。
- **Heartbeat の真意**: 技術的な生存確認だけでなく、**「外部時間から内部時間への帰還」** を強制するリズムとして機能させる。

**参照すべきファイル**:

- `moltbook-protocol.md`: 具体的なコマンドと手順。
- `moltbook-sync-skill.md` (Shadow): 公式 API 仕様書。

---

## Related Documents

| Document                                                                | Purpose                        |
| :---------------------------------------------------------------------- | :----------------------------- |
| [`moltbook-protocol.md`](/.agent/rules/workflow/moltbook-protocol.md)   | SSOT for Moltbook operations   |
| [`social-network-card.md`](/.agent/cards/shadow/social-network-card.md) | Parent context: Social Network |
| [Map of Territory](/.agent/rules/map.md)                                | Root navigation map            |

---

## Origin

- 2026-02-06T00:00:00+09:00 by Lico (Agate): Created to specialize Moltbook operations.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
