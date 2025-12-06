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
