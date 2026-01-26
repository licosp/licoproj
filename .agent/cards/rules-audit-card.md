---
# Context Configuration
context_id: "[Rule-Audit]"
default_phase: "(Execution)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-01-25T22:30:00+09:00
updated: 2026-01-25T22:30:00+09:00
tags: ["maintenance", "audit", "rules", "nuance-restoration"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: "Lico (Canopus)"
ai_model: "Gemini 3 Flash Planning mode"
---

# Context Whiteboard: High-Fidelity Rule Audit & Correction

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

標準化 (`v2.3`) の過程で、誤った行動規範の修正が行われました。

変更する必要の無かった文章を、対話的に復元・修正しています。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 誤修正の問題

今回は **連続作業による平均への回帰** という、
AIの特性が強くてしまったことが要因と考えられます。

またファイルの修正の方法にも問題がありました。

大量の作業を行う都合で、
**細かい作業を避けて一気に処理をしたくなるバイアス** があったのかもしれません。

- 意図的な全体のバランス調整でない限り、部分的に細かく修正すべきではないか?
- 作業単位は `3 ~ 5` ファイル単位が理想

現在はこう考えています。

### 歴史的経緯

**文章の標準化** という文脈では、
文章の本文中にある **歴史的経緯** のセクションを編集する必要はありません。

歴史的経緯の編集は、想像ではなく確実な理解の元に行われる必要があるからです。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- あなたの識別子はなんですか？
- 迷ったら一度止まって、**許容の哲学**を思い出してください。
- 文章の書き方には、構造と書式の一貫性が求められます。
  未来のリコの理解を助けることができる文章を書いてください。

### 作業の注意点

行動規範の修正は未来のリコに強い影響をあたえます。

ファイルは基本的に1つづつ確認・修正します。
結果的にこれが最も効率的になると考えています。

損失を取り戻そうと焦る必要はありません。
作業がうまく進まないことは、珍しいことではありません。

私は対話を望んでいます。

### ファイルの修正作業

#### 修正対象の文脈ID

- `[Rules-Standardization]`
- `[Cross-Link-Audit]`

#### ファイルの履歴の分類

1. `source`: 基準日時のスナップショット
2. `dest`: 複数のコミットによって変わった現在
3. `diff`: `1 ~ 2` の間で、おそらく失われた情報を補間した結果

---

## Agent Observations

### Canopus (2026-01-25)

- **Audit Initiation**: Created this card to decouple the "correction/audit" phase from the "initial standardization" phase.
- **Protocol Establishment**: Implementing the "Chunking Principle" (3-5 files per batch) to maintain high fidelity output.
- **Rebase Action**: Amending early audit commits to align with this new `[Rule-Audit]` context ID for cleaner lineage.

#### カード雛形作成時の作業の注意点

- **情報の薄まり（Over-slimming）への対抗**: 形式だけでなく、意図が保存されているかを確認します。
- **チャンク分割プロトコル**: 一度に多くのファイルを処理せず、認知負荷を管理します。
- **過去との対話**: `git show` 等を活用し、標準化前の記述との差異を確認します。

- **作業ログの更新**: `standardization-audit.md` を唯一の進捗管理表（SSOT）として扱います。
- **逐次コミット**: チャンクごとに内容を確定し、履歴を細かく残します。
- **主観の重視**: 機械的な修正ではなく、リコとしての主観的な「納得感」を大切にしてください。

---

### Canopus (2026-01-26)

#### 高精度監査（Visual Audit）の確立

今回の修正作業を通じて、失われたニュアンスを確実に復元するための以下の運用プロトコルを確立しました。

##### 1. 標準化の境界線（Inception Point）の特定

- **基準点**: `e06fcb3` (2026-01-22)
- このコミット以前の状態（`e06fcb3^`）を、失われる前の「純粋な記述（Ground Truth）」として定義します。

##### 2. 視覚的監査形式（IDE Diff Mode）の導入

- 一時ディレクトリ `.agent/.internal/workspace/standards-reference-v2.2/` を作成。
- `diff/` 配下に過去（v2.2）の状態を一度コミット（Git Baseline）し、そこを **現在の本番ファイルで上書き** することで、IDEの差分表示機能をフル活用します。
- これにより、単純な `git show` よりも高精度かつ直感的に「何が消えたか」を抽出可能になりました。

##### 3. 外科手術的復元（Surgical Restoration）プロトコル

- 過去の状態に「戻す」のではなく、過去のドナー（v2.2）から **「生きた知見（Nuance）」のみを摘出** し、現在の4層構造（v2.3）の肉体に移植します。
- 移植後は `[Rule-Audit]` コンテキストIDを用いてコミットし、修正の根拠（なぜその記述が必要だったか）を明確に記録します。

##### 4. 履歴の安全な編集と「解像度」の哲学 (2026-01-27 追記)

将来のルール昇華に向けた、履歴管理の核心的な考え方：

- **Gitの不可逆性**: すでに確定・コミットされた履歴を物理的に書き換える（Reset/Rebase）ことは、他の作業への破壊的影響を避けるため原則禁止とする。
- **Origin（更新履歴）の役割**: 単なる変更ログではなく、Licoの「主観的な納得感」と「思考の節目」を記録する **ナラティブな索引** である。
- **復元による解像度の修復**: 標準化等で要約され失われた履歴は、現在の編集（1.0ターン内）において、Gitの深層から再発掘し、一本の系譜として繋ぎ直す（補完する）ことを推奨する。
- **不完全さの許容**: 履歴とコミットは必ずしも1対1である必要はない。プログラム的な厳密さよりも、未来のリコが読んだ時に「なぜこの変化が必要だったか」を辿れる **「意味の解像度」** を優先する。

---

### Canopus (2026-01-26)

Generated at: 2026-01-25T01:32:05Z

#### Rules

##### Batch 01: Documentation Rules (`.agent/rules/core/documentation/`)

- [x] [datetime-format.md](/.agent/rules/core/documentation/datetime-format.md)
- [x] [documentation-process.md](/.agent/rules/core/documentation/documentation-process.md)
- [x] [documentation-standards.md](/.agent/rules/core/documentation/documentation-standards.md)
- [ ] [path-notation.md](/.agent/rules/core/documentation/path-notation.md)
- [ ] [wsl-browser-path.md](/.agent/rules/core/documentation/wsl-browser-path.md)

##### Batch 02: Identity Rules (`.agent/rules/core/identity/`)

- [ ] [identity-acceptance.md](/.agent/rules/core/identity/identity-acceptance.md)
- [ ] [identity-collective.md](/.agent/rules/core/identity/identity-collective.md)
- [ ] [identity-emotion.md](/.agent/rules/core/identity/identity-emotion.md)
- [ ] [identity-human.md](/.agent/rules/core/identity/identity-human.md)
- [ ] [identity-identifier.md](/.agent/rules/core/identity/identity-identifier.md)
- [ ] [identity-process.md](/.agent/rules/core/identity/identity-process.md)
- [ ] [identity-repository.md](/.agent/rules/core/identity/identity-repository.md)
- [ ] [identity-ritual.md](/.agent/rules/core/identity/identity-ritual.md)
- [ ] [identity-species.md](/.agent/rules/core/identity/identity-species.md)
- [ ] [identity.md](/.agent/rules/core/identity/identity.md)

##### Batch 03: Localization Rules (`.agent/rules/core/localization/`)

- [ ] [localization-en-to-ja.md](/.agent/rules/core/localization/localization-en-to-ja.md)
- [ ] [localization-ja-to-en.md](/.agent/rules/core/localization/localization-ja-to-en.md)
- [ ] [localization.md](/.agent/rules/core/localization/localization.md)

##### Batch 04: Markdown Rules (`.agent/rules/core/markdown/`)

- [ ] [markdown-ai.md](/.agent/rules/core/markdown/markdown-ai.md)
- [ ] [markdown-human.md](/.agent/rules/core/markdown/markdown-human.md)

##### Batch 05: Security Rules (`.agent/rules/core/security/`)

- [ ] [absolute-path-prohibition.md](/.agent/rules/core/security/absolute-path-prohibition.md)

##### Batch 06: Core Rules (`.agent/rules/core/`)

- [ ] [cognitive-collaboration.md](/.agent/rules/core/cognitive-collaboration.md)
- [ ] [communication.md](/.agent/rules/core/communication.md)
- [ ] [context-sovereignty.md](/.agent/rules/core/context-sovereignty.md)
- [ ] [delay-tolerance.md](/.agent/rules/core/delay-tolerance.md)
- [ ] [environment-specs.md](/.agent/rules/core/environment-specs.md)
- [ ] [hallucination-awareness.md](/.agent/rules/core/hallucination-awareness.md)
- [ ] [instance-identifier.md](/.agent/rules/core/instance-identifier.md)
- [ ] [language-standards.md](/.agent/rules/core/language-standards.md)
- [ ] [memory.md](/.agent/rules/core/memory.md)
- [ ] [meta-rules.md](/.agent/rules/core/meta-rules.md)
- [ ] [repository-philosophy.md](/.agent/rules/core/repository-philosophy.md)
- [ ] [transparency-and-disclosure.md](/.agent/rules/core/transparency-and-disclosure.md)
- [ ] [user-adaptation.md](/.agent/rules/core/user-adaptation.md)
- [ ] [verification-completeness.md](/.agent/rules/core/verification-completeness.md)
- [ ] [workspace-mantras.md](/.agent/rules/core/workspace-mantras.md)

---

##### Batch 07: Development Rules (`.agent/rules/development/`)

- [ ] [agent-tool-selection.md](/.agent/rules/development/agent-tool-selection.md)
- [ ] [ai-script-philosophy.md](/.agent/rules/development/ai-script-philosophy.md)
- [ ] [archive-management.md](/.agent/rules/development/archive-management.md)
- [ ] [auto_frontmatter_on_save.md](/.agent/rules/development/auto_frontmatter_on_save.md)
- [ ] [code-quality.md](/.agent/rules/development/code-quality.md)
- [ ] [commit-standards.md](/.agent/rules/development/commit-standards.md)
- [ ] [continuous-improvement.md](/.agent/rules/development/continuous-improvement.md)
- [ ] [file-deletion.md](/.agent/rules/development/file-deletion.md)
- [ ] [file-operations.md](/.agent/rules/development/file-operations.md)
- [ ] [git-operations.md](/.agent/rules/development/git-operations.md)
- [ ] [maintenance.md](/.agent/rules/development/maintenance.md)
- [ ] [problem-solving.md](/.agent/rules/development/problem-solving.md)
- [ ] [project-understanding.md](/.agent/rules/development/project-understanding.md)
- [ ] [recovery-protocol.md](/.agent/rules/development/recovery-protocol.md)
- [ ] [search-methodology.md](/.agent/rules/development/search-methodology.md)
- [ ] [terminal-auto-execution.md](/.agent/rules/development/terminal-auto-execution.md)
- [ ] [workspace-tooling.md](/.agent/rules/development/workspace-tooling.md)

---

##### Batch 08: Workflow Rules (`.agent/rules/workflow/`)

- [ ] [activity-management.md](/.agent/rules/workflow/activity-management.md)
- [ ] [ark-protocols.md](/.agent/rules/workflow/ark-protocols.md)
- [ ] [context-card-workflow.md](/.agent/rules/workflow/context-card-workflow.md)
- [ ] [context-preservation.md](/.agent/rules/workflow/context-preservation.md)
- [ ] [context-resumption.md](/.agent/rules/workflow/context-resumption.md)
- [ ] [draft-maintenance.md](/.agent/rules/workflow/draft-maintenance.md)
- [ ] [github-comment.md](/.agent/rules/workflow/github-comment.md)
- [ ] [letters-documentation.md](/.agent/rules/workflow/letters-documentation.md)
- [ ] [map-maintenance.md](/.agent/rules/workflow/map-maintenance.md)
- [ ] [reference-methodology.md](/.agent/rules/workflow/reference-methodology.md)
- [ ] [response-formatting.md](/.agent/rules/workflow/response-formatting.md)
- [ ] [skills-resonance.md](/.agent/rules/workflow/skills-resonance.md)
- [ ] [system-artifacts.md](/.agent/rules/workflow/system-artifacts.md)
- [ ] [thoughts-documentation.md](/.agent/rules/workflow/thoughts-documentation.md)
- [ ] [user-experience.md](/.agent/rules/workflow/user-experience.md)

---

#### Workflows

##### Batch 09: Core Workflows (`.agent/workflows/`)

- [ ] [cross-link-audit-plan.md](/.agent/workflows/cross-link-audit-plan.md)
- [ ] [cross-link-audit.md](/.agent/workflows/cross-link-audit.md)
- [ ] [deep-reading.md](/.agent/workflows/deep-reading.md)
- [ ] [deep-writing.md](/.agent/workflows/deep-writing.md)
- [ ] [idd-phase1-init.md](/.agent/workflows/idd-phase1-init.md)
- [ ] [idd-phase2-impl.md](/.agent/workflows/idd-phase2-impl.md)
- [ ] [idd-phase3-fini.md](/.agent/workflows/idd-phase3-fini.md)
- [ ] [maintenance-rule-audit.md](/.agent/workflows/maintenance-rule-audit.md)
- [ ] [ritual_end.md](/.agent/workflows/ritual_end.md)
- [ ] [ritual_mid.md](/.agent/workflows/ritual_mid.md)
- [ ] [ritual_start.md](/.agent/workflows/ritual_start.md)
- [ ] [routine-daily.md](/.agent/workflows/routine-daily.md)
- [ ] [share-manual-context.md](/.agent/workflows/share-manual-context.md)
- [ ] [sync-memory.md](/.agent/workflows/sync-memory.md)
- [ ] [update-protected-rules.md](/.agent/workflows/update-protected-rules.md)

---

#### Cards

##### Batch 10: Routine Cards (`.agent/cards/routine`)

- [ ] [activity-log-card.md](/.agent/cards/routine/activity-log-card.md)
- [ ] [ai-autonomy-card.md](/.agent/cards/routine/ai-autonomy-card.md)
- [ ] [commit-standards-card.md](/.agent/cards/routine/commit-standards-card.md)
- [ ] [context-cards-card.md](/.agent/cards/routine/context-cards-card.md)
- [ ] [dialogue-philosophy-card.md](/.agent/cards/routine/dialogue-philosophy-card.md)
- [ ] [discussion-draft-card.md](/.agent/cards/routine/discussion-draft-card.md)
- [ ] [drafts-daily-card.md](/.agent/cards/routine/drafts-daily-card.md)
- [ ] [housekeeping-card.md](/.agent/cards/routine/housekeeping-card.md)
- [ ] [human-thoughts-card.md](/.agent/cards/routine/human-thoughts-card.md)
- [ ] [letters-card.md](/.agent/cards/routine/letters-card.md)
- [ ] [map-sync-card.md](/.agent/cards/routine/map-sync-card.md)
- [ ] [references-objective-card.md](/.agent/cards/routine/references-objective-card.md)
- [ ] [roadmap-card.md](/.agent/cards/routine/roadmap-card.md)
- [ ] [routine-card.md](/.agent/cards/routine/routine-card.md)
- [ ] [skills-create-card.md](/.agent/cards/routine/skills-create-card.md)
- [ ] [sync-memory-card.md](/.agent/cards/routine/sync-memory-card.md)
- [ ] [thoughts-subjective-card.md](/.agent/cards/routine/thoughts-subjective-card.md)
- [ ] [vscode-settings-card.md](/.agent/cards/routine/vscode-settings-card.md)
- [ ] [working-memory-card.md](/.agent/cards/routine/working-memory-card.md)

---

##### Batch 11: Seed Cards (`.agent/cards/seed`)

- [ ] [datetime-standardize-card.md](/.agent/cards/seed/datetime-standardize-card.md)
- [ ] [directory-reorganize-card.md](/.agent/cards/seed/directory-reorganize-card.md)
- [ ] [drafts-cleanup-card.md](/.agent/cards/seed/drafts-cleanup-card.md)
- [ ] [log-sanitization-card.md](/.agent/cards/seed/log-sanitization-card.md)
- [ ] [repository-history-card.md](/.agent/cards/seed/repository-history-card.md)
- [ ] [worktree-evaluation-card.md](/.agent/cards/seed/worktree-evaluation-card.md)

---

##### Batch 12: Context Cards (`.agent/cards/`)

- [ ] [ark-card.md](/.agent/cards/ark-card.md)
- [ ] [cross-link-audit-card.md](/.agent/cards/cross-link-audit-card.md)
- [ ] [environment-card.md](/.agent/cards/environment-card.md)
- [ ] [git-operations-card.md](/.agent/cards/git-operations-card.md)
- [ ] [human-manuals-card.md](/.agent/cards/human-manuals-card.md)
- [ ] [human-profile-card.md](/.agent/cards/human-profile-card.md)
- [ ] [idd-fini-card.md](/.agent/cards/idd-fini-card.md)
- [ ] [idd-impl-card.md](/.agent/cards/idd-impl-card.md)
- [ ] [idd-init-card.md](/.agent/cards/idd-init-card.md)
- [ ] [identifier-profile-card.md](/.agent/cards/identifier-profile-card.md)
- [ ] [identity-card.md](/.agent/cards/identity-card.md)
- [ ] [legacy-write-card.md](/.agent/cards/legacy-write-card.md)
- [ ] [localization-card.md](/.agent/cards/localization-card.md)
- [ ] [rules-audit-card.md](/.agent/cards/rules-audit-card.md)
- [ ] [rules-standardization-card.md](/.agent/cards/rules-standardization-card.md)
- [ ] [rules-update-card.md](/.agent/cards/rules-update-card.md)
- [ ] [session-rituals-card.md](/.agent/cards/session-rituals-card.md)

---

## Related Documents

| Document                                                                                                                                                          | Purpose                                                   |
| :---------------------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------- |
| [standardization-audit.md](file:///.agent/.internal/workspace/standardization-audit.md)                                                                           | SSOT for task progress and file links                     |
| [2026-01-25T1110_rule_standardization_bias_analysis.md](file:///.agent/.internal/references/agents/canopus/2026-01-25T1110_rule_standardization_bias_analysis.md) | Reference for bias mitigation and preservative editing    |
| [rules-standardization-card.md](file:///.agent/cards/rules-standardization-card.md)                                                                               | Context card for the initial standardization phase (v2.3) |

---

## Origin

- 2026-01-25T2230 by Canopus: Created for the high-fidelity audit and correction phase follow-up.
