---
atom_id: CA-M-127
cce_version: cce_1
cce_form: method
subjects:
  governs:
    occurrent:
      - Set-valued Property Membership Evaluation
  depends_on:
    continuant:
      - CCE Condition Expression Evaluation
      - Set-valued Property
version: 7
updated_at: 2026-09-04 23:11:19 +0400
relations:
  child_of:
    - CA-M-122
---
# Evaluate Set-valued Property Membership

**to** evaluate **in** **or** **not in** for one set-valued governed property, the Resolver **must** evaluate **in** as true exactly **when** **`>=1`** property member **`=`** one listed value **and** **must** evaluate **not in** as true exactly **when** no property member **`=`** **any** listed value.
