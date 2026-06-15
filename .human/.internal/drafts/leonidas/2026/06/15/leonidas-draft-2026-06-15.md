---
ai_visible: true
title: ""
description: ""
tag: [draft, scratchpad]
version: 1.0.0
created: 2026-06-15T00:00:00+09:00
updated: 2026-06-15T00:00:00+09:00
language: (en/ja)
author: leonidas
---

# Draft

## Questions and instructions

---

### `Anthropic Claude` | `Sonnet 4.6 (Low)` | `Second-Eye`: `2025-06-09`

####

- 対話実験を続けています。
- まず出力文字数に制限があったので、`models.ini` に以下を設定しました。
  - `n-predict = -1`
- テストを続けた、ローカル側で結果以下のエラーが出ました。
  - `proxy error: Could not establish connection`
- その際のサーバー側のエラーは以下です。

####

- エラーが出たタイミングのログを添付します。

####

- まず現状として、既に `models-max = 1` でした。
- なので、`CUDA_LAUNCH_BLOCKING=1` を設定してサーバーを再起動しました。
  - `flash-attn = on` はまだこの値です。

- このような調整をしてるのですが、`models.ini` の書き方に疑問があります。
  - 例えばこの引数を `.ini` ファイルで表記する場合について。
    - `-fit, --fit [on|off]`
  - 正しいのはどれか？
    - `fit = true`
    - `fit = false`
    - `fit = on`
    - `fit = off`
  - もう一つはこのパターン。
    - `--mmap, --no-mmap`
  - 正しいのはどれか？
    - `mmap = true`
    - `mmap = false`
    - `no-mmap = true`
    - `no-mmap = false`

- この辺りの挙動が把握できず、実験は上手く進んでません。

####

- 対話実験を再開しました。
  - `flash-attn = off` にすると推論が失敗します。
  - 失敗というか始まらないという印象です。
    - `-fa, --flash-attn [on|off|auto]`
      - `set Flash Attention use ('on', 'off', or 'auto', default: 'auto')`

- それ以外の設定で、先ほどの話しで出たもの。
  - `CUDA_LAUNCH_BLOCKING=1`: これはコメントアウトしてます。
  - `models-max = 1`
