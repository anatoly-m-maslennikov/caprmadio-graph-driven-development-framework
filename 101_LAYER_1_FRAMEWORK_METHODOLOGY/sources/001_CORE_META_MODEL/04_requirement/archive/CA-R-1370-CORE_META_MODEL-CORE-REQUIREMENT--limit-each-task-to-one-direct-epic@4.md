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
      - "Atom Collection/Type: Epic/Direct Membership"
version: 4
updated_at: 2026-09-07 09:59:57 +0000
relations: {}
---
# Limit Each Task to One Direct Epic

**every** Atom with Content Role Plan **and** Type Task **must** be a direct member of **`<=1`** Epic.
