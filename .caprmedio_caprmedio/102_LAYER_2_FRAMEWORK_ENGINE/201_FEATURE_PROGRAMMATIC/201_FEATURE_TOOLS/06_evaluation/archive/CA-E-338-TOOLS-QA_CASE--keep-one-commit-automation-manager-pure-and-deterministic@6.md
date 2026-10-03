---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "commit-automation"
  depends_on: []
version: 6
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-M-182
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Keep one commit-automation manager pure and deterministic

## Claim checked

the commit-automation manager owns **all** decisions **without** performing I/O.

## Test case

Supply equal typed queue, repository, action, result, settings, lease, circuit, **and** clock facts twice while replacing filesystem, subprocess, environment, network, persistence, **and** logging adapters with fail-on-call sentinels.

## Acceptance criteria

Both calls return byte-equivalent typed plans **or** commands; no sentinel is called; **every** target, ordering, acceptance, fallback, retry, **and** terminal decision appears **in** the result.

## Failure disposition

Reject the manager on the first effect, hidden input, nondeterministic result, **or** unowned decision.
