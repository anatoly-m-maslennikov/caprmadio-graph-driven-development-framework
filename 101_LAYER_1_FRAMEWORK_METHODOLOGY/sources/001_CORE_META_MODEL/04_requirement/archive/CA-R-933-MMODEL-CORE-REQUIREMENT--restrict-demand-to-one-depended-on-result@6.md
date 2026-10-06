---
subjects:
  governs:
    continuant:
      - Demand/Producer Result
  depends_on:
    continuant:
      - Consumer/Job
      - Producer/Result
atom_id: CA-R-933
cce_version: cce_1
cce_form: obligation
version: 6
updated_at: 2026-08-29 01:16:37 +0400
relations:
  child_of:
    - CA-R-932
---
# Restrict Demand to one depended-on result

**every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Job depends.
