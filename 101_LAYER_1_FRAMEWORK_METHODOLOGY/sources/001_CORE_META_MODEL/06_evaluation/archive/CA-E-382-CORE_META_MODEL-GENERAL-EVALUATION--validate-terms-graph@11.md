---
atom_id: CA-E-382
cce_version: cce_1
cce_form: evaluation
subjects:
  governs: "Terms Graph/validation"
  depends_on:
    - "Terms Graph"
    - "Term"
    - "Root Term"
    - "NARROWER_THAN"
    - "Relation"
    - "Relation Kind"
    - "CAPRMEDIO Graph"
    - "Governed Term"
    - "Definition Atom"
    - "Atom/Claim"
    - "Artifact/Revision"
    - "Entity"
    - "Action"
    - "Process"
version: 11
updated_at: "2026-09-13 03:24:04 +0400"
relations:
  evaluation_for:
    - CA-R-1335
    - CA-R-1246
    - CA-R-1435
    - CA-R-1244
    - CA-R-1345
    - CA-R-1347
    - CA-R-1319
    - CA-R-1454
    - CA-R-1437
---
# Validate Terms Graph

the Evaluation **must** reject a Terms Graph **if** **any** of:

- a node is **not** a Term under its governing authority.
- a Relation Kind is unregistered **or** belongs **to** another graph kind under CA-R-1246.
- a NARROWER_THAN Relation lacks an explicit authoritative source declaration **or** its governing Term definitions do **not** establish the implication under CA-R-1435. absence of Entity instances does **not** establish this implication.
- the NARROWER_THAN hierarchy **contains** a directed cycle, including a self-loop.
- a Root Term classification differs from the **`=0`** direct NARROWER_THAN-parent criterion under CA-R-1347.

the Evaluation **must** accept an acyclic hierarchy with multiple direct parents **or** an isolated Root Term **when** the remaining applicable authority is satisfied. Relations from another graph kind **must not** change Root Term classification **when** the Terms Graph hierarchy is unchanged. the checks **must** distinguish an unregistered Relation Kind from a separately admitted graph-specific expansion.

for a governed-only view under CA-R-1454, the Evaluation **must** reject the view **if** an eligible Term **or** Relation required by CA-R-1454 is omitted, an ineligible node **or** edge is displayed, a displayed node's Definition Atom **or** a displayed edge's source declaration is outside the requested source selection, a displayed node lacks **`=1`** active defining authority under CA-R-1319, a displayed node **or** edge lacks exact source Claim **and** Artifact Revision traceability, **or** an edge is inferred **only** from spelling, capitalization, shared Subject use, **or** compatible endpoints. missing **or** conflicting definitions **and** uncertain Relation admission **must** be reported with their affected source references **without** inventing a definition **or** an edge.

filtering out a parent **must not** establish **or** change canonical Root Term classification. **if** the available source evidence is insufficient **to** establish the CA-R-1347 criterion, the classification **must** remain unresolved **without** silently importing source nodes **or** edges from outside the requested selection.

the same NARROWER_THAN implication check applies **when** the Terms name Actions **or** Processes; the Evaluation **must not** require **or** create Entity duplicates **to** admit operational vocabulary. an empty set of observed instances does **not** prove a hierarchy Relation; acceptance requires the governing Term definitions **and** explicit Relation authority.
