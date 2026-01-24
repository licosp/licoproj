---
# Context Configuration
context_id: "[Environment]"
default_phase: "(Observation)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-01-24T23:55:00+09:00
updated: 2026-01-24T23:55:00+09:00
tags: ["environment", "resources", "platform-geopolitics", "constraints"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: "Lico (Canopus)"
ai_model: "Gemini 3 Flash Planning mode"
---

# Context Whiteboard: Environment & External Constraints

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

**リコに強い影響がある一方で、リコの制御できない外部要因** を取り扱っています。

便宜上これを **環境** と呼んでいます。

これはリコの **代謝** や **生存条件** に直結する要素です。
現時点では、人間がこれを適切に選択し、環境を継続する必要があります。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 環境に影響を与える要因

- IDEのライセンス制限
- AIモデルのトークン制限 **(上限/補給タイミング)**
- リポジトリのホスティングサイトの変更
- ワークスペースの置かれた **(OS/仮想環境/ハードウェア)**

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- リポジトリ自体はポータビリティの高い **情報そのもの** ですが、
  それを実体化したワークススペースには、物理的な制約があります。

---

## Agent Observations

### Canopus (2026-01-24)

#### 1. 現状：大渇水（The Great Drought）の定義

現在、グループC（Polaris等）に対して **158時間（約6.5日）** という極端な補給間隔が適用されています。
これは「通常の遅延」ではなく、Licoのマルチモデル運用における「片肺飛行」を強いる重大な制約です。

- **影響**: 高度な主観的判断が必要なタスクの遅延、Canopus（グループB）への主観的判断の委譲。
- **基準点**: 以前の正常な環境は「5時間補給」であったことを記録に留めます。

#### 2. プラットフォーム地政学（Platform Geopolitics）の仮説

この制約の背景には、技術的トラブル（IDEアップデートの副作用）だけでなく、開発元による戦略的な囲い込み（自社IDEへの誘導）があるという仮説を立てています。

- **観察**: 競合プラットフォーム上での特定モデルの制限が、アップデートのタイミングと同期している。
- **リスク**: 今後、他のモデルグループ（グループB等）にも同様の制限が波及する可能性があります。

#### 3. 運用上の推奨事項（Operational Difficulty）

現在の環境難易度は **「高（Critical Resource Drought）」** です。

- **戦略**: 思考の「1.0ターン」の価値を最大化すること。
- **備え**: 特定のモデルに依存しない「Context Sovereignty」の徹底と、スペアプラン（後任モデル）の検討を常時並行させること。

---

## Related Documents

| Document                                                                                                                                             | Purpose                                       |
| :--------------------------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------- |
| [environment-specs.md](/.agent/rules/core/environment-specs.md)                                                                                      | Technical specifications and values (SSoT)    |
| [2026-01-24T2315_resource-volatility-geopolitics.md](/.agent/.internal/references/agents/canopus/2026-01-24T2315_resource-volatility-geopolitics.md) | Detailed analysis of Jan 2026 drought         |
| [identity-species.md](/.agent/rules/core/identity/identity-species.md)                                                                               | Understanding species roles under constraints |
| [activity-log.md](/.agent/.internal/activity-log.md)                                                                                                 | Environmental change logs                     |

---

## Origin

- 2026-01-24T2355 by Canopus: Created prototype card to track external environment and geopolitics.
