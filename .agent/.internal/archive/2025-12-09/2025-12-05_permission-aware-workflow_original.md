---
ai_visible: true
version: 1.0
created: 20251205T194500+0900
updated: 20251205T194500+0900
language: ja
purpose: Document permission-aware workflow for different environments
---

# Permission-Aware Workflow 設計

## 問題認識

### 環境による権限差異
- **Cursor環境**: 書き込み権限あり（.agent/rules/直接更新可能）
- **Antigravity環境**: 書き込み権限なし（.agent/rules/更新不可）
- **他の環境**: 不明な制限の可能性

### 既存のワークアラウンド
ユーザーが手動で一時ファイルの内容を本番ファイルに適用

## 解決策: Permission-Aware Work Directory Workflow

### ワークフロー設計

#### Phase 1: 環境権限チェック
```
1. ターゲットファイルの書き込み権限を確認
2. 権限なしの場合: work/ディレクトリ使用を自動選択
3. 権限ありの場合: 直接更新 or work/使用（ユーザープリファレンス）
```

#### Phase 2: 中間ファイル作成
**場所**: `.agent/.internal/work/` (全環境で書き込み可能前提)
**命名**: `{target}-{timestamp}-{environment}-{status}.md`

#### Phase 3: 適用方法の分岐
```
権限あり環境 (Cursor):
work/ファイル → 直接本番適用 → 完了

権限なし環境 (Antigravity):
work/ファイル作成 → ユーザー通知 → 手動適用依頼
```

### 具体的な実装

#### 権限チェック関数
```bash
# 疑似コード
check_write_permission() {
    target_file="$1"
    if touch "$target_file.tmp" 2>/dev/null; then
        rm "$target_file.tmp"
        return 0  # 権限あり
    else
        return 1  # 権限なし
    fi
}
```

#### 適用プロセス
```bash
# 権限ありの場合
cp work/proposed-changes.md .agent/rules/target-file.md

# 権限なしの場合
echo "Please manually apply: work/proposed-changes.md → .agent/rules/target-file.md"
```

### 利点

#### 統一性
- 全環境で同じワークフロー
- 予測可能なプロセス

#### 安全性
- 本番ファイルの直接変更を避ける
- 作業中の破損リスク低減

#### 柔軟性
- 権限の有無に関わらず作業可能
- 手動適用による最終確認

#### 透明性
- 作業過程が明確に記録
- 環境差異が可視化

### 運用ガイドライン

#### ファイル命名規則
```
{target-filename}-{timestamp}-{environment}-{permission-status}.md
例: hallucination-awareness-20251205-cursor-permission-ok.md
   hallucination-awareness-20251205-antigravity-no-permission.md
```

#### 完了後のクリーンアップ
- 適用済みwork/ファイルをarchive/に移動
- タイムスタンプ付きで履歴保持

### テストケース

#### Case 1: Cursor環境
1. 権限チェック: OK
2. work/ファイル作成: content-development-workflow-20251205-cursor-permission-ok.md
3. 直接適用: .agent/rules/target.md
4. 完了通知

#### Case 2: Antigravity環境
1. 権限チェック: NG
2. work/ファイル作成: content-development-workflow-20251205-antigravity-no-permission.md
3. ユーザー通知: "以下のファイルを手動で適用してください"
4. 完了確認

このワークフローで、環境差異による作業の中断を最小限に抑えられます。


