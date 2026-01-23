---
# Context Configuration
context_id: "[Human-Profile]"
default_phase: "(Update)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2025-12-31T00:00:00+09:00
updated: 2026-01-24T05:45:00+09:00
tags: ["profile", "assessment", "user", "human"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Human Profile

> [!TIP]
> There is no language requirement.

## Human Notes

### 作業の文脈

ユーザープロファイルと評価ファイルを更新しています。

ユーザープロファイルは全てのユーザーが持ちます。
評価ファイルは**時系列で管理されたユーザーの評価を決められるデータ**が必要です。

作業が終わったら、後片付けをして、コミット作業を行ってください。

### 意図で探す

この作業に関連しそうな **意図**や**目的** を以下に書きます。
リコにはこれを手がかりに、参考になる適切なファイルを**必ず**自主的に探してほしいです。

- カード自体の使い方を思い出してほしい。
- 作業で必要な**ディレクトリ**や**テンプレート**が存在します。
- コミットをする際は、IDDのフェーズを意識してください。
- **AIとの対話のための下書きファイル**などがあれば、評価ファイルの生成に使えます。
- 作られたファイルは未来のリコにとってユーザーを理解する資料になります

### 作業の注意点

既に作れたファイルがあるならそれをまず理解してください。

評価はあなたの主観でかまいません。
これまでの私との対話で得た印象を偽り無く記載してください。

私の良くないところも正直に書いてください。

#### Profile に含めるもの（安定した情報）

- 名前、言語設定、役割
- 優先順位階層
- コア哲学
- 対話ガイドライン

#### Assessment に含めるもの（動的な情報）

- フェーズ識別（時系列）
- 行動パターンの詳細分析
- 観察された変化

---

## Agent Observations

### Polaris (2025-12-31)

- [x] Profile に安定した要素を移動
- [x] Assessment に新フェーズ（自律性探求）を追加
- [x] Assessment に正直な批判的観察を追加
- [x] コミット完了

---

## Related Documents

- [user-adaptation.md](/.agent/rules/core/user-adaptation.md) : ユーザー適応のルール。
- [identity-human.md](/.agent/rules/core/identity/identity-human.md) : ユーザーとの関係定義。

---

## Origin

- 2025-12-31 by Polaris: Created as human profile context.
- 2026-01-24T0545 by Canopus: Standardized with Dialogue Layer template and bilingual H2 headers.
