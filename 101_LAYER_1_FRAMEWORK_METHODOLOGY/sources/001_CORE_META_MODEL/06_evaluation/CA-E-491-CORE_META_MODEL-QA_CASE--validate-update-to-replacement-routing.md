---
subjects:
  governs: "Workflow"
  depends_on:
    - "Action"
    - "Step"
    - "Assess Atom Update Identity"
    - "Atom"
    - "Atom/Summary"
    - "Artifact/Revision"
    - "Atom Change Classification"
    - "Workflow Run"
    - "Operator"
version: 5
updated_at: "2026-10-02 20:16:06 +0400"
relations: {"evaluation_for": ["CA-O-067", "CA-M-303", "CA-R-1432", "CA-R-1464", "CA-R-1520"]}
atom_id: "CA-E-491"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "QA Case"
global_tier: 11
---
# Summary

Validate update-to-replacement routing

## Scope

an update Workflow's routing of CA-O-067 assessment results.

## Claim

the Evaluation **must** check that an update Workflow owns the routing of CA-O-067 assessment results under CA-M-303.

## Details

- call the assessment Action **without** a continuation binding: require a read-only classification result, **not** a selected next Step, ended Workflow Run, **or** dispatched successor.
- supply a valid identity-preserving proposal: the caller follows its declared update path **and** remaining checks rather than treating assessment as completed persistence.
- change the proposed Summary: require a replacement-required assessment **and** the caller's terminal handoff under CA-R-1520; no intermediate update is persisted.
- change a previously assessed proposal **or** its evidence **before** persistence: require reassessment **and** routing using the new result.
- leave the assessment unresolved: require the caller's declared evidence **or** escalation path rather than presumed approval.
- omit the caller's continuation binding **or** performed-effect account needed for handoff: block continuation **without** making the assessment Action invent either value.
- the ending update Run does **not** call, wait for, **or** claim completion of replacement; the executor receives the caller's complete terminal result.

check the declared graph with read-only Action fixtures. this Evaluation does **not** require execution of the replacement effect.
