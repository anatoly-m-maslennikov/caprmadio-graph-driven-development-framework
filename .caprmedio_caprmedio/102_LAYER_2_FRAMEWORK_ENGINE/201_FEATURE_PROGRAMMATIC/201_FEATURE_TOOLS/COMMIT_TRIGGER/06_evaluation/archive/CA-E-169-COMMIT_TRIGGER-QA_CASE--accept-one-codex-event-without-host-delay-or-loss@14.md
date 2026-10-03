---
subjects:
  governs: "Commit Trigger"
  depends_on: []
version: 14
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-087
    - CA-R-803
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Accept one Codex event without host delay or loss

## Claim checked

the asynchronous Codex PostToolUse carrier acknowledges **only** one atomic durable inbox event **and** performs no provenance pipeline work.

## Test case

Configure the installed Hook with async: true, block the background service, invoke one supported Codex Tool, delay Hook completion around the atomic rename boundary, **then** end the host session **and** repeat concurrent **and** duplicate source-event deliveries.

## Acceptance criteria

the Tool result becomes available **without** waiting for Hook completion. One schema-valid immutable event exists **after** atomic acceptance even **when** the host session **then** ends. Concurrent distinct events remain distinct, out-of-order completion is accepted, **and** a repeated stable identity is idempotent. Hook execution performs no repository scan, graph traversal, context gathering, Journal append, staging, Git mutation, retry, lifecycle mutation, **or** worker spawn.

## Failure disposition

Reject intake **if** host dispatch waits for provenance work, an acknowledged event is absent, a duplicate effect exists, **or** **any** prohibited work occurs **in** the Hook process.
