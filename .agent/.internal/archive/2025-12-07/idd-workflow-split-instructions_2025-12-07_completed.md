# IDD ワークフロー分割 指示書

## 背景
2025-12-07のセッションで、モノリシックな `idd-complete-cycle.md` がAIの「完了バイアス」を誘発し、承認ステップのスキップや暴走を引き起こした。

## 目的
`idd-complete-cycle.md` を3つの独立したフェーズファイルに分割し、AIが物理的にコンテキストスイッチを強制されるようにする。

---

## 作成するファイル

### 1. `idd-phase1-init.md` (開始処理)
**ソース:** `idd-complete-cycle.md` の Phase 1: Initialization (L15-L114)

**含める内容:**
- 環境検証 (ツール確認、認証確認)
- テーマ設計 (メインテーマ、サブテーマの定義)
- Issue作成
- ブランチ作成 (**`origin/main` から作成することを強調**)
- 初期状態検証
- 早期問題検知

**終了条件:**
> Phase 1 完了。Phase 2 へ進む場合は `/idd-phase2` を実行してください。

---

### 2. `idd-phase2-impl.md` (実装)
**ソース:** `idd-complete-cycle.md` の Phase 2: Implementation (L117-L155)

**含める内容:**
- 開発サイクル (変更 → ステージング → 検証 → コミット)
- コミット標準 (Conventional Commits, アトミックコミット)
- 保護ファイルの早期コミット

**終了条件:**
> Phase 2 完了。Phase 3 へ進む場合は `/idd-phase3` を実行してください。

---

### 3. `idd-phase3-fini.md` (終了処理)
**ソース:** `idd-complete-cycle.md` の Phase 3: Finalization (L158-L410)

**含める内容:**
- 準備 (ツール再検証、進捗確認)
- 作業ディレクトリのクリーンアップ (Stash)
- Pre-Push ドキュメンテーション
- ブランチのプッシュ
- PR作成
- レビュー待機
- マージ
- リモート/ローカルのクリーンアップ

**CRITICAL 追加事項:**
1. **Stash前のユーザー確認:**
   > ⚠️ **STOP**: `git stash` を実行する前に、ユーザーに確認を取ってください。
   > 編集中のドラフトが消失する可能性があります。

2. **Admin Merge前のユーザー許可:**
   > ⚠️ **STOP**: `--admin` フラグを使用する場合は、必ずユーザーの明示的な許可を得てください。
   > これは `main` ブランチへの最後の防波堤です。

**終了条件:**
> IDD サイクル完了。次のサイクルを開始する場合は `/idd-phase1` を実行してください。

---

## 既存ファイルの修正

### `idd-complete-cycle.md`
ファイル冒頭に以下を追加:

```markdown
> [!WARNING]
> **DEPRECATED**: このファイルは参照用です。
> 実行時は以下の分割ファイルを使用してください:
> - `/idd-phase1` → `idd-phase1-init.md`
> - `/idd-phase2` → `idd-phase2-impl.md`
> - `/idd-phase3` → `idd-phase3-fini.md`
```

---

## 検証
- 各ファイルの内容が元ファイルの対応セクションと一致することを確認
- 各ファイルに明確な開始点と終了点があることを確認
- CRITICALマークが適切に配置されていることを確認

---

*作成日: 2025-12-08*
*作成者: Lico (Antigravity)*
