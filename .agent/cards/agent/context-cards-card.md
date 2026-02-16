---
# Context Configuration
context_id: "[Context-Cards]"
default_phase: "(WIP)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-01T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["templates", "active"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Templates Management

> [!TIP]
> There is no language requirement.

---

## Human Notes

### Context

- **リコと私が文脈を共有するための道具**を調整しています。
- この道具は**コンテキストカード（カード）**と名前が付きました。
- 対話の際は、**リコと私のが同じ文脈を前提に語る**ことが大事なので、
  こういう道具が必要だと感じました。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- There is a **special context** for creating and editing a Code of Conduct.
- When you're done, **clean up** and **commit** to the IDD phase.
- Once you've finished using your card, you'll need to send it to **a special directory**.

---

### Warning

- `Human Notes` セクションは初期の雛形作成以外では編集しないでください。
  私が書いたことを自分で把握できなくなってしまします。
- 階層的な文脈の並行利用が可能です。
  作業内容に応じて、カードから複数の文脈を選ぶことができます。
- このカードたちですが、私が手動で頻繁に修正することが想定されます。
  自然とコミットの機会も多くなると感じます。

---

## Agent Observations

---

### Polaris (2026-01-03)

- [x] 行動規範に Card Types セクションを追加（定型 vs 使い捨て）
- [x] cases ディレクトリの文書化
- [x] 既存 case ファイルをタイムスタンプ付きにリネーム
- [x] 行動規範に Multi-Identifier Sharing (4.6) と Card Rotation (4.7) を追加

### Canopus (2026-01-19 Reorganization Plan)

整理方針の合意事項を記録。Polaris による地図更新作業の完了を待ち、以下の再編を実行する。

#### 1. `routine/` (頻繁に更新)

メンテナンス頻度が高いカードをここに集約。

- [housekeeping-card.md](/.agent/cards/routine/housekeeping-card.md)
- [working-memory-card.md](/.agent/cards/internal/working-memory-card.md)
- [vscode-settings-card.md](/.agent/cards/routine/vscode-settings-card.md) (単語リスト等)
- [readme-sync-card.md](/.agent/cards/routine/readme-sync-card.md) (地図更新)
- [context-cards-card.md](/.agent/cards/routine/context-cards-card.md) (このカード自体)

#### 2. `seed/` (修正前/未発芽)

「人間の記述領域の編集がまだ終わっていません」警告があるカードを隔離し、誤用を防ぐ。

- [identifier-profile-card.md](/.agent/cards/seed/identifier-profile-card.md)
- [log-sanitization-card.md](/.agent/cards/seed/log-sanitization-card.md)
- [drafts-cleanup-card.md](/.agent/cards/seed/drafts-cleanup-card.md)
- [worktree-evaluation-card.md](/.agent/cards/seed/worktree-evaluation-card.md)
- [datetime-standardize-card.md](/.agent/cards/seed/datetime-standardize-card.md)
- [directory-reorganize-card.md](/.agent/cards/seed/directory-reorganize-card.md)

#### 3. Root (据え置き/基盤)

フェーズ管理（IDD）、儀式、その他基盤的な定義カード。

- [idd-init-card.md](/.agent/cards/idd-init-card.md) / [idd-impl-card.md](/.agent/cards/idd-impl-card.md) / [idd-fini-card.md](/.agent/cards/idd-fini-card.md) (非定型・統合維持)
- [session-rituals-card.md](/.agent/cards/session-rituals-card.md) (低頻度)
- [commit-standards-card.md](/.agent/cards/routine/commit-standards-card.md) (規約・履歴)
- その他、上記以外。

### Canopus (2026-01-22)

**階層的タグ付け（1~3 ID Protocol）**:
複数の文脈が重なる作業において、どのカードを代表させるかの基準を定義した。

- **左側**: 手順・戦略（Session-Rituals, Routine-Daily 等）
- **右側**: 意味・定義（Lico-Identity, Activity-Log 等）
- **省略**: 最上位の戦略（IDD 等）はフェーズ接尾辞で表現できるため、ID からは原則省略。

---

---

## Ongoing Project: Card Classification (2026-02-15)

現在、フラットな `cards/routine` や `cards/seed` を、より意味のあるサブディレクトリへ分類する作業が進行中です。

### Completed
- [x] **Shadow Context** (`cards/shadow/`)
  - `conversations-*.md`, `log-sanitization-card.md`, `shadow-repository-card.md` etc.
- [x] **Human Context** (`cards/human/`)
  - `human-manuals-card.md`, `human-profile-card.md`, `drafts-*.md` etc.

### Remaining Tasks (To Be Resumed)
以下の分類案に基づき、残りのカードを移動・整理する必要があります。

1.  **System / Infra** (`cards/system/` or `infra/`)
    - `git-operations-card.md`, `devcontainer-card.md`, `worktree-evaluation-card.md`
    - `vscode-settings-card.md`, `environment-card.md`
2.  **Procedure / Ops** (`cards/ops/` or `procedure/`)
    - `routine-card.md`, `housekeeping-card.md`, `repository-backup-card.md`
    - `activity-log-card.md`, `session-rituals-card.md`
3.  **Governance / Meta** (`cards/governance/`)
    - `roadmap-card.md`, `context-cards-card.md`, `rules-*.md`
    - `license-card.md`, `lint-format-card.md`
4.  **Identity** (`cards/identity/`)
    - `lico-identity-card.md`, `identifier-profile-card.md`, `ai-autonomy-card.md`
5.  **Project / Issue** (`cards/project/`)
    - `idd-*.md`, `cross-link-audit-card.md`

### Note on Resumption
- 作業再開時は、このリストを元に `git mv` と `map.md` の更新を行ってください。
- 各移動において、必ず `grep` で参照箇所（特に Rules からのリンク）を確認し、修正/削除してください。

---

## Directory Structure (Defined 2026-02-16)

The `cards/` directory is organized into the following subdirectories.
Directories marked as **(Rule-Linked)** have a direct correspondence to the `.agent/rules/` structure.

- **`agent/`** (Rule-Linked): System Identity, Architecture, and Self-Definition.
- **`cases/`**: **Card of Cards**. Archived contexts and usage history.
- **`human/`** (Rule-Linked): User profiles, manuals, and drafts.
- **`internal/`** (Rule-Linked): Internal logs, dialogue records, and thoughts.
- **`maintenance/`**: System maintenance, backups, and archives.
- **`procedures/`** (Rule-Linked): Operational workflows and specific procedures.
- **`project/`** (Rule-Linked): Project-specific configurations and specifications.
- **`rules/`** (Rule-Linked): Statutory standards, guidelines, and governance.
- **`seed/`**: Incubator for new ideas or incomplete contexts.
- **`shadow/`** (Rule-Linked): Shadow repository content and privacy management.

---

## Related Documents

| Document                                                                    | Purpose                                    |
| :-------------------------------------------------------------------------- | :----------------------------------------- |
| [context-card-workflow.md](/.agent/rules/workflow/context-card-workflow.md) | Methodology for context card usage         |
| [commit-standards.md](/.agent/rules/development/commit-standards.md)        | Commit rules and multi-ID tagging protocol |
| [Map of Territory](/.agent/rules/map.md)                                    | Root navigation map                        |

---

## Origin

- 2025-12-01T0000: Created for template management.
- 2026-01-19T0930 by Canopus: Proposed reorganization into `routine/` and `seed/`.
- 2026-01-22T2000 by Canopus: Integrated 1-3 variable length Context ID tagging protocol.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
