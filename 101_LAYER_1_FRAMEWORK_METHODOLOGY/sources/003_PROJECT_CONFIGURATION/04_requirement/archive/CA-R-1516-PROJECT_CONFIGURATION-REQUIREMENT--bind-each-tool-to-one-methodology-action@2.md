---
cce_version: cce_1
cce_form: obligation
subjects:
  governs: "Tool"
  depends_on:
    - "Action"
    - "Workflow"
    - "Step"
    - "Methodology"
    - "Atom/Content Role: Operations"
    - "Atom/Content Role: Implementation"
    - "Spec"
version: 2
updated_at: "2026-09-23 23:42:09 +0000"
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
relations:
  relates_to: [CA-R-1514, CA-R-1515, CA-R-1517, CA-R-1452, CA-R-1509]
---
# Bind each Tool to one methodology Action

**in** the caprmedio Project, a Tool **must** implement **`=1`** Action defined by an existing applicable methodology O Atom **unless** it is the explicitly admitted `VALIDATE_ATOMS` Workflow implementation below.

- the Tool's RMED identifies that Action as the behavior it realizes **and** specifies its implementation obligations **without** copying the canonical Action definition.
- a Workflow Step binds its Action under CA-R-1509; the corresponding Tool realizes that Action rather than redefining the Workflow graph.
- this cardinality constrains the Action implemented by the Tool. it does **not** count internal instructions, API calls, interactions, **or** retries.

the binding is **not** a requirement **to** use that Action **or** a particular Workflow **to** build the Tool.

for `VALIDATE_ATOMS` **only**, the **`=1`** operational entry binding is the applicable Atom Carrier Validation Workflow CA-O-080. its referenced Steps **and** Actions are constituent definition bindings, **not** competing Tool entry definitions. the Tool realizes that graph **without** copying it into RMED **or** redefining its Actions; definition ownership remains **in** methodology. this exception does **not** change the binding of other Tools.
