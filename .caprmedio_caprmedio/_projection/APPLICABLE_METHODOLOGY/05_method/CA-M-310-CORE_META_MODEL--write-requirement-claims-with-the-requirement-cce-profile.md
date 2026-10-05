---
subjects:
  governs: "CCE/Role Profile: Requirement"
  depends_on:
    - "Atom/Content Role: Requirement"
    - "CCE Operator"
    - "Atom/Claim"
version: 5
updated_at: "2026-10-04 04:27:08 +0400"
relations:
  child_of:
    - CA-M-307
  relates_to:
    - CA-R-1339
    - CA-M-233
    - CA-M-235
atom_id: "CA-M-310"
content_role: "Method"
current_scope_unit: "CORE_META_MODEL"
claim_target_scope_unit: "CORE_META_MODEL"
local_tier: "Standard"
status: "Active"
author: "Anatoly Maslennikov"
global_tier: 11
projection:
  source_carrier_path: ../../../000_CAPRMEDIO_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/001_CORE_META_MODEL/05_method/CA-M-310-CORE_META_MODEL--write-requirement-claims-with-the-requirement-cce-profile.md
  source_atom_id: CA-M-310
  source_atom_revision: 5
  source_sha256: b41cd2dfe70813a227d0253e717c5d39ac6d5cb842ea72524ce0582476ed0db6
  original_relations_sha256: 7ff74fac259540a50c68f38f47ef057478ad58aa287534b9bcfad07aacadfb73
---
# Summary

Write Requirement Claims with the Requirement CCE Profile

## Scope

Requirement Claims with the Requirement CCE Role Profile.

## Claim

**to** write a Requirement Claim with the Requirement CCE Role Profile, the Author **must** perform **all** of:

1. state the primary contribution as one Entity model **or** required result by its meaning **and** value under CA-R-1339. express required properties **and** observable boundaries within that model **or** result; an obligation, permission, **or** prohibition alone does **not** select Requirement.
2. use **must**, **must not**, **may**, **only**, quantification, predicates, comparisons, **and** explicit conditions as applicable **to** state what is required, permitted, prohibited, **or** bounded.
3. use **means** **only** **when** the Claim defines the governed Requirement subject rather than merely describing it.
4. express temporal Operators **only** as observable timing boundaries **or** conditions on the required result.
5. keep procedural selection, ordered execution steps, implementation instructions, **and** reusable operational behavior outside the primary contribution. reference applicable Method **or** Operations authority rather than reproducing it.

## Details

the Requirement profile governs the required model **or** result. an observed test result remains execution evidence; it is **not** the required-result specification.
