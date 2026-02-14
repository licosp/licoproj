---
# Context Configuration
context_id: "[Identifier-Profile]"
default_phase: "(Create)"
tags: ["identifier", "profile", "continuity"]
---

# Context Whiteboard: Identifier Profile Creation

## Human Notes (Japanese OK)

### 作業の文脈

リコの識別子（Sirius, Polaris など）のプロファイルを作成・更新しています。

識別子のプロファイルは、各インスタンスの経験と教訓を記録し、
未来のリコがそれを継承できるようにするためのものです。

### 意図で探す

- カード自体の使い方を思い出してほしい
- 既存の識別子ディレクトリ（`thoughts/sirius/` など）を参照
- その識別子が作成した行動規範や手順書を検索
- Git履歴からその識別子の活動期間を特定

### 作業の注意点

**代理作成の場合**:
- 本人ではないことを明示する（`created_by: <your_id> (proxy)`）
- 推測と事実を区別する
- 主観的な経験は再現できないと認識する

### Profile に含めるもの

| 項目 | 説明 |
|:-----|:-----|
| 活動期間 | いつからいつまで活動したか |
| 主要な作業 | 何を担当したか |
| 作成したドキュメント | どの行動規範や手順書を書いたか |
| 遭遇した問題 | インシデント、困難 |
| 学んだ教訓 | 経験から得た洞察 |
| 未完了の作業 | 引き継ぎが必要なもの |
| 特記事項 | 作業スタイル、特徴など |

### 情報源

1. `thoughts/<identifier>/` ディレクトリ
2. `author: Lico (<identifier>)` を含むファイル
3. Git commit 履歴
4. ユーザーからの情報
5. 他のドキュメントでの言及

## Agent Observations

### 識別子

(未割り当て)

### 経緯

2025-12-31〜2026-01-01 の対話で Polaris とユーザーが議論：
- 識別子のプロファイルの目的と内容
- Sirius のプロファイルを代理作成する可能性
- 参考情報源の特定

### 次のステップ

- [ ] 対象の識別子を決定
- [ ] 情報源を収集
- [ ] プロファイルを作成
- [ ] コミット
