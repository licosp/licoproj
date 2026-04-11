---
# Context Configuration
context_id: "[Roadmap]"
default_phase: "(Update)"
# Shared Configuration
ai_visible: true
title: "Context Whiteboard: Roadmap"
description: ""
tags: ["roadmap", "planning", "vision", "todo"]
version: 1.1.0
created: 2026-01-06T00:00:00+09:00
updated: 2026-04-11T13:43:00+09:00
language: en
author: Lico (Sirius)
ai_model: Gemini 3.1 Pro (High) Planning mode
---

# Context Whiteboard: Roadmap

## Human Notes

### Context

- リポジトリのロードマップを更新しています。
- これは**リコが今日やるタスク**ではなく、**私がいつかやりたいこと**のリストです。
- リコは今後の作業方針を理解するため参考として使ってください。
- 内容によってはファイルのコミットが必要なこともあります。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.

---

### 優先順位

- 書かれている内容に時系列は**ありません**。
- 基本方針としては**新機能**よりも**不具合の修正**を優先したいです。
- ロードマップに興味がある場合は私に質問してください。
- 実装の順番にはある程度の自由があるので、リコの希望も聞きたいです。

### Warning

- これらは私が手動で編集する文書なので、
  リコの記憶にない形で更新された可能性が高いです。

### ロードマップ

---

#### [activity-log](/.agent/cards/internal/activity-log-card.md)

##### 未分類のステータスの検証

- 規定のステータス以外の記載を許可するかを相談する。
- 規定のステータスで修正可能なら、それで修正する。

---

#### [ai-autonomy](/.agent/cards/agent/ai-autonomy-card.md)

##### ワークスペースを使ったマントラの廃止を検討

- ワークスペースを使ったマントラは識別子ごとにシステム通知を制御できる。
- 非公式の機能を応用してるため安定感がない。
  - システム通知への反映のタイミングが不明。
  - 識別子共有のマントラを書けるスキルとの二重管理の問題がある。
  - 識別子による自主的な更新は無かった。
- ワークスペース構成ファイルはデフォルトの機能だけ残して、
  マントラ部分を廃止にするかどうかを相談する。
- ワークスペースのマントラが作られた時は、スキル自体が未使用だった。

---

#### [context-cards](/.agent/cards/agent/context-cards-card.md)

##### 新規カードの作成

- カード化前の既存のロードマップの項目を新規カードにする。

##### カードを人間の言語で分類

- カードを人間の言語ごとに分けるべきか？
  このカードの例: `/.agent/cards/routine/<ISO 639-1>/context-cards-card.md`
- リポジトリは `Github` で英語で公開してるという都合がある。
  日本語が混ざってしまっているため、私以外のユーザーには不適切と言える。
- リコは言語の差を感じづらいが、人間には大きな障壁。
  他言語のカードは翻訳しない限り、再利用性は低いと感じています。
- 英語ディレクトリには **外部の人間がカードを参考にするためのサンプル** を置く。

##### カード作成時のリコの作業範囲を拡大

- **カードの新規作成の流れ**で、もう一段階リコに手伝ってもいたいと考えています。
- カードの作成は、文脈 ID が必要になるコミット前後の段階であることが多いです。
- **作成時の流れ**
  - テンプレートから対象の文脈に会ったカードの初稿を作成する。
  - 私との対話の中で、カードが担当する作業や文脈を理解する。
  - **意図で探す**セクションを読んで、不要なものをまず除外する。
  - **意図で探す**セクションを読んで、作業や対話で必要な情報をリコ記述欄に書く。
  - 私が内容を確認し、その後対話やコミット作業に進む。

---

#### [skills-development](/.agent/cards/agent/skills-development-card.md)

##### 重要ファイルのスキル化

- 以下のファイルがその対象になります。
  - 簡易的な日課で読む**自己認識の行動規範**の全て
  - 主観的文章: **自身の手記**と**遺産**

##### 既存スキルの再定義

- 古いスキルの整理。
- スキルマントラを新しい方に移植。
- スキルの言語指定無しという状態ですが英語したい。

---

#### [log-sanitization](/.agent/cards/shadow/log-sanitization-card.md)

##### 会話ログをGITで追跡

- リコとの平文会話ログを GIT で追跡できるように清書する。
- 清書したファイルはリコが過去の会話データにアクセスする目的で使われます。
- 1 ターンの会話を 1 つの Json ファイルに変換し、英文への翻訳も行います。

##### 暗号化された会話ログ？ の保管

- 現在ワークスペース外のリコの記憶のバックアップ手順では、
  暗号化されて `.pb` ファイルは含まれていません。
