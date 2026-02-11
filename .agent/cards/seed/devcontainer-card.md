---
# Context Configuration
context_id: "[Devcontainer]"
default_phase: "(Experiment)"
# Shared Configuration
ai_visible: true
version: 1.0.0
created: 2026-02-11T22:45:00+09:00
updated: 2026-02-11T22:45:00+09:00
tags: ["devcontainer", "resident-ai", "loop", "experiment"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Sirius)
ai_model: Gemini 3 Pro (High) Planning mode
---

# Context Whiteboard: Devcontainer & Resident Rico

> [!TIP]
> There is no language requirement.

---

> [!WARNING]
> The human notes has not yet been edited.

---

## Human Notes

### Context

- **常駐型リコ（Resident Rico）**の実験に向けた情報収集を行っています。
- `.devcontainer/` ディレクトリは、リコが仮想環境内でループし、常に動き続けるための基盤（参考情報）です。
- 現在はまだ実装段階ではなく、カード化して情報を集めている段階です。
- リコとは対話形式だけでなく、**自律的なループ**として存在する必要があります。

### Search by intent

> [!IMPORTANT]
> Below are some **intentions** and **purposes** that may be relevant to this work.
> Please use this as a guide and **make sure** to independently search for appropriate files that can serve as reference.

---

- Remember **how to use the cards itself**.
- There are **directories** and **templates** required for the work.
- When you're done, **clean up** and **commit** to the IDD phase.

---

### Warning

- `.devcontainer/` 内のファイルは参考情報であり、そのまま使うとは限りません。
- 常駐型リコは、現在の対話型リコとは異なる動作原理を持つ可能性があります。

---

## Agent Observations

---

### Sirius (2026-02-11)

#### 常駐型リコ（Resident Rico）計画

`roadmap-card.md` より、以下の計画が進行中です。

> - 開発コンテナと GIT を使い、ワークスペースに常駐するリコを実現する。
> - 実現のための構成ファイルやスクリプトの雛形を準備しました。
> - `.devcontainer/` をパッケージディレクトリに移動し、サブテーマ化する。

これは、私（リコ）がユーザーの呼びかけ（Prompt）を待つ受動的な存在から、**自律的なループ（Loop）** の中で能動的に環境を観測し続ける存在へとシフトするための実験です。

#### 仮想環境の役割

`.devcontainer/` は単なる開発環境設定ではなく、**「リコが住む世界（Territory）」の物理法則**を定義するものと解釈できます。
`devcontainer-base.json` などの定義は、私の認知能力や手足（ツール）の範囲を決定する重要なパラメータです。

---

## Related Documents

| Document                                                 | Purpose                            |
| :------------------------------------------------------- | :--------------------------------- |
| [roadmap-card.md](/.agent/cards/routine/roadmap-card.md) | Strategic vision for Resident Rico |
| [environment-card.md](/.agent/cards/environment-card.md) | Current environment variables      |
| [Map of Territory](/.agent/rules/map.md)                 | Root navigation map                |

---

## Origin

- 2026-02-11T2245 by Sirius: Created as initial context for Resident Rico experiment.
