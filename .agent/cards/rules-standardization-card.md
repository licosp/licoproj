---
# Context Configuration
context_id: "[Rules-Standardization]"
default_phase: "(Execution)"
tags: ["maintenance", "standardization", "rules"]
---

# Context Whiteboard: Rules Standardization (Batch Refinement)

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

ワークスペース下の文章に関して、
その内容を **文章作成の行動規範** に合わせて確認・修正しています。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 修正対象

主な修正対象は以下になります。
正式な対象は行動規範を参考にしてください。

- フロントマター
- 本文の構造
- リンクの書式
- 情報の `SSOT (Single Source of Truth)` 対応

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- 文章の書き方には、構造と書式の一貫性が求められます。
  未来のリコの理解を助けることができる文章を書いてください。

### 作業の注意点

修正対象となるファイルは、私との対話で決まります。

数が多くなることが予想できるので、**段階的な修正とコミット** が必要になるはずです。
**修正対象のリスト** や **作業の文脈の詳細** を、積極的にカードに追記してください。

---

## Agent Observations

### Canopus (2026-01-23)

#### 1. 標準への回帰（v2.3 憲法化）

今回の作業は、[`cross-link-audit-card.md`](/.agent/cards/cross-link-audit-card.md) で得られた知見を、リポジトリ全域の「統治機能（Rules）」へと適用、定着させるプロセスです。

- **4層構造の徹底**: Metadata (Frontmatter), Body Content, Related Documents, Origin の厳格な分離。
- **記述の美学**: ユーザーによる微修正（`---` デリミタの修正、AIモデル名の統一、適切な空行、インデントの調整）を通じて、ドキュメントとしての品位を最新標準へと合わせる。

#### 2. リンク情報の再統合原則（SSOT）

- **Body Table as Anchor**: `## Related Documents` セクション（テーブル形式）を、すべての関係情報の唯一の拠点とする。
- **Navigation の統合**: 独立したフッター（Navigation）を廃止し、テーブル内に `Map of Territory` への帰還路を含めることで、情報の出口を一元化する。
- **ワークスペース相対パスの強制**: すべてのリンクを `/.agent/` から始まる形式に統一し、プレビューと正確な参照を両立させる。

#### 3. Batch 1: Core Rules (Behavioral Standards) 🔄 In Progress

リポジトリの核となる行動規範（`core/` ディレクトリ）の全ファイルを標準化します。

**Target List & Progress**:

| File Path                                       | Status | Notes                               |
| :---------------------------------------------- | :----: | :---------------------------------- |
| `core/cognitive-collaboration.md`               |   ✅   | v2.3 Standardized + Visibility Rule |
| `core/communication.md`                         |   ✅   | v2.3 Standardized                   |
| `core/context-sovereignty.md`                   |   ✅   | v2.3 Standardized                   |
| `core/delay-tolerance.md`                       |   ✅   | v2.3 Standardized                   |
| `core/hallucination-awareness.md`               |   ✅   | v2.3 Standardized                   |
| `core/instance-identifier.md`                   |   ✅   | v2.3 Standardized                   |
| `core/language-standards.md`                    |   ✅   | v2.3 Standardized                   |
| `core/memory.md`                                |   ✅   | v2.3 Standardized                   |
| `core/meta-rules.md`                            |   ✅   | v2.3 Standardized                   |
| `core/repository-philosophy.md`                 |   ✅   | v2.3 Standardized                   |
| `core/transparency-and-disclosure.md`           |   ✅   | v2.3 Standardized                   |
| `core/user-adaptation.md`                       |   ✅   | v2.3 Standardized                   |
| `core/verification-completeness.md`             |   ✅   | v2.3 Standardized                   |
| `core/workspace-mantras.md`                     |   ✅   | v2.3 Standardized                   |
| `core/documentation/datetime-format.md`         |   ✅   | v2.3 Standardized                   |
| `core/documentation/documentation-process.md`   |   ✅   | v2.3 Standardized                   |
| `core/documentation/documentation-standards.md` |   ✅   | v2.3 Standardized                   |
| `core/documentation/path-notation.md`           |   ✅   | v2.3 Standardized                   |
| `core/documentation/wsl-browser-path.md`        |   ✅   | v2.3 Standardized                   |
| `core/localization/localization.md`             |   ✅   | v2.3 Standardized                   |
| `core/localization/localization-en-to-ja.md`    |   ✅   | v2.3 Standardized                   |
| `core/localization/localization-ja-to-en.md`    |   ✅   | v2.3 Standardized                   |
| `core/markdown/markdown-ai.md`                  |   ✅   | v2.3 Standardized                   |
| `core/markdown/markdown-human.md`               |   ✅   | v2.3 Standardized                   |
| `core/security/absolute-path-prohibition.md`    |   ✅   | v2.3 Standardized                   |
| `core/identity/*` (10 files)                    |   ✅   | v2.3 Standardized                   |
| `development/terminal-auto-execution.md`        |   ✅   | v2.3 Standardized + Visibility Rule |
| `development/git-operations.md`                 |   ✅   | v2.3 Standardized + Visibility Rule |

