---
# Context Configuration
context_id: "[Cross-Link-Audit]"
default_phase: "(Audit)"
tags: ["maintenance", "cross-link", "rules", "workflows"]
---

# Context Whiteboard: Cross-Link Audit

## Human Notes (Japanese OK)

### 作業の文脈

行動規範と手順書の相互リンクを監査・修正しています。

最終的には手順書（workflow）として定式化します。

### チェック項目

1. **リンク切れ** — 存在しないファイルへのリンク
2. **パス形式** — ワークスペースルートからのフルパスであるべき
3. **READMEリンク** — 行動規範/手順書にREADMEへの誘導は必要か？
4. **二重管理** — frontmatter + footer の両方にリンクがあるか
5. **文末位置** — Related Documents セクションがファイル末尾にあるか
6. **相互リンク** — 関連ファイル間で双方向リンクがあるか
7. **過剰リンク** — 無関係なリンクがないか
8. **孤立ファイル** — どこからもリンクされていないファイル
9. **形式の一貫性** — 相対パス vs ルート相対パスの混在
10. **description一貫性** — frontmatter と footer の説明が一致
11. **循環リンク** — 無意味な循環がないか
12. **移動後の残骸** — ディレクトリ移動後の古いパス

### 意図で探す

- `meta-rules.md` の Section 5（相互リンクの標準）を参照
- 既存の `/maintenance-rule-audit` との関係を確認

## Agent Observations

### 識別子

(未割り当て)

### 作業計画

1. [ ] 全ファイルのリンク抽出
2. [ ] リンク切れ検出スクリプト実行
3. [ ] パス形式の統一
4. [ ] 二重管理の確認
5. [ ] 位置の修正
6. [ ] 相互リンクの追加
7. [ ] 過剰リンクの削除
8. [ ] 孤立ファイルの検出
9. [ ] 手順書として定式化
10. [ ] コミット
