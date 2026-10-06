---
atom_id: CA-O-083
content_role: Operations
type: Action
current_scope_unit: CORE_META_MODEL
claim_target_scope_unit: CORE_META_MODEL
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Finalize Atom Carrier Validation"
  depends_on:
    - "Action"
    - "Action/Execution Kind"
    - "Atom"
    - "Artifact/Revision"
    - "Evaluation"
    - "Workflow Run"
version: 1
updated_at: "2026-09-23 23:38:45 +0000"
relations:
  relates_to:
    - CA-O-081
    - CA-O-082
    - CA-R-1525
---
# Summary

Finalize Atom Carrier validation

## Claim

Finalize Atom Carrier Validation **means** the Programmatic Action that returns the final validation assessment bound **to** the inputs actually checked.

- input: the prepared source fingerprints, selection evidence, check bindings, assessment coverage, findings, **and** execution diagnostics.
- recheck target-set membership **and** fingerprints of targets, methodology, reference context, **and** relevant configuration. changed, added, removed, **or** unreadable inputs make the result incomplete; do **not** silently check another Revision **or** restart the Run.
- return valid **only** for a nonempty, completely assessed target set with no failed applicable check **and** unchanged inputs.
- return invalid for complete, unchanged input coverage containing **>=1** failed applicable check.
- return incomplete **when** coverage, authority, prerequisites, **or** currentness cannot be established, even **if** some failures are already known; retain those failures.
- return error for an execution failure that prevents finalization; retain the available partial assessment.
- return selected/excluded/not-assessed counts, per-Carrier outcomes, rule coverage, source bindings, findings, **and** final currentness result sufficient **to** distinguish these outcomes.

returning the assessment does **not** publish a new authoritative Atom, approve a correction, modify a source, **or** certify semantic review. record Run evidence through the applicable executor/Journal mechanism, **not** by treating the returned report as source authority.
