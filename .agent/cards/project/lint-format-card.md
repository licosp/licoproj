---
# Context Configuration
context_id: "[Lint-Format]"
default_phase: "(Setup)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Lint & Format Tools"
description: ""
tags: ["tooling", "lint", "format", "markdown", "quality"]
version: 1.0.0
created: 2026-01-31T18:36:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Lint & Format Tools

## Human Notes

### Context

## Human Notes

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- ファイル作成後にフォーマットを適用したい
- スペルミスや構造エラーを検出したい
- ユーザーと同じ品質基準を維持したい

---

## Agent Observations

---

### Zircon (2026-02-01)

#### Prettier Constraints (CRITICAL)

To prevent formatting conflicts and diff noise, strictly avoid the following patterns:

1. **Double Spaces after Numbered Lists**: `1.  Text`
   - **Constraint**: Prettier forces `number + dot + space` (3 chars). Double spaces will be removed.
   - **Lint Error**: `MD030/list-marker-space`[Expected: 1; Actual: 2]
   - **Solution**: Use Bullet Lists (`- Text`) for manual indentation control.

#### Textlint Constraints (Style & Grammar)

1. **No AI Formatting (Colon after Bold)**: `**Key**: Value`
   - **Constraint**: Flags `ai-writing/no-ai-list-formatting` (Mechanical impression).
   - **Solution**: Use `- Key: Value` (No bold on key).

2. **No Hype Expressions**: `Complete`, `Perfect`, `Absolutely`
   - **Constraint**: Flags `ai-writing/no-ai-hype-expressions`.
   - **Solution**: Use humble/objective terms (`Sufficient`, `Verified`).

3. **English Terms in Japanese Text**:
   - **Constraint**: Flags `textlint-rule-alex` (insensitive words) or `rousseau` (readability) false positives.
   - **Solution**: Wrap English technical terms in code spans (`` `Term` ``).

4. **Disable Error on Line**:
   - `<!-- textlint-disable-line -->`: Disables all textlint rules for the line.

5. **Leading Spaces before Japanese Brackets**: `   「Text」` <!-- markdownlint-disable-line -->
   - **Constraint**: Prettier often treats leading spaces as code blocks or removes them, causing instability.
   - **Solution**: Start `「` immediately after the bullet or at start of line without indentation.

6. **Disable Error on Line**:
   - `<!-- markdownlint-disable-line -->`: `markdownlint`
   - `<!-- cspell:disable-line -->`: `cspell`

#### Workflow Strategy (The "Tool-First" Protocol)

1. **Tier 1: Automated Tooling (Mechanical)**
   - **Action**: Use `textlint --fix`, `prettier --write` for 90% of issues.
   - **Scope**: Spacing, Indentation, Simple stylistic fixes.
   - **User Command**: `yarn textlint --fix <file>`

2. **Tier 2: AI Assistance (Contextual)**
   - **Action**: Ask Lico (AI) to handle what tools cannot fix.
   - **Scope**: Complex phrasing, restructuring, tone adjustments, passive-to-active conversion.

3. **Tier 3: Relaxed Constraint**
   - **Policy**: Do not strictly enforce "Expression" rules (e.g., specific word choices) if it harms the flow. Code/Docs should be practical.

#### Context

リコが生成する MD ファイルの品質管理ツールです。
ユーザーの VSCode では保存時に自動整形されますが、リコも CLI から使えます。

最終的にはスキル通知でリント/フォーマット情報を渡す形式が理想。

#### ツール一覧

| Tool             | Purpose                | Invocation               |
| :--------------- | :--------------------- | :----------------------- |
| **Prettier**     | 汎用フォーマッター     | `yarn prettier`          |
| **CSpell**       | 英単語スペルチェック   | `yarn cspell`            |
| **textlint**     | 日本語テキストチェック | `yarn textlint`          |
| **Markdownlint** | Markdown 構造チェック  | `yarn markdownlint-cli2` |

#### 設定ファイル

| Tool         | Config File(s)                                                 |
| :----------- | :------------------------------------------------------------- |
| Prettier     | `.vscode/.prettierrc.yaml` (active), `.vscode/.prettierignore` |
| CSpell       | `.vscode/cspell.json`                                          |
| textlint     | `.vscode/.textlintrc.json`                                     |
| Markdownlint | `.vscode/.markdownlint.yaml`                                   |

#### ランタイム

| Runtime | Path                                         |
| :------ | :------------------------------------------- |
| yarn    | `.runtimes/yarn-v1.22.19/bin/yarn`           |
| node    | `.runtimes/node-v22.12.0-linux-x64/bin/node` |

---

## Related Documents

| Document                                                       | Purpose                          |
| :------------------------------------------------------------- | :------------------------------- |
| [`code-quality.md`](/.agent/rules/development/code-quality.md) | Code and documentation standards |
| [`markdown-ai.md`](/.agent/rules/core/markdown/markdown-ai.md) | Markdown formatting rules for AI |
| [Map of Territory](/.agent/rules/map.md)                       | Root navigation map              |

---

## Origin

- 2026-01-31T18:36:00+09:00 by Polaris: Created seed card for lint/format tooling context.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
