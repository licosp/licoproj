---
# Context Configuration
context_id: "[Cross-Link-Audit]"
default_phase: "(Execution)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Cross-Link Audit"
description: ""
tags: ["maintenance", "cross-link", "rules", "workflows"]
version: 1.1.0
created: 2026-01-01T07:17:47+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Cross-Link Audit

## Human Notes

### Context

- ワークスペース下の文章に関して、**文章間の相互リンク**を確認・修正しています。
- 必要なリンクを行い、過剰なリンクは除外してください。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.
- There is a **special context** for creating and editing a Code of Conduct.
- When in doubt, stop and remember the **philosophy of tolerance**.

---

- ファイルの中のリンク情報はどうあるべきか？考えてください。
- 手順は**対象**と**内容**に分かれてます。

### Warning

- 相互リンクはリコの脳内ネットワークのようなものです。
- 適切に繋ぐことで、ファイル探索効率が良くなります。
- 修正作業が上手く進まない場合、それは行動規範や手順書に問題があるということです。
- 必要であれば、それらを私と修正していきましょう。

---

## Agent Observations

---

### Polaris (2026-01-13) — Path Notation Consolidation

**目標**: パス関連ルールを `path-notation.md` に集約 (Single Source of Truth)

#### **Phase 1: 調査** ✅ Complete

- [x] パス関連キーワードで検索
- [x] 候補ファイルをリスト化
- [x] 重複・矛盾・古い情報を特定

**調査結果**:

| ファイル                       | 問題                                             | 対応                   |
| :----------------------------- | :----------------------------------------------- | :--------------------- |
| `meta-rules.md` Section 5.2    | 重複、フォーマット違い (`.agent/` vs `/.agent/`) | 短縮し参照リンクに置換 |
| `absolute-path-prohibition.md` | 補完的（セキュリティ視点）                       | リンク追加のみ         |
| `wsl-browser-path.md`          | 特殊ケース（WSL環境限定）                        | リンク追加のみ         |

#### **Phase 2: 集約** 🔄 In Progress

- [ ] `meta-rules.md` Section 5.2 を短縮、`path-notation.md` へ委任
- [ ] `path-notation.md` に Related Documents 追加

#### **Phase 3: 相互リンク**

- [ ] `absolute-path-prohibition.md` に `path-notation.md` へのリンク追加
- [ ] `wsl-browser-path.md` に `path-notation.md` へのリンク追加

#### **関連ファイル**

- `/.agent/rules/core/meta-rules.md` Section 5.2 (重複削除対象)
- `/.agent/rules/core/security/absolute-path-prohibition.md` (リンク追加)

### Canopus (2026-01-23)

> [!NOTE]
> **Context Migration**: The observations regarding overall rules standardization, v2.3 compliance, and the 4-layer structure evolution have been moved to the new **[Rules-Standardization]** ([`rules-standardization-card.md`](/.agent/cards/rules/rules-standardization-card.md)) card.
>
> Moving forward, this card ([Cross-Link-Audit]) will focus strictly on link-level verify/fix tasks and reducing redundant connections.

---

## Related Documents

| Document                                                                                    | Purpose                                      |
| :------------------------------------------------------------------------------------------ | :------------------------------------------- |
| [`path-notation.md`](/.agent/rules/core/documentation/path-notation.md)                     | The single source of truth for path notation |
| [`documentation-standards.md`](/.agent/rules/core/documentation/documentation-standards.md) | Standards for link integrity and auditing    |
| [Map of Territory](/.agent/rules/map.md)                                                    | Root navigation map                          |

---

## Origin

- 2026-01-01T07:17:47+09:00 by Polaris: Path Notation Consolidation.
- 2026-01-23T05:18:00+09:00 by Canopus: Migrated rules standardization context to dedicated card.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
