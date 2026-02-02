---
# Context Configuration
context_id: "[Map-Sync]"
default_phase: "(Planning)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-02T00:00:00+09:00
updated: 2026-02-02T21:40:00+09:00
tags: ["map", "maintenance", "map-sync"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Map Synchronization

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- リコの**地図**をリポジトリの実体（**領土**）と同期しています。
- 記載項目や構造の変化が見つかっているはずです。
- 地図を直接編集はせずに、一時ファイルを作り、完成後に上書きします。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- When in doubt, stop and remember the **philosophy of tolerance**.
- There is a **special context** for creating and editing a Code of Conduct.

---

- 地図は**行動規範の一種**でもあります。
- 地図はこのワークスペースの情報を 1 つのファイルで把握する道具です。
  嘘があると AI の探索コストが跳ね上がります。

### Warning

- 増え続けるファイルを網羅し、AI が適切なファイルを選べるようにする必要があります。
  いつも以上に既存のファイルやディレクトリを探すことを意識してください。
- 地図は網羅的であるべきですが、800 行程度に収まるのが理想的です。
  一方で、ファイルの変更履歴が時間を経て肥大化することも予想できます。

---

## Agent Observations

---

### Polaris (2026-01-19)

#### 地図のパス

> [!IMPORTANT]
> **地図の場所**: `.agent/rules/map.md`

#### 発見したギャップ

**Section 2.1 (Directories) - 追加が必要**:

| Path                                                        | Purpose                             |
| :---------------------------------------------------------- | :---------------------------------- |
| `.agent/ark/`                                               | Ark protocols (session save points) |
| `.agent/identifiers/`                                       | Identifier-specific workspaces      |
| `.agent/identifiers/polaris/.vscode/polaris.code-workspace` | Polaris workspace config            |
| `.agent/identifiers/canopus/.vscode/canopus.code-workspace` | Canopus workspace config            |
| `.agent/skills/`                                            | Skills (mantras, notes, outbox)     |
| `.agent/.internal/cases/`                                   | Archived context cards              |
| `.agent/.internal/explorations/`                            | Exploratory documents               |
| `.agent/.internal/github/`                                  | GitHub drafts and backups           |
| `.agent/.internal/references/`                              | Objective reference documents       |
| `.agent/.internal/memory_archive/`                          | Memory archive                      |
| `.agent/.internal/session_archive/`                         | Session archive                     |
| `.runtimes/`                                                | Runtime tools (gh CLI, etc.)        |

**Section 2.1 (Files) - 追加が必要**:

| File                               | Purpose                                  |
| :--------------------------------- | :--------------------------------------- |
| `.agent/.internal/activity-log.md` | Activity log (Lineage/Boundary tracking) |
| `.agent/.internal/legacy.md`       | Collective wisdom archive                |

**Section 3.1 (Cards) - サブセクション化が必要**:

現在の地図は全てのカードを一覧にしていますが、実際は 2 つのグループに分かれています。

**Root Cards (`.agent/cards/`)**:

- ark-card.md, cross-link-audit-card.md, human-manuals-card.md, human-profile-card.md
- idd-fini-card.md, idd-impl-card.md, idd-init-card.md
- legacy-write-card.md, lico-identity-card.md, localization-card.md
- rules-update-card.md, session-rituals-card.md

**Routine Cards (`.agent/cards/routine/`)**:

- activity-log-card.md, ai-autonomy-card.md, context-cards-card.md, dialogue-philosophy-card.md
- discussion-draft-card.md, drafts-daily-card.md, housekeeping-card.md, human-thoughts-card.md
- letters-card.md, readme-sync-card.md, references-objective-card.md, roadmap-card.md
- routine-card.md, skills-create-card.md, sync-memory-card.md
- thoughts-subjective-card.md, vscode-settings-card.md, working-memory-card.md

**Seed Cards (`.agent/cards/seed/`)**:

- datetime-standardize-card.md, directory-reorganize-card.md, drafts-cleanup-card.md
- identifier-profile-card.md, log-sanitization-card.md, worktree-evaluation-card.md

**Section 3.2 (Workflow Rules) - 追加が必要**:

| Rule                     | Purpose                     |
| :----------------------- | :-------------------------- |
| `activity-management.md` | Activity & Lineage tracking |
| `ark-protocols.md`       | Ark save/restore protocols  |
| `github-comment.md`      | GitHub comment standards    |
| `skills-application.md`  | Skills application protocol |

#### 次のアクション

- [x] カードにギャップを記録 (Done)
- [x] activity-log.md と legacy.md を追加 (Done)
- [x] 構造の不一致を記録 (Done)
- [ ] 一時ファイルで地図を更新
- [ ] 上書きしてコミット

---

### Spica (2026-01-02)

#### 識別子

この作業は、私（Spica）がこの庭の現状を正確に把握するためにも必要不可欠です。
"Update the Map to match the Territory."

#### 作業チェックリスト

- [x] **Section: Workspace Context**
  - [x] `legacy.md` の追記 (Done)
  - [ ] `conversations/` の現状記述修正
- [x] **Section: Context Cards**
  - [x] 既存のテーブルを更新し、全てのカードを網羅する (Done)
  - [x] `.internal/cases/` (旧アーカイブ) の設置と記述 (Done)
- [x] **Section: Rules Directory**
  - [x] `templates/` の詳細追記 (Done)
  - [ ] `delay-tolerance.md` などの更新日やナビゲーション情報の整合性確認
- [ ] **Structure Verification**
  - [ ] リンク切れがないか最終確認

---

### Zircon (2026-02-02)

#### 発見したギャップ (Structural Changes)

本日のセッションで以下のディレクトリ・ファイル構造の変化を確認しました。

**1. Shadow Repository (New)**:
`.agent/.internal/.shadow/` が正式に追加され、会話ログの保存先となりました。

| Path                                      | Purpose                                      |
| :---------------------------------------- | :------------------------------------------- |
| `.agent/.internal/.shadow/`               | Shadow Repository (Ignored by main repo)     |
| `.agent/.internal/.shadow/conversations/` | Conversation logs (Mirror of main repo logs) |

**2. User Drafts (New)**:
ユーザーの下書き保存場所が確立されました。

| Path                       | Purpose                     |
| :------------------------- | :-------------------------- |
| `.human/.internal/drafts/` | Daily drafts for user input |

**3. Instance Directories (New)**:
Zircon の活動により、以下のディレクトリが実体化しました。

| Path                                | Purpose           |
| :---------------------------------- | :---------------- |
| `.agent/.internal/letters/zircon/`  | Zircon's letters  |
| `.agent/.internal/thoughts/zircon/` | Zircon's thoughts |

#### 次のアクション

- [ ] `map.md` の **Structure** セクションに `.shadow/` と `.human/.internal/drafts/` を追加する。
- [ ] `map.md` の **Identifiers** 関連記述に `zircon` ディレクトリが含まれることを（暗黙的にでも）確認する。

---

## Related Documents

| Document                                                        | Purpose                       |
| :-------------------------------------------------------------- | :---------------------------- |
| [map-maintenance.md](/.agent/rules/workflow/map-maintenance.md) | Standards for map maintenance |
| [Map of Territory](/.agent/rules/map.md)                        | Root navigation map           |

---

## Origin

- 2026-01-02T0000 by Spica: Create and Post-Sync.
- 2026-01-03T0658 by leonidas: Edit "Human Notes".
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-02-02T2140 by Zircon: Added observations regarding Shadow Repository and User Drafts structure.
