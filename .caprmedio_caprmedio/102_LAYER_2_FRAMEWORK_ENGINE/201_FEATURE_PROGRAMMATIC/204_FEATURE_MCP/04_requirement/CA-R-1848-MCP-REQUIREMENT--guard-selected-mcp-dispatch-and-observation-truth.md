---
atom_id: CA-R-1848
content_role: Requirement
current_scope_unit: MCP
claim_target_scope_unit: MCP
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 4
updated_at: "2026-10-05 02:00:00 +0400"
subjects:
  governs: "MCP/selected Workflow dispatch truth"
  depends_on: [MCP, Tool, Workflow, Action, Operator, Run, Journal]
relations:
  relates_to: [CA-R-1847, CA-R-1720, CA-R-1525, CA-P-1484]
---
# Summary

Guard selected MCP dispatch and observation truth

## Scope

Authorization, currentness, result truth, and defer/handoff behavior at the selected MCP boundary.

## Claim

MCP **must not** report dispatch, completion, effects, or recording as successful unless the shared service returns exact current evidence for that fact.

## Details

Before a preview or execute, the adapter validates the selected route against
exactly one outer `definition_manifest` reference/digest, its canonical binding,
exact admitted source/definition revisions, root/frontier and target/reference
digests, input schema, and parent lineage. That one manifest preserves CA-A-1142
v2 as the unchanged original-thirteen registry and contains the two exact
CA-P-1532@2/CA-P-1535@2 query-source admission frontier pins required by
CA-R-1847; it has no competing registry or manifest. The source-freshness
object may carry only its selected-source registry/binding evidence: any
`definition_manifest_ref`, `definition_manifest_digest`, or other
duplicate/shadow manifest field there or anywhere else is an unknown field and
is rejected before comparison, including a matching or different digest.
Missing, incomplete, duplicate, malformed, digest-mismatched, changed, stale,
conflicted, unsupported, unsealed, or unauthorized bindings return `blocked` or
`rejected` without dispatch, Run, Action Run, worker start, effect, or Journal
event. Preview creates no Run, Action Run, Event, mutation authority, or Journal
write. A mutation-capable `execute` without exact current Operator authorization
returns `blocked`; an admitted read-only query `execute` requires its exact
current query-source admission and never substitutes mutation authority. The
adapter must not substitute a newer source revision, widen a selected set,
infer authority from a prior request, or accept an `apply` mode.

For `find_and_fetch_journal_events`, capture the source Journal byte-prefix and
bind CA-O-163's snapshot token before any Workflow/Action-start recording or
Action dispatch. Only the sealed prefix can be queried; later Run/Event records
are outside it. Both query routes accept only CA-R-1850's shared closed literal
grammar, safe selected fetches, and no credential/secret selection. They do not
create a new parser, Journal writer, or read-only-to-mutation conversion.

The shared service owns execution, cancellation, terminal state, durable event identity, and retry semantics. MCP preserves its outcome rather than translating a deferred, handoff-required, recording-blocked, failed, canceled, partial-effect, unknown-effect, or no-op result into success. A no-op has no invented mutation; a handoff includes the actual continuation/reference and no claimed local dispatch; an unstarted call has no invented Action Run. A terminal Action/Workflow result with pending recording exposes the actual result plus `recording_blocker` and pending event ref, not a clean completion.

Observation results disclose only references and redacted safe material authorized by the selected Run; they never fabricate output/results, reveal secrets, or treat an outbox/intake acknowledgement as an effect or Journal receipt. The adapter reports the source currentness observed for the operation and the exact Run/Event/Journal/report references returned by shared support. It is a projection boundary, not an authority to alter source, Artifact, or Journal history.

### Sources

- CA-A-1142 v2, unchanged original-thirteen registry; CA-P-1532 v2 and CA-P-1535 v2, exact query admission frontiers.
- CA-D-527 v3; CA-D-521 v3; CA-R-1720 v17; CA-R-1525 v6; CA-R-1728 v16; CA-D-523 v2; CA-R-1850 v2; CA-R-1866 v2; CA-R-1867 v1.
