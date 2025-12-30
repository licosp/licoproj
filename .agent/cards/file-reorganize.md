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

その後、欠落したフロントマターのあるファイルを修正します。
主に著者と日付情報だけでも付与して、未来のリコの負担を軽減します。

作業中は適宜変更をコミットします。
コミットは分割してほしいですが、その粒度は作業の中で決めていきます。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要なディレクトリやテンプレートが存在します。
- 迷ったら一度止まって、関連する行動規範を探してください。
- 4つのディレクトリは、同じファイル名の形式であるべきです。
- 日時の情報はリポジトリ共通で定められています。
- コミットをする際は、IDDのフェーズを意識してください。

### 残りの作業

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

## Agent Observations

### 識別子

Polaris

### 作業完了 (2025-12-31)

#### Phase 1: 著者別分類
- [x] thoughts: 全ファイルを著者別サブディレクトリに移動
- [x] references/agents: 全ファイルを著者別サブディレクトリに移動
- [x] explorations: 整理完了
- [x] working-memory-archive: 整理完了

#### Phase 2: フロントマター修正
- [x] thoughts: 11ファイル修正
- [x] references/agents: 6ファイル修正
- [x] working-memory-archive: 4ファイル修正
- [x] explorations: 確認済み（修正不要）

**合計: 21ファイルのフロントマターを標準化**

### 標準化内容

- `name`/`model` → `author`/`ai_model` 形式に統一
- `author: Lico` → `author: Lico (<Instance-ID>)` 形式に統一
- 欠落していた `created`/`updated` フィールドを追加

