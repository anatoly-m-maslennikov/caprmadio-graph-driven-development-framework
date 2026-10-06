---
atom_id: CA-E-382
cce_version: cce_1
cce_form: evaluation
subjects:
  governs:
    occurrent:
      - Term-System Graph Evaluation
  depends_on:
    continuant:
      - Term System
      - Term
      - Property
      - IS_ALLOWED_VALUE_OF
      - SUBKIND_OF
version: 8
updated_at: "2026-09-11 04:18:03 +0400"
relations:
  evaluation_for:
    - CA-R-1242
    - CA-R-1246
    - CA-R-1345
    - CA-R-1346
    - CA-R-1436
---
# Reject Invalid Term-System Graphs

the Evaluation **must** reject a Term-System Graph **if** it admits another primitive Relation Kind, admits a value **without** governing authority for its qualified Property context, **contains** a SUBKIND_OF cycle, **or** uses a Term-System Relation outside its registered graph.

the Evaluation **must not** reject the reuse of one Term as an allowed value **in** multiple qualified Property contexts **when** the value is separately admitted **in** **every** such context. an admission that is valid **in** one context **must not** justify admission **in** another context **without** its applicable authority.
