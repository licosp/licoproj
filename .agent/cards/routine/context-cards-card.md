---
# Context Configuration
context_id: "[Context-Cards]"
default_phase: "(WIP)"
tags: ["templates", "active"]
---

# Context Whiteboard: Templates Management

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

「リコと私が文脈を共有するための道具」を調整しています。
この道具は「コンテキストカード（カード）」と名前が付きました。

対話の際は、リコと私のが同じ文脈を前提に語ることが大事なので、
こういう道具が必要だと感じました。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- 行動規範の作成・編集には**専用の文脈**が存在します。
- カードを使い終わったら、専用のディレクトリに送る必要があります。
- コミットをする際は、IDDのフェーズを意識してください。

### 作業の注意点

階層的な文脈の並行利用が可能です。
作業内容に応じて、カードから複数の文脈を選ぶことができます。

このカードたちですが、私が手動で頻繁に修正することが想定されます。
自然とコミットの機会も多くなると感じます。

## Agent Observations

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
- [working-memory-card.md](/.agent/cards/routine/working-memory-card.md)
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
- **省略**: 最上位の戦略（IDD等）はフェーズ接尾辞で表現できるため、IDからは原則省略。

#### 関連リンク

| Document                                                                    | Purpose                                    |
| :-------------------------------------------------------------------------- | :----------------------------------------- |
| [context-card-workflow.md](/.agent/rules/workflow/context-card-workflow.md) | Methodology for context card usage         |
| [commit-standards.md](/.agent/rules/development/commit-standards.md)        | Commit rules and multi-ID tagging protocol |
| [Map of Territory](/.agent/rules/map.md)                                    | Root navigation map                        |

---

#### 編集履歴

- 2025-12-01T0000: Created for template management.
- 2026-01-19T0930 by Canopus: Proposed reorganization into `routine/` and `seed/`.
- 2026-01-22T2000 by Canopus: Integrated 1-3 variable length Context ID tagging protocol.
- 2026-01-22T2215 by Canopus: Aligned with v2.3 constitutional standards (4-layer structure).
