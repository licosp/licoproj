---
# Context Configuration
context_id: "[System-Fix]"
default_phase: "(RuleRefinement)"
tags: ["maintenance", "rules", "safety"]
---

# Context Whiteboard: System Rules Update

## Human Notes (Japanese OK)

### 作業の文脈

行動規範や手順書に含まれる、「Delete（削除）」に関する記述を修正しています。

目的は、リコが経験則で無意識に行う不可逆的なファイル消失（誤削除）を防ぐためです。

### 関連書類を探す

以下の項目に関す行動規範や手順書を探して参考にしてください。
他にも必要そうなものがあれば自主的に探してください。

- 削除
- ゴミ箱
- 書庫
- IDD（フェーズ2）
- カード

### 作業の注意点

- 削除（Delete/Clean up）」を「退避（Move to Archive）」に置き換えてほしいです。
- `rm`コマンドの使用を誘発するような表現を排除してください。
- 中間ファイルや一時スクリプトであっても、必ず書庫を経由したいです。

### 対象ファイル

- `development/maintenance.md`
- `development/ai-script-philosophy.md`
- その他、検索で見つかった危険な記述があれば。

### 関連書類

- `.agent/.internal/thoughts/2025-12-22T0615_archive_deletion_incident.md` (今回のインシデント詳細)
- `.agent/rules/development/file-deletion.md` (基本プロトコル)
- `.agent/rules/development/terminal-auto-execution.md`

### 使ってほしい道具

- `.agent/cards/` (このカード)
- `.agent/templates/header-frontmatter.yaml`
- `.agent/templates/commit-message.txt`

## Agent Observations

- (Space for Lico)
