---
# Context Configuration
context_id: "[Directory-Reorganize]"
default_phase: "(Done)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Default Directory Reorganization"
description: ""
tags: ["reorganization", "structure", "cleanup"]
version: 1.1.0
created: 2025-12-31T00:00:00+09:00
updated: 2026-05-08T15:15:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Default Directory Reorganization

## Human Notes

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- カード自体の使い方を思い出してほしい
- スクリプトの使い捨て哲学に関する行動規範がある
- `workflows/` の手順書と `rules/` の行動規範の違いを理解してほしい

---

## Agent Observations

---

### Spica

- (Initial setup)

### Polaris

2025-12-31〜2026-01-01 の対話で Polaris とユーザーが議論：

#### Context

Antigravity のデフォルトディレクトリ（`rules/`, `workflows/`, `scripts/`）の整理です。

現状の問題：

- `scripts/` は使い捨て哲学により実質未使用（`workspace/` が代替）
- `workflows/` と `rules/` のフロントマターが異なる
- 両方ともリコだけが読むものなのに、フォーマットが違う

#### ユーザーの前提

**重要**: ユーザーはスラッシュコマンドを使いません。

スラッシュコマンドはリコが内部的に処理するもので、
ユーザー向けの特別な配慮は不要です。

#### 統合案

```text
.agent/
├── rules/
│   ├── core/           # 基本原則
│   ├── development/    # 開発標準
│   ├── workflow/       # 既存のワークフロールール
│   └── procedures/     # 手順書（旧 workflows/）
├── cards/              # コンテキストカード
└── .internal/
    └── workspace/      # 一時ファイル・スクリプト
```

#### 作業内容

- [x] 1. `scripts/` ディレクトリの廃止検討 (Completed)
- [x] 2. `workflows/` の `rules/procedures/` への統合 (Completed: 2026-05-08)
- [ ] 3. 全手順書のフォントマターを行動規範と統一
- [ ] 4. ドキュメント標準の明文化---

## Related Documents

| Document                                                                  | Purpose                |
| :------------------------------------------------------------------------ | :--------------------- |
| [`repository-philosophy.md`](/.agent/rules/core/repository-philosophy.md) | The "Brain" philosophy |
| [Map of Territory](/.agent/rules/map.md)                                  | Root navigation map    |

---

## Origin

- 2025-12-31T00:00:00+09:00 by Polaris: Initial discussion from seed.
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
- 2026-05-08T15:15:00+09:00 by Sirius: Updated internal links to reflect workflows -> procedures directory relocation.