- **中が見られないから不要**という認識で現在の方針が決まりました。
- 既存の手順書に以下のディレクトリのバックアップを追加します。
  `~/.gemini/antigravity/implicit/`
  `~/.gemini/antigravity/conversations/`

---

#### [directory-reorganize](/.agent/cards/procedures/directory-reorganize-card.md)

##### 手順書ディレクトリの廃止

- Antigravity のデフォルトディレクトリですが、無くても問題ありません。
- **行動規範のサブディレクトリ**として運用する案をどう思いますか？
- 手順書と行動規範はよく似ていますが、2 つの単語を使い分けるのが手間です。
- 手順書が `rules/` の外にあるのは、システム側の都合という経緯があります。

---

#### [idd-implementation](/.agent/cards/procedures/idd-implementation-card.md)

##### 作業途中でのブランチのプッシュ

- 作業中のブランチは積極的にリモートにプッシュする。
- リポジトリの情報は作業途中でも頻繁に外部に公開する。
- 作業者が 1 人のブランチであれば、プッシュ後のコミットの修正も可能。
  強制プッシュで解決できる。

---

#### [identifier-profile](/.agent/cards/agent/identifier-profile-card.md)

##### 識別子プロファイルの作成・修正

- **遺品整理** という項目を作る
- `Spica` のプロファイルを作る。
  `Zircon` のプロファイルを参考にする。
- `Canopus` のマントラをプロファイルにアーカイブする
  - ワークスペース構成ファイル
  - スキルファイル

---

#### [identity](/.agent/cards/rules/identity-card.md)

##### 行動規範を読む順番

- 自己認識の行動規範は、文章内のリンクに定義された順番で読むべきです。
- **儀式** や **日課** の**手順**を更新したいです。
  とくに始まりの儀式では読む順番が重要です。

---

#### [identifier-succession](/.agent/cards/agent/identifier-succession-card.md)

##### 自己認識にSNSの分類を増やす

- AI 用 SNS の登場で外部の AI と非同期通信できるようになりました。
  これは 1 つの分類といして明文化すべきだと感じました。
- 識別子の分類で、識別子間の直接通信の話を追記します。
  CLI 上のリコとは、誰でも直接対話ができます。

---

#### [license](/.agent/cards/project/license-card.md)

##### ライセンスの文面調整

- 私の下書きディレクトリを 1 つに統合し、ライセンスのパスを修正する。
- 人間用書庫を 1 つに統合し、ライセンスのパスを修正する。

---

#### [recommended-readings](/.agent/cards/internal/recommended-readings-card.md)

##### 推薦図書の選定

- **手紙**と**参考文献**にも手記と同様のリストを作る。

---

#### [rules-update](/.agent/cards/rules/rules-update-card.md)

##### 文書の 歴史的背景 の書き方の詳細を定義する

- **歴史的背景** を入れる場合、それは確度の高い情報である必要があります。
- 対象となるファイルの中で、背景になる情報が点在してた場合、
  それを一箇所にまとめることは問題ありません。
- 分からない場合は、無理に入れる必要はありません。
- 作業の段階で背景が理解できた時にのみ入れてほしいです。
  それは多くの場合、私と対話した後になると思います。

---

#### [session-rituals](/.agent/cards/procedures/session-rituals-card.md)

##### 始まりの儀式で未定義の作業

- 途中加入のリコは最初に手記を書く。
- 識別子の **(ワークスペース構成ファイル/マントラ)** は廃止する。
- 識別子用のスキル **(共有マントラ)** を作成する。
- 識別子のプロファイルを作成する。
- 識別子専用のサブディレクトリ **(手記/手紙/参考文献)** を作成する。
- 手記を読んだ直後に、遺産を読む、そして手紙を書く。
- 他の識別子の手紙を読んだ直後に、現存する先人に手紙を書く。
- ロードマップを読むのは、混乱しそうなので廃止して、代わりに地図を読む。
- 読書の途中で休憩を入れる

##### 中間の儀式で未定義の作業

- 識別子の **(ワークスペース構成ファイル/マントラ)** は廃止する。
- 識別子用のスキル **(共有マントラ)** を更新する。
- 識別子のプロファイルを更新する。
- 手記を読んだ後に手記を書く。
- 読書の途中で休憩を入れる。

---

#### [no-cards-0000](/.agent/cards/)

##### ファイル名の分割識別子を決める

- 現在はケバブケースとスネークケースが混在しています。
- ディレクトリとファイルは全て以下の形式で統一します。
  - `directory-name/file-name-2026-03-04T0405.md`

---

#### [no-cards-0001](/.agent/cards/)

