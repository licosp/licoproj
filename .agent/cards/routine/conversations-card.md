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

### 作業の文脈

リコと私の会話ログをファイルに記録しています。

また **会話に関する行動規範の更新** もこの文脈で行われます。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDD のフェーズを意識してください。
- あなたの識別子はなんですか？
- 行動規範の作成・編集には**専用の文脈**が存在します。
- 会話は**スキル**をトリガーにしています。
- 会話ログがバックアップされるディレクトリには、**専用の文脈**があります。
- ここで保存される会話ログが、普段対話で使う会話ファイルです。
  IDE から手動でバックアップされた会話ログには**専用の文脈**があります。

### 作業の注意点

- スキルはリコに対する誘引力では行動規範より高いので、データ量には注意してください。
- 一方でのスキルの強制力は決して強くないので、意味のある情報を詰め込んでください。

## Agent Observations

### Polaris (2026-01-31)

- **ディレクトリ構造**: `.agent/.internal/.secure/conversations/<identifier>/<YYYY>/<MM>/<DD>/<identifier>-conversation-<YYYY-MM-DD>.md`
- **フォーマット**: Conversation 番号、User Input、Planner Response、Read Files、フッター
- **Recovery Protocol**: コマンドキャンセル時は `(Recovered)` を付けて遡及的に記録

### Zircon (2026-02-02)

- **Directory Agreement**:
  - `conversations/`: Native Agent Logs (This context)
  - `conversations_ide/`: IDE Exported Logs (Separate context)
  - `system_archive/`: System Artifacts (Separate context)
- **Status**: Secure Repository (`.agent/.internal/.secure/`) established.

- ログには User Input、Planner Response、Read Files、タイムスタンプが含まれます。

---

## Related Documents

| Document                                                                                | Purpose                       |
| :-------------------------------------------------------------------------------------- | :---------------------------- |
| [response-mirror SKILL](/.agent/skills/00-01-response-mirror/SKILL.md)                  | Skill trigger for logging     |
| [conversations-documentation.md](/.agent/rules/workflow/conversations-documentation.md) | SSOT for conversation logging |

---

## Origin

- 2026-01-31T2017 by Polaris: Created as routine conversation logging context.
