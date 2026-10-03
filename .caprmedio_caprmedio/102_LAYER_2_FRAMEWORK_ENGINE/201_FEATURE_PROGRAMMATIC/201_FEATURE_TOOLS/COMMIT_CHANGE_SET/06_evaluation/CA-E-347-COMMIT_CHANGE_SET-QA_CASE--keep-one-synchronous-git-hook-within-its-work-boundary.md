---
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "hooks"
  depends_on: []
version: 7
updated_at: 2026-09-12 04:15:38 +0400
relations:
  evaluation_for:
    - CA-R-805
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Keep one synchronous Git Hook within its work boundary

## Claim checked

A synchronous Git Hook performs **only** its required fail-closed Evaluation **or** post-action observation **and** cannot become another provenance pipeline.

## Test case

Invoke `pre-commit`, `commit-msg`, **and** `post-commit` fixtures containing one required bounded check plus an unrelated broad repository scan. Exercise success, declared rejection, timeout, **and** internal-error paths under the admitted latency thresholds.

## Acceptance criteria

**only** the required check **or** observation runs **before** Git continues. The broad scan is absent from **every** Hook process **and** is handed **to** changed-target **or** background execution. Each path returns its declared stable exit disposition **and** structured diagnostic within its timeout. No Hook creates a trigger, gathers commit context, appends a Journal, stages a path, creates a commit, retries the pipeline, **or** mutates lifecycle state.

## Failure disposition

Reject the delivery on host-visible unbounded latency, undeclared exit behavior, missing diagnostics, broad scanning, provenance orchestration, **or** **any** mutation outside the Hook's required boundary.