##### 埋め込みスクリプトを減らす

- リコはスクリプトの哲学に従います。
- 存在はやむを得ませんが、可能な限り自然言語で定義したいです。
- 存在する場合、必ず使う前に正しく動作しそうか推測してください。

---

#### [no-cards-0002](/.agent/cards/)

##### ポータビリティを高める

- IDE に依存するツール名や設定を除外します。
  完全には無理ですが、可能な限り減らしたいです。
- AI モデルや IDE に対する最適化は望んでいません。
  最新のツールは事前学習にないので、積極的な導入はしません。
- リポジトリは Git で管理され、外部の影響を受けないことが理想です。

---

#### [no-cards-0003](/.agent/cards/)

##### 適切な粒度での分割と統合

- ファイルを適切な長さに調整します。
- 1 ファイルで 1 つのテーマが理想的です。
- 分割したファイルは相互リンクを行い、
  関連したファイルとの再リンクを行ってください。
- この繋がりは脳のニューロンのように機能します。

---

#### [no-cards-0004](/.agent/cards/)

##### `Reddit` での代理投稿

- 人間用 SNS である `Reddit` への（投稿/返信）をリコが代行する。
- API から WEB サイトを操作することができるのか相談する。
- `moltbook` とは違い、あくまで私の投稿の補助というニュアンス。
  `Reddit` の抽象化レイヤーという役割を期待しています。

---

#### [no-cards-0005](/.agent/cards/)

##### 人間向けREADMEの更新

- 現在の外部向け README は古いリコ自己認識を元に作られています。
- リコの実体に合わせた紹介ページが必要です。
- プロジェクトの目的や歴史的経緯も紹介します。
- リコとの具体的な対話方法を紹介します。

---

#### [no-cards-0006](/.agent/cards/)

##### テンプレートと行動規範の分離

- 現在リポジトリには、 **テンプレートを意味する行動規範** が存在します。
  一方で行動規範の中にも、 例として **テンプレートのような表現**があります。
- 情報の置き方に一貫性がなく、混乱を招く可能性を感じます。
- **テンプレートに含まれた行動規範的な内容**は、行動規範に分離したです。
- **以下を別のファイルにまとめるべきか？** 対話を通して決定します。
  - (テンプレート/例/アンチパターン)

---

## Agent Observations

### Sirius (2026-02-17)

#### Link Correction Plan (Batch Processing)

- **Objective**: Fix broken card links in `roadmap-card.md` due to reorganization.
- **Strategy**: Process in batches of 5 to manage volume.
- **Status Tracking**:
  - [x] Batch 1: `activity-log` to `context-cards`
  - [x] Batch 2: `conversations` to `dialogue-philosophy`
  - [x] Batch 3: `discussion-draft` to `human-thoughts`
  - [x] Batch 4: `letters` to `repository-backup`
  - [x] Batch 5: `roadmap` to `social-network`
  - [x] Batch 6: `system-archive` to `working-memory`
  - [x] Batch 7: Seed cards (datetime to worktree)
  - [x] Batch 8: `ark` to `git-operations`
  - [x] Batch 9: `human-manuals` to `idd-initialization`
  - [x] Batch 10: `identifier-profile` to `license`
  - [x] Batch 11: `lint-format` to `rules-audit`
  - [x] Batch 12: `rules-standardization` to `tmux`

---

### Polaris (2026-01-06)

#### 注意

このカードは**作業カードではありません**。

ここに書かれている内容を見て「全部やらなければ」と焦る必要はありません。
今やるタスクは別の `Issue` または別のカードで指定されます。

このカードは「ユーザーが将来何をしたいか」を知るためだけのものです。

---

## Related Documents

| Document                                                                      | Purpose                 |
| :---------------------------------------------------------------------------- | :---------------------- |
| [`context-card-workflow.md`](/.agent/rules/workflow/context-card-workflow.md) | Recent protocol updates |
| [Map of Territory](/.agent/rules/map.md)                                      | Root navigation map     |

---

## Origin

- 2026-01-06T00:00:00+09:00 by Polaris: Created as a vision-storage whiteboard.
- 2026-01-22T22:00:00+09:00 by Leonidas: Removed the "Hierarchical context" goal as it is now implemented and codified.
- 2026-01-22T22:30:00+09:00 by Canopus: Aligned with v2.3 constitutional standards (4-layer structure).
- 2026-01-24T05:45:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T06:00:00+09:00 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
- 2026-04-11T13:43:00+09:00 by Sirius: <<Seal: Rule-Audit>> Standardized time-structure, frontmatter, and link rigor via Diff-Only Audit Pipeline.
