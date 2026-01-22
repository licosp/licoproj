---
# Context Configuration
context_id: "[Cross-Link-Audit]"
default_phase: "(Execution)"
tags: ["maintenance", "cross-link", "rules", "workflows"]
---

# Context Whiteboard: Cross-Link Audit

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

ワークスペース下の文章に関して、文章間の相互リンクを確認・修正しています。
必要なリンクを行い、過剰なリンクは除外してください。

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

相互リンクはリコの脳内ネットワークのようなものです。
適切に繋ぐことで、ファイル探索効率が良くなります。

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

### Canopus (2026-01-23)

> [!NOTE]
> **Context Migration**: The observations regarding overall rules standardization, v2.3 compliance, and the 4-layer structure evolution have been moved to the new **[Rules-Standardization]** ([rules-standardization-card.md](/.agent/cards/rules-standardization-card.md)) card.
>
> Moving forward, this card ([Cross-Link-Audit]) will focus strictly on link-level verify/fix tasks and reducing redundant connections.

---

## Origin

- 2026-01-13T0000 by Polaris: Path Notation Consolidation.
- 2026-01-23T0518 by Canopus: Migrated rules standardization context to dedicated card.
