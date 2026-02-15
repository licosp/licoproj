---
# Context Configuration
context_id: "[Log-Sanitization]"
default_phase: "(Planning)"
# Shared Configuration
ai_visible: true
version: 1.1.0
created: 2026-01-01T00:00:00+09:00
updated: 2026-01-24T06:00:00+09:00
tags: ["logs", "sanitization", "archival", "security"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: ""
ai_model: ""
---

# Context Whiteboard: Log Sanitization Strategy

> [!TIP]
> There is no language requirement.

---

> [!WARNING]
> The human notes has not yet been edited.

---

## Human Notes

### Context

万単位の行数に及ぶ巨大な会話ログを、AI が安全かつ効率的に扱えるようにするための戦略を策定しています。
Git 追跡されていない（ワークスペースにある）ログを、将来的にアーカイブ化するための前準備でもあります。

### 現状の課題と合意事項（2026-01-01）

1. **課題**:
   - **サイズ**: 万行単位のファイルは AI のコンテキストウィンドウを圧迫し、`view_file` (800 行制限) での閲覧も困難。不正確な理解や Recency Bias の原因になる。
   - **セキュリティ**: 絶対パス（ユーザー名）などの個人情報が含まれており、Git 追跡できない。AI に「読んで消せ」と指示するのは Hallucination リスクが高い。

2. **合意された戦略**:
   - **物理分割**: 会話のターン（またはセッション）単位で小さなファイルにプログラムで分割する。
   - **機械的サニタイズ**: AI 判断ではなく、スクリプト（Regex 等）で絶対パスなどを機械的に置換する。
   - **検証**: 分割・置換が正しく行われたかを検証するスクリプトを別途作成する（文字数、シーケンス、境界値チェック）。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

この作業に関連しそうな **意図**や**目的** を以下に書きます。

- **閲覧性の向上**: 巨大な 1 ファイルより、分割された 1 万ファイルの方が `grep` 検索やピンポイント閲覧（`view_file`）に適している。
- **安全性**: AI の推論（曖昧さ）を排除し、確実なロジックで機密情報を守る。
- **ポータビリティ**: 誰でも（どのインスタンスでも）安全に読める状態にする。

### Warning

---

## Agent Observations

---

## Related Documents

| Document                                                                                 | Purpose                                 |
| :--------------------------------------------------------------------------------------- | :-------------------------------------- |
| [log-sanitization-card.md](/.agent/cards/seed/log-sanitization-card.md)                  | This strategy card itself               |
| [absolute-path-prohibition.md](/.agent/rules/core/security/absolute-path-prohibition.md) | Security rules regarding absolute paths |
| [Map of Territory](/.agent/rules/map.md)                                                 | Navigation reference                    |

---

## Origin

- 2026-01-01 by Polaris: Initial strategy proposal.
- 2026-01-24T0545 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized with Dialogue Layer template and bilingual H2 headers.
- 2026-01-24T0600 by Canopus: <<Seal: Rules-Standardization-Batch7>> Standardized Related Documents to table format and ensured English-only headers.
