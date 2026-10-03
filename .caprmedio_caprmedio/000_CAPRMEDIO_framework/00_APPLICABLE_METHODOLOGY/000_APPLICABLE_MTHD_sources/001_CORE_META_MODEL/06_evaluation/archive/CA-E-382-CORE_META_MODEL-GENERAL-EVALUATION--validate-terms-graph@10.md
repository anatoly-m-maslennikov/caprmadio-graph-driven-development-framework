---
atom_id: CA-E-382
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Terms Graph/validation
  depends_on:
    continuant:
      - "Terms Graph"
      - "Term"
      - "Root Term"
      - "NARROWER_THAN"
      - "Relation Kind"
      - "CAPRMEDIO Graph"
version: 10
updated_at: "2026-09-11 05:44:27 +0400"
relations:
  evaluation_for:
    - CA-R-1335
    - CA-R-1246
    - CA-R-1435
    - CA-R-1244
    - CA-R-1345
    - CA-R-1347
---
# Validate Terms Graph

the Evaluation **must** reject a Terms Graph **if** **any** of:

- a node is **not** a Term under its governing authority.
- a Relation Kind is unregistered **or** belongs **to** another graph kind under CA-R-1246.
- a NARROWER_THAN Relation does **not** connect a narrower Term **to** a broader Term under CA-R-1435.
- the NARROWER_THAN hierarchy **contains** a directed cycle, including a self-loop.
- a Root Term classification differs from the **`=0`** direct NARROWER_THAN-parent criterion under CA-R-1347.

the Evaluation **must** accept an acyclic hierarchy with multiple direct parents **or** an isolated Root Term **when** the remaining applicable authority is satisfied. Relations from another graph kind **must not** change Root Term classification **when** the Terms Graph hierarchy is unchanged. the checks **must** distinguish an unregistered Relation Kind from a separately admitted graph-specific expansion.
