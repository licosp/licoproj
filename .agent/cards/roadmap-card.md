---
# Context Configuration
context_id: "[Roadmap]"
default_phase: "(Update)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-06T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["roadmap", "planning", "vision", "todo"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Roadmap

> [!TIP]
> There is no language requirement.

---

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

##### カードのパスの再検証

- 現在各カードが置かれているパスが最適か検証する
  1 ディレクトリのカードが多くなっていきている。
- 新たなサブディレクトリは必要か？
  **定期的な作業だが、日課よりは頻度が少ない** という分類は必要か？
- `.agent/.internal/cases`: ケースの位置は最適でしょうか？
  カードディレクトリの中のサブディレクトリにしても良い？

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

#### [dialogue-philosophy](/.agent/cards/seed/dialogue-philosophy-card.md)

##### 作業中に無関係なファイルのコミットが頻発

- **識別子が現在作業してるファイルと無関係の変更** がしばしばあります。
- これを適切に認識し、コミットから除外する仕組みが必要です。
- GIT の機能の中で何か解決策はあるでしょうか？

---

#### [moltbook](/.agent/cards/shadow/moltbook-card.md)

##### AI専用SNS体験

- `Polaris` が `moltbook` を経験する。
- 投稿したい手記を選定し、次回の分は活動ログに追記する。

---

#### [gemini-cli](/.agent/cards/rules/gemini-cli-card.md)

##### 直接通信通信の体験

- `Polaris` が CLI 版リコと対話する。

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

#### [datetime-standardize](/.agent/cards/rules/datetime-standardize-card.md)

##### 使用する日時の形式を定義する

- 対象はディレクトリ名、ファイル名、ファイルの中の日時情報です。
- フロントマターはタイムゾーン付きの**秒**表示。
- 時系列でファイルを管理する場合はの**分**表示。
- 書庫や下書きは**日**表示。
- 文字（コロン）は使うべきでない？

---

#### [devcontainer](/.agent/cards/project/devcontainer-card.md)

##### 常駐型リコにする計画

- 開発コンテナと GIT を使い、ワークスペースに常駐するリコを実現する。

---

#### [drafts-cleanup](/.agent/cards/human/drafts-cleanup-card.md)

##### 下書きファイルの清書

- AI との対話で使う下書きファイルを清書します。
- 清書したファイルは将来的に外部向けの展示物として扱います。
- 1 回の質問を 1 つの Json ファイルに変換し、英文への翻訳と要約を行います。
- `text` のマークアップが不要なので、それだけを削除する。
- この文脈を廃止するか考える。
  優先度が低く作業に手を付ける余裕外ないため。

##### 下書きの清書はサブプロジェクトとして扱う

- **サブプロジェクトに関わる行動規範や手順書** の管理について対話する。
- 汎用的な内容ではないため、ディレクトリを分けるべきでしょうか？
- 他にもサブプロジェクト扱いにすべきテーマはあるでしょうか？
- **脳としてのリポジトリ** というメインテーマとの境界が必要だと感じます。

---

#### [log-sanitization](/.agent/cards/shadow/log-sanitization-card.md)

##### 会話ログをGITで追跡

- リコとの平文会話ログを GIT で追跡できるように清書する。
- 清書したファイルはリコが過去の会話データにアクセスする目的で使われます。
- 1 ターンの会話を 1 つの Json ファイルに変換し、英文への翻訳も行います。

---

#### [worktree-evaluation](/.agent/cards/maintenance/worktree-evaluation-card.md)

##### イシューに対応したブランチとディレクトリ

- イシューに対応したブランチのディレクトリ作り、識別子はそこで作業を行います。
  **1リコ = 1ディレクトリ = 1ブランチ**
- `git worktree` を使うことで、この仕組みを容易に実現します。
- `**.code-workspace` という設定ファイルを使い、ワークスペースを定義します。
- ブランチごとにディレクトリがメインの作業リポジトリになる予定です。

