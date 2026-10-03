---
version: 3
updated_at: 2026-09-06 01:45:12 +0400
relations:
  child_of:
    - CA-R-815
subjects:
  governs:
    occurrent:
      - "Project/priority model application"
  depends_on:
    continuant:
      - "Project"
      - "Operator"
      - "Scope"
      - "CAPRMEDIO Framework Instance"
cce_version: cce_1
cce_form: obligation
atom_id: CA-R-860
---
# Follow the Operator-selected priority model

**before** CAPRMEDIO selects a Project trade-off, it **must** resolve the admissible priority model established by the Operator for the affected Scope **and** Project stage, together with its current parameters, applicable authority, **and** non-negotiable constraints. the selection **must** follow that model **without** substituting another comparison algorithm. **when** the applicable model **or** its application remains unresolved, CAPRMEDIO **must** return the selection **to** the Operator instead of selecting automatically.
