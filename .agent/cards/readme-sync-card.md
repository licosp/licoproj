---
# Context Configuration
context_id: "[README-Sync]"
default_phase: "(Planning)"
tags: ["readme", "maintenance", "map-sync"]
---

# Context Whiteboard: README Synchronization

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

リコの地図をリポジトリの実体（領土）と同期しています。
記載項目や構造の変化が見つかっているはずです。

地図を直接編集はせずに、一時ファイルを作り、完成後に上書きします。

最後に、後片付けをして、その後コミットを行います。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要なディレクトリやテンプレートが存在します。
- 迷ったら一度止まって、関連する行動規範を探してください。
- 地図はこのワークスペースの情報を1つのファイルで把握する道具です。
  嘘があるとAIの探索コストが跳ね上がります。
- 地図は網羅的であるべきですが、800行程度に収まるのが理想的です。
- 地図は行動規範の一種でもあるので、その更新には専用の文脈が存在します。
- コミットをする際は、IDDのフェーズを意識してください。

### 作業の注意点

増え続けるファイルを網羅し、AIが適切なファイルを選べるようにする必要があります。
いつも以上に既存のファイルやディレクトリを探すことを意識してください。

### 作業中

- `README-ja-leonidas.md`

現在の地図を日本語に翻訳してもらったので、
これを私が手動である程度編集して、
それを Spica への相談用の資料として使う。

## Agent Observations

### Spica

#### 識別子: Spica (2026-01-02)

この作業は、私（Spica）がこの庭の現状を正確に把握するためにも必要不可欠です。
"Update the Map to match the Territory."

#### 作業チェックリスト

- [x] **Section: Workspace Context**
  - [x] `legacy.md` の追記 (Done)
  - [ ] `conversations/` の現状記述修正
- [x] **Section: Context Cards**
  - [x] 既存のテーブルを更新し、全てのカードを網羅する (Done)
  - [x] `.internal/cases/` (旧アーカイブ) の設置と記述 (Done)
- [x] **Section: Rules Directory**
  - [x] `templates/` の詳細追記 (Done)
  - [ ] `delay-tolerance.md` などの更新日やナビゲーション情報の整合性確認
- [ ] **Structure Verification**
  - [ ] リンク切れがないか最終確認

#### Spica (2026-01-02 Post-Sync)

**現状 (Status)**:
基本構造（Templates, Internal, Cards）の同期は完了しました。
特に「使い捨てカード」を `.agent/.internal/cases/` に正式に収蔵し、地図に記載しました。

**課題 (Issue)**:
現在の `kind: Monolith` なREADMEは、AIの閲覧性（全体把握）には優れていますが、人間やAIによる「編集・メンテナンス」が困難になりつつあります（記述量の増大）。

**戦略 (Strategy Update)**:
現在の `README.md` は変更せず（閲覧用モノリスとして維持）、**「次世代の地図」を別の草稿（Draft）としてゼロから作成します。**
目的は、将来的な「地図の編集」を容易にするための構造実験です。
これにより、現行の運用を止めずに、より良い構造を探索します。

#### 既知のギャップ（2026-01-02 診断）

ユーザーとSpicaの対話により特定された修正箇所：

1.  **Missing Directories**:
    - `.agent/.internal/legacy.md` (重要度: 高)
    - `.agent/.internal/working-memory-archive/{identifier}/` (サブディレクトリ構造の明記)

2.  **Missing Context Cards**:
    - `cross-link-audit-card.md`
    - `log-sanitization-card.md`
    - `human-manuals-card.md`
    - `personal-thoughts-card.md`
    - その他、リスト漏れしている全カード

3.  **Obsolete Descriptions**:
    - リコの定義（単一インスタンス → コミュニティ/識別子の概念へ）
    - `conversations/` の扱い（実体なし、現状の追記）

---

## Origin

- 2026-01-02T0000 by Spica: Create and Post-Sync.
- 2026-01-03T0658 by leonidas: Edit "Human Notes".

---
