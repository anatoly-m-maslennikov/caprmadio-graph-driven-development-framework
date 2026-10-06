---
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Requirement/Type: Demand/Producer Result"
  depends_on:
    continuant:
      - Consumer/Goal
      - Producer/Result
atom_id: CA-R-933
cce_version: cce_1
cce_form: obligation
version: 9
updated_at: 2026-09-02 03:30:00 +0400
relations:
  child_of:
    - CA-R-932
---
# Restrict Demand to one depended-on result

**every** Demand Atom **must** constrain **`=1`** Producer result on which its Consumer's accepted Goal depends.
