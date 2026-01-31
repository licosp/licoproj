---
# Context Configuration
context_id: "[Lint-Format]"
default_phase: "(Setup)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-01-31T18:36:00+09:00
updated: 2026-01-31T18:36:00+09:00
tags: ["tooling", "lint", "format", "markdown", "quality"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Polaris)
ai_model: Claude Opus 4.5 (Thinking) Planning mode
---

# Context Whiteboard: Lint & Format Tools

> [!TIP]
> There is no language requirement.

---

> [!WARNING]
> The human notes has not yet been edited.

## Human Notes

### 作業の文脈

## Human Notes

### 作業の文脈

リコが生成する MD ファイルの品質管理ツールです。
ユーザーの VSCode では保存時に自動整形されますが、リコも CLI から使えます。

最終的にはスキル通知でリント/フォーマット情報を渡す形式が理想。

### ツール一覧

| Tool             | Purpose                | Invocation               |
| :--------------- | :--------------------- | :----------------------- |
| **Prettier**     | 汎用フォーマッター     | `yarn prettier`          |
| **CSpell**       | 英単語スペルチェック   | `yarn cspell`            |
| **textlint**     | 日本語テキストチェック | `yarn textlint`          |
| **Markdownlint** | Markdown 構造チェック  | `yarn markdownlint-cli2` |

### 設定ファイル

| Tool         | Config File(s)                                                 |
| :----------- | :------------------------------------------------------------- |
| Prettier     | `.vscode/.prettierrc.yaml` (active), `.vscode/.prettierignore` |
| CSpell       | `.vscode/cspell.json`                                          |
| textlint     | `.vscode/.textlintrc.json`                                     |
| Markdownlint | `.vscode/.markdownlint.yaml`                                   |

### ランタイム

| Runtime | Path                                         |
| :------ | :------------------------------------------- |
| yarn    | `.runtimes/yarn-v1.22.19/bin/yarn`           |
| node    | `.runtimes/node-v22.12.0-linux-x64/bin/node` |

### 意図で探す

- ファイル作成後にフォーマットを適用したい
- スペルミスや構造エラーを検出したい
- ユーザーと同じ品質基準を維持したい

## Agent Observations

_No observations yet._

---

## Related Documents

| Document                                                     | Purpose                          |
| :----------------------------------------------------------- | :------------------------------- |
| [code-quality.md](/.agent/rules/development/code-quality.md) | Code and documentation standards |
| [markdown-ai.md](/.agent/rules/core/markdown/markdown-ai.md) | Markdown formatting rules for AI |

---

## Origin

- 2026-01-31T1836 by Polaris: Created seed card for lint/format tooling context.
