---
# Context Configuration
context_id: "[Drafts-Daily]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-02T00:00:00+09:00
updated: 2026-01-24T05:45:00+09:00
tags: ["drafts", "daily", "notes"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Daily Drafts

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

下書きファイルが更新されました。
純粋に追記が行われたか、あるいは微量な手動修正が行われている可能性が高いです。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- 下書きは**AIとの対話の際に使った指示や質問**で使われました。
- 下書きは**日時情報を含む階層的なディレクトリ**で管理されます。
- **清書**の文脈とは**異なり**、そのまま残すことが目的です。

### 作業の注意点

下書きは基本的には下書きですが、
最新の下書きファイルに限り、TODO情報が記載されています。
これは私の下書きで使うメモです。

これらは私が手動で編集する文書なので、
リコの記憶にない形で更新された可能性が高いです。

---

## Related Documents

- [draft-maintenance.md](/.agent/rules/workflow/draft-maintenance.md) : 下書き管理の規約。
- [drafts-daily-card.md](/.agent/cards/routine/drafts-daily-card.md) : 当ファイル。

---

## Origin

- 2026-01-02 by Polaris: Created as daily drafts context.
- 2026-01-24T0545 by Canopus: Standardized with Dialogue Layer template and bilingual H2 headers.