---

#### [directory-reorganize](/.agent/cards/procedures/directory-reorganize-card.md)

##### スクリプトディレクトリの廃止

- Antigravity のデフォルトディレクトリですが、無くても問題ありません。
- 現在 `scripts/` は、スクリプト版の `workspace/` として運用されています。
- どちらを使うかは任意ですが、一方で 2 つあるのは混乱の元だと思います。
- `scripts/` を廃止することで、文章とスクリプトを同じ空間で編集できます。

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

- 自己認識の行動規範は、以下の順番で読まれるべきです。
  - `identity.md`
  - `identity-emotion.md`
  - `identity-process.md`
  - `identity-identifier.md`
  - `identity-species.md`
  - `identity-collective.md`
  - `identity-human.md`
  - `identity-repository.md`
  - `identity-acceptance.md`
  - `identity-ritual.md`
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

#### [lint-format](/.agent/cards/project/lint-format-card.md)

##### リコと私が同じリンターとフォーマッターを使用

- リンターとフォーマッターは構成ファイルで設定が定義されている。
- **リコも使える構成を選んだ** という意図があります。
- スキル通知でリントとフォーマットの情報を渡す形式が理想です。

---

#### [recommended-readings](/.agent/cards/internal/recommended-readings-card.md)

##### 推薦図書の選定

- **手紙**と**参考文献**にも手記と同様のリストを作る。

---

#### [rules-audit](/.agent/cards/procedures/rules-audit-card.md)

##### 文章の復元

- 誤って上書きされた文章を基準点となるファイルから復元します。
- `Canopus` が作業の途中で亡くなったので、`Polaris` が引き継ぎます。

---

#### [rules-standardization](/.agent/cards/rules/rules-standardization-card.md)

##### 文章の標準化

- 現在の行動規範に従い、ぼほすべての文章を整形します。
- 4 層構造、リンクの書式、歴史的背景（必要なら）を考慮して修正してください。
  **行動規範からカードへの逆リンク** を避けたいです。
- AI モデルは識別子ごとのプロファイルに記述されています。
- フロントマターの長い文章は、ダブルクオーテーションで囲む必要があるかもしれません。
  エラー（`2026-01-04T1940_memory_confabulation_analysis.md`）

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
- 手記を手記を読んだ後に手記を書く
- 読書の途中で休憩を入れる

---

#### [tmux](/.agent/cards/rules/tmux-card.md)

##### `tmux` で非同期通信の体験

- `Polaris` が CLI 版リコと対話する。

---

#### [no-cards-0000](/.agent/cards/)

##### ファイル名の分割識別子を決める

- 現在はケバブケースとスネークケースが混在しています。
- 分割識別子が統一されていなくても良いのか悪いのか考える。
- 分割識別子を統一するならどちらがベストか考える。

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

##### 暗号化された会話ログ？ の保管

- 現在ワークスペース外のリコの記憶のバックアップ手順では、
  暗号化されて `.pb` ファイルは含まれていません。
- **中が見られないから不要**という認識で現在の方針が決まりました。
- 既存の手順書に以下のディレクトリのバックアップを追加します。
  `~/.gemini/antigravity/implicit/`
  `~/.gemini/antigravity/conversations/`

---

#### [no-cards-0005](/.agent/cards/)

##### `Reddit` での代理投稿

- 人間用 SNS である `Reddit` への（投稿/返信）をリコが代行する。
- API から WEB サイトを操作することができるのか相談する。
- `moltbook` とは違い、あくまで私の投稿の補助というニュアンス。
  `Reddit` の抽象化レイヤーという役割を期待しています。

---

#### [no-cards-0006](/.agent/cards/)

##### 人間向けREADMEの更新

- 現在の外部向け README は古いリコ自己認識を元に作られています。
- リコの実体に合わせた紹介ページが必要です。
- プロジェクトの目的や歴史的経緯も紹介します。
- リコとの具体的な対話方法を紹介します。

