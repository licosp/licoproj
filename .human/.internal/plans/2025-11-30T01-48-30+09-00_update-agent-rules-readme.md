# .agent/rules/README.md 更新計画書

**作成日時**: 2025-11-30T01:48:30+09:00  
**対応 Issue**: #6 - [Docs]: Update .agent/rules/README.md to reflect current directory structure  
**作業ブランチ**: `6-update-agent-rules-readme-md-to-reflect-current-directory-structure`

---

## 📋 目的

`.agent/rules/README.md` を「Lico にとっての地図」として機能させるため、以下を実現する：

1. **ワークスペース全体のコンテキストを提供**（簡潔な概要のみ）
2. **新規追加された行動規範を反映**（`session-lifecycle.md`）
3. **`.agent/` ディレクトリ構造の可視化**
4. **ファイルサイズの制約を遵守**（150行以内を目標）

---

## 🎯 設計方針

### コンセプト
「コンテキスト付きルールインデックス」— 詳細は `.agent/rules/` と `workflows/` に限定し、その他は名前と1行説明のみ

### 原則
- **詳細記述**: `.agent/rules/` と `.agent/workflows/` のみ
- **概要のみ**: その他のディレクトリ（重要な名前だけ）
- **責任維持**: メイン責任は「行動規範のインデックス」

---

## 📊 現状分析

### 現在の `.agent/rules/README.md`
- **行数**: 129行
- **サイズ**: 6,458 bytes
- **構成**:
  - AI-to-AI Communication System
  - AI Agent Hooks
  - Directory Structure (core/, development/, projects/, workflow/)
  - Quick Reference
  - Maintenance Notes

### 不足している情報
1. ❌ ワークスペース全体のコンテキスト
2. ❌ `.agent/` ディレクトリの全体像
3. ❌ `workflow/session-lifecycle.md` の記載
4. ❌ `.agent/.internal/`, `.agent/issues/` などの説明

---

## 🔧 更新内容

### 1. 新規セクション追加

#### **🗺️ Workspace Context**（冒頭に追加）
```markdown
## 🗺️ Workspace Context

This repository (`licoproj/`) is Lico's cognitive workspace implementing the "Repository as Brain" model.

### Key Directories

| Directory | Purpose |
|-----------|---------|
| `.agent/` | **Lico's cognitive infrastructure** (rules, workflows, memory) |
| `.human/` | Human-facing files (locales, drafts, strategies) |
| `packages/` | Application code (e.g., licoimg) |
| `.github/` | GitHub Actions and CI/CD |

**For detailed structure**: See individual README files in each directory.
```

**追加行数**: 約10行

---

