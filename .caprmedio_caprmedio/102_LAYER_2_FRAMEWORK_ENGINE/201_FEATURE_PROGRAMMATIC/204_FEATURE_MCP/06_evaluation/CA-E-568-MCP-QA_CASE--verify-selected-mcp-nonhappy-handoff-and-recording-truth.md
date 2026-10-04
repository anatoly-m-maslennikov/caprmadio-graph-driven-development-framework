---
atom_id: CA-E-568
content_role: Evaluation
type: QA Case
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-05 02:00:00 +0400"
subjects:
  governs: "MCP/selected Workflow non-happy truth"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal]
relations:
  evaluation_for: [CA-R-1847, CA-R-1848]
---
# Summary

Verify selected MCP non-happy, handoff, and recording truth

## Scope

Functional MCP failures for unauthorized execute, incomplete or stale binding manifests, deferred/handoff, cancellation, partial/unknown effects, and shared event-recording recovery.

## Claim

Every realization **must** preserve the shared service's non-happy evidence and must never replay work to recover recording.

## Details

Using a functional fixture, submit unauthorized mutation `execute`, unsupported
`apply`, unsealed/unknown route, missing route binding, altered manifest digest,
stale original-source or query-admission pin, stale source/frontier, malformed
parent lineage, and absent worker cases. For both query routes submit a secret
selection, a mutation parameter, and each malformed/ambiguous/nonliteral
CA-R-1850 filter case. Also submit a
`source_freshness.definition_manifest_ref` or `.definition_manifest_digest`
shadow field both equal to and different from the outer canonical
`definition_manifest` digest. Each returns blocked/rejected/deferred as
applicable, performs no unapproved mutation or autostart, and creates no
invented Run, Action Run, Event, or effect for an unstarted call. Simulate
handoff-required, cancellation, failed, partial-effect, unknown-effect, and
no-op outcomes from shared support; assert the MCP result retains the exact
outcome, safe refs, and diagnostics without a success conversion or fabricated
effect.

For `find_and_fetch_journal_events`, retain the pre-dispatch sealed source
prefix, then attempt source-member mutation, truncation, deletion, duplicate or
malformed Event, stale continuation, and self-Run/Event inclusion. Each retained
member failure is rejected with its diagnostic; later append strictly outside the
prefix remains allowed; neither the query's own Event nor a recovery retry can
enter or enlarge the result. Assert a preview has no Run/Event and an admitted
actual query records only actual outcomes through shared support after snapshot
capture, never by replay.

Simulate an Action that completed but whose canonical event append is pending. Observation must return the actual Action/Run status plus `recording_blocker` and pending event ref. Invoke `recover_selected_run_recording` twice with the same event ref and verify only the same event/payload is retried, no Action/Workflow execution is called, and a durable receipt is visible only after shared support confirms it. Reject a mismatched event/run or raw replacement payload.

Acceptance retains request traces, target mutation traces, service invocation count, event identities/payload digests, and output/result/receipt references. This is planned functional proof, not a runtime pass.

### Sources

- CA-R-1847 v4; CA-R-1848 v4; CA-D-547 v5; CA-A-1142 v2; CA-P-1532 v2; CA-P-1535 v2; CA-D-527 v3; CA-R-1850 v2; CA-R-1866 v2; CA-R-1867 v1.
