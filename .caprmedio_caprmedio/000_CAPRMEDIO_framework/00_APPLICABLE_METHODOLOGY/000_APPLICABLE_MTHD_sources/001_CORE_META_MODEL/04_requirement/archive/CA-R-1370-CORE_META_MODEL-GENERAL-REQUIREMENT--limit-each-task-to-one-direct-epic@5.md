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
version: 5
updated_at: "2026-09-10 03:38:57 +0400"
relations: {}
---
# Limit Each Task to One Direct Epic

**every** Atom with Content Role Plan **and** Type Task **must** be a direct member of **`<=1`** Epic.
