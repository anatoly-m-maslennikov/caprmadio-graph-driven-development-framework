---
atom_id: CA-R-1440
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Framework Instance Settings/interaction/reporting mode/mandatory information"
  depends_on:
    - "Framework Instance Settings/interaction/reporting mode"
    - "Operator"
version: 2
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  child_of:
    - "CA-R-1402"
  relates_to:
    - "CA-R-1420"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Preserve mandatory information in every reporting mode

**every** interaction reporting mode **must** report the following mandatory information:

- blockers **and** failed operations;
- ambiguity that requires Operator input;
- permission **or** approval requests;
- safety-critical information;
- material deviations from the requested outcome.
