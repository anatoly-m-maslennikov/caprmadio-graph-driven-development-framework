---
atom_id: CA-D-350
cce_version: cce_1
cce_form: grammar
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Type: Objective/Carrier/Filename"
  depends_on:
    continuant:
      - Atom/Current Scope/Owner
      - Atom/Summary
      - Epic/Identity
version: 1
updated_at: 2026-09-02 03:30:00 +0400
relations: {}
---
# Serialize Objective Filenames

**every** Objective Atom filename **must** match `<PLAN_ATOM_ID>-<CURRENT_SCOPE_OWNER>-OBJECTIVE_FOR-<EPIC_ID>--<SUMMARY>.md`.
