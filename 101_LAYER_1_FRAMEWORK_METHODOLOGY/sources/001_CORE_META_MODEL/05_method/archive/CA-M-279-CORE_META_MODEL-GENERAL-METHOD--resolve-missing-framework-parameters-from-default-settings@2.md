---
atom_id: CA-M-279
cce_version: cce_1
cce_form: method
subjects:
  governs: "Framework Instance Settings/parameter resolution"
  depends_on:
    - "Framework Instance Settings"
    - "Default Settings"
    - "Project"
    - "Operator"
version: 2
updated_at: "2026-09-16 23:48:40 +0000"
relations:
  relates_to:
    - "CA-R-1402"
    - "CA-R-1441"
    - "CAPRMEDIO-META-REQU-675"
    - "CA-D-407"
    - "CA-D-408"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Resolve missing framework parameters from Default Settings

**to** resolve a Framework Instance Settings parameter, use its explicit value **if** that parameter is present **in** the current Project's Framework Instance Settings; **otherwise**, use the corresponding value from Default Settings. determine presence for the individual parameter, **not** its containing section **or** the truthiness of its value, so valid `false`, `0`, **and** empty values remain explicit selections. validate the selected value against its governing parameter authority **and** reject an invalid explicit value **without** falling back. **if** neither source supplies a required parameter, report that parameter as unresolved **and** stop the operation that requires it; an optional parameter **may** remain absent. do **not** copy inherited values into Framework Instance Settings as explicit selections.
