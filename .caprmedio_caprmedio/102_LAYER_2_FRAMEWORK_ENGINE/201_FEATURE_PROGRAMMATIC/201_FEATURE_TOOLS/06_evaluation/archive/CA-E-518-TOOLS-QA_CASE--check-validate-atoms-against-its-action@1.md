---
atom_id: CA-E-518
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
    - "Action"
    - "Check Atoms"
    - "Evaluation"
    - "Scope Unit"
    - "Global Tier"
    - "Local Tier"
version: 1
updated_at: "2026-09-23 23:53:58 +0000"
relations:
  evaluation_for:
    - CA-R-1622
    - CA-M-316
    - CA-D-492
  relates_to:
    - CA-O-087
    - CA-E-513
---
# Summary

Check VALIDATE_ATOMS against its Action

## Claim

the `VALIDATE_ATOMS` implementation check **must** reject divergence from its bound Check Atoms Action.

- exercise **every** declared result, including empty selection, unresolved selection, partial assessment, complete assessment with failures, changed inputs, **and** execution failure; compare the output with the exact Action Revision, **not** a second operational definition.
- verify Scope Unit-only selection **and** selection with descendants; declared parentage, **not** physical folder nesting, determines descendants. Atom ownership comes from carried Properties.
- verify Global Tier filters, Local Tier filters, their intersection, **and** explicit Atom lists, including exact Revisions, unassigned Drafts, missing entries, **and** ambiguous identities. listed values are alternatives; supplied criteria intersect.
- remove required selector Properties **or** change declared parentage while keeping paths unchanged: require explicit unresolved membership **or** the newly correct set, never path-derived values. request an out-of-bound Atom: require a safe unresolved result, **not** a read outside the boundary.
- changing an Action **or** rule definition **must** trigger compatibility validation **or** an unsupported-definition result, **not** silent old behavior.
- require equivalent direct Action results **and** results returned through the Workflow's invocation Step. no Workflow engine, repair branch, **or** retry policy **may** be required inside the Tool.
- definition validation remains **in** methodology; this Evaluation checks the Tool realization.
