---
atom_id: CA-E-514
content_role: Evaluation
type: QA Case
current_scope_unit: TOOLS
claim_target_scope_unit: TOOLS
local_tier: Standard
author: Anatoly Maslennikov
status: Active
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Tool/VALIDATE_ATOMS"
  depends_on:
    - "Tool"
    - "Workflow"
    - "Step Run"
    - "Evaluation"
    - "Atom Carrier Validation"
version: 1
updated_at: "2026-09-23 23:38:45 +0000"
relations:
  evaluation_for:
    - CA-M-316
    - CA-R-1622
  relates_to:
    - CA-E-513
    - CA-O-080
---
# Summary

Check VALIDATE_ATOMS against its Workflow

## Claim

the `VALIDATE_ATOMS` implementation check **must** reject divergence from the exact referenced Workflow **and** Step/Action definitions.

- exercise **every** declared result branch, including incomplete preparation, partial assessment, invalid complete assessment, stale finalization, unexpected result, **and** execution failure.
- compare entry, Action bindings, transitions, returned result tags, **and** terminal outcomes against the O graph; do **not** maintain a second expected Workflow as test authority.
- require exact definition Revision evidence. changing a referenced definition **must** trigger compatibility validation **or** an unsupported-definition result, **not** silent use of old behavior.
- confirm no repair **or** retry branch exists beyond the admitted graph. delegate definition-validity assessment **to** methodology Evaluation CA-E-513; this Evaluation checks **only** its Tool realization.
