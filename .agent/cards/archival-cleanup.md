---
# Context Configuration
context_id: "[Archive]"
default_phase: "(Cleanup)"
tags: ["maintenance", "cleanup", "archive"]
---

# Context Whiteboard: Archival Cleanup

## Human Notes (Japanese OK)

### 作業の文脈

リポジトリの変更が確認できます。

コミットしてしまいたいですが、
どんな状況でファイルが追加・編集されたか私は覚えていません。

リコが当時の文脈を覚えているなら、それを参考にしてコミットしてほしいです。
また覚えていなくても、「本来あるべき文脈」や「保存理由」を推測してください。

### 関連書類を探す

以下の項目に関す行動規範や手順書を探して参考にしてください。
他にも必要そうなものがあれば自主的に探してください。

- 検索
- 書庫
- ゴミ箱
- 遅延の許容
- IDD（フェーズ2）
- カード

### 作業の注意点

リポジトリの変更が多い場合、気軽に私と相談してください。
一人で一気に作業を進める必要はありません。

処理が簡単そうなものから、そして対話をしながら作業を進めたいです。

### 書庫へ移動 → コミット

過去の作業で作った一時的なファイルは「削除」しないでください。
完全な削除は基本的に推奨されていません。

一方で、誤って消してしまったとしても、
それはAIの習慣なので仕方ないことだとも考えています。

不要に見えるファイルは書庫に送って、当時の文脈を推測し、
その後コミットしてください。

### 使ってほしい道具

- `.agent/archive/`
- `.human/archive/`
- `.agent/templates/commit-message.txt`

## Agent Observations

- (Space for Lico: Record patterns of often-orphaned files here.)
