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
version: 2
updated_at: 2026-08-30 16:32:06 +0400
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

## Operator Disposition

conflict identity: `a9fcdbf6e39196b029e0397c1b4d360f8f3998d774b8d696f6bb87160cfaa6c0`.

source-frontier digest: `b46f92b26830e9e8c00eae3b82872720629ec0dd8610951d97df09a8c8233289`.

selected semantic result: preserve the Routing Tree Claim **and** replace the obsolete specialist-prefix Claim with the CAPRMEDIO Skill Interface model in which `ca` is the Main Skill identity, **only** the Main Skill loads the General System Prompt, the Main Skill routes through the canonical Routing Tree, **and** an Operator-defined Direct Route Skill invokes **`=1`** registered branch **or** leaf directly.

authorized action:

1. archive revision 8 of `CAPRMEDIO-GOV-REQU-316` **and** replace it with revision 9 that defines the CAPRMEDIO Main Skill.
2. add `CA-R-1354` through `CA-R-1357` for General System Prompt loading, Main Skill routing, Direct Route Skill definition, **and** Operator permission.
3. add `CA-D-344` for host-specific Main Skill invocation serialization.
4. archive revision 8 of `CAPRMEDIO-GOV-REQU-333` **and** replace its definition classification with an obligation governing the CAPRMEDIO Routing Tree.
5. archive revision 8 of `CAPRMEDIO-GOV-REQU-334` **and** qualify its validation Subject to the CAPRMEDIO Routing Tree without changing its Claim.
6. regenerate the conflict report from the resulting source frontier **and** stop for another Operator disposition if **any** conflict remains **or** appears.

affected source Carrier paths:

- `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CAPRMEDIO-GOV-REQU-316--register-ca-as-specialist-skill-prefix.md`
- `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CAPRMEDIO-GOV-REQU-316--define-caprmedio-main-skill.md`
- `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CA-R-1354-REQUIREMENT--restrict-general-system-prompt-loading-to-main-skill.md`
- `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CA-R-1355-REQUIREMENT--route-main-skill-through-canonical-routing-tree.md`
- `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CA-R-1356-REQUIREMENT--define-caprmedio-direct-route-skill.md`
- `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CA-R-1357-REQUIREMENT--permit-operator-defined-direct-route-skills.md`
- `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/07_delivery/CA-D-344-DELIVERY--serialize-main-skill-invocation-per-host.md`
- `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CAPRMEDIO-GOV-REQU-333--register-one-canonical-routing-tree.md`
- `.caprmedio_framework/00_APPLICABLE_METHODOLOGY/000_APPLICABLE_MTHD_sources/003_LOCAL_CONFIGURATION/04_requirement/CAPRMEDIO-GOV-REQU-334--validate-the-routing-tree.md`

disposition status: approved by the Operator.
