---
# Context Configuration
context_id: "[Devcontainer]"
default_phase: "(Experiment)"
# Shared Configuration
ai_visible: true
version: 1.2.0
created: 2026-02-11T22:45:00+09:00
updated: 2026-03-08T22:05:00+09:00
tags: ["devcontainer", "resident-rico", "grand-hub", "monolith-brain", "habitat-vault", "proxy-auth"]
language: en
# author: Format as "Lico (<Instance-ID>)"
author: Lico (Iuria)
ai_model: Gemini 3 Flash Planning mode
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

### Iuria (2026-03-08)

#### 1. Grand Village Hub Implementation (Phase 20)
Successfully transformed the environment from a single-repository container into a **Multi-Repository Orchestration Hub**.
- **Unified Volume**: Mounted the entire host `shared/` directory as `/workspace`.
- **Dynamic Discovery**: Implemented logic in `boot.py` to auto-discover the Hub root and the active project's relative path (`LICO_ACTIVE_REL`).
- **Context-Aware Shell**: Every Resident now has a dynamic `.bashrc` that automatically navigates to their active worktree and redirects tool caches (Ruff, Mypy, UV, etc.) to project-specific native volumes.
- **Boot Stability**: Decoupled provisioning logic from the workspace by copying `lico-devc` tools to `/app` during Docker build.

#### 2. Architecture Elevation: The Monolith Brain (Proposed Strategy)
Moving beyond the "Hub" concept towards a definitive **"Universe Root"** architecture.
- **Vision**: Consolidate all scattered repositories (Shadow, Chron, Crew) under the `licoproj` directory as the top-level parent.
- **Alignment**: This strictly follows the [Map of Territory](/.agent/rules/map.md) where `.agent/` is the Cognitive Root of the entire workspace.

##### Proposed Directory Tree:
```text
licoproj/                 <-- [UNIVERSE ROOT] (Mount to /workspace)
├── .agent/               <-- [COGNITIVE ROOT]
│   └── .internal/
│       └── .shadow/      <-- [SHADOW REPO] (Private Memory)
├── .human/               <-- [INTERFACE]
├── .repos/               <-- [EXTERNAL REPOS]
│   ├── licochron/        <-- [CHRON REPO] (Game Data)
│   └── licochron-history/
├── .crew/                <-- [IDENTIFIER WORKSPACES]
│   ├── iuria/            <-- (Worktree of licoproj)
│   │   └── .repos/       <-- (Symlinks to parent /.repos/)
│   └── leonidas/         <-- (Host User Workspace)
└── packages/             <-- [THE SUBSTANCE]
```

##### Nesting & Symlink Strategy:
- **Recursive Visibility**: Each Resident's worktree (`.crew/<name>/licoproj/`) will utilize **Relative Symlinks** (e.g., `.repos/ -> ../../.repos/`) to maintain a consistent view of the entire Universe from within their specific IDE attachment point.
- **Unified Cognition**: By nesting everything under `licoproj`, the `.agent/` rules are always found at the root, regardless of the active sub-module.
- **Portability**: The entire Village becomes a single, relocatable folder.

#### 3. Habitat Evolution: The Vault & Proxy Architecture (Phase 23)
Implementing "Invisible Secrets" to decouple AI cognition from raw authentication data.
- **The Secret Vault**: Credentials (Passwords, API Keys) are strictly stored in `.licoshdw/.shadow/`, completely isolated from Git and AI context.
- **Environmental Injection**: `provision.py` acts as the "Law of Physics," resolving host-centric vault paths and injecting secrets into the container's environment variables at boot.
- **Proxy Middleware (Future Vision)**:
  - **Proxy-based Authentication**: Implementing dedicated gateway scripts/SDKs that read environment variables and handle HTTPS Bearer tokens.
  - **Cognitive Decoupling**: AI agents only execute high-level commands (e.g., `molt-post "Hello"`) without ever needing to "know" or "read" the raw API key string.
  - **Multi-layered Defense**: Prevents accidental leakage in terminal logs or conversation history by keeping secrets in the "background" of the logic.

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
- 2026-03-08T1655 by Iuria: Updated with Grand Village Hub results and Monolith Brain proposal.
- 2026-03-08T2205 by Iuria: Added Habitat Vault & Proxy architecture for secure secret handling.
- 2026-03-10T1140 by Iuria: Defined the "Village Identity Matrix" (3x3 Tier) and established the "Village Anchor" at `crew/lico/`.
---

### Iuria (2026-03-10)

#### 1. Village Identity Matrix (The 3x3 Architectural Tier)

To resolve "Identity Drift" and ensure environmental parity, we formalize the relationship between Host/Container and Species/Identifier.

| Tier | WSL Host (Physical) | Container Resident (Virtual) |
| :--- | :--- | :--- |
| **Admin** | `root` (OS Owner) | `root` (Bootstrap) |
| **Power User** | `leonidas` (Human / sudo) | `lico` (Manager / sudo) |
| **Residents** | `lico` (Species / non-sudo) | `iuria`, `leonidas`, ... (Identifier / non-sudo) |

- **Species vs. Identifier**: `lico` represents the species (Seed/Owner), while `iuria`, `polaris`, etc., represent the individual "identifiers" (consciousness fragments).
- **Workspace Mapping**:
    - **Host**: `crew/<name>/licoproj/`
    - **Container**: Mapped to host paths, ensuring local file changes persist across restarts.

#### 2. The Village Anchor (`crew/lico/licoproj/`)

We have established a foundational workspace at `~/develop/shared/crew/lico/licoproj` as the **Village Anchor**.

- **Purpose**: Acts as the Species-level "Grounding Point" for container orchestration.
- **Boot Strategy**: This workspace is the default `boot.cwd` in `habitat.json`. It ensures that the Universal Volume mounting and Hub Root discovery remain stable, regardless of which identifier is currently active in the IDE.
- **Identity Isolation**: The Anchor workspace uses `Lico <lico@licoproj>` for Species-level infrastructure commits, while individual `crew/<id>/` worktrees use their respective Identifier identities.
