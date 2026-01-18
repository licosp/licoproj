---
context_id: "[Worktree-Eval]"
default_phase: "(Analysis)"
tags: ["git", "worktree", "multi-agent", "structure"]
---

# Context Whiteboard: 1 Agent = 1 Worktree Evaluation

> [!TIP]
> There is no language requirement.

> [!WARNING]
> 人間の記述領域の編集がまだ終わっていません。

## Human Notes

### 意図で探す

- 現在のディレクトリ構成：`licoproj`, `.agent/identifiers/canopus`, `.human/users/leonidas`
- ロードマップの項目：`#### 作業場を識別子ごとに分ける`
- Git Worktree の仕組みと、Antigravity (IDE) でのマルチエージェント動作の親和性。

### 作業の注意点

- **目的**: 複数の AI エージェント（Canopus, Spica, Polaris 等）が並行して作業する場合に、ファイル衝突を避け、それぞれの独立したコンテキストを維持するための最適な構造を提案・検証すること。
- **背景**: 現在は単一のリポジトリの中でディレクトリを分けて擬似的に実現しているが、Git Worktree を使って物理的にブランチと作業ディレクトリを紐付けることのメリット・デメリットを考える。
- Canopus として「第二の目」の視点で、将来的な拡張性（常駐型 Lico 等）も考慮に入れること。

## Agent Observations

### Canopus (2026-01-10)

- **課題の認識**: 識別子ごとにワークスペースを分けることで、エージェント間の「注意の干渉」を防げる可能性がある。
- **探索対象**:
  - 現在の `identifiers/` ディレクトリの運用状況。
  - Git Worktree を導入した場合の IDE コンテキストへの影響。
  - ロードマップにある「作業場を識別子ごとに分ける」の進捗。
