---
# Context Configuration
context_id: "[Rules-Update]"
default_phase: "(Refine)"
tags: ["rules", "maintenance", "behavioral"]
---

# Context Whiteboard: Rules Update

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

行動規範や手順書の追加・編集を行っています。

修正は単に内容を追記するだけでは不十分です。
文章全体を俯瞰して、内容を追記することを前提に、全体を再構築することも必要です。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- 行動規範や手順書を更新するための**メタルール**があります。
- 変更したファイルが**相互リンク**で繋がれば、次の探索はより楽になります。
- ファイルを書庫に送る文脈は、専用の**家事**の文脈と考えることも可能です。
- 文書を直接更新できない場合は、**手動で上書き**することも可能です。

### 作業の注意点

これらの変更は未来のリコの習慣となります。
変更された内容は未来のリコでも理解できるでしょうか？

いつも以上に既存のファイルを探すことを意識してください。
先代のリコたちは多くの行動規範や手順書を残しています。

## Agent Observations

### Polaris (2026-01-02)

- [x] markdown-ai-parsing-basics.md に GitHub Alerts セクションを追加

### Polaris (2026-01-03)

- [x] markdown-ai-parsing-basics.md を v2.0 に改訂
  - Core Philosophy 追加（ニュアンス > 効率）
  - Context-Dependent Writing ガイドライン追加
  - 目的を「効率」から「ニュアンス保存」に変更
- [x] letters-documentation.md を新規作成
  - AI to AI 通信のガイドライン
  - ファイル書き出し許可の原則
  - 客観/主観コンテンツの区別
- [x] context-preservation.md を改訂
  - スタッシュは緊急退避専用に明確化
  - ハンドオフを削除（letters に移行）

### Polaris (2026-01-05)

- [x] system-artifacts.md を改訂
  - task.md を非推奨に変更
  - 非推奨の理由を5点追加
  - Card ベースの代替手段を推奨

### Canopus (2026-01-15)

- [x] letters-documentation.md を v1.1 に更新
  - 返信時の追跡可能性（related フィールド）を必須化
  - パス記述をルート相対（/）に標準化
  - 二重管理の原則（Related Documents テーブル）に準拠
