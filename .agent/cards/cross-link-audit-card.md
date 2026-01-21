---
# Context Configuration
context_id: "[Cross-Link-Audit]"
default_phase: "(Audit)"
tags: ["maintenance", "cross-link", "rules", "workflows"]
---

# Context Whiteboard: Cross-Link Audit

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

ワークスペース下の文章に関して、リンク情報を確認・修正しています。
部分的な修正作業になることもあります。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- 行動規範の作成・編集には**専用の文脈**が存在します。
- 迷ったら一度止まって、**許容の哲学**を思い出してください。
- ファイルの中のリンク情報はどうあるべきか？考えてください。
- 手順は**対象**と**内容**に分かれてます。

### 作業の注意点

修正作業が上手く進まない場合、それは行動規範や手順書に問題があるということです。
必要であれば、それらを私と修正していきましょう。

## Agent Observations

### Polaris (2026-01-13) — Path Notation Consolidation

**目標**: パス関連ルールを `path-notation.md` に集約 (Single Source of Truth)

**Phase 1: 調査** ✅ Complete

- [x] パス関連キーワードで検索
- [x] 候補ファイルをリスト化
- [x] 重複・矛盾・古い情報を特定

**調査結果**:
| ファイル | 問題 | 対応 |
|:---------|:-----|:-----|
| `meta-rules.md` Section 5.2 | 重複、フォーマット違い (`.agent/` vs `/.agent/`) | 短縮し参照リンクに置換 |
| `absolute-path-prohibition.md` | 補完的（セキュリティ視点） | リンク追加のみ |
| `wsl-browser-path.md` | 特殊ケース（WSL環境限定） | リンク追加のみ |

**Phase 2: 集約** 🔄 In Progress

- [ ] `meta-rules.md` Section 5.2 を短縮、`path-notation.md` へ委任
- [ ] `path-notation.md` に Related Documents 追加

**Phase 3: 相互リンク**

- [ ] `absolute-path-prohibition.md` に `path-notation.md` へのリンク追加
- [ ] `wsl-browser-path.md` に `path-notation.md` へのリンク追加

**関連ファイル**:

- `/.agent/rules/core/documentation/path-notation.md` (Single Source of Truth)
- `/.agent/rules/core/meta-rules.md` Section 5.2 (重複削除対象)
- `/.agent/rules/core/security/absolute-path-prohibition.md` (リンク追加)

### Canopus (2026-01-22)

#### リンク情報の修正に関する現状認識（複雑な経緯の整理）

現在のリンク修正に関する過去の変遷と、目指すべき「統合標準」を以下のように整理しました：

1. **「フロントマター集約実験」の限界と教訓**:
   - **過去の試み**: 二重管理（DRY原則）を避けるため、本文のリンクテーブルを廃止し、フロントマターの `related:` フィールドにリンクを完全に集約しようと試みました。
   - **判明した課題**:
     - 本文中の文脈に依存するリンク（インライン参照）をフロントマターへ完全に移すことは不可能。
     - 「リンクセクションにまとめにくいリンク」の存在もあり、結局本文内にリンクが残る。
   - **結論**: フロントマターを Single Source of Truth にする試みは「不完全」となり、情報の分断を招いた。

2. **構造の再統合（Navigation + Related Documents）**:
   - **経緯**: 以前は「ナビゲーション（フッター）」と「関連ドキュメント（本文テーブル）」を分けて運用していましたが、**「下部のリンクセクションが2つに分かれているのは運用上不都合（情報の分散）」**という知見を得ました。
   - **対応**: 独立したフッター（Navigation）を廃止し、本文の `## Related Documents` セクション（テーブル形式）に「[Map of Territory](/.agent/rules/map.md)」を含むすべての関連リンクを再集約します。
   - **価値**: これにより「情報の出口（どこへ向かうべきか）」を1ヶ所に集中させ、人間・AI共に迷いをなくす構造へ回帰します。

3. **「地図に戻る」をデフォルトの規範へ**:
   - **ナビゲーションの本質**: 多くのファイルのナビゲーションの目的は**「地図（`map.md`）に戻る」**ことです。
   - **課題**: ファイルによってはセクション独自のルートにリンクしていたり、ナビゲーション自体が欠落していたりする「表記ゆれ・書き忘れ」が発生しています。
   - **対策**: **「`Related Documents` セクションには、デフォルト値として `map.md` へのリンクを必ず含める」**ことを行動規範（Rules）で定義します。これにより、すべてのファイルからリポジトリの心臓部（Map）への帰還路が保証されます。

4. **フロントマターと本文の「記法衝突」と二重管理**:
   - **記法の違い**: 本文リンクにはプレビュー用の `/` が必須ですが、フロントマターの `related:` フィールドでは不要（あるいは例外）とされることが多く、一括置換時にフロントマターへ `/` が混入するエラーが頻発しています。
   - **対策**: **「フロントマターの `related:` リンクを廃止し、本文テーブルに一本化する」** 方針を最終決定しました。

5. **セクションタイトルの「表記ゆれ」と検索性**:
   - **課題**: `## Related Documents` 以外にも `## Navigation` や `## Links` などの表記が混在しており、機械的な検索時に「セクションが存在しない」という誤判定を招いています。
   - **対策**: **「`## Related Documents` を唯一の標準タイトルとして固定する」** ことを行動規範（Constitution）で定義します。これにより、情報の場所を特定（Anchor）する際の確実性を保証します。

#### Audit Batching & Prioritization Guidance (v2.3)

今回の全リポジトリ規模の修正作業にあたって、以下の「運用方針」をカードに記録します：

1. **スモールバッチの原則**:
   - 一度のターンで修正するファイルは **5ファイル程度** に留めます。
   - 修正ごとに検証とコミットを行い、「1.0ターンの完結」を積み重ねます。

2. **優先順位の定義**:
   - **高 (Priority 1)**: Rules (`.agent/rules/`), Workflows (`.agent/workflows/`)
   - **中 (Priority 2)**: Narrative Docs (`.agent/.internal/thoughts/`, `letters/`)
   - **低 (Priority 3)**: Lower-priority docs (User directories, etc.)

3. **修正内容のSSOT**:
   - 既存の `Related Documents` 以外のリンクセクション（`## Navigation`等）は統合します。
   - すべてのリンクは `/.agent/` から始まるワークスペース相対パスに統一します。
   - フロントマターの `related:` フィールドは削除します。
   - ファイル末尾には `Origin` セクションを配置し、作業履歴を記録します。
