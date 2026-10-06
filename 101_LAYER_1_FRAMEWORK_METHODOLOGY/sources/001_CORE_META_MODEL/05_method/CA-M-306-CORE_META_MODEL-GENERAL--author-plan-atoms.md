---
subjects:
  governs: "Atom/Content Role: Plan/Type: Plan"
  depends_on:
    - "Atom/Content Role: Plan/Type: Plan"
    - "Atom/Claim"
    - "Atom/Summary"
    - "Atom/Author"
    - "Atom/Content Role: Plan/Type: Plan/Assignee"
    - "Atom/Content Role: Plan/Type: Plan/Label"
    - "Atom/Content Role: Plan/Type: Plan/Subtype"
    - "Atom/Content Role: Plan/Type: Plan/Definition of Done"
    - "Atom/Content Role: Plan/Type: Plan/Decomposition"
    - "Atom/Content Role: Plan/Type: Plan/Blocking"
    - "Autonomous Confidence Threshold"
    - "Implementation Retry Limit"
    - "Scope Unit"
    - "File Carrier"
version: 7
updated_at: "2026-10-02 20:35:16 +0400"
relations: {"relates_to": ["CA-R-1574", "CA-R-1575", "CA-R-1576", "CA-R-1577", "CA-R-1599", "CA-R-1584", "CA-R-1588", "CA-R-1589", "CA-R-1591", "CA-R-1418", "CA-M-123", "CA-M-271", "CA-M-295", "CA-D-470", "CA-D-471", "CA-D-481"]}
atom_id: "CA-M-306"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "General"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 10
---
# Summary

Author Plan Atoms

## Scope

Plan Atoms.

## Claim

**to** author a Plan Atom, apply the common Plan authoring rules independently of Label:

1. resolve **`=1`** effective Author.
2. state **`=1`** intended work **or** outcome **in** Objective, supported by own work, direct decomposition, **or** both under CA-R-1575.
3. resolve its Claim Target Scope Unit under CA-R-1588; keep narrower **or** composite work restrictions **in** Objective, **and** do **not** target an ancestor Scope Unit.
4. **if** it has own work, resolve **`=1`** effective Assignee **and** assign that work **to** that Assignee. retain the leaf-work bound under CA-R-1589.
5. write **`=1`** Definition of Done under CA-M-123, carried inside Details under CA-D-470; include decomposed completion obligations **when** applicable.
6. use a Label **only** for navigation; apply an authoring Subtype **only when** explicitly governed.
7. express required start dependencies with `BLOCKS`; declare `IS_DECOMPOSITION_OF` **only** on the decomposing Plan under CA-D-481. derive the inverse; do **not** infer execution dependencies from leading numbers **or** folder placement.
8. resolve confidence **and** retry values from their applicable sources; store **only** explicitly selected overrides on this Plan.
9. keep supporting Details within Objective **and** its restrictions **without** another intended outcome. review Objective against the completed Details **and** Definition of Done; explicitly revise Objective **if** needed **and** recheck their agreement.
10. **only after** that review, derive Summary from the finalized Objective under CA-R-1418 **and** CA-R-1465. retain the established Summary across Revisions; **if** it needs changing, replace the Atom identity under CA-R-1464.

## Details
