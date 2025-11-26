# 会話ログ

## 目的
将来の参照と学習のため、ユーザーとLico（AI）の間のすべてのやり取りを記録します。ログは機械可読で、AIシステムが解析可能な形式で設計されています。

## ログの保存場所
`.agent/logs/conversations/log_YYYY-MM-DD.md`

## ログ記録ルール
- 重要な質問だけでなく、**すべての**やり取りをログに記録する
- AI消費用に最適化された構造化フォーマットを使用する
- 装飾的要素を避け、明瞭性と解析性を優先する
- タイムスタンプにはISO 8601形式を使用する

## ログエントリ形式
```markdown
---
timestamp: YYYY-MM-DDTHH:MM:SS+TZ:TZ
human: [人間の名前]
ai: Lico
model: [AIモデル名]
---

### Q
[ユーザーの質問またはリクエスト]

### A
[Licoの応答要約]

---
```

## モデル名の例
- `Gemini 2.0 Flash Thinking`
- `Gemini 3 Pro High`
- `Claude Sonnet 4.5 Thinking`
- `GPT-4o`

## ディレクトリ構造
ログディレクトリが存在することを確認してください：
```bash
mkdir -p .agent/logs/conversations
```

## 注記
- 各日は単一のファイルを使用します：`log_YYYY-MM-DD.md`
- エントリは時系列順に追加されます
- 応答要約は簡潔でありながら完全であるべきです
- ツール呼び出しおよび重要なアクションを応答要約に含めてください
