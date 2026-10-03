---
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Requirement/Requirement Type: Demand/Admission"
  depends_on:
    continuant:
      - Consumer/Job
      - Producer/Result
atom_id: CA-R-951
cce_version: cce_1
cce_form: obligation
version: 7
updated_at: 2026-08-29 02:40:41 +0400
relations:
  child_of:
    - CA-R-933
---
# Require an exact dependency before a Demand

a Consumer Scope Unit **must** own a Demand Atom **only** **when** its accepted Job authorizes an exact dependency on the demanded Producer result.
