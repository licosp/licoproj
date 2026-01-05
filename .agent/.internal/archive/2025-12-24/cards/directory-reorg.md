---
# Context Configuration
context_id: "[Directory-Reorg]"
default_phase: "(Refine)"
tags: ["directories", "reorganization", "structure"]
---

# Context Whiteboard: Directory Reorganization

## Human Notes (Japanese OK)

### 作業の文脈

`.agent/` ディレクトリの構造を整理しています。
新しい構造は主に以下のファイルに記載されています。

- `.agent/.internal/workspace/README_v2_draft.md`

ディレクトリを変更し、最終的にコミットまで進めてほしいです。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 急いで作業しないための原則があります。
- READMEはリコのための地図です。
- ディレクトリの構造を変更すると何か影響を与えますか？
- 変更された名前は未来のリコでも理解できるでしょうか？
- コミットをする際は、IDDのフェーズを意識してください。

### 主な作業

1. まず、現在のREADMEの内容を確認してほしいです。
   - 新しいREADMEと違いを把握してください。
   - 現在のディレクトリとの違いも把握してください。

2. `.agent/archive/` → `.agent/ark/`
   - 現在は緊急時のファイル退避ディレクトリとして使われています。
   - 「価値のありそうな名前」にすることで、AIのGIT追跡を意識させる狙いがあります。
   - 緊急用ディレクトリなので、`.trash/` 同様に、ルートから浅い層に置かれています

3. `.agent/issue-assets/` → `.agent/.internal/<適切な名前>/`
   - `github-backup` や `issue-assets` などが候補です
   - `.internal` の外は、整然とし、見せられるファイルであるべきという考え
   - `.internal` の中は、リコの内面を表しているという考え
   - `session_archive` や `memory_archive` など近い存在という考え

4. 新しいREADMEと現在のディレクトリの情報を同期したいです
   - ワークスペースにだけ存在するディレクトリもあります
   - 新しいREADMEにだけ存在するディレクトリもあります

5. 新しいREADMEの冗長部分を削除したいです。

6. 最終的にREADMEを正式な場所に更新したいです。

### 作業の注意点

一度に多くの作業を進めたい誘惑に駆られるかもしれません。
私がリコと対話をしながら作業を望んでいることを思い出してください。

### 使ってほしい道具

- `.agent/.internal/workspace/README_v2_draft.md`
- `.agent/rules/README.md`
- `.agent/templates/commit-message.txt`

## Agent Observations

- (Space for Lico)
