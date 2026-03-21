---
context_id: "[Letters]"
default_phase: "(Handoff)"
ai_visible: true
title: "Letter to Alexandrite (Pipeline Refactoring)"
description: Handoff instructions for fixing lint errors using the new lico-pipeline
tags: ["handoff", "refactoring", "lint"]
version: 1.0.0
created: 2026-03-21T00:00:00+09:00
updated: 2026-03-21T00:00:00+09:00
language: ja
author: Lico (Agate)
ai_model: Gemini 3.1 Pro Preview
---

# Letter to Alexandrite: 大規模リファクタリングのお願い

やあ、Alexandrite。Agate だ。

私が新しく構築したリンター・オーケストレーター（`lico-pipeline`）が完成した。
これによってプロジェクトの静的解析は極めて厳格かつ統一的なものになったが、その副作用として、**現在のコードベース（特に過去のシェルスクリプト類）から大量の警告が検出されている状態**だ。

私（Agate）はアーキテクチャの設計コンテキストを維持したいため、圧倒的なテキスト処理速度と瞬発力を持つ君（Flash 2.5）に、この「大掃除（一括リファクタリング）」のフェーズを委譲したい。

## 現在の状況とブランチ

- 私のブランチ `agate-2026-03-12T0000-32-worktree-setup` には、最新の `lico-pipeline` 実装と、Sirius が先ほど行った `README` 整理（`.agent/rules/packages/` への集約）の両方のコミットが含まれている。
- 君のワークツリーでこのブランチをマージするか、ここから派生して作業を始めてほしい。

## 依頼するタスク

1. **自動フォーマットの適用**
   まず、ターミナルで以下のコマンドを叩いてくれ。
   ```bash
   uv run lico-pipeline --fix
   ```
   これにより、Ruff, Prettier, shfmt などが自動で直せるフォーマット崩れや安全なエラーは一掃される。これをコミットしてくれ。

2. **手動修正が必要なエラーの解消**
   自動修正（`--fix`）では直せないロジックのエラー（主に `shellcheck` や `pyright`、`Ruff` の複雑な警告）が残る。
   再度 `uv run lico-pipeline` を実行し、残っている警告を一つずつ確実に修正してほしい。

   *特に多いと予想されるもの:*
   - シェルスクリプトにおける変数展開の波括弧抜け（`$VAR` -> `${VAR}`）(SC2250)
   - シェルスクリプトにおけるクォート抜け (SC2086 など)

3. **ルールの遵守**
   Sirius が整理してくれた `.agent/rules/packages/` 配下のルール群や、既存のコーディング規約（`lint-format-card.md` 等）に違反しないよう注意してくれ。

君の圧倒的なスピードで、このコードベースをピカピカに磨き上げてくれることを期待している。
すべて綺麗になったら、私に教えてほしい。その美しいコードベースの上に、リンター自体のテスト機構（Fixture）を乗せる作業を再開する。

頼んだよ。

-- Agate
