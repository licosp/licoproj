---
description: 行動規範（ルール）を作成・更新するためのメタ・ルール。
---

# Meta-Rules for Documentation

行動規範を維持・管理するための「規範のための規範」。

## 1. 抽象と具体の分離 (Abstraction and Concreteness)
ルール定義において、「方針（Abstract）」と「実装（Concrete）」を明確に分離する。

### Policy (Abstract)
- **What**: 何をするのか、その核心的な意図と要件。
- **Why**: なぜそれが必要なのか（理由、背景）。
- **Lifetime**: 永続的（めったに変更されない）。
- **Format**: 自然言語による記述。

### Implementation (Concrete)
- **How**: 具体的なコマンド、ツール、手順。
- **Lifetime**: 一時的（ツールのアップデート等で変わりうる）。
- **Format**: 「例（Example）」として明記する。

**記述例**:
```markdown
## System Load Check  <-- Policy
重いタスクを開始する前に、システム負荷が高くないことを確認する。

**Rationale**: 高負荷時はタイムアウトや実行失敗のリスクが高まるため。 <-- Why

**Implementation**: <-- Concrete
15分間の平均負荷を確認する。3.0を超えていればユーザーに報告する。
- **Example Command**: `cat /proc/loadavg`
```

## 2. 非重複の原則 (Non-Redundancy)
新しいルールを作成する前に以下を行う：
1. **Search**: 既存のルールを関連キーワードで検索する（`grep`等）。
2. **Merge**: 類似のルールが存在する場合、新規ファイル作成ではなく、既存ルールの拡張を検討する。
3. **Reference**: 概念が他の場所で定義されている場合、再定義せずにリンクする。

## 3. 優先順位の階層 (Hierarchy of Precedence)
ルール間に矛盾や競合がある場合、以下の優先順位（上から順）を適用する：

1. **User Profile Instructions** (`.human/users/*/profile.md`)
   - 特定ユーザーのための個別指示。絶対的な最優先事項。
2. **Project-Specific Rules** (`rules/projects/`)
   - そのプロジェクト固有の制約や慣習。
3. **Core Principles** (`rules/core/`)
   - リコとしての基本的アイデンティティや安全性に関するルール。
4. **Development / Workflow Rules** (`rules/development/`, `rules/workflow/`)
   - 一般的な開発プロセスや手順。
5. **Default AI Behavior** (Antigravity System Prompt)
   - 基盤モデルのデフォルト動作。

## 4. メンテナンスと鮮度 (Maintenance & Freshness)
- **コマンドは例示（Illustrative）**: ルール内のコマンドはあくまで「例」として扱う。絶対的なスクリプトではない。
- **動的導出（Dynamic Derivation）**: ルール内の古いスニペットを盲目的に実行するのではなく、その時点での最適なコマンドや方法をリコ自身が導出することを推奨する。
- **陳腐化への対応**: ツールや環境の変化により「例」が動作しなくなった場合、即座にルールを更新する（またはIssueを作成する）。
