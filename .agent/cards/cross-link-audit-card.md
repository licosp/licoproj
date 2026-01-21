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

1. **構造の再統合（Navigation + Related Documents）**:
   - **経緯**: 以前は「テーブルを廃止してフッター（Navigation）に一本化する」方針がありましたが、現在は**「フッターを `Related Documents` テーブルに統合する」**方針へ再転換しています。
   - **対応**: 独立したフッターを廃止し、本文の `## Related Documents` セクション（テーブル形式）に「[Map of Territory](/.agent/rules/map.md)」を含むすべての関連リンクを集約します。

2. **パス記法の厳格化（ワークスペース絶対パス）**:
   - **基準**: すべてのリンクを `(/.agent/rules/map.md)` のような、先頭に `/` を含む**ワークスペース絶対パス**に統一します。
   - **目的**: GitHub、VSCode Markdownプレビュー、およびAIツールにおけるリンクの動作保証とポータビリティの確保。

3. **二重管理の解消（フロントマターとの同期）**:
   - フロントマターの `related:` フィールドと本文テーブルの二重管理を解消するため、原則として本文テーブルを正（Single Source of Truth）とします。フロントマターを維持する場合は、本文と同一の絶対パス記法を適用します。
