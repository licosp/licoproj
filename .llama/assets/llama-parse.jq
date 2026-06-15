def format_timestamp:
  . + (9 * 3600) |
  strftime("%Y-%m-%dT%H:%M:%S") + "+09:00";

{
  uuid: $req.uuid,
  model: .model,
  created_at: (.created | format_timestamp),
  finish_reason: .choices[0].finish_reason,
  prompt: $req.messages[0].content,
  thinking: .choices[0].message.reasoning_content,
  response: .choices[0].message.content,
  total_duration: null,
  completion_tokens: .usage.completion_tokens,
  prompt_tokens: .usage.prompt_tokens,
  tokens_per_second: (
    if .timings.predicted_per_second != null
    then .timings.predicted_per_second
    else null
    end
  ),
  draft_accepted_rate: (
    if .timings.draft_n != null and .timings.draft_n > 0
    then (.timings.draft_n_accepted / .timings.draft_n * 100)
    else null
    end
  )
}
