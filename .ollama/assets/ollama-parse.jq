def to_jst:
  gsub("\\.[0-9]+Z$"; "Z") |
  strptime("%Y-%m-%dT%H:%M:%SZ") |
  mktime + (9 * 3600) |
  strftime("%Y-%m-%dT%H:%M:%S") + "+09:00";

{
  model: .model,
  created_at: (.created_at | to_jst),
  finish_reason: .done_reason,
  prompt: $req.prompt,
  thinking: .thinking,
  response: .response,
  total_duration: (if .total_duration != null then (.total_duration / 1000000000) else null end),
  eval_count: .eval_count,
  eval_duration: (if .eval_duration != null then (.eval_duration / 1000000000) else null end),
  tokens_per_second: (if (.eval_duration != null and .eval_duration > 0) then (.eval_count / (.eval_duration / 1000000000)) else null end)
}
