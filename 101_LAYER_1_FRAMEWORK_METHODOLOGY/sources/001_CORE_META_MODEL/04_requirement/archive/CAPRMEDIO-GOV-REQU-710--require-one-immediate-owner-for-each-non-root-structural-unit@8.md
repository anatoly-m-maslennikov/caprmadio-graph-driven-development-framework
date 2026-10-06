---
subjects:
  governs:
    continuant:
      - scope-topology
  depends_on:
    continuant:
      - authority
cce_version: cce_1
cce_form: cardinality
version: 8
updated_at: 2026-08-29 02:40:41 +0400
relations:
  child_of:
    - CAPRMEDIO-META-REQU-706
---
# Require one parent Scope Unit

**every** Scope Unit except a Scope Unit root **must** have **`=1`** direct parent Scope Unit.
