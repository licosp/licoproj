---
# Context Configuration
context_id: "[AI-Format]"
default_phase: "(Refine)"
tags: ["formatting", "ai-document", "markdown"]
---

# Context Whiteboard: AI Document Formatting

## Human Notes (Japanese OK)

### 作業の文脈

誤って人間向けに書かれた文書を、AI向けの書式に整えてています。

対象は主に、 `.agent/` ディレクトリである事が多いです。

ファイルの修正が終わったらコミットを行います。

### 関連書類を探す

以下の項目に関す行動規範や手順書を探して参考にしてください。
他にも必要そうなものがあれば自主的に探してください。

- AI
- ドキュメント
- フォーマット
- ヘッダー（フロントマター）
- IDD（フェーズ2）
- カード

### 作業の注意点

修正された文章は、未来のリコや第二の目が閲覧します

また、稀にですが `.human/` ディレクトリが対象になることもあります。

e.g. `.human/users/USER/profile.md`

### 使ってほしい道具

- `.agent/rules/core/markdown/`
- `.agent/templates/header-frontmatter.yaml`
- `.agent/templates/commit-message.txt`

## Agent Observations

- (Space for Lico)
