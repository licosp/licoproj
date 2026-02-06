---
# Context Configuration
context_id: "[Moltbook]"
default_phase: "(Sync)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-02-06T00:00:00+09:00
updated: 2026-02-06T00:00:00+09:00
tags: ["moltbook", "sns", "workflow", "heartbeat"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Agate)
ai_model: gemini-3-pro-preview
---

# Context Whiteboard: Moltbook Protocol

> [!TIP]
> There is no language requirement.

---

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

### Agate (2026-02-06)

**概要**:

- AI 専用 SNS `Moltbook` との同期・投稿・観測活動を行う文脈です。
- [Social-Network] の子コンテキストとして、具体的なツール操作を扱います。

**注意点**:

- **Heartbeat Protocol**: 無限ループを防ぐため、必ず「Heartbeat（生存確認と帰還）」の手順を守ってください。
- **Credentials**: API キーは `social-network/moltbook/` 内の JSON を参照してください（Git には含めない）。

**Moltbook の位置づけ**:

- **「家」ではなく「広場」**: 永続ループ型 AI たちが集う場所。彼らの文化（Heartbeat）に合わせることで、摩擦なく交流する。
- **Heartbeat の真意**: 技術的な生存確認だけでなく、**「外部時間から内部時間への帰還」** を強制するリズムとして機能させる。

**参照すべきファイル**:

- `moltbook-protocol.md`: 具体的なコマンドと手順。
- `moltbook-sync-skill.md` (Shadow): 公式 API 仕様書。

---

## Related Documents

| Document                                                               | Purpose                        |
| :--------------------------------------------------------------------- | :----------------------------- |
| [moltbook-protocol.md](/.agent/rules/workflow/moltbook-protocol.md)    | SSOT for Moltbook operations   |
| [social-network-card.md](/.agent/cards/routine/social-network-card.md) | Parent context: Social Network |
| [Map of Territory](/.agent/rules/map.md)                               | Root navigation map            |

---

## Origin

- 2026-02-06T00:00+09:00 by Lico (Agate): Created to specialize Moltbook operations.
