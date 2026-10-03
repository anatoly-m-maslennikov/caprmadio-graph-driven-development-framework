---
atom_id: CA-R-1461
cce_version: cce_1
cce_form: definition
subjects:
  governs: "Projection/Type: Reconciled Projection"
  depends_on:
    - "Projection"
    - "Type"
    - "Artifact/Revision"
    - "Atom/Claim"
    - "Carrier"
    - "Operator"
version: 1
updated_at: "2026-09-13 22:36:08 +0400"
relations: {}
---
# Define Reconciled Projection

Reconciled Projection **means** the Type value under Projection whose instances preserve selected source content, canonical identities, **and** exact final selected Revisions **without** synthesis **or** merge, **and** have no unresolved source conflict under the applicable declared checks.

source selection **and** conflict resolution remain governed by applicable source authority. **any** needed source correction **must** be separately authorized by the Operator **and** applied upstream **to** that authority, **not** by editing the projected content **or** treating projection production as authorization **to** change a source. a result **must not** be published as a Reconciled Projection **until** its final selected source Revisions have been re-evaluated **after** **any** such correction **and** no conflict remains unresolved under those checks. this classification does **not** grant the result independent source authority **or** determine its Carrier materialization strategy.
