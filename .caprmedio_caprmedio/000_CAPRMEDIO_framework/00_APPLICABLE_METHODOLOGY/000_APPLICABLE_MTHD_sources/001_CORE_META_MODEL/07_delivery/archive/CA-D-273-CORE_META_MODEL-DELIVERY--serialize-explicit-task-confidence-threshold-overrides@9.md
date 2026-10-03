---
cce_version: cce_1
cce_form: serialization
subjects:
  governs: "Autonomous Confidence Threshold/Carrier"
  depends_on:
    - "Autonomous Confidence Threshold"
    - "Atom/Content Role: Plan/Type: Task"
    - "Atom/Content Role: Plan/Type: Objective"
    - "Atom Collection/Type: Epic"
    - "Markdown Atom Carrier"
    - "Property"
version: 9
updated_at: "2026-09-16 14:01:24 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to:
    - CA-R-1428
    - CA-R-1365
    - CA-R-1367
    - CA-D-351
---
# Serialize explicit Task confidence-threshold overrides

an explicitly selected Autonomous Confidence Threshold **must** be serialized **only** **at** its owning override source:

- a Task override uses the integer frontmatter field `autonomous_confidence_threshold` **in** that Task's Markdown Atom Carrier.
- an Epic override uses the integer frontmatter field `epic_overrides.autonomous_confidence_threshold` **in** the active Objective Atom that targets that Epic.

## inheritance and ownership

- the Objective field belongs **to** its target Epic, **not** **to** the Objective's current Scope Unit **or** the folder that **contains** the Objective Carrier.
- omit an unselected field; omit `epic_overrides` **if** it has no explicit fields. do **not** serialize inherited values as explicit overrides.
- an Epic **without** an active Objective Atom has no stored Epic override. do **not** create an Objective **or** another settings file merely **to** materialize an inherited value.
- the Objective remains outside its target Epic under CA-D-351; its body retains **=1** intended outcome under CA-R-1365.
