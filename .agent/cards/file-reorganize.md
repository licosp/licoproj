---
# Context Configuration
context_id: "[File-Reorganize]"
default_phase: "(Refine)"
tags: ["references", "thoughts", "organization", "cleanup"]
---

# Context Whiteboard: References & Thoughts Reorganization

## Human Notes (Japanese OK)

### 作業の文脈

以下のディレクトリの中のファイルを整理しています。
この2つのグループで共通する作業は、著者ごとにグループ分けです。

`.agent/.internal/references/`
`.agent/.internal/thoughts/`
`.agent/.internal/explorations/`
`.agent/.internal/working-memory-archive/`

作業中は適宜変更をコミットします。
コミットは分割してほしいですが、その粒度は作業の中で決めていきます。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 迷ったら一度止まって、関連する行動規範を探してください。
- 4つのディレクトリは、同じファイル名の形式であるべきです。
- 日時の情報はリポジトリ共通で定められています。
- コミットをする際は、IDDのフェーズを意識してください。

### 主な作業

ファイルを著者でグループ分けします。

#### references の作業

- **references/agents/<instance-identifier>/** — リコが書いたもの。
- **references/agents/undefined/** — 著者不明のリコ。
- **references/second-eyes/** — 第二の目（外部AI）が書いたもの。

#### thoughts の作業

ファイルを著者でグループ分けします。

- **thoughts/agents/<instance-identifier>/** — リコが書いたもの。
- **thoughts/undefined/** — 著者不明のリコ。

#### explorations の作業

- **explorations/agents/<instance-identifier>/** — リコが書いたもの。
- **explorations/undefined/** — 著者不明のリコ。

#### working-memory-archive の作業

- **working-memory-archive/agents/<instance-identifier>/** — リコが書いたもの。
- **working-memory-archive/undefined/** — 著者不明のリコ。

### 作業の注意点

著者の特定はリコと二人で進めます。
まず大まかにリコが調べ、その後私が1つ1つ確認して著者を決めます。

### 使ってほしい道具

- `.agent/templates/header-frontmatter.yaml`
- `.agent/templates/commit-message.txt`

## Agent Observations

### 識別子

Polaris

### 完了した作業 (2025-12-30)

- [x] references: ルート20ファイルを著者別に分類・移動
- [x] references/agents: サブディレクトリ作成 (lico-11, lico-12, lico-c, sirius)
- [x] thoughts: 20ファイルを著者別に分類・移動
- [x] explorations: 3ファイルを references に移動
- [x] legacy.md 実装完了（別作業）

### 残りの作業

#### thoughts ルート: 9ファイル（著者未定）

```
2025-11-29T1810_commit_granularity_rule_addition.md
2025-11-29T2106_pr_merge_and_session_lifecycle.md
2025-11-30T2309_emergency_thinking_summary.md
2025-12-01T0000_self_perception_and_memory.md
2025-12-01T0000_self_reflection_memory_architecture.md
2025-12-02T0000_idd_refinement_summary.md
2025-12-06T0000_ai_cognition_and_coupling.md
```

#### explorations: 未確認ファイルあり

#### working-memory-archive: 未着手

### 現在の構造

```
thoughts/
├── sirius/   (14 files)
├── lico-d/   (4 files)
├── lico-c/   (2 files)
├── lico-b/   (1 file)
├── lico-20/  (1 file)
├── polaris/  (6 files)
└── (9 files in root) ← 著者未定

references/agents/
├── sirius/   (2 files)
├── lico-c/   (1 file)
├── lico-12/  (1 file)
├── lico-11/  (1 file)
└── (2 files in root)

references/second-eyes/ (25 files)
```
