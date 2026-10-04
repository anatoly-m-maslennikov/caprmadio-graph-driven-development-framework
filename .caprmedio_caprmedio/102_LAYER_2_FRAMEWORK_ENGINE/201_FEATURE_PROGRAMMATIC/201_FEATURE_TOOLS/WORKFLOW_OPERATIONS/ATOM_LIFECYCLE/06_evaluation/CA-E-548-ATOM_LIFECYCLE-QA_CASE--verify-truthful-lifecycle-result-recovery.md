---
atom_id: CA-E-548
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
global_tier: 11
author: Anatoly Maslennikov
status: Active
subjects:
  governs: "Workflow Operations/Atom Lifecycle/Result Recovery"
  depends_on: ["Atom", "Atom/Revision", "Artifact/Carrier", "Journal/Record"]
version: 2
updated_at: "2026-10-04 23:01:23 +0400"
relations:
  evaluation_for: [CA-R-1826, CA-R-1828]
---
# Summary

Verify truthful lifecycle result recovery

## Scope

Golden shared-run outcomes for authorized Create, no-effect admission failures, accepted changes, and partial/unverified effect.

## Claim

Run an actual authorized Create golden E2E through CA-D-527's one shared outer request/result: prove the one complete new target Carrier set and absence/identity admission, then verify the actual native effect, observed Version and Updated At, started Run/definition bindings, and canonical receipt. Run duplicate-identity, stale expected Version/digest, and multi-target/predecessor variants; each must stop before effect with no fabricated Carrier change, Run, Event, receipt, retry, or history. Verify exact shared-result and lifecycle-payload fields for an actual no-op, a successful semantic Update, a model-admitted Change Status transition, and a separately admitted Replace. For an authorized Archive that newly breaks Relations, verify the status transition proceeds, reports every newly broken Relation and active referrer, provides only a separate repair handoff, and performs no automatic repair. Inject failure after a known effect but before final verification and after result-carrier persistence. Verify known effects, unknown remainder, prior history, model/currentness context, canonical receipt or `recording_pending`, and retry disposition are reported without a success claim.

## Details

### Acceptance criteria

Observed Version and actual Updated At values match native outcomes; no-op, preview, duplicate, stale, and multi-target/predecessor variants make no fictitious changes; incomplete recovery remains incomplete in the shared result.