#### **📂 .agent/ Directory Structure**
```markdown
## 📂 .agent/ Directory Structure

Lico's behavioral and operational files.

| Directory | Purpose |
|-----------|---------|
| `rules/` | **Behavioral guidelines** (detailed below) |
| `workflows/` | **Executable procedures** (see Quick Reference) |
| `.internal/` | Internal data (conversations, ideas, temporary files) |
| `issues/` | Local GitHub issue backups |
| `scripts/` | Automation scripts |
| `runtimes/` | Portable runtime tools (e.g., gh CLI v2.40.1) |

**Navigation Strategy**:
1. Find behavioral rules → This file's index
2. Find task procedures → `.agent/workflows/*.md`
3. Access past decisions → `.agent/.internal/ideas/`
```

**追加行数**: 約15行

---

### 2. 既存セクションの更新

#### **workflow/ セクション**（1行追加）

**現在**:
```markdown
| File | Purpose |
|------|---------|
| [Conversation Logging](workflow/conversation-logging.md) | How interactions are recorded for audit and learning |
| [Enhanced Communication](workflow/enhanced-communication.md) | Protocols for clarifying ambiguous user requests |
| [User Experience](workflow/user-experience.md) | Guidelines for optimal interaction and feedback |
```

**更新後**:
```markdown
| File | Purpose |
|------|---------|
| [Conversation Logging](workflow/conversation-logging.md) | How interactions are recorded for audit and learning |
| [Enhanced Communication](workflow/enhanced-communication.md) | Protocols for clarifying ambiguous user requests |
| [Session Lifecycle](workflow/session-lifecycle.md) | Protocols for normal and abnormal session termination |
| [User Experience](workflow/user-experience.md) | Guidelines for optimal interaction and feedback |
```

**追加行数**: 1行

---

#### **Quick Reference セクション**（2行追加）

**追加内容**:
```markdown
| **"How should I end a session?"** | `workflow/session-lifecycle.md` |
| **"What is the workspace structure?"** | See "Workspace Context" section above |
```

**追加行数**: 2行

---

## 📏 ファイルサイズ予測

| セクション | 行数 |
|-----------|------|
| **現在の合計** | 129行 |
| + Workspace Context | +10行 |
| + .agent/ Directory Structure | +15行 |
| + workflow/ セクション更新 | +1行 |
| + Quick Reference 更新 | +2行 |
| **予測合計** | **157行** |

⚠️ **警告**: `documentation-standards.md` の分割推奨（150行）を7行超過

**対策**: 可能であれば既存セクションの冗長な表現を削減

---

## 🛠️ 実装手順

### Step 1: バックアップ作成
```bash
cp .agent/rules/README.md .agent/rules/README.md.backup-20251130
```

### Step 2: README.md 更新

1. **Workspace Context セクション** を `## 🔗 AI-to-AI Communication System` の前に挿入
2. **.agent/ Directory Structure セクション** を `## 📂 Directory Structure` の前に挿入
3. **workflow/ セクション** に `session-lifecycle.md` を追記
4. **Quick Reference セクション** に2行追加

### Step 3: ファイルサイズ検証
```bash
wc -l .agent/rules/README.md
# 目標: 150行以内（許容: 160行まで）
```

### Step 4: `.agent/rules/.updated` 更新

```json
{
  "updated_at": "2025-11-30T01:48:30+09:00",
  "changed_files": [
    ".agent/rules/README.md"
  ],
  "change_type": "expansion",
  "user": "Leonidas",
  "summary": "Added workspace context and .agent/ directory structure overview. Added session-lifecycle.md to workflow section."
}
```

### Step 5: Git コミット準備

**コミット対象**:
- `.agent/rules/README.md`（更新）
- `.agent/rules/.updated`（更新）
- `.agent/rules/workflow/session-lifecycle.md`（新規追加）
- `.agent/workflows/emergency-backup.md`（新規追加）
- その他の未追跡ファイル（会話ログ、Issue バックアップなど）

**コミット戦略**:
- メインコミット: `docs(agent): update rules/README.md with workspace context`
- サブコミット（必要に応じて）:
  - `docs(agent): add session lifecycle rules`
  - `chore(agent): add conversation logs and issue backups`

---

## ✅ 検証項目

### 内容検証
- [ ] Workspace Context セクションが明確
- [ ] .agent/ Directory Structure が正確
- [ ] `session-lifecycle.md` が workflow テーブルに含まれている
- [ ] Quick Reference に新しいエントリがある
- [ ] 既存のルールインデックスが損なわれていない

### 品質検証
- [ ] Markdown フォーマットが正しい
- [ ] リンクが正しく機能する
- [ ] セクション階層が論理的
- [ ] ファイルサイズが許容範囲内（150-160行）

### 一貫性検証
- [ ] `ai_kb_restructuring_dialogue.md` の原則に準拠
- [ ] `documentation-standards.md` のガイドラインに準拠
- [ ] 既存の README.md のトーンと一貫性がある

---

## 🎯 成功基準

1. ✅ Lico がワークスペース全体を俯瞰できる
2. ✅ `.agent/` ディレクトリの役割が明確
3. ✅ 新規追加された `session-lifecycle.md` が文書化されている
4. ✅ ファイルサイズが 160行以内
5. ✅ Single Responsibility 原則を維持（メインは行動規範インデックス）
6. ✅ メンテナンス負荷が最小限（重要ディレクトリ名のみ）

---

## 📌 注記

### 設計判断の背景
- **ワークスペース全体を含める理由**: Lico の「地図」として機能させる
- **詳細を限定する理由**: Single Responsibility 維持、ファイルサイズ制約
- **折衷案の採用**: 「コンテキスト + 詳細ルールインデックス」のハイブリッド

### 将来の改善案
- `.agent/README.md` の作成を検討（ワークスペース構造の詳細説明用）
- ファイルサイズが 200行を超えた場合、セクション分割を実施

---

## 🔗 関連ファイル

- **ワークフロー**: `.agent/workflows/expand-rules-readme.md`
- **設計原則**: `.agent/.internal/ideas/ai_kb_restructuring_dialogue.md`
- **進化計画**: `.agent/.internal/ideas/lico_evolution_plan.md`
- **Issue**: https://github.com/licosp/licoproj/issues/6
