---
atom_id: CA-D-001
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - "Project/technical realization"
  depends_on:
    continuant:
      - "Project"
      - "Atom/Content Role: Method"
version: 13
updated_at: 2026-09-05 01:15:08 +0400
relations:
  child_of:
    - CA-INTENT
---
# Provide replaceable technical realizations

CAPRMEDIO **must** make **every** technical realization replaceable within that realization's declared operating prerequisite envelope by providing **`>=1`** replacement Method available within that envelope **and** capable of producing **or** selecting a replacement that satisfies **all** of these conditions:

1. the replacement is distinct from the original realization.
2. the replacement operates within the original realization's declared operating prerequisite envelope.
3. the replacement is admissible for the original realization.
4. the replacement preserves the original realization's governed specification.
5. the replacement has acceptance conditions equivalent to those of the original realization.
6. the original **and** replacement acceptance conditions are observable within the original realization's declared operating prerequisite envelope.

a concrete replacement **may** be absent **when** replaceability is evaluated; the available Method **must** be capable of producing **or** selecting a replacement meeting **all** these conditions **when** required.
