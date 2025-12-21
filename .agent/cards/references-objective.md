---
# Context Configuration
context_id: "[References]"
default_phase: "(Add)"
tags: ["references", "analysis", "external-input", "second-eyes"]
---

# Context Whiteboard: References Update

## Human Notes (Japanese OK)

### 作業の文脈

外部AI（第二の目）による分析レポートや参考文献が追加されました。
あるいは、リコと私の対話の結果、参考文献として残すべきファイルを作ります。

作られたファイルをコミットしてください。

### 関連書類を探す

- references
- 第二の目
- IDD（フェーズ2）
- カード

### 作業の注意点

ファイルの配置場所は原則 `.agent/.internal/references/` 配下とする。
コミット時は「どのような分析（何に基づく分析か）」を要約に含めること。
AIによる生成物であることを認識し、メタデータ（作成者、モデル名など）があれば保持する。

### 使ってほしい道具

- `.agent/.internal/references/`
- `.agent/templates/header-frontmatter.yaml`
- `.agent/templates/commit-message.txt`

## Agent Observations

- (Space for Lico)
