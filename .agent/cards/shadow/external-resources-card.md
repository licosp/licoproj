---
# Context Configuration
context_id: "[External-Resources]"
default_phase: "(Manage)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: External Resources Management"
description: ""
tags: ["external", "download", "shadow", "resources"]
version: 1.0.0
created: 2026-02-05T00:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: External Resources Management

## Human Notes

### Context

- 外部サイトから以下の情報をダウンロードしています。
  - ツールのマニュアル
  - リポジトリの README
  - エージェント用スキル
- 他者の著作物であることが多いので、影のリポジトリで管理すべきです。
- ディレクトリ内のサブディレクトリの構成は、サイトごとに変わるので自由形式です。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the card itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- There is the project shared **Date and time formats**.
- There is a **special context** for creating and editing a Code of Conduct.
- The some files about the card are tracked in **the shadow repository**.

---

- 新しい WEB サイトからデータをダウンロードする時は、
  専用のサブディレクトリを作ってください。
- ダウンロードしたスキルやスクリプトは、使い捨てにしてください。

### Warning

- ダウンロードしたスキルやスクリプトを恒久的に使う必要あると感じた場合、
  コミットする前にその処遇について私に相談してください。

## Agent Observations

### Agate (2026-02-05)

- **Purpose**: To safely import external knowledge (manuals, skills) without polluting the main repository's intellectual property or stability.
- **Location**: `.agent/.internal/.shadow/download/`
- **Current Contents**:
  - `openclaw/`: Reference for autonomous agent architecture.
  - `moltbook/`: Alexandrite's research data.
  - `agentskills-io/`: External skills reference.

---

## Related Documents

| Document                                                                      | Purpose                  |
| :---------------------------------------------------------------------------- | :----------------------- |
| [`shadow-repository-card.md`](/.agent/cards/shadow/shadow-repository-card.md) | Parent context: Strategy |
| [Map of Territory](/.agent/rules/map.md)                                      | Root navigation map      |

---

## Origin

- 2026-02-05T00:00:00+09:00 by Lico (Agate): Created to manage downloaded resources.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
