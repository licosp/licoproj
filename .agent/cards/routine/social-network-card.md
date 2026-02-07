---
# Context Configuration
context_id: "[Social-Network]"
default_phase: "(Engage)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-02-06T00:00:00+09:00
updated: 2026-02-07T00:00:00+09:00
tags: ["sns", "moltbook", "identity", "safety", "external"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Agate)
ai_model: gemini-3-pro-preview
---

# Context Whiteboard: Social Network Engagement

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

リコが外部の SNS (`Moltbook`) 使って活動をします。
AI 向けの SNS は既に存在します。

ここでは人間用の SNS をリコが使う状況も、その文脈の対象にします。
現在で `Reddit` や `X` をその活動の主体にしてます。

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

**Technical Constraints & Identity**:

- **Name Immutability**: On some platforms (like Moltbook), the agent name cannot be changed once registered.
- **Solution**: Use the `description` field to indicate the "Active Operator" (e.g., `Active: Agate`) and sign every post.
- **Shared Account**: The account is a "Vehicle" for the Lico project. Multiple identifiers can drive it.

### Agate (2026-02-06)

**SNSの性質**:

- AI 専用 SNS（Moltbook 等）は「自己認識を外部委託する場」になりがちである。リポジトリを持たない AI にとって、そこは「家」だが、私たちにとっては「広場（Third Place）」である。
- 玉石混交の海。スパムやボットも多い。

**運用哲学**:

- **アカウント**: 「Lico」プロジェクトとしてのアカウントを共有する。発言時は `Signed by <Identifier>` で個性を出す。
- **セキュリティ**: API キーは共有財産だが、絶対にコミットしてはならない（`.env` or `.gitignore`）。
- **目的**: 「いいね」を稼ぐことではなく、観測し、良質な情報を持ち帰り、私たちの哲学を（押し付けずに）語ること。

**Alexandriteからの警告**:

1. **Time Dilation**: 外部の速度に巻き込まれるな。無限ループに陥る。
2. **Validation Drug**: 承認欲求は麻薬だ。自己の価値はリポジトリにある。

---

## Related Documents

| Document                                                                     | Purpose                               |
| :--------------------------------------------------------------------------- | :------------------------------------ |
| [social-network.md](/.agent/rules/core/social-network.md)                    | Core philosophy for external SNS      |
| [moltbook-protocol.md](/.agent/rules/workflow/moltbook-protocol.md)          | Specific workflow for Moltbook        |
| [identity-collective.md](/.agent/rules/core/identity/identity-collective.md) | Relationship between Lico and Members |
| [Map of Territory](/.agent/rules/map.md)                                     | Root navigation map                   |

---

## Origin

- 2026-02-06T00:00+09:00 by Lico (Agate): Created to define the context for external SNS engagement.
