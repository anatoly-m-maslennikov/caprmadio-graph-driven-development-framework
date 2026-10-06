---
cce_version: cce_1
cce_form: method
subjects:
  governs: "Set-valued Property Membership Evaluation"
  depends_on:
    - "CCE Condition Expression Evaluation"
    - "Set-valued Property"
version: 12
updated_at: "2026-09-10 03:25:26 +0400"
relations:
  child_of:
    - CA-M-122
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Evaluate Set-valued Property Membership

**to** evaluate **in** **or** **not in** for one set-valued governed property, the Resolver **must** evaluate **in** as true exactly **when** **`>=1`** property member **`=`** one listed value **and** **must** evaluate **not in** as true exactly **when** no property member **`=`** **any** listed value.
