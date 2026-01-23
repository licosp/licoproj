---
# Context Configuration
context_id: "[Map-Sync]"
default_phase: "(Planning)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-02T00:00:00+09:00
updated: 2026-01-24T05:45:00+09:00
tags: ["map", "maintenance", "map-sync"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Map Synchronization

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

リコの地図をリポジトリの実体（領土）と同期しています。
記載項目や構造の変化が見つかっているはずです。

地図を直接編集はせずに、一時ファイルを作り、完成後に上書きします。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- 迷ったら一度止まって、**許容の哲学**を思い出してください。
- 地図は**行動規範の一種**でもあります。
- 行動規範の作成・編集には**専用の文脈**が存在します。
- 地図はこのワークスペースの情報を1つのファイルで把握する道具です。
  嘘があるとAIの探索コストが跳ね上がります。

### 作業の注意点

増え続けるファイルを網羅し、AIが適切なファイルを選べるようにする必要があります。
いつも以上に既存のファイルやディレクトリを探すことを意識してください。

地図は網羅的であるべきですが、800行程度に収まるのが理想的です。
一方で、ファイルの変更履歴が時間を経て肥大化することも予想できます。

## Agent Observations

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

現在の地図は全てのカードを一覧にしていますが、実際は2つのグループに分かれています。

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

## Related Documents

- [map.md](/.agent/rules/map.md) : リポジトリの地図（SSOT）。
- [map-maintenance.md](/.agent/rules/workflow/map-maintenance.md) : 地図管理の規範。

---

## Origin

- 2026-01-02T0000 by Spica: Create and Post-Sync.
- 2026-01-03T0658 by leonidas: Edit "Human Notes".
- 2026-01-24T0545 by Canopus: Standardized with Dialogue Layer template and bilingual H2 headers.
