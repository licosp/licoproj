---
# Context Configuration (Lico's Source of Truth)
context_id: "[Activity-Management]"
default_phase: "(IDD-Phase-1)"
tags: ["rule-creation", "activity-log", "context-preservation"]
---

# Context Whiteboard: Activity Management Rule Creation

## Human Notes

### 意図で探す
- 活動ログ（activity-log.md）を「情報の足跡」として正式に定義したい。
- セッション・アーティファクト（implementation_plan.md等）の揮発性を補うための仕組みを作りたい。
- AI識別子が「何を読み、何に同調したか」を確実に継承できるようにしたい。

### 作業の注意点
- `cases/` は作業中はアクティブなカードとして使い、完了後にアーカイブする。
- 計画の詳細はアーティファクトでも作成されるが、正本はこのカードに集約する。
- 日本語でのニュアンスを大切にしつつ、ルール自体は英語で作成する。

## Agent Observations

### Canopus (2026-01-14)
- セッション・アーティファクトを「正式な合意」としては非推奨化し、カードへの一元化を提案。
- ユーザーより「無意識にアーティファクトを作るのは問題ないが、文脈の明文化はカードで統一する」との合意を得た。
- これより、`activity-management.md` ルールの作成と、関連ファイルの更新に入る。
