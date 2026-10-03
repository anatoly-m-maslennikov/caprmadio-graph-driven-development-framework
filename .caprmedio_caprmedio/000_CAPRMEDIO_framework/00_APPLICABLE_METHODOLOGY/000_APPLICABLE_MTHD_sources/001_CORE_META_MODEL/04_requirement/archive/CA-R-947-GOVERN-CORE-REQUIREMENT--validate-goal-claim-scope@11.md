---
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Requirement/Type: Goal/Claim Scope"
  depends_on:
    continuant:
      - Atom/Current Scope/Owner
      - Atom/Claim Scope/Scope Unit Set
      - Scope Unit/Parent
      - Project
atom_id: CA-R-947
cce_version: cce_1
cce_form: obligation
version: 11
updated_at: 2026-09-02 03:30:00 +0400
relations:
  child_of:
    - CA-R-925
    - CA-R-926
    - CA-R-927
---
# Validate Goal Claim Scope

a Goal Atom Claim Scope Unit Set **must** **contain** **`=1`** Scope Unit that is the direct child of its Current Scope Owner Scope Unit **or** the Project Scope Unit **if** its Current Scope Owner **contains** no Scope Unit.
