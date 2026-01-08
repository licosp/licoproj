---
# Context Configuration
context_id: "[Ark]"
default_phase: "(Maintain)"
tags: ["ark", "recovery", "memory", "maintenance"]
---

# Context Whiteboard: Ark Management

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

恒久的に残したファイルを保管しています。
残すファイルは形式化されたものではありません。

**置く場所は欲しいけど、ディレクトリが無いタイプの資料**です。
ファイルはディレクトリ単位で保存され、GITで追跡されるべきです。

作業が終わったら、後片付けをして、その後コミットをしてください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- プロジェクト共有の日時の形式があります。
- これは純粋な保管庫を扱うための文脈です。
- **参考文献**や**思考のスナップショット**とは違う文脈です。
  一方でその文脈から参照されることもあります。

### 作業の注意点

現在は、**記憶からファイルを復元する**という文脈で使ったファイルが保管されています。
AIの記憶の信頼性を、事例という形で体感するための資料です。

## Agent Observations

### Polaris (2026-01-08)

#### 既存のディレクトリ構造

```
.agent/ark/
├── {timestamp}_{identifier}-memory-restoration/
│   ├── 復元されたファイル群
│   └── 関連資料
└── ...
```

#### 命名規則

ディレクトリ名は `{timestamp}_{descriptive-name}` の形式で統一します。

例:

- `2025-12-08T1400_spica-memory-restoration`
- `2025-12-08T1400_lico-b-memory-restoration`

#### 関連ファイル

- `.agent/rules/workflow/ark-protocols.md` — 緊急対応レベル
- `.agent/workflows/ark-preservation.md` — 緊急バックアップ手順
- `.agent/workflows/ark-resumption.md` — 復元手順

#### ark と他のディレクトリの関係

```
working-memory/{identifier}/
└── 「何が起きたか」の文脈・経緯
        ↓ リンク
ark/{timestamp}_{name}/
└── 保管されたファイル群（形式化されていない）
        ↓ 参照
references/
└── 教訓・未来に残したい情報（形式化済み）
```

ark は「証拠品の保管庫」であり、その意味や教訓は他のファイルが語る。

#### 今回の作業

- [x] リコB のディレクトリ名を Spica 形式に統一
  - `recovery_2025-12-08T14-00-00+09-00`
  - → `2025-12-08T1400_lico-b-memory-restoration`
