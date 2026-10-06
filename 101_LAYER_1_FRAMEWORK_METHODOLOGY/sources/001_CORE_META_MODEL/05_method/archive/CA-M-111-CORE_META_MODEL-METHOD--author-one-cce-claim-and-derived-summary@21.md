---
subjects:
  governs: "Atom Claim Authoring"
  depends_on:
    - "Atom/Claim"
    - "CCE"
    - "Atom/Summary"
version: 21
updated_at: "2026-09-22 23:02:20 +0000"
relations: {}
---
# Summary

Author one CCE Claim and derived Summary

## Claim

**to** author one CAPRMEDIO Atom Claim, the Author **must** perform **all** of:

1. write **`=1`** independently replaceable Claim **in** CAPRMEDIO Controlled English.
2. resolve **`=1`** Claim Target Scope Unit independently of ownership. select the current Scope Unit **as** the default during authoring **or** select an explicitly permitted different target; carry the resolved value under CA-D-482. express **any** narrower **or** composite applicability as part of the Claim text under CA-D-477; those restrictions alone do **not** make the Atom Relational.
3. derive **`=1`** concise Summary from the complete Claim, including its textual applicability restrictions, **when** creating the Atom. **when** revising an existing Atom, retain its Summary **and** check its source faithfulness under CA-R-1273; **if** that Summary needs changing, use a new Atom identity under CA-R-1464 instead of revising the existing identity.
4. derive **every** Translation from the complete Claim, including its textual applicability restrictions, rather than from the Summary.
