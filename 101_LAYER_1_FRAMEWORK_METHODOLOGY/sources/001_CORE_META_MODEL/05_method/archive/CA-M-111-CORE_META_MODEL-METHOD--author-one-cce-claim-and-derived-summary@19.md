---
subjects:
  governs: "Atom Claim Authoring"
  depends_on:
    - "Atom/Claim"
    - "CCE"
    - "Atom/Summary"
cce_version: cce_1
cce_form: method
version: 19
updated_at: "2026-09-22 17:59:17 +0000"
relations: {}
llm_session_ids:
  - codex:01a02650-eff7-7453-8c37-0699b36773c6
---
# Author one CCE Claim and derived Summary

**to** author one CAPRMEDIO Atom Claim, the Author **must** perform **all** of:

1. write **`=1`** independently replaceable Claim **in** CAPRMEDIO Controlled English.
2. resolve **`=1`** Claim Target Scope Unit independently of ownership. use the current Scope Unit **when** the target is omitted for a Current-scope Atom; otherwise preserve the explicit permitted target under CA-D-476. express **any** narrower **or** composite applicability as part of the Claim text under CA-D-477; those restrictions alone do **not** make the Atom Relational.
3. derive **`=1`** concise Summary from the complete Claim, including its textual applicability restrictions, **when** creating the Atom. **when** revising an existing Atom, retain its Summary **and** check its source faithfulness under CA-R-1273; **if** that Summary needs changing, use a new Atom identity under CA-R-1464 instead of revising the existing identity.
4. derive **every** Translation from the complete Claim, including its textual applicability restrictions, rather than from the Summary.
