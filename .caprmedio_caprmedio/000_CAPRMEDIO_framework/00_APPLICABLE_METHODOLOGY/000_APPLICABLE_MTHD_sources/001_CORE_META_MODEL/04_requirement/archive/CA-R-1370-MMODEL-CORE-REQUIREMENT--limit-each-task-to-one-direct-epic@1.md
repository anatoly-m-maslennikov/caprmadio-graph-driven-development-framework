---
atom_id: CA-R-1370
cce_version: cce_1
cce_form: cardinality
subjects:
  governs:
    continuant:
      - "Atom/Content Role: Plan/Type: Task/Epic Membership"
  depends_on:
    continuant:
      - Epic/Direct Membership
version: 1
updated_at: 2026-09-03 00:06:31 +0400
relations:
  replacement_of:
    - CAPRMEDIO-META-REQU-140
---
# Limit Each Task to One Direct Epic

**every** Atom with Content Role Plan **and** Type Task **must** be a direct member of **`<=1`** Epic.
