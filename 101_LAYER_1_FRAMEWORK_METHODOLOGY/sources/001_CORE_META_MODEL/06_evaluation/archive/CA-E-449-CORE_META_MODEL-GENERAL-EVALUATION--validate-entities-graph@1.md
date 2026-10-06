---
atom_id: CA-E-449
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Entities Graph/validation
  depends_on:
    continuant:
      - "Entities Graph"
      - "Entity"
      - "Dependent Entity"
      - "Primary Entity"
      - "Property"
      - "Term"
      - "IS_BORNE_BY"
      - "IS_ALLOWED_VALUE_OF"
      - "BEARS"
      - "Relation Kind"
version: 1
updated_at: "2026-09-11 05:44:27 +0400"
relations:
  evaluation_for:
    - CA-R-1438
    - CA-R-1246
    - CA-R-1260
    - CA-R-1192
    - CA-R-1351
    - CA-R-1436
    - CA-R-1346
    - CA-R-1243
---
# Validate Entities Graph

the Evaluation **must** reject an Entities Graph **if** **any** of:

- a node is **not** an Entity under its governing authority.
- a Relation Kind is unregistered **or** belongs **to** another graph kind under CA-R-1246.
- an IS_BORNE_BY Relation has an invalid endpoint **or** direction under CA-R-1260, **or** violates the applicable immediate-bearer cardinality under CA-R-1192 **or** CA-R-1351.
- an IS_ALLOWED_VALUE_OF Relation admits a value **without** governing authority for its qualified Property context under CA-R-1436.
- admission **in** one Property context is used **to** justify admission **in** another context **without** its applicable authority.
- allowed-value admission is treated as assigning a value **to** a particular Property occurrence **or** determining that Property's cardinality.
- BEARS is independently authored as another primitive Relation Kind instead of being derived from IS_BORNE_BY under CA-R-1243.

the Evaluation **must not** reject the reuse of one Term as an allowed-value name **in** multiple qualified Property contexts **when** the value is separately admitted **in** **every** such context. the checks **must** cover valid **and** invalid bearer endpoints, applicable bearer cardinalities, independent value admission across Property contexts, derived inverse navigation, **and** a Relation Kind imported from another graph kind.
