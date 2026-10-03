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
version: 3
updated_at: 2026-08-29 02:40:41 +0400
relations: {}
---
# Reject Invalid Term-System Graphs

the Evaluation **must** reject a Term-System Graph **if** it admits another primitive Relation Kind, **contains** a SUBTYPE_OF cycle, ignores a compatible inherited invariant, accepts conflicting inherited invariants, **or** uses a Term-System Relation outside its registered graph.