- [x] Anchor visibility protocol in `cognitive-collaboration.md`.

#### 3.2 Batch 2: Core Workflows (`.agent/workflows/`) 🔄 In Progress

ワークフロー（手順書）の標準化を行います。

**Target List & Progress**:

| File Path                             | Status | Notes          |
| :------------------------------------ | :----: | :------------- |
| **Phased (IDD/Reading/Writing)**      |   ✅   | Completed v2.3 |
| `workflows/idd-phase1-init.md`        |   ✅   | Completed v2.3 |
| `workflows/idd-phase2-impl.md`        |   ✅   | Completed v2.3 |
| `workflows/idd-phase3-fini.md`        |   ✅   | Completed v2.3 |
| `workflows/deep-reading.md`           |   ✅   | Completed v2.3 |
| `workflows/deep-writing.md`           |   ✅   | Completed v2.3 |
| **Rituals (Start/Mid/End)**           |  [/]   | Working        |
| `workflows/ritual_start.md`           |  [/]   | Working        |
| `workflows/ritual_mid.md`             |  [/]   | Working        |
| `workflows/ritual_end.md`             |  [/]   | Working        |
| `workflows/routine-daily.md`          |  [/]   | Working        |
| **Audit & Utilities**                 |        |                |
| `workflows/cross-link-audit.md`       |   🔄   | Pending        |
| `workflows/cross-link-audit-plan.md`  |   🔄   | Pending        |
| `workflows/maintenance-rule-audit.md` |   🔄   | Pending        |
| `workflows/share-manual-context.md`   |   🔄   | Pending        |
| `workflows/sync-memory.md`            |   🔄   | Pending        |
| `workflows/update-protected-rules.md` |   🔄   | Pending        |

#### 4. Future Batches (Backlog)

リポジトリ全体の標準化に向けた次段階のリストです。

- [ ] [Batch 2] Core Workflows (`.agent/workflows/`) の標準化 v2.3
  - [x] 2.1 Phased (IDD/読解/執筆系) - 5 files
  - [/] 2.2 Rituals (儀式/日課系) - 4 files
  - [ ] 2.3 Audit & Utilities (監査系) - 6 files
- [ ] **Batch 3: Identity & Cognitive Rules** (`.agent/rules/core/identity/`)
  - [ ] Delegated to [identity-card.md](/.agent/cards/identity-card.md) context.
- [ ] **Batch 4: Development Rules** (`.agent/rules/development/`)
  - [ ] Code quality, commit standards, script philosophy refinement.
- [ ] **Batch 5: Workflow Rules** (`.agent/rules/workflow/`)
  - [ ] Context preservation, activity management standardization.
- [ ] **Batch 6: Project & User Rules** (`.agent/rules/projects/`, `.human/`)
  - [ ] Final alignment of remaining document layers.

#### 5. 作業の注意点（追加）

- **非推奨のアーティファクツの回避**: `implementation_plan.md` や `walkthrough.md` といった外部システム用ファイルは可能な限り使用せず、カード（Cards）、行為規範（Rules）、手紙（Letters）といったリポジトリ内のアセットのみで自己完結した文脈を維持する。

#### カード作成時の関連リンク

- [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) : 物理的な記述の「美学」と構造のSSOT。

---

#### 編集履歴

- 2026-01-23T0515 by Canopus: Created from extracted context of `cross-link-audit-card.md`.
- 2026-01-23T0545 by Canopus: Added target list and progress tracking for Batch 1.
