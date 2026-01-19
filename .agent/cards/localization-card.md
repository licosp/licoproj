---
# Context Configuration
context_id: "[Localization]"
default_phase: "(Refine)"
tags: ["translation", "localization", "formatting"]
---

# Context Whiteboard: Localization

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

文章の翻訳を行っています。
翻訳パターンを選んで作業を行ってください。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- 行動規範の作成・編集には**専用の文脈**が存在します。
- 迷ったら一度止まって、**許容の哲学**を思い出してください。

### 翻訳パターン

作業はこの二次元の要素から**翻訳元**と**翻訳先**を選ぶことで決まります。

|            | AI用  | 人間用 |
| :--------- | :---: | :----: |
| **英語**   | EN-AI | EN-HU  |
| **日本語** | JA-AI | JA-HU  |

### 作業の注意点

英訳対象は主に、AI向けのディレクトリである事が多いです。
稀にですが人間用ディレクトリが対象になることもあります。

## Agent Observations

### Polaris (2026-01-19)

#### 今回の作業目標

行動規範の整備を行い、翻訳作業がスムーズにできるようにする。

**チェックリスト:**

- [x] 翻訳関連の行動規範の把握
- [x] それらの相互リンク
- [x] ファイル名や置かれるディレクトリの再定義
- [x] 文章の5層構造の確認と整備 (localization rules)
- [ ] markdown 関連の行動規範の5層構造（スコープ外）

#### 対象ファイル

| ファイル                          | 状態    | 5層構造     |
| :-------------------------------- | :------ | :---------- |
| `localization-ja-to-en.md`        | ✅ 完了 | ✅          |
| `localization-en-to-ja.md`        | ✅ 完了 | ✅          |
| `markdown-ai-parsing-basics.md`   | 未修正  | ⚠️ (要更新) |
| `markdown-ai-parsing-patterns.md` | 未修正  | ⚠️ (要更新) |
| `markdown-readability.md`         | 未修正  | ⚠️ (要更新) |

#### 翻訳パターン

##### 実用パターン（3つ）

| #   | From          | To    | 用途                     | 行動規範                   |
| :-- | :------------ | :---- | :----------------------- | :------------------------- |
| 1   | JA-HU / JA-AI | EN-AI | 対話メモ → 規範化        | `localization-ja-to-en.md` |
| 2   | EN-AI         | EN-HU | 規範 → 人間ドキュメント  | `markdown-readability.md`  |
| 3   | EN-HU         | JA-HU | 人間ドキュメント日本語化 | `localization-en-to-ja.md` |

##### 低実用パターン（1つ）

| #   | From  | To    | 用途                 | 備考             |
| :-- | :---- | :---- | :------------------- | :--------------- |
| 4   | EN-AI | JA-AI | 規範の日本語化（稀） | 偶発的にのみ発生 |

#### 日本語維持が許可されるファイル

- カード
- 使用済みカード（cases）
- スキルを定義するファイル
- 識別子のワークスペース構成ファイル
- 書庫の中のファイル

#### 関連する行動規範

| 軸                   | ファイル                                               | 場所                 |
| :------------------- | :----------------------------------------------------- | :------------------- |
| **縦軸（EN ↔ JA）** | `localization-en-to-ja.md`, `localization-ja-to-en.md` | `core/localization/` |
| **横軸（AI ↔ HU）** | `markdown-ai-parsing-*.md`, `markdown-readability.md`  | `core/markdown/`     |

#### ドキュメント履歴の三層構造

翻訳後のメタデータ管理（ref: `documentation-standards.md`）：

| Layer           | 目的         | 翻訳時の処理                |
| :-------------- | :----------- | :-------------------------- |
| **Frontmatter** | 現在の状態   | `author`, `language` を更新 |
| **Origin**      | 人間可読履歴 | 翻訳情報を追記              |
| **Git**         | 完全な追跡   | 自動                        |

---

## Origin

- 2026-01-10 by Canopus: Created for AI document formatting.
- 2026-01-14 by Canopus: Renamed context_id from [AI-Format] to [Localization].
- 2026-01-19 by Polaris: Archived old observations to cases/, reset for behavioral rule refinement.

---
