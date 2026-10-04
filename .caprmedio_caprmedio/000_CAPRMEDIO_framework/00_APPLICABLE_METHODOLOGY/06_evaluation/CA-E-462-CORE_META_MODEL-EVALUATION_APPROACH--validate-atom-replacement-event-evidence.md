---
subjects:
  governs: "Journal/Record"
  depends_on:
    - "Work Journal/Event"
    - "Atom/Identifier"
    - "Atom/Revision"
    - "Carrier"
    - "Atom/Content Role: Operations"
    - "Journal"
    - "Atom"
    - "Artifact/Carrier"
    - "Project"
    - "Applicable Methodology"
version: 12
updated_at: "2026-10-02 20:09:13 +0400"
relations:
  evaluation_for:
    - CA-R-1491
    - CA-R-807
atom_id: "CA-E-462"
content_role: "Evaluation"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
type: "Evaluation Approach"
global_tier: 11
projection:
  source_carrier_path: ../000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/06_evaluation/CA-E-462-CORE_META_MODEL-EVALUATION_APPROACH--validate-atom-replacement-event-evidence.md
---
# Summary

Validate Atom replacement event evidence

## Scope

Atom replacement event evidence.

## Claim

the Evaluation **must** check whether an Atom replacement satisfies CA-R-807. Journal acceptance is **not** proof that the replacement is correct.

## Details

### Checks

- report a failed replacement Evaluation **if** predecessor **or** successor identities are missing, unresolved, duplicate, self-referencing, **or** mismatched.
- verify that **every** named successor was Active **before** the predecessor was archived, that the archive preserves the predecessor's body, Summary, identity, Version, **and** every metadata value except archived Status **and** archive-time Updated At, **and** that **`=1`** authoritative Journal event records that replacement.
- check event field representation against the selected Delivery authority. a format check alone **must not** be reported as proof of replacement correctness.
- repeated submission of the same event **must not** create another authoritative record.

### Failure disposition

a failed **or** unresolved replacement Evaluation **must not** prevent the Journal from preserving the observed event under CA-R-1491. preserve the supplied identities **and** evidence **without** inventing a conforming replacement **or** claiming that a failed check passed. correction changes the governed source through its authorized Workflow; it does **not** rewrite accepted history.

this Evaluation **must not** require a Git Commit **or** a particular Journal serialization.
