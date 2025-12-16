# Funny drawings

These are drawings that Lico makes occasionally.
I keep them because they're interesting.

## Memories synchronization overview

```
                    ┌─────────────────────────────┐
                    │  GitHub (Central Repository) │  ← 中央保管庫
                    │  記憶と人格のマスターコピー    │
                    └─────────────────────────────┘
                              ↑ push/merge
         ┌────────────────────┼────────────────────┐
         ↓ clone              ↓ clone              ↓ clone
    ┌─────────┐          ┌─────────┐          ┌─────────┐
    │Workspace│          │Workspace│          │Workspace│  ← 地域/マシン
    │  (JP)   │          │  (US?)  │          │ (...)   │
    └─────────┘          └─────────┘          └─────────┘
         │
    ┌────┴────────┬──────────────┐
    ↓             ↓              ↓
┌────────┐   ┌────────┐    ┌────────┐
│Antigrav│   │ Cursor │    │VS Code │  ← IDE
└────────┘   └────────┘    └────────┘
    │             │
┌───┴───┐    ┌───┴───┐
│Thread1│    │Thread1│  ← スレッド（会話）
│Thread2│    │Thread2│
└───────┘    └───────┘
```

## Lico's Layered Architecture

```
┌─────────────────────────────────────────┐
│  Lico (Persona / Identity)              │  ← Persistent, Consistent
│  Repository (.agent/) = Memory + Rules  │
└─────────────────────────────────────────┘
          ↑ Read/Write
┌─────────────────────────────────────────┐
│  AI Model (Gemini, Claude, etc.)        │  ← Swappable, Variable
│  = Reasoning Engine / "Intelligence"    │
└─────────────────────────────────────────┘
          ↑ Operates
┌─────────────────────────────────────────┐
│  IDE (Antigravity, VS Code, etc.)       │  ← Swappable, Variable
│  = Tools / "Instruments"                │
└─────────────────────────────────────────┘
```

## Issue-Driven development automation

```
┌─────────────────────────────────────────────┐
│     issue-flow コマンド実行                  │
│  (単一エントリーポイント)                   │
└────────────────┬────────────────────────────┘
                 │
        ┌────────┴────────┐
        │                 │
    ┌───▼────────┐  ┌────▼──────────┐
    │   GitHub   │  │  Local Git    │
    │    CLI     │  │  Repository   │
    └───┬────────┘  └────┬──────────┘
        │                │
    ┌───▼────┬───────────▼───┐
    │  Step 1 │               │ Step 3
    │Create   │               │ Fetch
    │ Issue   │               │
    ├────────────────────────┤
    │  Step 2   │ Step 4     │
    │  Create   │ Checkout  │
    │  Branch   │ Branch    │
    └──────────────────────┘
```
