---
atom_id: CA-R-1440
cce_version: cce_1
cce_form: obligation
subjects:
  governs:
    continuant:
      - "Framework Instance Settings/interaction/reporting mode/mandatory information"
  depends_on:
    continuant:
      - "Framework Instance Settings/interaction/reporting mode"
      - "Operator"
version: 1
updated_at: "2026-09-11 18:18:55 +0400"
relations:
  child_of:
    - "CA-R-1402"
  relates_to:
    - "CA-R-1420"
---
# Preserve mandatory information in every reporting mode

**every** interaction reporting mode **must** report the following mandatory information:

- blockers **and** failed operations;
- ambiguity that requires Operator input;
- permission **or** approval requests;
- safety-critical information;
- material deviations from the requested outcome.
