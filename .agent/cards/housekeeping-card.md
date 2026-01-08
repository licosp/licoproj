---
# Context Configuration
context_id: "[Housekeeping]"
default_phase: "(WIP)"
tags: ["maintenance", "cleanup", "quick-task"]
---

# Context Whiteboard: Housekeeping

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

**文脈が不要なほど短い作業**、あるいは**文脈が不明な作業**を行っています。

既に作業が行われている場合、まず既存の文脈かどうか確認してください。
既存のものが無い場合は、リコが私の記憶を頼りに文脈を推測します。

作業が終わったら、後片付けとして、コミットを行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。

### 作業の注意点

リポジトリの変更が多い場合、気軽に私と相談してください。
一人で一気に作業を進める必要はありません。

処理が簡単そうなものから、そして対話をしながら作業を進めたいです。

### 書庫へ移動 → コミット

過去の作業で作った一時的なファイルは「削除」しないでください。
完全な削除は基本的に推奨されていません。

一方で、誤って消してしまったとしても、
それはAIの習慣なので仕方ないことだとも考えています。

## Agent Observations

### Polaris (2026-01-08)

#### 現在の作業: licoimg サブプロジェクトの廃止

削除対象:

- [x] `packages/licoimg/` — サブプロジェクト本体
- [x] `.github/workflows/jekyll-gh-pages.yml` — GitHub Pages ワークフロー
- [x] `.agent/rules/projects/coding-conventions.md` — コーディング規約
- [x] README への参照を削除

参照更新:

- [x] `README.md` — licoimg への言及を削除
- [x] `README.ja.md` — licoimg への言及を削除
- [x] `.agent/rules/README.md` — coding-conventions への参照を削除
- [x] `roadmap-card.md` — 完了項目として削除
