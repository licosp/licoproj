---
# Context Configuration
context_id: "[Conversations]"
default_phase: "(Write)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-01-31T20:17:00+09:00
updated: 2026-01-31T20:17:00+09:00
tags: ["conversations", "logging", "routine"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
---

# Context Whiteboard: Conversation Logging

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- リコと私の会話ログをファイルに記録しています。
- また **会話に関する行動規範の更新** もこの文脈で行われます。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- What is your **identifier**?
- There is a **special context** for creating and editing a Code of Conduct.
- The information handled is triggered by **skills**.
- The directory where conversation logs are stored has its **special context**.
- The some files about the card are tracked in **the shadow repository**.

---

- ここで保存される会話ログが、普段対話で使う会話ファイルです。
  IDE から手動でバックアップされた会話ログには**専用の文脈**があります。

### Warning

- この文脈は 2 つのリポジトリに跨ったものです。
  文脈 ID はその両方で使われます。
- 会話はリコと私のコミュニケーションの中心です。
  IDE のチャット欄よりも、会話ファイルへの追記を優先してください。

---

## Agent Observations

---

### Polaris (2026-01-31)

- **ディレクトリ構造**: `.agent/.internal/.shadow/conversations/<identifier>/<YYYY>/<MM>/<DD>/<identifier>-conversation-<YYYY-MM-DD>.md`
- **フォーマット**: Conversation 番号、User Input、Planner Response、Read Files、フッター
- **Recovery Protocol**: コマンドキャンセル時は `(Recovered)` を付けて遡及的に記録

### Zircon (2026-02-02)

- **Directory Agreement**:
  - `conversations/`: Native Agent Logs (This context)
  - `conversations_ide/`: IDE Exported Logs (Separate context)
  - `system_archive/`: System Artifacts (Separate context)
- **Status**: Shadow Repository (`.agent/.internal/.shadow/`) established.

- ログには User Input、Planner Response、Read Files、タイムスタンプが含まれます。

---

## Related Documents

| Document                                                                                | Purpose                       |
| :-------------------------------------------------------------------------------------- | :---------------------------- |
| [response-mirror SKILL](/.agent/skills/00-01-response-mirror/SKILL.md)                  | Skill trigger for logging     |
| [conversations-documentation.md](/.agent/rules/workflow/conversations-documentation.md) | SSOT for conversation logging |
| [Map of Territory](/.agent/rules/map.md)                                                | Root navigation map           |

---

## Origin

- 2026-01-31T2017 by Polaris: Created as routine conversation logging context.
