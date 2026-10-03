---
atom_id: CA-P-922
cce_version: cce_1
cce_form: obligation
author: Operator
assignee: Operator
subjects:
  governs:
    continuant:
      - Methodology Conflict Disposition
    occurrent:
      - Methodology Conflict Approval
  depends_on:
    occurrent:
      - CA-P-921
version: 1
updated_at: 2026-08-29 05:10:05 +0400
autonomous_confidence_threshold: 99
relations: {}
---
# Approve Exact Methodology Conflict Dispositions

**when** CA-P-921 is Done, **then** the Operator **must** assign **`=1`** exact disposition **to** **every** reported conflict **before** **any** conflict changes source authority **or** Applicable Methodology output.

## Scope

`(all unresolved conflicts in the exact CA-P-921 report)`

## Definition of Done

the Task is **not done if** (**any** reported conflict lacks **`=1`** explicit Operator disposition **or** a disposition omits its conflict identity, source-frontier digest, selected semantic result, affected Carrier paths, **and** authorized action **or** a disposition relies on compiler preference, layer order, filename order, confidence, **or** unstated inference **or** a disposition selects one Carrier **when** both Claims **must** remain under corrected classifications **or** a stale disposition is reused **after** its source frontier changes **or** an unreported conflict is resolved implicitly).

## Details

permit dispositions such as retain one exact Candidate, replace an exact Claim, reclassify one **or** more Atoms while preserving both Claims, split an invalid Atom, **or** reject the proposed source frontier. use a native digest-bound approval Carrier **only** **when** selection among unchanged Candidate Carriers is the approved semantic result. authorize source-Atom repair explicitly **when** preserving the accepted Claims requires changing their classification **or** Subjects.
