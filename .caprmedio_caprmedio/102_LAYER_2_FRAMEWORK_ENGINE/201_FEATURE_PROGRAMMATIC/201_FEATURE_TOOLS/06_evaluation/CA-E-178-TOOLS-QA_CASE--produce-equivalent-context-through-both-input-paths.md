---
subjects:
  governs: "Commit Context"
  depends_on: []
version: 15
updated_at: "2026-09-17 03:09:42 +0000"
relations: {"evaluation_for":["CA-M-087","CA-R-803","CA-R-804","CA-R-805","CA-R-802"]}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
cce_version: cce_1
cce_form: evaluation
---
# Produce equivalent context through both input paths

## Claim checked

COMMIT_CONTEXT returns equivalent provisional context for the same durable trigger **and** observed repository frontier whether invoked directly **or** by the independently supervised COMMIT_AUTOMATION service under CA-R-802/804 **and** CA-M-087.

## Test case

1. freeze the sealed trigger, Initiative, action identity, observation inputs, **and** repository fixture. invoke the standalone Finder **and** retain its context.
2. independently enqueue the same trigger **and** let COMMIT_AUTOMATION dispatch **only** the context-gathering worker for comparison. retain the durable intake **and** scheduler transitions; do **not** ask COMMIT_CHANGE_SET **to** gather context **or** orchestrate peer Tools.
3. compare the contexts from equivalent observation frontiers, excluding **only** registered non-semantic transport metadata. account for authorized intake **and** scheduler state separately from the Finder's read-only boundary.

## Acceptance criteria

- the contexts preserve the same Initiative, action identity, repository frontier, target, expected Revisions **or** digests, provenance bindings, **and** real-change message Projection.
- **every** Finder invocation is read-only: it acquires no Git lease, appends no Journal Record, writes no runtime state, stages no path, **and** creates no Commit.
- the scheduled route **may** persist its admitted intake **and** scheduling state under CA-R-802/803. those effects **must** be attributed **to** their owners **and** do **not** authorize Finder mutation **or** a peer-orchestrating Git Doer.
- stop the fixture at the context boundary; no Journal worker **or** Git effect is dispatched by this comparison. a message Projection is **not** a Commit **or** a receipt claiming that one exists.
- a changed observation frontier is **not** hidden as transport metadata. resupply an equivalent frontier **or** report that equivalence was **not** established.

## Failure disposition

reject a realization on a divergent semantic context field, unregistered exclusion, Finder mutation, peer orchestration by COMMIT_CHANGE_SET, **or** effects outside the admitted intake/scheduling fixture. preserve the inputs, observation frontier, returned contexts, **and** attributable effect evidence.
