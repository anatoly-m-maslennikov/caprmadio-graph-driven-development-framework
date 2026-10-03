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
version: 6
updated_at: 2026-09-06 01:45:12 +0400
relations: {}
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-382-CORE_META_MODEL-CORE-EVALUATION--reject-invalid-term-system-graphs.md
---
# Reject Invalid Term-System Graphs

the Evaluation **must** reject a Term-System Graph **if** it admits another primitive Relation Kind, gives one Term **`>1`** direct IS_ALLOWED_VALUE_OF parents, **contains** a SUBKIND_OF cycle, **or** uses a Term-System Relation outside its registered graph.
