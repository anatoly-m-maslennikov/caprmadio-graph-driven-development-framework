---
atom_id: CA-R-155
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - Atom/Local Tier
  depends_on:
    continuant:
      - Atom
      - "Atom/Content Role: Requirement/Type: Goal"
version: 22
updated_at: 2026-09-04 23:37:00 +0400
relations:
  child_of:
    - CA-R-680
---
# Give Every Non-Project-Goal Atom One Local Tier

**every** Atom other than a Project Goal Atom **must** have **`=1`** Local Tier **in** (Principle, Core, Standard).