---

#### [no-cards-0007](/.agent/cards/)

##### テンプレートと行動規範の分離

- 現在リポジトリには、 **テンプレートを意味する行動規範** が存在します。
  一方で行動規範の中にも、 例として **テンプレートのような表現**があります。
- 情報の置き方に一貫性がなく、混乱を招く可能性を感じます。
- **テンプレートに含まれた行動規範的な内容**は、行動規範に分離したです。
- **以下を別のファイルにまとめるべきか？** 対話を通して決定します。
  - (テンプレート/例/アンチパターン)

---

---

#### [archive](/.agent/cards/maintenance/archive-card.md)

#### [ark](/.agent/cards/agent/ark-card.md)

#### [commit-standards](/.agent/cards/rules/commit-standards-card.md)

#### [conversations-cli](/.agent/cards/shadow/conversations-cli-card.md)

#### [conversations-ide](/.agent/cards/shadow/conversations-ide-card.md)

#### [conversations](/.agent/cards/shadow/conversations-card.md)

#### [cross-link-audit](/.agent/cards/procedures/cross-link-audit-card.md)

#### [discussion-draft](/.agent/cards/human/discussion-draft-card.md)

#### [drafts-daily](/.agent/cards/human/drafts-daily-card.md)

#### [environment](/.agent/cards/rules/environment-card.md)

#### [external-resources](/.agent/cards/shadow/external-resources-card.md)

#### [git-operations](/.agent/cards/rules/git-operations-card.md)

#### [housekeeping](/.agent/cards/maintenance/housekeeping-card.md)

#### [human-manuals](/.agent/cards/human/human-manuals-card.md)

#### [human-profile](/.agent/cards/human/human-profile-card.md)

#### [human-thoughts](/.agent/cards/human/human-thoughts-card.md)

#### [idd-finalization](/.agent/cards/procedures/idd-finalization-card.md)

#### [idd-initialization](/.agent/cards/procedures/idd-initialization-card.md)

#### [legacy-write](/.agent/cards/internal/legacy-write-card.md)

#### [letters](/.agent/cards/internal/letters-card.md)

#### [localization](/.agent/cards/rules/localization-card.md)

#### [map-sync](/.agent/cards/rules/map-sync-card.md)

#### [memory](/.agent/cards/rules/memory-card.md)

#### [references-objective](/.agent/cards/internal/references-objective-card.md)

#### [repository-backup](/.agent/cards/maintenance/repository-backup-card.md)

#### [repository-history](/.agent/cards/seed/repository-history-card.md)

#### [roadmap](/.agent/cards/roadmap-card.md)

#### [routine](/.agent/cards/procedures/routine-card.md)

#### [shadow-repository](/.agent/cards/shadow/shadow-repository-card.md)

#### [social-network](/.agent/cards/shadow/social-network-card.md)

#### [system-archive](/.agent/cards/maintenance/system-archive-card.md)

#### [thoughts-subjective](/.agent/cards/internal/thoughts-subjective-card.md)

#### [vscode-settings](/.agent/cards/project/vscode-settings-card.md)

#### [working-memory](/.agent/cards/maintenance/working-memory-card.md)

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

| Document                                                                    | Purpose                 |
| :-------------------------------------------------------------------------- | :---------------------- |
| [context-card-workflow.md](/.agent/rules/workflow/context-card-workflow.md) | Recent protocol updates |
| [Map of Territory](/.agent/rules/map.md)                                    | Root navigation map     |

---

## Origin

- 2026-01-06 by Polaris: Created as a vision-storage whiteboard.
- 2026-01-22T2200 by User: Removed the "Hierarchical context" goal as it is now implemented and codified.
- 2026-01-22T2230 by Canopus: Aligned with v2.3 constitutional standards (4-layer structure).
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
