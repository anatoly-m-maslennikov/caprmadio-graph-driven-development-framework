---
atom_id: CA-R-1834
content_role: Requirement
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
status: Active
author: Anatoly Maslennikov
version: 1
updated_at: "2026-10-04 18:30:17 +0000"
subjects:
  governs: "Tool/WORKFLOW_OPERATIONS/REVERT_CHANGES"
  depends_on: [Tool, Workflow, Action, Operator, Artifact, Journal, Workflow Run, Step Run]
relations:
  relates_to: [CA-R-1833, CA-O-130, CA-O-131, CA-O-132, CA-R-1525, CA-R-1720]
---
# Summary

Execute one admitted approved change reversal

## Scope

The REVERT_CHANGES Tool's guarded execution and exact effect-account boundary for an admitted CA-R-1833 manifest.

## Claim

REVERT_CHANGES **must** revalidate current target, hash, affected-reference, authority, and permission bindings before each admitted effect; it **must** preserve history/provenance and report exact observed effects without automatic inverse or replay.

## Details

Before dispatch and on recovery, revalidate the manifest's exact bindings. A changed or unresolved binding blocks further effects and names the completed, failed, unattempted, and uncertain effects. Current complete satisfaction of the exact result plus required history/reference conditions returns `no_op` with zero applied effects. Otherwise apply only the ordered approved effects through governed capabilities, preserving before/after/result evidence, prior Revisions, archives, accepted Events, referenced identities, and the exact safe boundary.

The output is `{ outcome, manifest_id, selection_and_currentness_bindings, expected_result, observed_result, effect_account, history_reference_disposition, evidence_refs, run_receipt_refs }`. `effect_account` contains each ordered effect as `completed`, `failed`, `unattempted`, or `uncertain`; `applied_effect_count` is established completed effects only. The only successful outcomes are `reverted` and `no_op`. `failed` requires confirmed zero applied effects and zero uncertain completion. Any established applied effect **or any uncertain completion**, including with zero confirmed applied effects, is `partial_failure`. Revalidation/approval/currentness/permission/capability/reference failure before a further effect is `blocked`; admitted cancellation is `canceled`; unconfirmed required recording is `recording_blocked` with known effects and pending-recording evidence.

The Tool uses the accepted shared CA-P-1443/CA-P-1451 J01–J08 Run/Journal contract rather than redefining its schema: confirmed start precedes target effects; actual Workflow/Step/Action lineage and exact revisions are referenced; identical pending-recording retry reconciles the same event identity/payload and never replays an effect; conflicting retry is rejected. A returned receipt reference is not a claim that the Tool independently owns Journal serialization. No outcome authorizes an automatic inverse, blind retry, substitute source Revision, or broader repair.

### Sources

- CA-O-131 v2, clauses 2–5, outcomes, and durable handoff; CA-O-130 v1 terminal routing; CA-O-132 v1 returned-effect handoff.
- CA-P-1463 v1, exact accepted `failed`/`partial_failure` correction; CA-P-1451 J01–J08 shared contract.
